#! /usr/bin/env python3

from typing import Generator
import common


def main():
    pattern = "magica/resource/image_web[-a-zA-Z0-9_/]*\.png"
    common.scrape_all_regex("bella_donna", pattern)
    common.scrape_all_regex("puella-historia", pattern)
    common.scrape_all_regex("MITaMa", pattern)

if __name__ == "__main__":
    main()
