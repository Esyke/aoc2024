from dataclasses import dataclass

all_antennas = dict()
antinodes_set = set()

@dataclass
class Position:
    col: int
    row: int

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __eq__(self, other):
        if self.col == other.col and self.row == other.row:
            return True
        return False

    def __str__(self):
        return f"[{self.col};{self.row}]"

    def __add__(self, other):
        row = self.row + other.row
        col = self.col + other.col
        return Position(col, row)

    def __sub__(self, other):
        row = self.row - other.row
        col = self.col - other.col
        return Position(col, row)

    def __hash__(self):
        return (hash(self.row)+7) * (hash(self.col)+29)


class Antenna:
    position: Position
    frequency: str
    def __init__(self, col, row, freq):
        self.position = Position(col, row)
        self.frequency = freq

    def __str__(self):
        return f"{self.position} - ({self.frequency})"

def read_file(file_name):
    global MAX_COL, MAX_ROW
    with open(f"inputs/{file_name}", "r") as f:
        all = f.read().splitlines()
        MAX_COL = len(all)
        MAX_ROW = len(all[0])
        for i in range(MAX_COL):
            for j in range(MAX_ROW):
                if all[i][j] != ".":
                    antenna = Antenna(i, j, all[i][j])
                    print(antenna)
                    if all[i][j] not in all_antennas.keys():
                        all_antennas[all[i][j]] = list()
                    all_antennas[all[i][j]].append(antenna)


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def display_dict(my_dict):
    print("--------------------------------------")
    for k, v in my_dict.items():
        print(f"{k}: {','.join(str(x) for x in v)}") # very omg much wow
    print("######################################")
    print("\n")

def determine_antinodes(antennas_dict):
    for k, v in antennas_dict.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                new_antinodes = get_antinodes(v[i], v[j])
                for n in new_antinodes:
                    antinodes_set.add(n)


def get_antinodes(antenna_1, antenna_2):
    new_antinodes = list()
    diff_point = antenna_1.position - antenna_2.position
    p1 = antenna_1.position + diff_point
    p2 = antenna_2.position - diff_point
    for p in (p1, p2):
        if is_this_position_valid(p, MAX_COL, MAX_ROW):
            new_antinodes.append(p)
    
    return new_antinodes


def is_this_position_valid(pos: Position, max_col, max_row):
    if 0 <= pos.col < max_col and 0 <= pos.row < max_row:
        return True
    return False

def day8_part1():
    read_file("day8.txt")
    # read_file("day8small.txt")
    display_dict(all_antennas)
    display_list(antinodes_set)
    determine_antinodes(all_antennas)

    final_sum_1 = len(antinodes_set)

    print("-----")
    print(final_sum_1)


if __name__ == "__main__":
    day8_part1()
