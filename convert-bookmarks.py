#!/usr/bin/env python
#
# Convert browser bookmark export (NETSCAPE-Bookmark-file-1 format) to json
#
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import json


parser = ArgumentParser(description='Convert Netscape bookmarks to JSON')
parser.add_argument(dest='filenames', metavar='filename', nargs='+')
parser.add_argument('-t', '--tag', metavar='tag', dest='tags',
                    action='append', help='add tag to bookmarks, repeat \
                                           for multiple tags')
parser.add_argument('-m', '--mongodb', action='store_true', dest='mongo',
                    help='output in mongodb import format')
args = parser.parse_args()

for filename in args.filenames:
    soup = BeautifulSoup(open(filename, encoding='utf8'), "html5lib")
    for link in soup.find_all('a'):
        bookmark = {}
        bookmark['url'] = link.get('href')
        bookmark['title'] = link.string.strip()
        secs = link.get('add_date')
        date = datetime.fromtimestamp(int(secs), tz=timezone.utc)
        bookmark['add_date'] = {'$date': date.isoformat()} if args.mongo \
            else date.isoformat()
        bookmark['tags'] = link.get('tags').split(',')
        if args.tags:
            bookmark['tags'] += args.tags
        sibling = link.parent.next_sibling
        if sibling and sibling.name == 'dd':
            bookmark['comment'] = sibling.string.strip()
        print(json.dumps(bookmark, sort_keys=False, indent=4))
