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