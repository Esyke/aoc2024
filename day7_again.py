import re
import itertools


test_value_regex = r"(?P<test_value>\d*):"
operand_regex = r"\d+"
test_value_list = list()
operands_list = list()
possible_operator_list = ["+", "*"]
possible_operator_list_2 = ["+", "*", "|"]

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



def do_one_operation(operand_1, operand_2, operator):
    if operator == "+":
        return operand_1 + operand_2
    if operator == "*":
        return operand_1 * operand_2
    if operator == "|":
        return int(str(operand_1)+str(operand_2))

def count_valid_tests():
    counter = 0
    for i in range(len(test_value_list)):
        if operator_sequence_found(test_value_list[i], operands_list[i]):
            counter += test_value_list[i]
    return counter

def operator_sequence_found(test_value, operand_list):
    # operator_combinations = [list(tup) for tup in itertools.product(possible_operator_list, repeat=len(operand_list)-1)]  # part1
    operator_combinations = [list(tup) for tup in itertools.product(possible_operator_list_2, repeat=len(operand_list)-1)]  # part2
    for comb in operator_combinations:
        my_sum = operand_list[0]
        for i in range(len(operand_list)-1):
            if my_sum > test_value:
                break
            my_sum = do_one_operation(my_sum, operand_list[i+1], comb[i])
        if my_sum == test_value:
            return True
    return False


def day7():
    read_file("day7.txt")
    # read_file("day7small.txt")
    display_list(test_value_list)
    display_list(operands_list)
    final_sum_1 = count_valid_tests()
    print("-----")
    print(final_sum_1)


if __name__ == "__main__":
    day7()