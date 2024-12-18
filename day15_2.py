import time
import copy

warehouse_map_list = list()
global instruction_list
robot_character = "@"
wall_character = "#"
empty_space_character = "."
old_box_character = "O"
box_left_character = "["
box_right_character = "]"


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        my_string = ""
        for c in line:
           my_string += c
        print(my_string)
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        my_string = ""
        for next_line in f:
            if wall_character in next_line:
                my_list = list()
                for c in next_line:
                    if c == wall_character:
                        my_list.append(wall_character)
                        my_list.append(wall_character)
                    elif c == old_box_character:
                        my_list.append(box_left_character)
                        my_list.append(box_right_character)
                    elif c == empty_space_character:
                        my_list.append(empty_space_character)
                        my_list.append(empty_space_character)
                    elif c == robot_character:
                        my_list.append(robot_character)
                        my_list.append(empty_space_character)
                warehouse_map_list.append(my_list.copy())
            else:
                my_string += next_line.strip()
        instruction_list = list(my_string)
    return instruction_list


def simulate_robot_route(my_warehouse_map_list, my_instruction_list):
    (
        robot_coordinate_row,
        robot_coordinate_column,
    ) = get_robot_info(my_warehouse_map_list)
    for instruction in my_instruction_list:
        (
            robot_coordinate_row,
            robot_coordinate_column,
        ) = next_move(
            robot_coordinate_row,
            robot_coordinate_column,
            instruction,
            my_warehouse_map_list,
        )


def count_characters(c, my_warehouse_map_list):
    count = 0
    for i in range(len(my_warehouse_map_list)):
        for j in range(len(my_warehouse_map_list[0])):
            if my_warehouse_map_list[i][j] == c:
                count += (100 * i + j)
    return count


def next_move(
        robot_coordinate_row,
        robot_coordinate_column,
        current_instruction_character,
        my_warehouse_map_list,
):
    next_coordinate_row = robot_coordinate_row
    next_coordinate_column = robot_coordinate_column
    diff_x = 0
    diff_y = 0

    if current_instruction_character == ">":
        diff_x = 1
    elif current_instruction_character == "v":
        diff_y = 1
    elif current_instruction_character == "<":
        diff_x = -1
    elif current_instruction_character == "^":
        diff_y = -1

    if diff_y == 0:
        while my_warehouse_map_list[next_coordinate_row][next_coordinate_column] not in (
                empty_space_character,
                wall_character,
        ):
            next_coordinate_column += diff_x
            next_coordinate_row += diff_y

        if (
                my_warehouse_map_list[next_coordinate_row][next_coordinate_column]
                == wall_character
        ):
            return robot_coordinate_row, robot_coordinate_column
        else:
            while not (
                    next_coordinate_column == robot_coordinate_column
                    and next_coordinate_row == robot_coordinate_row
            ):
                update_char_to(
                    next_coordinate_row,
                    next_coordinate_column,
                    my_warehouse_map_list[next_coordinate_row - diff_y][
                        next_coordinate_column - diff_x
                        ],
                    my_warehouse_map_list,
                )
                next_coordinate_column -= diff_x
                next_coordinate_row -= diff_y
            update_char_to(
                next_coordinate_row,
                next_coordinate_column,
                empty_space_character,
                my_warehouse_map_list,
            )
            return next_coordinate_row + diff_y, next_coordinate_column + diff_x
    else:
        if (
                my_warehouse_map_list[robot_coordinate_row+diff_y][robot_coordinate_column+diff_x]
                == wall_character
        ):
            return robot_coordinate_row, robot_coordinate_column
        elif (
                my_warehouse_map_list[robot_coordinate_row+diff_y][robot_coordinate_column+diff_x]
                == empty_space_character
        ):
            update_char_to(
                robot_coordinate_row+diff_y,
                robot_coordinate_column+diff_x,
                robot_character,
                my_warehouse_map_list,
            )
            update_char_to(
                robot_coordinate_row,
                robot_coordinate_column,
                empty_space_character,
                my_warehouse_map_list,
            )
            return robot_coordinate_row+diff_y, robot_coordinate_column+diff_x
        else:
            return doit(robot_coordinate_row, robot_coordinate_column, diff_y, my_warehouse_map_list)


def doit(robot_coordinate_row, robot_coordinate_column, diff_y, my_warehouse_map_list):
    found_a_wall = False
    next_coordinate_row = robot_coordinate_row + diff_y
    next_coordinate_column = robot_coordinate_column
    my_new_box_coordinates = list() # of x, y
    my_box_coordinates = list() # of x, y all the boxes we found in previous iterations
    my_affected_coordinates = list()
    my_affected_coordinates.append((next_coordinate_row, next_coordinate_column))
    while (not found_a_wall) and len(my_affected_coordinates) > 0:
        for coo in my_affected_coordinates:
            if my_warehouse_map_list[coo[0]][coo[1]] in (box_right_character, box_left_character):
                add_to_list(my_new_box_coordinates, (coo[0], coo[1]))
                if my_warehouse_map_list[coo[0]][coo[1]] == box_left_character:
                    add_to_list(my_new_box_coordinates, (coo[0], coo[1] + 1))
                else:
                    add_to_list(my_new_box_coordinates, (coo[0], coo[1] - 1))
        for coo in my_affected_coordinates:
            if my_warehouse_map_list[coo[0]][coo[1]] == wall_character:
                found_a_wall = True
                break
        my_affected_coordinates.clear()
        for box_coo in my_new_box_coordinates:
            my_affected_coordinates.append((box_coo[0] + diff_y, box_coo[1]))
            add_to_list(my_box_coordinates, box_coo)
        my_new_box_coordinates.clear()

    if found_a_wall:
        return robot_coordinate_row, robot_coordinate_column

    for box_coo in reversed(my_box_coordinates):
        # print(box_coo)
        update_char_to(box_coo[0] + diff_y, box_coo[1], my_warehouse_map_list[box_coo[0]][box_coo[1]], my_warehouse_map_list)
        update_char_to(box_coo[0], box_coo[1], empty_space_character, my_warehouse_map_list)

    update_char_to(
        robot_coordinate_row + diff_y,
        robot_coordinate_column,
        robot_character,
        my_warehouse_map_list,
    )
    update_char_to(
        robot_coordinate_row,
        robot_coordinate_column,
        empty_space_character,
        my_warehouse_map_list,
    )

    return robot_coordinate_row + diff_y, robot_coordinate_column

def add_to_list(my_list, my_element):
    if my_element not in my_list:
        my_list.append(my_element)

def update_char_to(
        coordinate_row, coordinate_column, char_to_use, my_warehouse_map_list
):
    # print(f"old char: {my_warehouse_map_list[coordinate_row][coordinate_column]}")
    my_warehouse_map_list[coordinate_row][coordinate_column] = char_to_use
    # print(f"new char: {my_warehouse_map_list[coordinate_row][coordinate_column]}")
    # print(f"row: {coordinate_row}, column: {coordinate_column}")


def get_robot_info(my_lab_map_list):  # x(row), y(column)  coordinates
    for i in range(len(my_lab_map_list)):
        if robot_character in my_lab_map_list[i]:
            return i, my_lab_map_list[i].index(robot_character)


def day15_part2():
    instruction_list = read_file("day15.txt")
    # instruction_list = read_file("day15small.txt")
    display_list(warehouse_map_list)
    simulate_robot_route(warehouse_map_list, instruction_list)
    display_list(warehouse_map_list)
    # display_list(instruction_list)
    final_sum_2 = count_characters(box_left_character, warehouse_map_list)
    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day15_part2()
