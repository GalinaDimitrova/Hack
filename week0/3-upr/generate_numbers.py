# generate_numbers.py
import sys
from random import randint

filename = sys.argv[1]
number = int(sys.argv[2])
# using " with - as  we don't have to use .close() to close the file \
# after that
# " w " -- Opens a file for writing only. Overwrites the file if the \
# file exists. If the file does not exist, creates a new file \
# for writing.
with open(filename, "w") as my_file:
    for i in range(number):
        my_file.write(" ".join(str(randint(1, 1000))))


def main():
    pass

if __name__ == '__main__':
    main()
