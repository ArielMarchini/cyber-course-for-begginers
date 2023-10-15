import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.fetch import fetch
import os
import time


MAX_FETCH_TIME = 0.1


def did_fetch(user, url):
    os.environ["USER"] = user
    start_time = time.time()
    fetch(url)
    end_time = time.time()
    total_time = end_time - start_time
    if total_time >= MAX_FETCH_TIME:
        return False
    return True

    

