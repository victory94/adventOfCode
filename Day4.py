import sys

#Reads input from file, createst bingo boards and bingo input
#first line bingo numbers: seperated by ,
#next lines are boards, lines come in 5x5 squares like:
#57 19 40 54 64
#22 69 15 88  8
#79 60 48 95 85
#34 97 33  1 55
#72 82 29 90 84
def Day4Problem(file_name):
    bingo_numbers = []

    with open(file_name) as file:

        for line in file:
            if ',' in line:
                bingo_numbers = line.split(',')
            else:
                if line == '\n':
                    break
                else:
                    #TODO: hantera bingo boards


if __name__ == "__main__":
    bingo_score = Day4Problem(sys.argv[1])