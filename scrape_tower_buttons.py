#! /usr/bin/env python3

from typing import Generator
import common

def tower_button_candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/event/tower/"
    p3 = "/tab_"
    for i in range(10000):
        p2 = str(i).zfill(4)
        for p4 in ["normal", "challenge"]:
            for part5 in ["_on.png", "_off.png"]:
        yield f"{p1}{p2}{p3}{p4}"

def main():
    common.scrape_all(tower_button_candidates)

if __name__ == "__main__":
    main()
