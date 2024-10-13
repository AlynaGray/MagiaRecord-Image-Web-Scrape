#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/campaign/drop_up/"
    p3 = "/global_icon.png"
    for i in range(900, 2001):
        # Check leading zeroes
        for j in range(len(str(i)), 5):
            p2 = str(i).zfill(j)
            yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
