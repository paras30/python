def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1)+f(n-2)

a= int(input('how many terms : '))
for i in range(a):
    print(f(i))