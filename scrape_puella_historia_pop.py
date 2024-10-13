#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/page/quest/puellaHistoria_lastBattle/event/"
    p3 = "/event_pop.png"
    for i in range(1000, 2001):
        p2 = str(i).zfill(4)
        yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
