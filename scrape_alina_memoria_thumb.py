#! /usr/bin/env python3

from typing import Generator
import common

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/eventWitch/common/alina_request/memoria_thumb_s4_"
    p3 = ".png"
    for i in range(0, 21):
        p2 = str(i)
        yield f"{p1}{p2}{p3}"

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
