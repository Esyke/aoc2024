from array import *
full_matrix = []
string_to_find = "XMAS"

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
    counter = 0
    if my_matrix[x][y] != string_to_find[0]:
        return 0
    else:
        coordinates = get_coordinates(x, y)
        valid_coordinates = filter_valid_coordinates(0, 0, len(my_matrix) - 1, len(my_matrix[0]) - 1, coordinates)
        for vector in valid_coordinates:
            if build_string_by_vector(vector, my_matrix) == string_to_find:
                counter += 1
        return counter


def get_coordinates(x, y):
    coordinates = list()
    coordinates.append([(x,y), (x,y+1), (x,y+2), (x,y+3)])
    coordinates.append([(x,y), (x,y-1), (x,y-2), (x,y-3)])
    coordinates.append([(x,y), (x+1,y), (x+2,y), (x+3,y)])
    coordinates.append([(x,y), (x-1,y), (x-2,y), (x-3,y)])
    coordinates.append([(x,y), (x+1,y+1), (x+2,y+2), (x+3,y+3)])
    coordinates.append([(x,y), (x+1,y-1), (x+2,y-2), (x+3,y-3)])
    coordinates.append([(x,y), (x-1,y-1), (x-2,y-2), (x-3,y-3)])
    coordinates.append([(x,y), (x-1,y+1), (x-2,y+2), (x-3,y+3)])
    return coordinates

def filter_valid_coordinates(min_x, min_y, max_x, max_y, coordinates):
    valid_coordinates = list()
    for vector in coordinates:
        vector_looks_valid = True
        for coo in vector:
            if not min_x <= coo[0] <= max_x:
                vector_looks_valid = False
            if not min_y <= coo[1] <= max_y:
                vector_looks_valid = False
        if vector_looks_valid:
           valid_coordinates.append(vector)
    return valid_coordinates

def build_string_by_vector(vector, my_matrix):
    string_built = ""
    for coo in vector:
        string_built += my_matrix[coo[0]][coo[1]]
    return string_built


def day4_part1():
    read_file("day4.txt")
    display_list(full_matrix)
    final_sum_1 = search_matrix(full_matrix)
    print("-----")
    print(final_sum_1)


if __name__ == "__main__":
    day4_part1()
    # x = 5
    # y = 15
    # coordinates = list()
    # coordinates.append([(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
    # coordinates.append([(x, y), (x, y - 1), (x, y - 2), (x, y - 3)])
    # display_list(coordinates)