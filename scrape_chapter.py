#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/chapter/chapter_"
    for i in range(0, 100):
        for j in range(len(str(i)), 3):
            p2 = str(i).zfill(j)
            for k in (".png", "_a.png"):
                p3 = k
                yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
