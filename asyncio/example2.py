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