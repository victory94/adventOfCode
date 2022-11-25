import sys
from collections import Counter



def Day6Problem(file_name):
    with open(file_name) as file:
        for line in file:
            array_of_time = list(map(int, line.split(",")))

    count_of_lives = Counter(array_of_time)
    number_of_days = 256
    for days in range(1,number_of_days+1):
        count_of_lives = {life: (0 if count_of_lives.get(life + 1) is None else count_of_lives.get(life+1)) for life in range(-1,8)}
        #changes those = 8 to -1 to change them to create new fish
        count_of_lives[8] = count_of_lives[-1]
        #counts down those which have reched -1 = are exhausted
        count_of_lives[6] += count_of_lives[-1]
        #reset exhausted lives
        count_of_lives[-1] = 0
    return sum(count_of_lives.values())


if __name__ == "__main__":
    number_of_fishes = Day6Problem(sys.argv[1])
    print("number of fish " + str(number_of_fishes))
