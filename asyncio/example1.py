import asyncio

# Coroutine that simulates a time consuming task
async def fetch_data(delay,id):
    print(f"fetching data from coroutine with id {id} .... ")
    await asyncio.sleep(delay)
    print(f"Data fetched for coroutine with id {id}")
    return{"data" : f"some data with id:'{id}'"}


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