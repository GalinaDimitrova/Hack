# concat_files.py
import sys

to_file = open("MEGATRON.txt", "a")

for i in range(1, len(sys.argv)):
    from_file = open(sys.argv[i], "r")
    content = from_file.read()
    to_file.write(content + '\n')

    from_file.close()
to_file.close()


def main():
    pass

if __name__ == '__main__':
    main()
