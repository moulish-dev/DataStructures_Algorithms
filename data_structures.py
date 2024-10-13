# BASIC DATA STRUCTURES

# contiguous memory = block of memory locations sequentially adjacent 
# self is the current instance in the class

# ARRAYS
# collection of items stored at contiguous memory location
# implemented using lists in python
# allows random access using an index

array = [1,2,3,4,5]
#Accessing array lists
print(array[2])
#modifying arrays
array[2] = 10
print(array)


# LINKED LISTS
# linear data structure
# each object is seperate as a node
# node contains data of the element and a reference of next element
# can be added without the need of contiguous memory


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

l_l = LinkedList()
l_l.insert_at_end(2)
l_l.display()
l_l.insert_at_end(6)
l_l.display()
l_l.insert_at_end(8)
l_l.display()
l_l.insert_at_end(3)
l_l.display()

# STACKS
# linear data structure
# follows Last In First Out (LIFO) principle
# functions: push, pop, peek

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def display(self):
        print(self.stack)
    
stack = Stack()
stack.push(10)
stack.display()
stack.push(30)
stack.push(20)
stack.peek()
stack.display()
stack.pop()
stack.display()

# Queues
# linear data structure
# uses First In First Out (FIFO) principle 
# functions: enqueue, dequeue

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def display(self):
        print(self.queue)

queue = Queue()
queue.enqueue(5)
queue.display()
queue.enqueue(10)
queue.display()
queue.enqueue(15)
queue.display()
queue.dequeue()
queue.display()
queue.peek()

# # HASH TABLES
# data structure which maps values to keys
# uses hash fuction to create a index for values
# implemented as dictionaries
# provides fast access to data using keys (time complexity O(1))
# Collisions handled using chaining and open addressing

hash_table = {}

#adding key value pairs
hash_table["company"] = "Cisco"
hash_table["domain"] = "IT Services"
print(hash_table)
# accessing values
print(hash_table["company"])
print(hash_table["domain"])

#check if a key exists
print("domain" in hash_table)

#del a key-value pair
del hash_table["domain"]
print(hash_table)

# COMPARISON
# Data Structure	Access-Time	Insert Time	    Delete Time	Use Case

# Array (List)	    O(1)	    O(1) or O(n)	O(n)	    Fast access by index
# Linked List	    O(n)	    O(1)	        O(1)	    Dynamic size, efficient insert/delete
# Stack	            O(n)	    O(1)	        O(1)	    LIFO operations
# Queue	            O(n)	    O(1)	        O(1)	    FIFO operations
# Hash Table	    O(1)	    O(1)	        O(1)	    Fast key-based lookup


# USE CASES

#Arrays : fast access of elements  MATRIX OPERATIONS AND LARGE DATASETS
#Linked Lists : frequent insertions and deletions LRU CACHES AND REAL TIME SYSTEMS
#Stacks : used in algorithms for recursion, backtracking
#Queues : bfs algorithm, cpu scheduling, task scheduling
#Hash Tables : quick lookups in dictionaries and caches