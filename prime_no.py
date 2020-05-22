a,b=input("enter starting and ending no. separated by comma : ").split(',')
a=int(a)
b=int(b)
for i in range(a,b+1):
    for j in range(2,i):
        if i!=2 and i%j==0:
            break
    else:
        print(i)
	
   
         