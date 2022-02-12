#! /usr/bin/python3
import os
import sys
import csv

AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
TV_PATH = os.getenv("TV_PATH", './resources/tv.csv')

def main(tv_path):
    with open(tv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        spamreader = csv.DictReader(csvfile)
        print('#EXTM3U')
        for no, e in enumerate(spamreader, 1):
            tags = [
                f'group-title="{e["group"]}"',
                f'tvg-id="{e["tvg-id"]}"',
                f'tvg-name="{e["tvg-name"]}"',
            ]
            if e["logo"]:
                tags.append(f'tvg-logo="{e["logo"]}"')
            print(f'#EXTINF:-1 {" ".join(tags)},{e["name"]}')
            print(f'#EXTVLCOPT:http-user-agent={AGENT}')
            if e["referrer"]:
                print(f'#EXTVLCOPT:http-referrer={e["referrer"]}')
            print(e["url"])


if __name__ == '__main__':
    main(TV_PATH)
