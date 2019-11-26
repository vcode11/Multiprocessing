import asyncio

async def count():
    print("One");
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([count(), count(), count()]))
    elapsed = time.perf_counter() - start
    print(f"{__file__} exectued in {elapsed:0.2f} seconds.")
