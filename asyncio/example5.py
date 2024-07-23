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


