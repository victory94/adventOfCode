import math
import sys
import numpy as np
from collections import deque


def Day9Problem(file_name):
    list_of_numbers = []
    with open(file_name) as file:
        list_of_numbers = list(np.array([[int(val) for val in list(line.rstrip())] for line in file.readlines()]))
    index_of_low_point = []
    sum_of_risk = 0
    for index, line in enumerate(list_of_numbers):
        if index == 0:
            sum_of_risk_1, indexes = lowest_first(index, line, list_of_numbers)
            index_of_low_point.extend(indexes)
            sum_of_risk = sum_of_risk + sum_of_risk_1
        elif index == len(list_of_numbers) -1 :
            sum_of_risk_1, indexes =  lowest_last(index, line, list_of_numbers)
            index_of_low_point.extend(indexes)
            sum_of_risk = sum_of_risk + sum_of_risk_1
        else:
            sum_of_risk_1, indexes =  lowest(index,line, list_of_numbers)
            index_of_low_point.extend(indexes)
            sum_of_risk = sum_of_risk + sum_of_risk_1
    basins = []
    for index in index_of_low_point:
        basins.append(len(find_basin(list_of_numbers, index[0], index[1])))
    return sum_of_risk, math.prod(sorted(basins, reverse=True)[:3])


def surrounding(input, x, y):
    vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]


def find_basin(input, x, y):
    basin = []
    visited = set()
    queue = deque([(x, y)])

    while queue:
        (x_i, y_i) = queue.pop()

        if (x_i, y_i) in visited:
            continue
        else:
            visited.add((x_i, y_i))
            if input[x_i][y_i] != 9:
                basin.append((x_i, y_i))
                queue.extend([(x_j, y_j) for (x_j, y_j) in surrounding(input, x_i, y_i) if (x_j, y_j) not in visited])

    return basin


def lowest_first(index, line, list):
    risk_of_line = 0
    indexes = []
    for index1, number in enumerate(line):
        if index1 == 0:
            if number < line[index1 +1] and number < list[index + 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        elif index1 == len(line) -1:
            if number < line[index1 -1] and number < list[index + 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        else:
            if number < line[index1 -1] and number < list[index + 1][index1] and number < line[index1 +1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
    return risk_of_line, indexes


def lowest_last(index, line, list):
    risk_of_line = 0
    indexes = []
    for index1, number in enumerate(line):
        if index1 == 0:
            if number < line[index1 +1] and number < list[index - 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        elif index1 == len(line) -1 :
            if number < line[index1 -1] and number < list[index - 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        else:
            if number < line[index1 -1] and number < list[index - 1][index1] and number < line[index1 +1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
    return risk_of_line, indexes


def lowest(index, line, list):
    risk_of_line = 0
    indexes = []
    for index1, number in enumerate(line):
        if index1 == 0:
            if number < line[index1 +1] and number < list[index - 1][index1] and number < list[index + 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        elif index1 == len(line) -1:
            if number < line[index1 -1] and number < list[index - 1][index1] and number < list[index + 1][index1]:
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
        else:
            if number < line[index1 -1] and number < list[index - 1][index1] and number < line[index1 +1] and number < list[index +1][index1] :
                risk_of_line = risk_of_line + int(number) + 1
                indexes.append((index, index1))
    return risk_of_line, indexes

if __name__ == "__main__":
    amount_of_numbers, amount_of_numbers2 = Day9Problem(sys.argv[1])
    print("amount of numbers 1 " + str(amount_of_numbers))
    print("amount of numbers 2 " + str(amount_of_numbers2))
