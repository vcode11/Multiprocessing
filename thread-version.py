import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as r:
        print(f"Read {len(r.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exc:
        exc.map(download_site, sites)
sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
]*80
start_time = time.time()
download_all_sites(sites)
print(f'Downloaded {len(sites)} in {time.time()-start_time}s.')
