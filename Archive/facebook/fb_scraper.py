import facebook_scraper as fs
import json


data = []

count = 0
for post in fs.get_posts(
    group="1373361046396315", pages=1000, options={"comments": 100, "progress": True}
):
    try:
        item = {}

        if post["post_id"] != None:
            item["id"] = str(post["post_id"])
        if post["post_text"] != None:
            item["text"] = post["post_text"]
        if post["post_url"] != None:
            item["link"] = post["post_url"].split("m.")[1]
        if post["likes"] != None:
            item["likes"] = post["likes"]

        comments = []
        if post["comments_full"] != None:
            for comment in post["comments_full"]:
                comment_data = {}
                comment_data["username"] = comment["commenter_name"]
                comment_data["comment_text"] = comment["comment_text"]
                comments.append(comment_data)

        item["comments"] = comments

        data.append(item)
        count += 1
        print("POSTS SCRAPPED : " + str(count))
        if count % 100 == 0:
            filename = "data_" + str(count - 100) + "_" + str(count) + ".json"
            with open(filename, "w") as f:
                json.dump(data, f)
            data = []
    except:
        filename = "data" + str(count - 100) + "_" + str(count) + ".json"
        with open(filename, "w") as f:
            json.dump(data, f)
            data = []

filename = "data" + str(count - 100) + "_" + str(count) + "FINAL.json"
with open(filename, "w") as f:
    json.dump(data, f)
    data = []
