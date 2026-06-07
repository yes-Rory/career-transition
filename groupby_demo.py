import pandas as pd

# read file
df = pd.read_csv("students.csv")
print(df)

# data analyse
grouped = df.groupby("gender")
print(grouped)

# print data
print(grouped["score"].mean())
print(grouped["score"].count())
print(grouped["score"].max())
print(grouped["score"].min())
