def divide(a,b):
	try:
		print(a/b)
	except ZeroDivisionError as err:
		print("you cannot divide a number by zero")
	except TyperError as err:
		print("number must be int or float")
	except:
		print("unexcepted error")
a,b=input("exception handling\nenter two number separted by comma : ").split(',')

divide(int(a),int(b))
		
