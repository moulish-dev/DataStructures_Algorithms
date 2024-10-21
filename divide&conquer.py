# Divide and Conquer Algo

#divide, search each subproblems recursively and combine

#merge sort is a divide and conquer algo
import math

def arithmeticMean(list):
    sum=0
    mn=9
    for i in list:
        t=i
        sum +=t
    sum=sum/mn
    return sum

def multiply(list):
    sum=0
    mn=9
    a = arithmeticMean(list)
    for i in list:
        t = i - a
        t = t*t
        sum +=t
    sum=sum/mn
    sum = math.sqrt(sum)
    print(round(sum,2))
list1=[86,123,191,106,179,193,89,228,194]
y = multiply(list1)

# print(p)

# list=[22,253,175,155,202,88,166,206,207]
# m1(list)