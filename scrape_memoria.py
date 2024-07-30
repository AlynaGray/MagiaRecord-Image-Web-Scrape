#! /usr/bin/env python3

from pathlib import Path
import urllib.request
import os
from typing import Generator

USER_AGENT = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
BASE_URL = "https://android.magi-reco.com/"

def main() -> None:
    scrape_memoria()

def memoria_candidates() -> Generator[str, None, None]:
    part1 = "magica/resource/image_web/memoria/memoria_"
    part3 = "_s.png"
    for i in range(10000):
        part2 = str(i).zfill(4)
        yield f"{part1}{part2}{part3}"

def scrape_memoria() -> None:
    for asset in memoria_candidates():
        print(f"Scraping: {asset}")
        scrape(asset)

def scrape(asset: str) -> None:
    # asset is the portion after the domain, without the leading /
    # e.g. "magica/resource/image_web/memoria/memoria_1003_s.png"
    req = urllib.request.Request(f"{BASE_URL}{asset}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            print(f"Returned status code {response.status}")
        else:
            os.makedirs(os.path.dirname(Path(asset)), exist_ok=True)
            with open(Path(asset), mode="wb") as file:
                file.write(response.read())

if __name__ == "__main__":
    main()
