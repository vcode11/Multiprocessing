import asyncio

async def count():
    print("One");
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count()) 
    #can be run using asyncio.run(main()) in python3.7

if __name__ == "__main__":
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([count(), count(), count()]))
    elapsed = time.time() - start
    print(f"{__file__} exectued in {elapsed:0.2f} seconds.")
