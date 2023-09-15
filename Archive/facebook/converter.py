import pandas as pd


df = pd.read_json("data_full.json")

print(df)

df.to_excel("data.xlsx")

f = open("data.jsonl", "w")
print(df.to_json(orient="records", lines=True), file=f, flush=False)

df.to_csv("data.csv")
