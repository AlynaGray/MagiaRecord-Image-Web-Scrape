#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/banner/common/banner_week_0"
    for i in range(0, 10):
        p2 = str(i)
        for j in range(0, 10):
            p3 = str(j)
            for k in ("_a.png", "_m.png"):
                p4 = k
                yield f"{p1}{p2}{p3}{p4}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
