#! /usr/bin/env python3

from typing import Generator
import common
import os


## TODO
def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/item/event/"
    p3 ="_chara_"
    p5 = ".png"
    for dirpath, _, _ in os.walk("magica/resource/image_web/event/branch"):
        p2 = dirpath.removeprefix("magica/resource/image_web/")
        p2 = p2.replace(os.path.sep, "_")
        p2 = p2.lower()
        for i in range(10000):
            for j in range(len(str(i)), 5):
                p4 = str(i).zfill(j)
                yield f"{p1}{p2}{p3}{p4}{p5}"


def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
