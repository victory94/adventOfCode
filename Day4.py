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
                    bingo_cards['card' + str(counter)].append(numpy.array(line.split()))
    bingo_cards['card' + str(counter)] = numpy.array(bingo_cards['card' + str(counter)])
    bingo_score = check_winning_board(bingo_numbers, bingo_cards)
    last_bingo_score = get_last_winning_board(bingo_numbers, bingo_cards)
    return bingo_score, last_bingo_score


def get_last_winning_board(bingo_numbers, bingo_cards):
    bingo_cards_last = bingo_cards
    for number in bingo_numbers:
        for card in bingo_cards_last:
            bingo_cards_last[card] = numpy.where(bingo_cards_last[card] == number, -1, bingo_cards_last[card])
        won, card_names = see_if_card_has_won(bingo_cards_last)
        if won:
            if len(bingo_cards_last) == 1:
                return calc_wning_board(bingo_cards_last[card_names[0]], number)
            for card_name in card_names:
                del(bingo_cards_last[card_name])




def check_winning_board(bingo_numbers, bingo_cards):
    bingo_cards_chaged = bingo_cards
    for number in bingo_numbers:
        for card in bingo_cards_chaged:
            bingo_cards_chaged[card] = numpy.where(bingo_cards_chaged[card] == number, -1, bingo_cards_chaged[card])
        won, card_name = see_if_card_has_won(bingo_cards_chaged)
        if won:
            if len(card_name) == 1:
                return calc_wning_board(bingo_cards_chaged[card_name[0]], number)
            else:
                wins = []
                for card in card_name:
                    wins.append(calc_wning_board(bingo_cards_chaged[card],number))
                return wins


def calc_wning_board(board, number):
    sum_num = 0
    for array in board:
        for val in array:
            if val == '-1':
                continue
            else:
                sum_num = sum_num + int(val)
    return sum_num * int(number)


def see_if_card_has_won(cards):
    winning_cards = []
    for card in cards:
        if isBingo(cards[card]):
            winning_cards.append(card)
    if len(winning_cards) == 0:
        return False, 'no_card'
    else:
        return True, winning_cards

def isBingo(card):
    for rows in card:
        counter_negative = 0
        for vals in rows:
            if vals == '-1':
                counter_negative = counter_negative +1
        if counter_negative == 5:
            return True

    for col in range(5):
        counter_negative = 0
        for row in range(5):
           if card[row][col] == '-1':
                counter_negative = counter_negative +1
        if counter_negative == 5:
            return True

    return False




if __name__ == "__main__":
    bingo_score, last_score = Day4Problem(sys.argv[1])
    print("bingo score " + str(bingo_score))
    print("last score " + str(last_score))