#Synchronous Programming
'''Synchronous programming means tasks are executed one by one, in order.
A task must finish before the next task starts.'''

print("Task 1 started")
for i in range(5):
    print(i)
print("Task 1 completed")

print("Task 2 started")
print("Task 2 completed")

'''
Task 1
   ↓
wait until Task 1 finishes
   ↓
Task 2
   ↓
wait until Task 2 finishes
   ↓
Task 3

So synchronous programming is often called:

Blocking execution

because one task can block the execution of the next task.
'''

#Synchronous Example ,Let's say we have three tasks.
import time
def task1():
    print("Synchronous Task 1 started")
    time.sleep(3)
    print("Synchronous Task 1 completed")

def task2():
    print("Synchronous Task 2 started")
    time.sleep(2)
    print("Synchronous Task 2 completed")

task1()
task2()

'''Execution:

Task 1 started
    ↓
wait 3 seconds
    ↓
Task 1 completed
    ↓
Task 2 started
    ↓
wait 2 seconds
    ↓
Task 2 completed

Approximate total time:

3 + 2 = 5 seconds'''

#Asynchronous Programming
'''(Asynchronous programming allows a program to start a task and continue doing other 
work while waiting for that task to complete.)

Instead of:
Task 1 → wait → Task 2

we can have:
Start Task 1
      ↓
while Task 1 is waiting
      ↓
do Task 2
      ↓
Task 1 completes

The important concept is:
Don't waste time waiting when you can do other work.'''


#Asynchronous Example
#Python provides:async and await for asynchronous programming.
import asyncio

async def task1():
    print("Asynchronous Task 1 started")
    await asyncio.sleep(3)
    print("Asynchronous Task 1 completed")

async def task2():
    print("Asynchronous Task 2 started")
    await asyncio.sleep(2)
    print("Asynchronous Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

'''Possible output:
Task 1 started
Task 2 started
Task 2 completed
Task 1 completed
Approximate execution time:
max(3, 2) = 3 seconds
rather than:
3 + 2 = 5 seconds
Why?
Because while Task 1 is waiting:
await asyncio.sleep(3)
Task 2 can run.'''


'''
Sync vs Async
Synchronous	                                           Asynchronous
Tasks execute sequentially	                  Tasks can overlap while waiting
One task can block another	                 Waiting task doesn't necessarily block other work
Simple to understand	                            Slightly more complex
Good for CPU/simple sequential work             	Excellent for I/O waiting
Uses normal functions	                            Often uses async/await
Blocking operations are common                	Non-blocking operations are possible
'''

#Blocking means:The program cannot continue because it is waiting for something.
import time
print("Start")
time.sleep(5)#During those 5 seconds, that particular execution path is blocked.
print("End")

#async tells Python:"This function is asynchronous and can work with await."
async def hello():
    print("Hello")#This is called an async function or coroutine function.
#await means:"Wait for this asynchronous operation, but allow the event loop to handle other async work meanwhile."
async def task():
    await asyncio.sleep(5)

'''
The important difference is that:
time.sleep(5)
is a blocking sleep, while:
await asyncio.sleep(5)
is designed for asynchronous execution.
'''



'''
I/O means:Input/Output

Network I/O
API request
↓
wait for server
↓
response

Database I/O
Send SQL query
↓
wait for database
↓
result

File I/O
Read file
↓
wait for disk
↓
data

External service
Send request to payment API
↓
wait
↓
response
These operations can spend significant time waiting.
That's where async programming can be very useful.
'''
#Basic asyncio Example
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

asyncio.run(hello())

