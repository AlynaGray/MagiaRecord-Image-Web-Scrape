#! /usr/bin/env python3

from typing import Generator
import common
import os

def candidates() -> Generator[str, None, None]:
    p1 = "magica/resource/image_web/common/treasure/event/"
    for dirpath, _, _ in os.walk("magica/resource/image_web/event"):
        p2 = dirpath.removeprefix("magica/resource/image_web/")
        p2 = p2.replace(os.path.sep, "_")
        p2 = p2.lower()
        for i in ("_key_close.png", "_key_open.png"):
            p3 = i
            yield f"{p1}{p2}{p3}"

    for dirpath, _, _ in os.walk("magica/resource/image_web/regularEvent"):
        p2 = dirpath.removeprefix("magica/resource/image_web/")
        for i in ("event", "regularEvent"):
            p2 = p2.replace("regularEvent", i)
            p2 = p2.replace(os.path.sep, "_")
            p2 = p2.lower()
            for j in ("_key_close.png", "_key_open.png"):
                p3 = j
                yield f"{p1}{p2}{p3}"


def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
