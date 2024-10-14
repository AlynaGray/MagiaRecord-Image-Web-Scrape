#! /usr/bin/env python3

from typing import Generator
import common
from itertools import chain

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/item/main/campaign_"
    p4 = ".png"
     # 9010, 202002, and 20200601 from https://github.com/GrygrFlzr/MagiRecoStatic
    for i in chain(range(900, 3000), range(8000, 10000), range(202002, 202003), range(20200601, 20200602)):
        for j in range(len(str(i)), 5):
            p2 = str(i).zfill(j)
            for k in ("_exchange", "_exchange_2", "_key"):
                p3 = k
                yield f"{p1}{p2}{p3}{p4}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
