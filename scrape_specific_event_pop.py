#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    event_pops = ("magica/resource/image_web/common/global/event_pop.png",
                  "magica/resource/image_web/event/arenaRankMatch/common/event_pop.png",
                  "magica/resource/image_web/regularEvent/groupBattle/common2/event_pop.png",
                  "magica/resource/image_web/page/quest/puellaHistoria/top/event_pop.png",
                  "magica/resource/image_web/campaign/sumo/event_pop.png",
                  "magica/resource/image_web/test/aj2018/event_pop.png",
                  "magica/resource/image_web/event/arenaranking/common/event_pop.png")
    for i in event_pops:
        yield i

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
