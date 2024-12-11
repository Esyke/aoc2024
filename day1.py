import re
import math

list1 = list()
list2 = list()
list_distances = list()
list_simscore = list()
my_regex = r"(?P<num1>\d*)\s*(?P<num2>\d*)"

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if not re.match(my_regex, next_line):
                print("PROBLEM")
                return
            match = re.search(my_regex, next_line)
            list1.append(int(match.group("num1")))
            list2.append(int(match.group("num2")))

def get_sum_of_both_lists(l1, l2, l3):
    for n in range(len(l1)):
        l3.append(math.fabs(l1[n] - l2[n]))

def get_sum_of_list(l3):
    my_sum = 0
    for n in l3:
        my_sum += int(n)
    return my_sum



def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def count_instances_of_num_in_list(n, l1):
    counter = 0
    for number in l1:
        if number == n:
            counter += 1
    return counter

def day1_part1():
    read_file("day1.txt")
    # display_list(list1)
    # display_list(list2)
    list1.sort()
    list2.sort()
    get_sum_of_both_lists(list1, list2, list_distances)
    # display_list(list_distances)
    final = get_sum_of_list(list_distances)
    print("-----")
    print(final)

def day1_part2():
    read_file("day1.txt")
    for number in list1:
        list_simscore.append(int(number*count_instances_of_num_in_list(number, list2)))
    final = get_sum_of_list(list_simscore)
    print(final)



if __name__ == "__main__":
    print("hi")
    # day1_part1()
    day1_part2()


    # list_yay = list()
    # list_yay.append(2)
    # list_yay.append(1)
    # list_yay.append(5)
    # list_yay.append(4)
    # display_list(list_yay)
    # list_yay.sort()
    # display_list(list_yay)
