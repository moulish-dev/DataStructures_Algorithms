#Concurrency in python
#allows to do multiple processes in parallel to speed up programs

#concepts in concurrency - GIL, multiprocessing, threading , asynchrony, GIL

#GIL - Global Interpreter Lock
#prevents multiple native threads to execute at once in a multi core system
#limits the multithreading processes

#Threading
#allows to run multiple threads at the same time
#best for I/O tasks
#less useful in cpu-bound tasks due to GIL
import threading

# threading.Thread() #creates a new thread
# threading.start() #starts a thread
# threading.join()   #waits for a thread to finish

def task():
    print("Task Started")

#creating threads
thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

#starting threads
thread1.start()
thread2.start()

#waiting for threads to complete
thread1.join()
thread2.join()

#Multiprocessing
#involves creating seperate processes wach with its 
# own interpreter and memory space so each has its own GIL
#better suited for CPU-bound tasks

import multiprocessing

# multiprocessing.Process()  #creates a new process
# multiprocessing.start() #starts a process
# multiprocessing.join()  #waits for a process to finish

def m_task():
    print("Multiprocessing task started")

#creating processes
process1 = multiprocessing.Process(target=m_task)
process2 = multiprocessing.Process(target=m_task)

#starting processes
process1.start()
process2.start()

#waiting for process to complete
process1.join()
process2.join()

#Asynchrony
#involves executing tasks which don't block the execution of a program
#useful in I/O tasks like HTTP requests or file reading

import asyncio

async def async_task():
    print("Async Task Started")
    await asyncio.sleep(1) #a non-blocking I/O task
    print("Async Task completed")

async def main():
    await asyncio.gather(async_task(),async_task())

#running a async function
asyncio.run(main())

#ThreadPoolExecutor and ProcessPoolExecutor
#threadpoolexecutor for I/O tasks
#processpoolexecutor for CPU bound tasks

from concurrent.futures import ThreadPoolExecutor
def th_task():
    print("thread Task executed")

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(th_task) for _ in range(2)]

# I/O-bound tasks (e.g., network, file handling):
# Use threading or asyncio for better performance.
# CPU-bound tasks (e.g., heavy computation):
# Use multiprocessing or ProcessPoolExecutor to bypass the GIL and leverage multiple cores.