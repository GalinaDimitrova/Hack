# wc.py
import sys

filename = sys.argv[2]
command = sys.argv[1]
with open(filename, "r") as my_file:
    if command == "chars":
        chars = my_file.read()
        print(len(chars))

    if command == "words":
        words = my_file.read().split(" ")
        print(len(words))

    if command == "lines":
        lines = my_file.read().split("\n")
        print(len(lines))


def main():
    pass

if __name__ == '__main__':
    main()
