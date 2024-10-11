#Lambdas in python
#Anonymous single-line functions
#used where functions needed temporarily

#cannot include loops or conditionals but can use ternary

#SYNTAX -- lamdas arguments : expression

def divide(x,y):
    return x/y

divide_lambda = lambda x,y : x/y

print("method: " , divide(2480,8))
print("Lambda: ", divide_lambda(2480,8))

#High order Functions

numbers_list = [23,45,65,97,25]
square_root = list(map(lambda x:x**2, numbers_list))
print("Numbers_list squared with map and lambda: ", square_root)

#filtering numbers
filter = list(filter(lambda x:x % 5 == 0, numbers_list))
print("Filtered with the numbers of 5 multiplications  ",filter)