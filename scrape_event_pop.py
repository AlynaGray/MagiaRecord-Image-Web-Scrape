#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/"
    p3 = "/"
    p5 = "/event_pop.png"
    for i in ("accomplish", "aprilfool2018", "arenaMission", "arenaRankMatch", "arenaranking", "branch", "dailytower", "dungeon", "eventWalpurgis", "eventWitch", "raid", "singleraid", "storyraid", "tower", "training"):
        p2 = i
        for j in range(1000, 1401):
            p4 = str(j).zfill(4)
            yield f"{p1}{p2}{p3}{p4}{p5}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
