import sys


def Day2_problem1(file_name):
    horizontal = 0
    depth = 0

    with open(file_name) as file:
        for line in file:
            if line == '':
                break
            split_line = line.split()
            if split_line[0] == "down":
                depth = depth + int(split_line[1])
            elif split_line[0] == "up":
                depth = depth - int(split_line[1])
            elif split_line[0] == "forward":
                horizontal = horizontal + int(split_line[1])

    return horizontal * depth


if __name__ == "__main__":
    horizontal_depth = Day2_problem1(sys.argv[1])
    print(str(horizontal_depth))