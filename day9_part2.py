import math

empty_space_character = "."

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        all_list = list(int(x) for x in f.read().strip())
    return all_list


def display_list_as_one_line(my_list):
    print("--------------------------------------")
    print(*my_list)
    print("######################################")
    print("\n")

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")

def unfurl_diskmap(compact_list):
    full_list = list()
    for i in range(len(compact_list)):
        new_list = list()
        for j in range(compact_list[i]):
            if i % 2 == 0:
                new_list.append(str(int(math.ceil(i/2))))
            else:
                new_list.append(empty_space_character)
        if new_list:
            full_list.append(new_list.copy())
    return  full_list

def defrag(my_full_list):
    end_index = len(my_full_list)
    while end_index > 0:
        start_index = 0
        end_index -= 1
        while start_index < end_index:
            if not (my_full_list[start_index][0] == empty_space_character and len(my_full_list[start_index]) >= len(my_full_list[end_index])):
                start_index += 1
                continue
            if my_full_list[end_index][0] == empty_space_character:
                end_index -= 1
                continue
            for temp_index in range(len(my_full_list[end_index])):
                my_full_list[start_index][temp_index] = my_full_list[end_index][temp_index]
                my_full_list[end_index][temp_index] = empty_space_character
            if len(my_full_list[end_index]) != len(my_full_list[start_index]):
                first_list = my_full_list[start_index].copy()[:len(my_full_list[end_index])]
                second_list = my_full_list[start_index].copy()[len(my_full_list[end_index]):]
                my_full_list[start_index] = first_list.copy()
                my_full_list.insert(start_index+1, second_list.copy())
                end_index += 1
                start_index -= 1
            #update end
            empty_list = my_full_list[end_index].copy()
            if end_index + 1 < len(my_full_list) and my_full_list[end_index+1][0] == empty_space_character:
                empty_list += my_full_list[end_index+1].copy()
                my_full_list.pop(end_index+1)
            if my_full_list[end_index-1][0] == empty_space_character:
                empty_list += my_full_list[end_index - 1].copy()
                my_full_list.pop(end_index - 1)
                end_index -= 1
            my_full_list[end_index] = empty_list.copy()
            break

    return my_full_list

def make_full_list(compact_list):
    full_list = list()
    for small_list in compact_list:
        for k in small_list:
            full_list.append(k)
    return full_list

def get_checksum(my_full_list):
    counter = 0
    for i in range(len(my_full_list)):
        if my_full_list[i] != empty_space_character:
            counter += (i*int(my_full_list[i]) )
    return counter


def day9_part2():
    dense_diskmap_list = read_file("day9.txt")
    # dense_diskmap_list = read_file("day9small.txt")
    # dense_diskmap_list = read_file("day9dbg.txt")  # should be 97898222299196, thank you!
    # credit to https://www.reddit.com/user/Standard_Bar8402/

    # display_list_as_one_line(dense_diskmap_list)
    compact_diskmap_list = unfurl_diskmap(dense_diskmap_list)
    # display_list(compact_diskmap_list)

    defragmented_list = defrag(compact_diskmap_list.copy())
    full_defragmented_list = make_full_list(defragmented_list)
    final_sum_2 = get_checksum(full_defragmented_list)
    # display_list(defragmented_list)
    # display_list_as_one_line(full_defragmented_list)
    # print(len(full_defragmented_list))

    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day9_part2()
    # a = [1, 3, 4, "2"]
    # b = [1, 3, 4, "2"]
    # print(a+b)