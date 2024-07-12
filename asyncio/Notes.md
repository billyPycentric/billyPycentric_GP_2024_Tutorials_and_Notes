# Assynchronous Programming
# Assynchronous Programming   
> **When to use asyncio** 
>> when your program waits a lot

Event loop -> core that manages and distributes tasks , when a task awaits it steps aside while the other task take charge   

1. How to use Asyncio   
~~~python
import asyncio

async def main():
    print("start a coroutine")

#"main()" -> coroutine obj 
main() -> you are not calling the func but an object
asyncio.run(main())
~~~  
2. Use await   
~~~python
# await keyword -> await keyword allows us to get the result of async function

~~~   
~~~python
// example1.py
import asyncio

# Coroutine that simulates a time consuming task
async def fetch_data(delay,id):
    print("fetching data .... ")
    await asyncio.sleep(delay)
    print("Data fetched")
    return{"data" : "some data"}


async def main():
    
    print("Start of the main Coroutine ..")
    
    print("Lets see something")
    task1 = fetch_data(10,1)
    result = await task1
    print(f"Recieved result : {result}  ")
    task2 = fetch_data(10,2)
    result = await task2
    
    print("Did something happen")
    print(f"Recieved result : {result}  ")
    print("End of main Coroutine ... ")


asyncio.run(main())

~~~   
~~~python

// Example2.py

import asyncio
import example1

async def main():
    task1 = asyncio.create_task(example1.fetch_data(3,4))
    task2 = asyncio.create_task(example1.fetch_data(1,9))
    task3 = asyncio.create_task(example1.fetch_data(2,3))
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1,result2,result3)


asyncio.run(main())


~~~

~~~python 

// Example3.py

# gather -> runs them concurrently , not great at error handling

import asyncio

async def fetch_data(delay,id):
    print(f"fetching data from coroutine with id {id} .... ")
    await asyncio.sleep(delay)
    print(f"Data fetched for coroutine with id {id}")
    return{"data" : f"some data with id:'{id}'"}


async def main():
    results = await asyncio.gather(fetch_data(3,11),fetch_data(5,16),fetch_data(1,12))
    for result in results:
        print(f" Recieved results :{result}")

asyncio.run(main())

~~~   
~~~python
import asyncio

async def fetch_data(delay,id):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(delay)
    return {"id" : id,"data": f"Sample data from coroutine {id} which was asleep for {delay}"}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([3,5,4],start=1):
            task = tg.create_task(fetch_data(sleep_time,i))
            tasks.append(task)
    results = [task.result() for task in tasks]

    for result in results:
        print(f"recieved results : {result}")

asyncio.run(main())
~~~   
## Locking Resources
~~~python

# Using Locks
import asyncio
shared_resource = 0

lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        print(f"Resource before Mod : {shared_resource}")
        shared_resource+= 1
        await asyncio.sleep(1)
        print(f"Resource After Mod : {shared_resource}")

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())



~~~


