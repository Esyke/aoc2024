import re

MAP_SIZE_X = 101
# MAP_SIZE_X = 11 #small
MAP_SIZE_Y = 103
# MAP_SIZE_Y = 7 #small

my_regex = r"p=(?P<px>(-){0,1}\d+),(?P<py>(-){0,1}\d+)\sv=(?P<vx>(-){0,1}\d+),(?P<vy>(-){0,1}\d+)"
robot_list = list()


class Robot:
    def __init__(self, start_x, start_y, vector_x, vector_y):
        self.start_x_coo = start_x
        self.start_y_coo = start_y
        self.current_x = start_x
        self.current_y = start_y
        self.vector_x = vector_x
        self.vector_y = vector_y

    def next_move(self):
        self.current_x = (self.current_x + self.vector_x) % MAP_SIZE_X
        self.current_y = (self.current_y + self.vector_y) % MAP_SIZE_Y

    def make_moves(self, move_count):
        for i in range(move_count):
            self.next_move()


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if not re.match(my_regex, next_line):
                print("PROBLEM")
                return
            else:
                match = re.search(my_regex, next_line)
                robot_list.append(Robot(int(match.group("px")), int(match.group("py")), int(match.group("vx")), int(match.group("vy"))))


def count_robots():
    count_list = [0, 0, 0, 0]
    for robot in robot_list:
        if robot.current_x < (MAP_SIZE_X-1) / 2 and robot.current_y < (MAP_SIZE_Y-1) / 2:
            count_list[0] += 1
        elif robot.current_x > (MAP_SIZE_X-1) / 2 and robot.current_y < (MAP_SIZE_Y-1) / 2:
            count_list[1] += 1
        elif robot.current_x > (MAP_SIZE_X-1) / 2 and robot.current_y > (MAP_SIZE_Y-1) / 2:
            count_list[2] += 1
        elif robot.current_x < (MAP_SIZE_X-1) / 2 and robot.current_y > (MAP_SIZE_Y-1) / 2:
            count_list[3] += 1
    count = 1
    for n in count_list:
        count *= n
    return count


def advance_all_robots_by_x_moves(move_count, my_robot_list):
    for robot in my_robot_list:
        robot.make_moves(move_count)


def advance_all_robots_by_one_move_x_times(move_count, my_robot_list):
    with open("my_log2.txt", 'a') as yay:
        for i in range(move_count):
            print(f"{i}----------------")
            yay.writelines(f"{i}----------------\n")
            for robot in my_robot_list:
                robot.make_moves(101)
            display_robots_map(my_robot_list, yay)


def day14_part1():
    read_file("day14.txt")
    # read_file("day14small.txt")
    advance_all_robots_by_x_moves(100, robot_list)
    # display_robots_map(robot_list)
    final_sum_1 = count_robots()

    print("-----")
    print(final_sum_1)


def day14_part2():
    read_file("day14.txt")
    # read_file("day14small.txt")
    advance_all_robots_by_x_moves(13, robot_list)
    # for x in range(100):
    advance_all_robots_by_one_move_x_times(100, robot_list)
    # advance_all_robots_by_x_moves(100, robot_list)
    # display_robots_map(robot_list)
    # final_sum_1 = count_robots()

    # print("-----")
    # print(final_sum_1)
    # I am ashamed but I hate this task so I dont really care :P 

def display_robots_map(my_robot_map, file = None):
    my_list = list()
    for i in range(MAP_SIZE_Y):
        new_list = list()
        for j in range(MAP_SIZE_X):
            new_list.append(0)
        my_list.append(new_list.copy())
    # for m in my_list:
    #     print(m)
    for robot in my_robot_map:
        my_list[robot.current_y][robot.current_x] += 1
    # print("-------------------")

    my_other_list = list()
    for i in range(MAP_SIZE_Y):
        new_list = list()
        for j in range(MAP_SIZE_X):
            if my_list[i][j] == 0:
                new_list.append(".")
            else:
                new_list.append("0")
        my_other_list.append(new_list.copy())

    for m in my_other_list:
        print(m)
        file.writelines(m)
        file.writelines("\n")


if __name__ == "__main__":
    day14_part2()
