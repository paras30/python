a= list(map(int,input("enter a element separted by comma : ").split(',')))
a.sort()
print(f'The sorted list is: {a} ')
b =int(input('Enter element to be found: '))
start = 0
end = len(a)-1
while start <= end:
    mid = (start + end) //2
    if a[mid] == b:
        print(f"{b} is at index : {mid}")
        break
    elif a[mid] < b:
        start = mid + 1
    else:
        end = mid - 1
