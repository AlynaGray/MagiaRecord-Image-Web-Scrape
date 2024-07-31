#! /usr/bin/env python3

from typing import Generator
import common

def memoria_candidates() -> Generator[str, None, None]:
    part1 = "magica/resource/image_web/memoria/memoria_"
    part3 = "_s.png"
    for i in range(1000, 10000):
        part2 = str(i).zfill(4)
        yield f"{part1}{part2}{part3}"

def main():
    common.scrape_all(memoria_candidates)

if __name__ == "__main__":
    main()
