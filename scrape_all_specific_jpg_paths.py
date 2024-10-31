#! /usr/bin/env python3

import common

def main():
    pattern = "magica/resource/image_web[-a-zA-Z0-9_/]*\.jpg"
    common.scrape_all_regex("bella_donna", pattern)
    common.scrape_all_regex("puella-historia", pattern)
    common.scrape_all_regex("MITaMa", pattern)

if __name__ == "__main__":
    main()
