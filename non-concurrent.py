import requests
import time
sites = ['https://www.jython.org', "http://olympus.realpython.org/dice"]*40
def download_all_sites(sites):
    with requests.Session() as s:
        for url in sites:
            response = s.get(url)
            print(f'Read {len(response.content)} from {url}')
start_time = time.time()
download_all_sites(sites)
duration = time.time()-start_time
print(f'Your program took {duration}s')

