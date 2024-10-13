#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/page/quest/puellaHistoria_lastBattle/result/_number/b_num_"
    p3 = ".png"
    for i in range(0, 201):
        # Try out leading zeros just in case they're necessary
        for j in range(len(str(i)), 4):
            p2 = str(i).zfill(j)
            yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
