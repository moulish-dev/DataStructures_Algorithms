def firstMethod():
    secondMethod()
    print('First Method Called') #Appears Third in Output

def secondMethod():
    thirdMethod()
    print('Second Method Called') #Appears Second in Output

def thirdMethod():
    print('Third Method Called') #First appears in output

firstMethod()