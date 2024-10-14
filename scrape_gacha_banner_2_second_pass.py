#! /usr/bin/env python3

from typing import Generator
import common
import os

def candidates() -> Generator[str, None, None]:
    preq1 = "magica/resource/image_web/gacha/gacha_"
    preq3 = "_banner.png"
    for i in range(0, 2201):
        preq2 = str(i).zfill(3)
        # Check if the preq exists
        if os.path.isfile(f"{preq1}{preq2}{preq3}"):
            for j in ("_banner_s.png", "_banner_l.png", "_card.png", "_card_a.png", "_detail.png"):
                p3 = j
                yield f"{preq1}{preq2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
