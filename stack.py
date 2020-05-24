class Stack_op:
    def __init__(self):
        self.arr = []
    def push(self, a):
        self.arr.append(a)
    def pop(self):
        if self.arr==[]:
            return 'stack is empty'
        return self.arr.pop()
    def peep(self):
        if self.arr==[]:
            return 'stack is empty'
        return self.arr[-1]

b= Stack_op()
i =0
while i != 4:
    print('\n       *  stack_operation  *\n1.Push\n2.Pop\n3.Peep\n4.exit')
    a = int(input('Enter any one choice: '))
    if a == 1:
        element = input('Enter element to be pushed: ')
        b.push(element)
        print(b.arr)
    elif a == 2:
        print(b.pop())
        print(b.arr)
    elif a == 3:
        print(b.peep())
        print(b.arr)
    elif a == 4:
    	exit()
    else:
        print('Enter betwween1 to 3.')
