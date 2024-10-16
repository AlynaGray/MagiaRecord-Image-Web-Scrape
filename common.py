#! /usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Generator
import os
import random
import requests

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
           "Priority": "u=0, i"}

GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0m"


# Scrape for filename in every directory inside magica recursively.
# If prerequisite_file is not None, only scrape in directories with prerquisite_file
def scrape_all_in_dirs(filename: str, prerequisite_file: str | None = None) -> None:
    scrape_all(lambda: scrape_all_in_dirs_generator(filename, prerequisite_file))

def scrape_all_in_dirs_generator(filename: str, prerequisite_file: str | None = None) -> Generator[str, None, None]:
    for dirpath, _, files in os.walk("magica"):
        if prerequisite_file is not None and prerequisite_file not in files:
            continue
        yield f"{dirpath}/{filename}"


def scrape_all(candidates: callable) -> None:
    if not nonexistent_asset_page_correct():
        exit(1)
    
    # I believe requests isn't thread safe when using cookies, but this should be fine
    with requests.Session() as session, ThreadPoolExecutor(max_workers=10) as executor:
        for asset in candidates():
            # Use loop to retry after each connection, so transient network errors don't stop the program
            while True:
                try:
                    print(f"Scraping: {asset}")
                    executor.submit(scrape, session, asset)
                    break
                except Exception as e:
                    print(f"{RED}{e}{RESET}")


def scrape(session: requests.Session, asset: str) -> None:
    # asset is the portion after the domain, without the leading /
    # e.g. "magica/resource/image_web/memoria/memoria_1003_s.png"
    response = session.get(f"{BASE_URL}{asset}", headers=HEADERS, timeout=random.randint(4,10))
    if response.status_code != 200:
        raise Exception(f"returned status code {response.status}")
    else:
        # The game server always returns a html page if the asset is not found
        content = response.content
        if content == NONEXISTENT_ASSET_PAGE:
            return
        print(f"{GREEN}Found {asset}!{RESET}")
        os.makedirs(os.path.dirname(Path(asset)), exist_ok=True)
        with open(Path(asset), mode="wb") as file:
            file.write(content)

def nonexistent_asset_page_correct() -> bool:
    print("Verifying nonexistent asset page")
    response = requests.get(f"{BASE_URL}{NONEXISTENT_ASSET}", headers=HEADERS, timeout=20)
    if response.status_code != 200:
        print(f"Returned status code {response.status}")
        return False
    else:
        content = response.content
        if NONEXISTENT_ASSET_PAGE != content:
            print(f"Error: {NONEXISTENT_ASSET_PAGE_FILENAME} not correct page")
            print(f"Expected response:\n{NONEXISTENT_ASSET_PAGE}")
            print(f"Actual response:\n{content}")
            return False
        else:
            print("Nonexistent asset page correct")
            return True
