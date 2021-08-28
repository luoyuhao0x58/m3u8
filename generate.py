#! /usr/bin/python3
import os
import sys
import csv

TV_PATH = os.getenv("TV_PATH", './resources/tv.csv')

def main(tv_path):
    with open(tv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        spamreader = csv.DictReader(csvfile)
        print('#EXTM3U')
        for no, e in enumerate(spamreader):
            tags = [
                f'tvg-chno="{no}"',
            ]
            tvg_id = e["tvg-id"] if e["tvg-id"] else 'NO_%04d' % no
            tags.append(f'tvg-id="{tvg_id}"')
            if e["tvg-name"]:
                tags.append(f'tvg-name="{e["tvg-name"]}"')
            if e["logo"]:
                tags.append(f'tvg-logo="{e["logo"]}"')
            print(f'#EXTINF:-1 {" ".join(tags)},{e["name"]}')
            print(f'#EXTINF:{e["group"]}')
            print(e["url"])


if __name__ == '__main__':
    main(TV_PATH)
