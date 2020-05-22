list=[]
list_=[]
for i in range(1,21):
    list.append(i)
print("main list is: ",list)
for i in range(0,11):
    a=list[i]
    if a%2==0:
        list_.append(a)
        list.remove(a)
print("odd list is: ",list)
print("even list is: ",list_)