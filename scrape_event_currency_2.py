#! /usr/bin/env python3

from typing import Generator
import common
import os

# This didn't actually scrape anything and doesn't correspond to everything. I made this after misreading a filepath.
# I'm leaving this here for informational purposes to show that there's nothing with this pattern.
def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/common/icon/event/"
    p4 = ".png"
    for dirpath, _, _ in os.walk("magica/resource/image_web/event"):
        p2 = dirpath.removeprefix("magica/resource/image_web/")
        p2 = p2.replace(os.path.sep, "_")
        p2 = p2.lower()
        for i in ("", "_exchange_1", "_exchange_2", "_exchange_destiny", "_coin", "_part_1", "_part_2", "_key", "_potion", "_key_open", "_key_close"):
            p3 = i
            yield f"{p1}{p2}{p3}{p4}"

    for dirpath, _, _ in os.walk("magica/resource/image_web/regularEvent"):
        p2 = dirpath.removeprefix("magica/resource/image_web/")
        p2 = p2.replace("regularEvent", "event")
        p2 = p2.replace(os.path.sep, "_")
        p2 = p2.lower()
        for i in ("", "_exchange_1", "_exchange_2", "_exchange_destiny", "_coin", "_part_1", "_part_2", "_key", "_potion", "_key_open", "_key_close"):
            p3 = i
            yield f"{p1}{p2}{p3}{p4}"


def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()