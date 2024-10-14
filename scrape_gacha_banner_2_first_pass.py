#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/gacha/gacha_"
    p3 = "_banner.png"
    for i in range(0, 2201):
        p2 = str(i).zfill(3)
        yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
