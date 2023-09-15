import scrapy
from footywire.items import FootywireItem
import datetime
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.footywire.com/afl/footy/ft_match_list?year=2023']

    def parse(self, response):
        for row in response.xpath('//*[@id="contentpagecell"]/form/table/tr[7]/td/table/tr'):
            
            if row.xpath('td/@class').extract_first() == 'tbtitle':
                current_round = row.xpath('td/a/@name').extract_first().replace('round_', '')
                match = 1
            elif row.xpath('@class').extract_first() == "lightcolor" or row.xpath('@class').extract_first()== "darkcolor": 
                timeStr = row.xpath('td[1]/text()').get().replace('\xa0', '')
                venue = row.xpath('td[3]/text()').get()
                date_object = datetime.datetime.strptime(timeStr, '%a %d %b %I:%M%p')
                date = date_object.strftime('%d/%m/2023')
                time = date_object.strftime('%I:%M%p')


                rowData1 = FootywireItem()
                rowData2 = FootywireItem()

                rowData1["round"] = current_round
                rowData1["year"] = "2023"
                rowData1["match"] = match
                rowData1['date'] = date
                rowData1['time'] = time
                rowData1['venue'] = venue
                rowData1['team'] = row.xpath('td[2]/a[1]/text()').get()

                rowData2["round"] = current_round
                rowData2["year"] = "2023"
                rowData2["match"] = match
                rowData2['date'] = date
                rowData2['time'] = time
                rowData2['venue'] = venue
                rowData2['team'] = row.xpath('td[2]/a[2]/text()').get()

                statsPage = row.xpath('td[5]/a/@href').get()
                request = response.follow(statsPage, callback=self.parse_basic)
                request.meta['rowData1'] = rowData1
                request.meta['rowData2'] = rowData2
                
                match+=1

                yield request
    
    def parse_basic(self, response):
        rowData1 = response.meta['rowData1']
        rowData2 = response.meta['rowData2']

        rowData1['player'] = response.xpath("//*[@id='match-statistics-team1-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[1]/a/text()").get()
        rowData1['k'] = response.xpath("//*[@id='match-statistics-team1-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[2]/text()").get()
        
        rowData2['player'] = response.xpath("//*[@id='match-statistics-team2-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[1]/a/text()").get()
        rowData2['k'] = response.xpath("//*[@id='match-statistics-team2-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[2]/text()").get()
        
        advPage = response.url+"&advv=Y"
        
        request = response.follow(advPage, callback=self.parse_adv)
        request.meta['rowData1'] = rowData1
        request.meta['rowData2'] = rowData2
        
        yield request

    def parse_adv(self, response):
        rowData1 = response.meta['rowData1']
        rowData2 = response.meta['rowData2']

        rowData1['tog'] = response.xpath("//*[@id='match-statistics-team1-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[18]/text()").get()
        rowData2['tog'] = response.xpath("//*[@id='match-statistics-team2-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[18]/text()").get()
        
        player1 =  response.xpath("//*[@id='match-statistics-team1-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[1]/a/@href").get()
        player2 =  response.xpath("//*[@id='match-statistics-team2-row']/table[1]/tr[2]/td[2]/table/tr[2]/td[1]/a/@href").get()
        
        request1 =  response.follow(player1, callback=self.parse_player)
        request1.meta['rowData'] = rowData1
        yield request1

        request2 =  response.follow(player2, callback=self.parse_player)
        request2.meta['rowData'] = rowData2
        yield request2

    def parse_player(self, response):
        rowData = response.meta['rowData']

        rowData['born'] = response.xpath("//*[@id='playerProfileData1']/text()").get().split('Born:')[1].strip().split('\xa0')[0].strip()
        
        data = response.xpath("//*[@id='playerProfileData2']/text()").get().split('\xa0\xa0\xa0')

        rowData['height'] = data[0].split(":")[1].strip()
        rowData['weight'] = data[1].split(":")[1].strip()
        rowData['position'] = data[2].split(":")[1].replace('\n', '').replace('  ', '')

        yield rowData