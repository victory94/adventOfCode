import statistics
from statistics import mode
from collections import defaultdict
import sys


def Day3problem1(file_name):

    with open(file_name) as file:
        dict_post = defaultdict(list)
        list_num = []
        for line in file:
            if line == '':
                break
            char_counter = 1
            list_num.append(line)
            for char in line:
                if char == "\n":
                    break
                dict_post["char" + str(char_counter)].append(char)
                char_counter = char_counter + 1

    return get_power_consumption(dict_post), get_life_support(list_num)

def get_life_support(list_num):
    oxygen_setting = int(get_oxygen_generator_settings(list_num), 2)
    c02_setting = int(get_c02_settings(list_num), 2)

    return oxygen_setting * c02_setting

def get_power_consumption(dict_post):
    gamma_rate = ""
    epsilon_rate = ""

    for char_list in dict_post:
        mFN,lfn = calc_most_and_least_freq_number(dict_post[char_list])
        gamma_rate = gamma_rate  + str(mFN)
        epsilon_rate = epsilon_rate + str(lfn)
    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)

    return gamma_rate_int * epsilon_rate_int


def get_oxygen_generator_settings(list_numbers):
    counter = 1
    while len(list_numbers) != 1:
        list_numbers = list_of_most_common_on_pos(list_numbers, counter)
        counter = counter +1

    return list_numbers[0]


def get_c02_settings(list_numbers):
    counter = 1
    while len(list_numbers) != 1:
        list_numbers = list_of_least_common_on_pos(list_numbers, counter)
        counter = counter +1

    return list_numbers[0]

def calc_most_and_least_freq_number(list_of_numbers):
    counter_1 = 0
    counter_0 = 0
    for element in list_of_numbers:
        if element == "0":
            counter_0 = counter_0 +1
        else:
            counter_1 = counter_1 +1

    if counter_1 == counter_0:
        return 1,0
    else:
        if counter_1 > counter_0:
            return 1,0
        else:
            return 0,1


def list_of_most_common_on_pos(list_of_numbers, pos):

    dict_of_pos = defaultdict(list)
    for num in list_of_numbers:
        counter = 1
        for numerical in num:
            dict_of_pos["char"+str(counter)].append(numerical)
            counter = counter + 1

    most_common,least_common = calc_most_and_least_freq_number(dict_of_pos["char" + str(pos)])
    new_list = []
    for num in list_of_numbers:
        if num[pos - 1] == str(most_common):
            new_list.append(num)

    return new_list


def list_of_least_common_on_pos(list_of_numbers, pos):

    dict_of_pos = defaultdict(list)
    for num in list_of_numbers:
        counter = 1
        for numerical in num:
            dict_of_pos["char"+str(counter)].append(numerical)
            counter = counter + 1

    most_common,least_common = calc_most_and_least_freq_number(dict_of_pos["char" + str(pos)])
    new_list = []
    for num in list_of_numbers:
        if num[pos - 1] == str(least_common):
            new_list.append(num)

    return new_list

if __name__ == "__main__":
    power_consumption, life_support = Day3problem1(sys.argv[1])
    print(power_consumption)
    print(life_support)
