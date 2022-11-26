import math
import sys


def Day8Problem(file_name):
    amount_of_num = []
    with open(file_name) as file:
        for line in file:
            array_of_first = []
            array_of_second = []
            line.strip('\n')
            array_of_first.extend(line.split("|")[0].split())
            array_of_second.extend(line.split("|")[1].split())
            array_of_first = sorted(array_of_first, key=len)
            dict_with_values = {}
            value_in_second = ""
            for value in array_of_first:
                if len(value) == 2:
                    dict_with_values[1] = value
                elif len(value) == 4:
                    dict_with_values[4] = value
                elif len(value) == 3:
                    dict_with_values[7] = value
                elif len(value) == 7:
                    dict_with_values[8] = value
            while len(dict_with_values) != 10:
                for value in dict_with_values.values():
                    if value in array_of_first:
                        array_of_first.remove(value)
                for value in array_of_first:
                    dict_with_values = check_values(value, dict_with_values)
                    if len(dict_with_values) == 10:
                        break

            for strings in array_of_second:
                for key, value in dict_with_values.items():
                    if len(value) == len(strings) and has_all_char(strings, value):
                        value_in_second = value_in_second + str(key)
                        break
            amount_of_num.append(int(value_in_second))


    return sum(amount_of_num)



def check_values(value, dict_with_nums):
    if len(value) == 6 and 9 not in dict_with_nums:
        amount_of_matching = 0
        for char in value:
            if char in dict_with_nums[4]:
                amount_of_matching = amount_of_matching + 1
        if amount_of_matching == 4:
            dict_with_nums[9] = value
    elif len(value) == 6 and 0 not in dict_with_nums and 9 in dict_with_nums:
        amount_of_matching = 0
        for char in value:
            if char in dict_with_nums[7]:
                amount_of_matching = amount_of_matching + 1
        if amount_of_matching == 3:
            dict_with_nums[0] = value
    elif len(value) == 6 and 6 not in dict_with_nums and 0 in dict_with_nums and 9 in dict_with_nums:
        dict_with_nums[6] = value
    elif len(value) == 5 and 3 not in dict_with_nums:
        amount_of_matching = 0
        for char in value:
            if char in dict_with_nums[1]:
                amount_of_matching = amount_of_matching + 1
        if amount_of_matching == 2:
            dict_with_nums[3] = value
    elif len(value) == 5 and 5 not in dict_with_nums and 4 in dict_with_nums:
        amount_of_matching = 0
        for char in value:
            if char in dict_with_nums[4]:
                amount_of_matching = amount_of_matching + 1
        if amount_of_matching == 3:
            dict_with_nums[5] = value
    elif len(value) == 5 and 2 not in dict_with_nums and 3 in dict_with_nums and 5 in dict_with_nums:
        dict_with_nums[2] = value
    return dict_with_nums



def has_all_char(chars, string):
    for char in chars:
        if char not in string:
            return False
    return True


if __name__ == "__main__":
    amount_of_numbers = Day8Problem(sys.argv[1])
    print("amount of numbers " + str(amount_of_numbers))
