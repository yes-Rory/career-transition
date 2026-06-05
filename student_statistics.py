# store data
scores=[90, 85, 95, 78, 66, 55, 40]

# data analyse
pass_count=0
excellent_count=0
for score in scores:
    if score >=60:
        pass_count+=1
    if score >=90:
        excellent_count+=1

# output data
print("Pass Count:",pass_count)
print("Excellent Count:",excellent_count)