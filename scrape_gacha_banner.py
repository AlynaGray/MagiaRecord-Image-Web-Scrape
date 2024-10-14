#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/banner/gacha/gachabanner_"
    for j in ("_m.png", "_a.png"):
        p3 = j
        for i in range(0, 3201):
            p2 = str(i).zfill(4)
            yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
