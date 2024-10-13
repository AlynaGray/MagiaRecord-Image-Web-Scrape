#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/page/quest/main/titleBg/bg_chapter_"
    p4 = ".png"
    for i in ("", "challenge_"):
        p2 = i
        for j in range(0, 201):
            # Check leading zeroes
            for k in range(len(str(j)), 4):
                p3 = str(j).zfill(k)
                yield f"{p1}{p2}{p3}{p4}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
