import asyncio, time , aiohttp
async def download_site(url, session):
    async with session.get(url) as response:
        print(f'Read {response.content_length} from {url}')


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        'https://www.jython.org',
        "http://olympus.realpython.org/dice"
    ]*80
    start = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    print(f'Dowloaded {len(sites)} in {time.time() - start}s.')
