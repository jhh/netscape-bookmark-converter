# Netscape Bookmark Converter

A Python tool to convert bookmark export files in [Netscape bookmark
format](https://msdn.microsoft.com/en-us/library/aa753582.aspx) into JSON.

## Requirements

1. Clone this repository and `cd netscape-bookmark-converter`.
2. Create a Python 3 virtual environment in the project directory: `python3 -m
venv venv`.
3. Activate virtual environment using script in the venv's script directory.
See Python [documentation page](https://docs.python.org/3/library/venv.html).
4. Install dependencies: `pip install -r requirements.txt`.
5. Get usage instructions: `./convert-bookmarks.py -h`

## Usage

```
$ ./convert-bookmarks.py -h
usage: convert-bookmarks.py [-h] [-t tag] [-m] [filename [filename ...]]

Convert Netscape bookmarks to JSON

positional arguments:
  filename

optional arguments:
  -h, --help         show this help message and exit
  -t tag, --tag tag  add tag to bookmarks
  -m, --mongodb      output in mongodb import format
```

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
