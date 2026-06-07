import pandas as pd

# read file
df = pd.read_csv("student_scores.csv")

# data analysis
df["total"]=(
    df["math"]
    +df["chinese"]
    +df["english"]
    )

# df["average"]=round(df["total"]/3,2)
df["average"] =(
    df["total"]/3
).round(2)

def get_grade(avg):
    if avg >=90:
        grade = "A"
    elif avg >=80:
        grade = "B"
    elif avg >=70:
        grade = "C"
    else:
        grade = "D"
    return grade

df["grade"]=df["average"].apply(get_grade)

df= df.sort_values(
    "total",
    ascending=False
    )

print(df)

# reset index
df = df.reset_index(drop=True)

ggrade = df.groupby("grade")
ggcount = ggrade["name"].count()
print(ggcount)

grouped=df.groupby("gender")
# print(grouped)
gcount= grouped["name"].count()
gtotal= grouped["total"].sum()
# print(gcount,gtotal)
gaverage= round(gtotal/gcount,2)
print(gaverage)

# use mean count
print("Class Average:",round(df["average"].mean(),2))
print(round(df.groupby("gender")["average"].mean(),2))
print(df.groupby("grade")["name"].count())

# optimize
grade_count =(
    df.groupby("grade")["name"]
    .count()
)

gender_average =(
    df.groupby("gender")["average"]
    .mean()
    .round(2)
)
print(grade_count)
print(gender_average)

# save file
df.to_csv("analysis.csv",index=False)