#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/banner/announce/banner_"
    p4 = "_m.png"
    for i in range(0, 2201):
        p2 = str(i).zfill(4)
        for i in ("", "_1", "_2"):
            p3 = i
            yield f"{p1}{p2}{p3}{p4}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
