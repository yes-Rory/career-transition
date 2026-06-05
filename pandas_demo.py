import pandas as pd

df=pd.read_csv("scores.csv")

excellent=df[df["score"]>=90]
print(excellent)

print(df[df["score"]<60])

# 如果出现多个引号，只能双引号和单引号一起搭配使用，而不是两个双引号一起使用
print(f"Excellent Student:{(df['score']>=90).sum()}")

# print("Max Score:",df["score"].max())
# print("Min Score:",df["score"].min())
# print("Average:",round(df["score"].mean(),2))
# print("Pass Count:",(df["score"]>=60).sum())

# print(df)