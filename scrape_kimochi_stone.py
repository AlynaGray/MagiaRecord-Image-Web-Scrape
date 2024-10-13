#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/regularEvent/groupBattle/"
    for i in range(5900, 6601):
        p2 = str(i).zfill(4)
        for j in ("/stone_off.png", "/stone_on.png"):
            p3 = j
            yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
