import random
import re
import math


test_value_regex = r"(?P<test_value>\d*):"
operand_regex = r"\d+"
test_value_list = list()
operands_list = list()

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if re.match(test_value_regex, next_line):
                match = re.search(test_value_regex, next_line)
                test_value_list.append(int(match.group("test_value")))
                matches = re.findall(operand_regex, next_line.split(":")[1])
                my_operands = list()
                for m in matches:
                    my_operands.append(int(m))
                operands_list.append(my_operands)

# def generate_possible_operand_sequences(operand_count):
#     my_possible_operand_strings_list = list()
#

def count_valid_tests():
    counter = 0
    for i in range(len(test_value_list)):
        if operator_sequence_found(test_value_list[i], operands_list[i]):
            counter += 1
    return counter

def operator_sequence_found(test_value, operand_list):
    operator_list = ["/", "-"]
    my_operand_list = operand_list.copy()
    my_operand_list.append(test_value)
    current_value = test_value
    index = len(my_operand_list)-2
    while current_value != operand_list[0]:
        for op in operator_list:
            if is_this_value_possible(do_one_operation(current_value, my_operand_list[index], op)):
             current_value = do_one_operation(current_value, my_operand_list[index], op)
             index -= 1
            else:
                continue


    return True

def do_next():
    # ugh idk
    return

def is_this_value_possible(my_float):
    return my_float.is_integer()

def do_one_operation(operand_1, operand_2, operator):
    if operator == "/":
        return operand_1 / operand_2
    if operator == "-":
        return operand_1 - operand_2

def day7_part1():
    # read_file("day7.txt")
    read_file("day7small.txt")
    display_list(test_value_list)
    display_list(operands_list)
    final_sum_1 = count_valid_tests()
    print("-----")
    print(final_sum_1)



if __name__ == "__main__":
    day7_part1()