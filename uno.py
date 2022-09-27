from genericpath import isdir
import os
from pprint import pprint
from unittest.mock import patch

def main():
    path = '/Users/fer/Downloads'
    files = os.listdir(path)
    pprint("Todos los archivos son: ")
    pprint(files)

    for p in files:
        if os.path.isdir(p):
            print(p)
        else:
            print("")


if __name__ == "__main__":
    main()