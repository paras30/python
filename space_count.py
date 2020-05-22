x="the quick brown fox jumps over the lazy dog"
c=0
y=x.split()
z=len(y)
for i in range(1,z):
    if y[i] !=" ":
    	c+=1
print(c)