#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/accomplish/"
    p3 = "/reward_list.png"
    for i in range(1000, 2001):
        p2 = str(i).zfill(4)
        yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
