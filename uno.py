import os
from pprint import pprint
from unittest.mock import patch

def main():
    path= '/Users/fer/Downloads'
    files = os.listdir(path)
    #pprint(files)
    for p in files:
        print(p)


if __name__ == "__main__":
    main()