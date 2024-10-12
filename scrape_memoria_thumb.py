#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/dailytower/common/memoria_thumb_s"
    p3 = "_"
    p5 = ".png"
    for i in range(0, 21):
        p2 = str(i)
        for j in (1, 2):
            p4 = str(j)
            yield f"{p1}{p2}{p3}{p4}{p5}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
