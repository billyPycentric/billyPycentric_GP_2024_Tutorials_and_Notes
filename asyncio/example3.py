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