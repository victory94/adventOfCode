import sys
import numpy as np



def Day5Problem(file_name):
    matrix = np.zeros((1000, 1000))
    with open(file_name) as file:
        count = 0
        for line in file:
            line = line.strip()
            from_xy_to_xy = line.split("->")
            x1 = int(from_xy_to_xy[0].split(",")[0])
            y1 = int(from_xy_to_xy[0].split(",")[1])
            x2 = int(from_xy_to_xy[1].split(",")[0])
            y2 = int(from_xy_to_xy[1].split(",")[1])
            matrix = add_line_to_matrix(x1,y1,x2,y2, matrix)


    return np.count_nonzero(matrix > 1)

def add_line_to_matrix(x0, y0,x1,y1,in_matrix):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            in_matrix = plotLineLow(x1, y1, x0, y0, in_matrix)
        else:
            in_matrix = plotLineLow(x0, y0, x1, y1, in_matrix)
    else:
        if y0 > y1:
            in_matrix = plotLineHigh(x1, y1, x0, y0, in_matrix)
        else:
            in_matrix = plotLineHigh(x0, y0, x1, y1, in_matrix)

    return in_matrix

def plotLineLow(x0, y0, x1, y1, in_matrix):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = (2 * dy) - dx
    y = y0
    for x in range(x0, x1+1):
        in_matrix[x][y] = in_matrix[x][y] + 1
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy

    return in_matrix

def plotLineHigh(x0, y0, x1, y1, in_matrix):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = (2 * dx) - dy
    x = x0

    for y in range(y0,y1 +1):
        in_matrix[x][y] = in_matrix[x][y] + 1
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2*dx
    return  in_matrix

if __name__ == "__main__":
    overlapping_lines = Day5Problem(sys.argv[1])
    print("overlapping_lines " + str(overlapping_lines))
