#! /usr/bin/env python3

from typing import Generator
import common

def main():
    common.scrape_all_in_dirs("navi_01.png")
    for i in range(0, 14):
        p2 = str(i).zfill(2)
        filename = f"navi_{p2}.png"
        common.scrape_all_in_dirs(filename, "navi_01.png")
    common.scrape_all_in_dirs("navi_02_a.png", "navi_01.png")
    common.scrape_all_in_dirs("navi_03_a.png", "navi_01.png")

if __name__ == "__main__":
    main()
