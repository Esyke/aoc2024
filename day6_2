import time
import copy

warehouse_map_list = list()
instruction_list = list()
guard_character_list = ['<', '^', '>', 'v']
wall_character = "#"
empty_space_character = "."
seen_tile_character = "X"
max_time_elapsed = 1


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            warehouse_map_list.append(list(next_line[:-1]))


def simulate_guard_route(my_lab_map_list):
    (
        guard_coordinate_row,
        guard_coordinate_column,
        guard_current_character,
    ) = get_guard_info(my_lab_map_list)
    start = time.time()
    is_stuck = False
    counter = 0
    while guard_current_character != -1 and not is_stuck:
        (
            guard_coordinate_row,
            guard_coordinate_column,
            guard_current_character,
        ) = next_move(
            guard_coordinate_row, guard_coordinate_column, guard_current_character, my_lab_map_list
        )
        is_stuck = stuck_in_a_loop(start, max_time_elapsed)
        counter += 1
    print(f"took {counter} moves")
    print(f"stuck: {is_stuck}")
    if is_stuck:
        return 1
    return 0


def stuck_in_a_loop(start_time, max_time):
    now_time = time.time()
    if now_time - start_time < max_time:
        return False
    else:
        return True


def count_characters(c, my_lab_map_list):
    count = 0
    for row in my_lab_map_list:
        for col in row:
            if col == c:
                count += 1
    return count


def next_move(guard_coordinate_row, guard_coordinate_column, guard_current_character, my_lab_map_list):
    next_coordinate_row = guard_coordinate_row
    next_coordinate_column = guard_coordinate_column
    if guard_current_character == ">":
        next_coordinate_column += 1
    elif guard_current_character == "v":
        next_coordinate_row += 1
    elif guard_current_character == "<":
        next_coordinate_column -= 1
    elif guard_current_character == "^":
        next_coordinate_row -= 1

    if not is_it_in_bounds(next_coordinate_row, next_coordinate_column, my_lab_map_list):
        update_char_to(
            guard_coordinate_row, guard_coordinate_column, seen_tile_character, my_lab_map_list
        )
        return -1, -1, -1
    else:
        if my_lab_map_list[next_coordinate_row][next_coordinate_column] in (
                empty_space_character,
                seen_tile_character,
        ):
            update_char_to(
                next_coordinate_row, next_coordinate_column, guard_current_character, my_lab_map_list
            )
            update_char_to(
                guard_coordinate_row, guard_coordinate_column, seen_tile_character, my_lab_map_list
            )
            return next_coordinate_row, next_coordinate_column, guard_current_character
        else:
            guard_next_character = guard_character_list[
                (guard_character_list.index(guard_current_character) + 1)
                % len(guard_character_list)
            ]
            update_char_to(
                guard_coordinate_row, guard_coordinate_column, guard_next_character, my_lab_map_list
            )
            return guard_coordinate_row, guard_coordinate_column, guard_next_character


def update_char_to(coordinate_row, coordinate_column, char_to_use, my_lab_map_list):
    my_lab_map_list[coordinate_row][coordinate_column] = char_to_use


def is_it_in_bounds(next_coordinate_row, next_coordinate_column, my_lab_map_list):
    if (0 <= next_coordinate_column < len(my_lab_map_list[0])) and (
        0 <= next_coordinate_row < len(my_lab_map_list)
    ):
        return True
    else:
        return False


def get_guard_info(my_lab_map_list):  # x, y  coordinates and character of direction
    for i in range(len(my_lab_map_list)):
        for char in guard_character_list:
            if char in my_lab_map_list[i]:
                return i, my_lab_map_list[i].index(char), char


def get_all_possible_obstructions(my_lab_map_list):
    counter = 0
    for i in range(len(my_lab_map_list)):
        for j in range(len(my_lab_map_list[i])):
            if my_lab_map_list[i][j] == empty_space_character:
                my_copy = copy.deepcopy(my_lab_map_list)
                my_copy[i][j] = wall_character
                counter += simulate_guard_route(my_copy)
    return counter


def day6_part2():
    read_file("day6.txt")
    # read_file("day6small.txt")
    # display_list(lab_map_list)
    final_sum_2 = get_all_possible_obstructions(warehouse_map_list)
    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day6_part2()
