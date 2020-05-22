a=int(input("enter the pattern no."))
b=a**2
print("1",end='')
for i in range(2,a+1):
	if i<=a:
		print(f"0{i}",end='') 
for j in range(b+1,a+b+1):
	print(f"0{j}",end='')
print()
for i in range(a+1,a+2):
	print(f"**{i}",end='')
for i in range(a+2,b+1):
	print(f"0{i}",end='')


            

