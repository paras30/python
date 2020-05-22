list=[]
sum=0
for i in range(1,101):
    if i%2 !=0:
        sum+=i
        list.append(i)
print(f"odd numbers sum is : {sum}")
print()
print(list)