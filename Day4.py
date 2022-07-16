import sys
import numpy

# Reads input from file, creates bingo boards and bingo input
# first line bingo numbers: seperated by ,
# next lines are boards, lines come in 5x5 squares like:
# 57 19 40 54 64
# 22 69 15 88  8
# 79 60 48 95 85
# 34 97 33  1 55
# 72 82 29 90 84
def Day4Problem(file_name):
    bingo_numbers = []
    bingo_cards = {}

    with open(file_name) as file:
        counter = 0
        for line in file:
            if ',' in line:
                bingo_numbers = line.split(',')
            else:
                if line == '\n':
                    if counter > 0:
                        bingo_cards['card'+str(counter)] = numpy.array(bingo_cards['card'+str(counter)])
                    counter = counter +1
                    bingo_cards['card' + str(counter)] = []
                    continue
                else:
                    bingo_cards['card' + str(counter)].append(line.split())

    for number in bingo_numbers:
        for card in bingo_cards:
            bingo_cards[card] = numpy.where(bingo_cards[card] == number, -1, bingo_cards[card])
        won, card_name = see_if_card_has_won(bingo_cards)
        if won:
            return calc_wning_board(bingo_cards[card_name],number)


    return "won"

def calc_wning_board(board, number):
    sum_num = 0
    for array in board:
        for val in array:
            if val == '-1':
                continue
            else:
                sum_num = sum_num + int(val)
    return sum_num * number


def see_if_card_has_won(cards):
    for card in cards:
        if isBingo(cards[card]):
            return True, card
    return False, 'no_card'

def isBingo(card):
    cols = []
    for i in range(5):
        row_zeros = numpy.count_nonzero(card[i:, ] == '-1')
        col_zeros = numpy.count_nonzero(card[:, i] == '-1')
        if row_zeros == 5 or col_zeros == 5:
            return True

    return False

    # diagonal_zeros=np.count_nonzero(np.diag(card))
    # diagonal1_zeros=np.count_nonzero(np.diag(np.fliplr(card)))
    # if not diagonal_zeros or not diagonal1_zeros:
    #     return(True)
   #  return(True)



if __name__ == "__main__":
    bingo_score = Day4Problem(sys.argv[1])
    print(bingo_score)