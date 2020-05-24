class Phone: 
    def __init__(self): 
        print('phone.')
        
    def __del__(self): 
        print('destructor.')
        
if __name__=='__main__':
	a=Phone()
	del a