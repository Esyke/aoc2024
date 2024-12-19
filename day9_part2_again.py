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

def unfurl_diskmap(compact_list):
    full_list = list()
    for i in range(len(compact_list)):
        for j in range(compact_list[i]):
            if i % 2 == 0:
                full_list.append(str(int(math.ceil(i/2))))
            else:
                full_list.append(empty_space_character)
    return  full_list

def defrag(my_full_list):
    end_index = len(my_full_list)
    while end_index > 0:
        start_index = 0
        end_index -= 1
        my_length = 0
        while start_index <= end_index:
            if not my_full_list[start_index] == empty_space_character:
                start_index += 1
                continue
            if my_full_list[end_index] == empty_space_character:
                end_index -= 1
                continue
            # find out length
            if my_length == 0:
                end_start_index = end_index
                while my_full_list[end_start_index] == my_full_list[end_index]:
                    end_start_index -=1
                    my_length += 1
                end_index = end_start_index+1
            #are there enough spaces
            start_end_index = start_index
            for i in range(my_length):
                if my_full_list[start_end_index] != my_full_list[start_index]:
                    break
                start_end_index += 1
            if start_end_index - start_index != my_length:
                start_index += 1
                continue
            #swappy swappy
            for i in range(my_length):
                my_full_list[start_index] = my_full_list[end_index]
                my_full_list[end_index] = empty_space_character
                start_index += 1
                end_index += 1
            end_index = end_index - my_length + 1
            break
            # start_index += 1
            # end_index -= 1

    return my_full_list

def get_checksum(my_full_list):
    counter = 0
    for i in range(len(my_full_list)):
        if my_full_list[i] != empty_space_character:
            counter += (i*int(my_full_list[i]) )
    return counter


def day9_part1():
    # dense_diskmap_list = read_file("day9.txt")
    # dense_diskmap_list = read_file("day9small.txt")
    dense_diskmap_list = read_file("day9dbg.txt")  # should be 97898222299196, thank you!
    # credit to https://www.reddit.com/user/Standard_Bar8402/

    display_list_as_one_line(dense_diskmap_list)
    full_diskmap_list = unfurl_diskmap(dense_diskmap_list)
    display_list_as_one_line(full_diskmap_list)
    defragmented_list = defrag(full_diskmap_list.copy())
    final_sum_2 = get_checksum(defragmented_list)
    display_list_as_one_line(defragmented_list)
    print(len(defragmented_list))

    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day9_part1()
