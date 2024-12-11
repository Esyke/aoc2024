import math

full_matrix = []
string_to_find = "MAS"


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            full_matrix.append(next_line[:-1])


def search_matrix(my_matrix):
    counter = 0
    for x in range(len(my_matrix)):
        for y in range(len(my_matrix[0])):
            counter += search_from_coords(x, y, my_matrix)
    return counter


def search_from_coords(x, y, my_matrix):
    counter = 0.0
    if my_matrix[x][y] != string_to_find[1]:
        return counter
    else:
        coordinates = get_coordinates(x, y)
        if not are_all_coordinates_valid(0, 0, len(my_matrix) - 1, len(my_matrix[0]) - 1, coordinates):
            return counter
        for vector in coordinates:
            if strings_match_forward_or_backward(build_string_by_vector(vector, my_matrix), string_to_find):
                counter += 0.5
        return int(math.floor(counter))

def strings_match_forward_or_backward(string1, string2):
    if string1 == string2:
        return True
    if string1 == string2[::-1]:
        return True
    return False

def get_coordinates(x, y):
    coordinates = list()
    coordinates.append([(x - 1, y - 1), (x, y), (x + 1, y + 1)])
    coordinates.append([(x - 1, y + 1), (x, y), (x + 1, y - 1)])
    return coordinates

def are_all_coordinates_valid(min_x, min_y, max_x, max_y, coordinates):
    for vector in coordinates:
        for coo in vector:
            if not min_x <= coo[0] <= max_x:
                return False
            if not min_y <= coo[1] <= max_y:
                return False
    return True

def build_string_by_vector(vector, my_matrix):
    string_built = ""
    for coo in vector:
        string_built += my_matrix[coo[0]][coo[1]]
    return string_built


def day4_part2():
    read_file("day4.txt")
    display_list(full_matrix)
    final_sum_2 = search_matrix(full_matrix)
    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day4_part2()
    # x = 5
    # y = 15
    # coordinates = list()
    # coordinates.append([(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
    # coordinates.append([(x, y), (x, y - 1), (x, y - 2), (x, y - 3)])
    # display_list(coordinates)