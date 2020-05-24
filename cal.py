a,b,op=input('calculator\nEnter first & second no. & operator \nusing separted by comma : ').split(',')
a=int(a)
b=int(b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

if op == '+' :
    ans = add(a,b)    
elif op == '-':
    ans = sub(a,b)
elif op == '*':
    ans = mul(a,b)
elif op == '/':
    ans = div(a,b)
elif op == '%':
    ans = mod(a,b)
print(f" \n2 number {(op)} is : {a} {op} {b} = {ans}")

