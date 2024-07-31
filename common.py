#! /usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import urllib.request
import os
import random

BASE_URL = "https://android.magi-reco.com/"
# The game server always returns the same html page with status code 200 is the asset is not found
NONEXISTENT_ASSET = "magica/resource/nonexistent_asset"
NONEXISTENT_ASSET_PAGE_FILENAME = "nonexistent_asset_page.html"
with open(NONEXISTENT_ASSET_PAGE_FILENAME, mode="rb") as file:
    NONEXISTENT_ASSET_PAGE = file.read()

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5",
           "Accept-Encoding": "gzip, deflate",
           "DNT": "1",
           "Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1",
           "Priority": "u=0, i",
           "Pragma": "no-cache",
           "Cache-Control": "no-cache"}

GREEN = "\033[0;32m"
RESET = "\033[0m"

def scrape_all(candidates: callable) -> None:
    if not nonexistent_asset_page_correct():
        exit(1)
    
    with ThreadPoolExecutor(max_workers=1) as executor:
        for asset in candidates():
            while True:
                try:
                    print(f"Scraping: {asset}")
                    executor.submit(scrape(asset))
                    break
                except Exception as e:
                    print(e)


def scrape(asset: str) -> None:
    # asset is the portion after the domain, without the leading /
    # e.g. "magica/resource/image_web/memoria/memoria_1003_s.png"
    req = urllib.request.Request(f"{BASE_URL}{asset}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=random.randint(4,10)) as response:
        if response.status != 200:
            print(f"Returned status code {response.status}")
        else:
            # The game server always returns a html page if the asset is not found
            content = response.read()
            if content == NONEXISTENT_ASSET_PAGE:
                return
            print(f"{GREEN}Found {asset}!{RESET}")
            os.makedirs(os.path.dirname(Path(asset)), exist_ok=True)
            with open(Path(asset), mode="wb") as file:
                file.write(content)

def nonexistent_asset_page_correct() -> bool:
    req = urllib.request.Request(f"{BASE_URL}{NONEXISTENT_ASSET}", headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            print(f"Returned status code {response.status}")
            return False
        else:
            content = response.read()
            if NONEXISTENT_ASSET_PAGE != content:
                print(f"Error: {NONEXISTENT_ASSET_PAGE_FILENAME} not correct page")
                print(f"Actual response: \"{NONEXISTENT_ASSET_PAGE}\"")
                return False
            else:
                return True
