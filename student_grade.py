import pandas as pd

# read data
df=pd.read_csv("scores.csv")

# data analyse
def get_grade(score):
    if score >= 90:
        grade="A"
    elif score >= 80:
        grade="B"
    elif score >= 70:
        grade="C"
    else:
        grade="D"

    return grade

df["grade"]=df["score"].apply(get_grade)
df=df.sort_values("score",ascending=False)

# print data
print(df)

print(df[df["grade"]=="A"])

print(df[df["score"] >= 90])

# save file
df.to_csv("result.csv",index=False)
df.to_csv("result1.csv")
