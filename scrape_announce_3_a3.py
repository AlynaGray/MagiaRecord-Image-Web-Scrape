#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/announce/announce_"
    # Due to how long this is, the nested loops are reordered to prioritize more likely arrangements
    for k in (".png", ".png.png"):
        p7 = k
        p6 = "a"
        for i in range(0, 5):
            p5 = str(i)
            for year in range(17, 25):
                p2 = str(year).zfill(2)
                for month in range(0, 13):
                    p3 = str(month).zfill(2)
                    for day in range(0, 32):
                        p4 = str(day).zfill(2)
                        yield f"{p1}{p2}{p3}{p4}{p5}{p6}{p7}"
def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
