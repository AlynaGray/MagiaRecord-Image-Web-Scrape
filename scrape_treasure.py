#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/common/treasure/"
    for i in ("bronze", "silver", "gold"):
        p2 = i
        for j in (".png", "_close.png", "_open.png"):
            p3 = j
            yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
