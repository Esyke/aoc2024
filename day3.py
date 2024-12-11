import re

product_list = list()
product_list2 = list()

my_regex = r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)"
my_regex_to_delete = r"don't\(\).+?(?=do\(\))"
my_regex_to_sub = r"k"

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def get_sum_of_list(my_list):
    my_sum = 0
    for n in my_list:
        my_sum += int(n)
    return my_sum


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            matches = re.findall(my_regex, next_line)
            if matches is None:
                continue
            for m in matches:
                product_list.append((int(m[0]) * int(m[1])))

def read_file2(file_name):
    full_text = ""
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            full_text += next_line[:-1]
        # print(full_text)
        next_clean_line = re.sub(my_regex_to_delete,my_regex_to_sub, full_text)
        # print(next_clean_line)
        matches = re.findall(my_regex, next_clean_line)
        if matches is None:
            print("jaj")
            return
        for m in matches:
            product_list2.append((int(m[0]) * int(m[1])))

def day3_part1():
    read_file("day3.txt")
    final_sum_1 = get_sum_of_list(product_list)

    print("-----")
    print(final_sum_1)


def day3_part2():
    read_file2("day3.txt")
    final_sum_2 = get_sum_of_list(product_list2)

    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day3_part1()