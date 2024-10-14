#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/announce/announce_"
    p5 = ".png"
    for i in range(0, 1200):
        for j in range(len(str(i)), 5):
            p2 = str(i).zfill(j)
            for k in ("", "_1", "_2", "_3"):
                p3 = k
                for w in ("", "_a", "_b"):
                    p4 = w
                    yield f"{p1}{p2}{p3}{p4}{p5}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
