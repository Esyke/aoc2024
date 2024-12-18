warehouse_map_list = list()
global instruction_list
robot_character = "@"
wall_character = "#"
empty_space_character = "."
box_character = "O"


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        my_string = ""
        for next_line in f:
            if wall_character in next_line:
                warehouse_map_list.append(list(next_line[:-1]))
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
                count = count + (100 * i + j)
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


def update_char_to(
        coordinate_row, coordinate_column, char_to_use, my_warehouse_map_list
):
    my_warehouse_map_list[coordinate_row][coordinate_column] = char_to_use


def get_robot_info(my_lab_map_list):  # x(row), y(column)  coordinates
    for i in range(len(my_lab_map_list)):
        if robot_character in my_lab_map_list[i]:
            return i, my_lab_map_list[i].index(robot_character)


def day15_part1():
    instruction_list = read_file("day15.txt")
    # instruction_list = read_file("day15small.txt")
    simulate_robot_route(warehouse_map_list, instruction_list)
    final_sum_1 = count_characters(box_character, warehouse_map_list)
    print("-----")
    print(final_sum_1)


if __name__ == "__main__":
    day15_part1()
