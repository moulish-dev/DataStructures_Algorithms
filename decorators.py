#Decorators in python
#to modify or extend the use of a function without modifying the actual function
#used in logging, memoization, access control

def say_hello():
    return "Hello!"

def greet(func):
    return func()

print(greet(say_hello))

def decorator_ex(func):
    def wrapper():
        print("Before calling function")
        func()
        print("After calling the function")
    return wrapper

@decorator_ex
def say_hii():
    print("Hii!")

say_hii()

#with arguments
def decorator_args(func):
    def wrapper(*args, **kwargs):
        print("Before args function")
        result = func(*args, **kwargs)
        print("After args function")
        return result
    return wrapper

@decorator_args
def hello_person(name):
    print(f"Hello,{name}")

hello_person("Elon")

#usecases: logging, timing, access control , caching
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Time taken for '{func.__name__}' : {duration:.4f} seconds. ")
        return result
    return wrapper

@timer_decorator
def calculate_sum(n):
    print(sum(range(n)))

calculate_sum(5167)
#for number 51 = 0s
#for number 516734 = 0.035
#for number 51673477 = 1.95s

#caching - memoizataion
def memoize(func):
    cache={}
    def wrapper(*args):
        if args in cache:
            print("Fetching cache")
            return cache[args]
        print("Calculating result")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@timer_decorator
@memoize
def fibonacci_seq(n):
    if n<=1:
        return n
    return fibonacci_seq(n-1) + fibonacci_seq(n-2)

print(fibonacci_seq(10))
#second call uses from the cache
print(fibonacci_seq(10))        
