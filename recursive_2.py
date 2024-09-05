def recursiveNumberPrinting_till1(n):
    if(n < 1):
        print('' , n , 'is less than 1') #stops the function
    else:
        print(n) #prints number from n to 1
        recursiveNumberPrinting_till1(n-1) #goes back to the function
        print(n) #prints number from 1 to n

recursiveNumberPrinting_till1(6)