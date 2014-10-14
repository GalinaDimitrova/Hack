# cat.py
import sys
# items in sys.argv[] are the names of the files we want to read
for i in range(1, len(sys.argv)):
    my_file = open(sys.argv[i], "r")
    content = my_file.read()
    print(content)
    # print("\n")
    my_file.close()


def main():
    pass

if __name__ == '__main__':
    main()
