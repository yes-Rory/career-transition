# input data 
ch_score=int(input("Input your Chinese score:"))
math_score=int(input("Input your Math score:"))
en_score=int(input("Input your English score:"))

# store data
scores=[ch_score,math_score,en_score]

# analyse data
total=sum(scores)
average=total/len(scores)
biggest=max(scores)
smallest=min(scores)

if average>= 90:
    grade='A'
elif average>=80:
    grade='B'
elif average>=70:
    grade='C'
else:
    grade='D'

# output data
print("Total:",total)
print(f"Total:{total}")
print("Average:",average)
print("Average:",round(average,2))
print(f"Average:{average:.2f}")
print("Max:",biggest)
print(f"Max:{biggest}")
print("Min:",smallest)
print(f"Min:{smallest}")
print("Grade:",grade)
print(f"Grade:{grade}")