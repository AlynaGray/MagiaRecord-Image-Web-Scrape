#! /usr/bin/env python3

from typing import Generator
from itertools import chain
import common

def candidates() -> Generator[str, None, None]:
    # hardcoded path in code
    yield "magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/1198/story_collection_title.png"

    p1 = "magica/resource/image_web/event/"
    p3 = "/"
    p5 = "/story_collection_title.png"
    for i in ("accomplish", "aprilfool2018", "arenaMission", "arenaRankMatch", "arenaranking", "branch", "dailytower", "dungeon", "eventWalpurgis", "eventWitch", "raid", "singleraid", "storyraid", "tower", "training"):
        p2 = i
        for j in range(10000):
            for k in range(len(str(j)), 5):
                p4 = str(j).zfill(k)
                yield f"{p1}{p2}{p3}{p4}{p5}"

    p1 = "magica/resource/image_web/regularEvent/"
    p3 = "/"
    p5 = "/story_collection_title.png"
    for i in ("accomplish", "extermination", "groupBattle"):
        p2 = i
        for j in range(10000):
            for k in range(len(str(j)), 5):
                p4 = str(j).zfill(k)
                yield f"{p1}{p2}{p3}{p4}{p5}"
    
    p1 = "magica/resource/image_web/campaign/story/"
    p3 = "/story_collection_title.png"
    for i in range(10000):
        for j in range(len(str(i)), 5):
            p2 = str(i).zfill(j)
            yield f"{p1}{p2}{p3}"

    p1 = "magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/"
    p3 = "/story_collection_title.png"
    for i in range(10000):
        for j in range(len(str(i)), 5):
            p2 = str(i).zfill(j)
            yield f"{p1}{p2}{p3}"


def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
