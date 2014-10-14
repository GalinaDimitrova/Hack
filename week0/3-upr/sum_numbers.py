# sum_numbers.py
import sys

filename = sys.argv[1]
sum_num = 0
with open(filename, "r") as my_file:
    # we make a list with the arguments separated with " " in the file
    contents = my_file.read().split(" ")
    for number in contents:
        sum_num += int(number)
    print(sum_num)


def main():
    pass

if __name__ == '__main__':
    main()
