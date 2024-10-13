#! /usr/bin/env python3

from typing import Generator
import common
from itertools import chain

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/"
    p3 = "/"
    p5 = "/navi_01.png"
    for i in ("accomplish", "aprilfool2018", "arenaMission", "arenaRankMatch", "arenaranking", "branch", "dailytower", "dungeon", "eventWalpurgis", "eventWitch", "raid", "singleraid", "storyraid", "tower", "training"):
        p2 = i
        for j in range(1000, 1401):
            p4 = str(j).zfill(4)
            yield f"{p1}{p2}{p3}{p4}{p5}"

    p1 = "magica/resource/image_web/regularEvent/"
    p3 = "/"
    p5 = "/navi_01.png"
    for i in ("accomplish", "extermination"):
        p2 = i
        for j in range(1900, 2101):
            p4 = str(j).zfill(4)
            yield f"{p1}{p2}{p3}{p4}{p5}"

    p1 = "magica/resource/image_web/regularEvent/groupBattle/"
    p3 = "/navi_01.png"
    for i in chain(range(1900, 2201), range(5900, 6601)):
        p2 = str(i).zfill(4)
        yield f"{p1}{p2}{p3}"


def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
