#! /usr/bin/env python3

from typing import Generator
import common
import os
import re

def search_in_file(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            return []
        matches = re.findall(pattern, content)
        return matches

def search_recursively(directory, pattern):
    matches_found = []
    for dirpath, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(dirpath, file)
            try:
                matches = search_in_file(file_path, pattern)
                matches_found.extend(matches)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return matches_found


def candidates() -> Generator[str, None, None]:
    starting_points = ("bella_donna",
                       "puella-historia",
                       "MITaMa")
    for starting_point in starting_points:
        matches = search_recursively(starting_point, "magica/resource/image_web[-a-zA-Z0-9_/]*\.png")
        for m in matches:
            yield m

def main():
    common.scrape_all(candidates)

if __name__ == "__main__":
    main()
