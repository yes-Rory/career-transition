# read data
# open file and close file
# file=open("scores.csv","r")
# content=file.read()
# print(content)

# line="Tom,90"
# data=line.split(",")
# print(data)

# for line in file:
#     print(line.strip())

# file.close()

# open file
file=open("scores.csv","r")
# jump the header
next(file)

# data analyse
count=0
total=0
pass_count=0
max_score=0
min_score=100

# read file
for line in file:
    count+=1
    data=line.strip().split(",")
    score=int(data[1])
    total+=score
    if score >=60:
        pass_count+=1
    if score > max_score:
        max_score=score
    if score < min_score:
        min_score=score

# close file
file.close()

average=total/count

# output data
print("Average:",round(average,2))
print("Pass Count:",pass_count)
print(f"Max Score:{max_score}")
print(f"Min Score:{min_score}")