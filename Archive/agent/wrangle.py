import pandas as pd
import json

# load json data
with open('main.json') as f:
    data = json.load(f)

# create dataframe with selected columns
df = pd.DataFrame(data, columns=['id', 'name', 'address', 'city', 'postal', 'country', 'email', 'phone', 'web'])


# save dataframe as csv
#df.to_csv('data.csv', index=False)

# save dataframe as json
# df.to_json('data.json', orient='records')

# save dataframe as jsonl
df.to_json('data.jsonl', orient='records', lines=True)