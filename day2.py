
def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    record = list()
    safe_record_count = 0
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            record = [int(x) for x in next_line.split(' ')]
            parity = -1
            if record[0] < record[1]:
                parity = 1
            if check_separation_by_num(record, 1, 3, parity):
                safe_record_count += 1
    return safe_record_count


def check_separation_by_num(rec, min_sep, max_sep, parity):
    # if we go up, the parity is positive
    for n in range(len(rec)-1):
        diff = rec[n+1] - rec[n]
        if not check_number_against_parity_and_sep(diff, min_sep, max_sep, parity):
            return False
    return True

def check_number_against_parity_and_sep(diff, min_sep, max_sep, parity):
    if min_sep <= diff*parity <= max_sep:
        return True
    else:
        return False

def determine_parity(rec):
    # 1 2 5 6
    p = 0
    for n in range(4):
        if rec[n] < rec[n+1]:
            p += 1
        if rec[n] > rec[n+1]:
            p -= 1
    if p > 0:
        return 1
    else:
        return -1

def check_separation_by_num2(rec, min_sep, max_sep, parity):
    # if we go up, the parity is positive
    element_to_remove = 0
    lets_remove = False
    for n in range(len(rec)-1):
        diff = rec[n+1] - rec[n]
        if not check_number_against_parity_and_sep(diff, min_sep, max_sep, parity):
            # modify rec and try again
            element_to_remove = n
            lets_remove = True
            break
    if not lets_remove:
        return True

    rec_copy1 = rec.copy()
    rec_copy2 = rec.copy()

    rec_copy1.pop(element_to_remove)
    rec_copy2.pop(element_to_remove + 1)

    is_1_bad = False
    is_2_bad = False
    for n in range(len(rec_copy1)-1):
        diff = rec_copy1[n+1] - rec_copy1[n]
        if not check_number_against_parity_and_sep(diff, min_sep, max_sep, parity):
            is_1_bad = True
            break
    for n in range(len(rec_copy2)-1):
        diff = rec_copy2[n+1] - rec_copy2[n]
        if not check_number_against_parity_and_sep(diff, min_sep, max_sep, parity):
            is_2_bad = True
            break

    if not is_1_bad or not is_2_bad:
        return True
    return False

def read_file2(file_name):
    record = list()
    safe_record_count = 0
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            record = [int(x) for x in next_line.split(' ')]
            parity = determine_parity(record)
            if check_separation_by_num2(record, 1, 3, parity):
                safe_record_count += 1
    return safe_record_count


def day2_part1():
    final_sum_1 = read_file("day2.txt")

    print("-----")
    print(final_sum_1)


def day2_part2():
    final_sum_2 = read_file2("day2.txt")

    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day2_part2()

