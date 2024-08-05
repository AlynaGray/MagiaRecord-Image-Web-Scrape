#! /usr/bin/env python3

from typing import Generator
import common

def tower_chara_candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/tower/"
    p3 = "/chara/chara_"
    p5 = ".png"
    for i in [1003, 1007, 1035, 1036]:
        p2 = str(i).zfill(4)
        for p4 in ["normal", "challenge"]:
            # This is not the correct format, still can't figure it out
            for j in range(0, 10):
                p4 = str(j)
                yield f"{p1}{p2}{p3}{p4}{p5}"
            for j in range(0, 100):
                p4 = str(j).zfill(2)
                yield f"{p1}{p2}{p3}{p4}{p5}"
            for j in range(0, 1000):
                p4 = str(j).zfill(3)
                yield f"{p1}{p2}{p3}{p4}{p5}"
            for j in range(0, 10000):
                p4 = str(j).zfill(4)
                yield f"{p1}{p2}{p3}{p4}{p5}"

def main():
    common.scrape_all(tower_chara_candidates)

if __name__ == "__main__":
    main()
