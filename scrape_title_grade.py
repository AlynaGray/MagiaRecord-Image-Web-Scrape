#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/common/grade/title_"
    p4 = "00"
    p6 = ".png"
    for i in range(0, 10):
        p2 = str(i)
        for j in range(0, 100):
            p3 = str(j)
            for k in range(0, 10):
                p5 = str(k)
                yield f"{p1}{p2}{p3}{p4}{p5}{p6}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
