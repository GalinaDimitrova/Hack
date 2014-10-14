# cat.py
import sys

filename = sys.argv[1]
my_file = open(filename, "r")
content = my_file.read()
print(content)
my_file.close()


def main():
    pass

if __name__ == '__main__':
    main()
