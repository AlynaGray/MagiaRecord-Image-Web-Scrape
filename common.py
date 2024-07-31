#! /usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import urllib.request
import os
from typing import Iterator

USER_AGENT = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
BASE_URL = "https://android.magi-reco.com/"
# The game server always returns the same html page with status code 200 is the asset is not found
NONEXISTENT_ASSET = "magica/resource/nonexistent_asset"
NONEXISTENT_ASSET_PAGE_FILENAME = "nonexistent_asset_page.html"
with open(NONEXISTENT_ASSET_PAGE_FILENAME, mode="rb") as file:
    NONEXISTENT_ASSET_PAGE = file.read()

GREEN = "\033[0;32m"
RESET = "\033[0m"

def scrape_all(candidates: callable) -> None:
    if not nonexistent_asset_page_correct():
        print(f"Error: {NONEXISTENT_ASSET_PAGE_FILENAME} not correct page")
        exit(1)
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for asset in candidates():
            print(f"Scraping: {asset}")
            executor.submit(scrape(asset))

def scrape(asset: str) -> None:
    # asset is the portion after the domain, without the leading /
    # e.g. "magica/resource/image_web/memoria/memoria_1003_s.png"
    req = urllib.request.Request(f"{BASE_URL}{asset}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            print(f"Returned status code {response.status}")
        else:
            # The game server always returns a html page if the asset is not found
            content = response.read()
            if content == NONEXISTENT_ASSET_PAGE:
                return
            with open(Path(asset), mode="wb") as file:
                print(f"{GREEN}Found {asset}{RESET}!")
                os.makedirs(os.path.dirname(Path(asset)), exist_ok=True)
                file.write(response.read())

def nonexistent_asset_page_correct() -> bool:
    req = urllib.request.Request(f"{BASE_URL}{NONEXISTENT_ASSET}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            print(f"Returned status code {response.status}")
            return False
        else:
            return NONEXISTENT_ASSET_PAGE == response.read()
