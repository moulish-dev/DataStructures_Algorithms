#Iterators
#allow to traverse through all elements of collection like tuples, lists, dicts one element at a time
#__iter__() - iterator object
#__next__() - next object and if there is nothing raises StopIteration Exception

list1 =[1,2,3]
iter_list1 = iter(list1)#creates an iterator from list1
print(next(iter_list1))
print(next(iter_list1))
print(next(iter_list1))
#print(next(iter_list1)) raises StopIteration Exception

#for loops in python use iter

#custom iterator for generating first (n) odd number
class OddNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 1


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        else:
            number = self.current
            self.current += 2
            return number
        
#using
odd_iter = OddNumbers(9)
for n in odd_iter:
    print(n)

#useful in looping over collections