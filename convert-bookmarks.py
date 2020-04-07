#!/usr/bin/env python
#
# Convert browser bookmark export (NETSCAPE-Bookmark-file-1 format) to json
#
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json

parser = ArgumentParser(description='Convert Netscape bookmarks to JSON')
parser.add_argument(dest='filenames', metavar='filename', nargs='+')
parser.add_argument('-t', '--tag', metavar='tag', dest='tags',
                    action='append', help='add tag to bookmarks, repeat \
                                           for multiple tags')
args = parser.parse_args()

for filename in args.filenames:
    soup = BeautifulSoup(open(filename, encoding='utf8'), "html5lib")
    for link in soup.find_all('a'):
        bookmark = {}
        # url and title
        bookmark['url'] = link.get('href')
        bookmark['title'] = link.string.strip() if link.string\
                                                else bookmark['url']
        # tags
        tags = link.get('tags')
        bookmark['tags'] = tags.split(',') if tags else []
        if args.tags:
            bookmark['tags'] += args.tags
        # comment
        sibling = link.parent.next_sibling
        bookmark['comment'] = \
            sibling.string.strip() if sibling and sibling.name == 'dd' \
        else ''
        print(json.dumps(bookmark, sort_keys=False, indent=4))
