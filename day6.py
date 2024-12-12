import random
import re

lab_map_list = list()
guard_character_list = ['<', '^', '>', 'v']
obstacle_character = "#"
normal_tile_character = "."
seen_tile_character = "X"


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            lab_map_list.append(list(next_line[:-1]))


def simulate_guard_route():
    (
        guard_coordinate_row,
        guard_coordinate_column,
        guard_current_character,
    ) = get_guard_info()
    while guard_current_character != -1:
        (
            guard_coordinate_row,
            guard_coordinate_column,
            guard_current_character,
        ) = next_move(
            guard_coordinate_row, guard_coordinate_column, guard_current_character
        )


def count_characters(c):
    count = 0
    for row in lab_map_list:
        for col in row:
            if col == c:
                count += 1
    return count


def next_move(guard_coordinate_row, guard_coordinate_column, guard_current_character):
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

    if not is_it_in_bounds(next_coordinate_row, next_coordinate_column):
        update_char_to(
            guard_coordinate_row, guard_coordinate_column, seen_tile_character
        )
        return -1, -1, -1
    else:
        if lab_map_list[next_coordinate_row][next_coordinate_column] in (
            normal_tile_character,
            seen_tile_character,
        ):
            update_char_to(
                next_coordinate_row, next_coordinate_column, guard_current_character
            )
            update_char_to(
                guard_coordinate_row, guard_coordinate_column, seen_tile_character
            )
            return next_coordinate_row, next_coordinate_column, guard_current_character
        else:
            guard_next_character = guard_character_list[
                (guard_character_list.index(guard_current_character) + 1)
                % len(guard_character_list)
            ]
            update_char_to(
                guard_coordinate_row, guard_coordinate_column, guard_next_character
            )
            return guard_coordinate_row, guard_coordinate_column, guard_next_character


def update_char_to(coordinate_row, coordinate_column, char_to_use):
    lab_map_list[coordinate_row][coordinate_column] = char_to_use


def is_it_in_bounds(next_coordinate_row, next_coordinate_column):
    if (0 <= next_coordinate_column < len(lab_map_list[0])) and (
        0 <= next_coordinate_row < len(lab_map_list)
    ):
        return True
    else:
        return False


def get_guard_info():  # x, y  coordinates and character of direction
    for i in range(len(lab_map_list)):
        for char in guard_character_list:
            if char in lab_map_list[i]:
                return i, lab_map_list[i].index(char), char


def day6_part1():
    read_file("day6.txt")
    # read_file("day6small.txt")
    # display_list(lab_map_list)
    simulate_guard_route()
    final_sum_1 = count_characters(seen_tile_character)
    # print("-----")
    print(final_sum_1)
    # print("-----")


if __name__ == "__main__":
    day6_part1()
