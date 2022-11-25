import math
import sys

def Day7Problem(file_name):
    with open(file_name) as file:
        for line in file:
            array_of_pos = list(map(int, line.split(",")))
    n = len(array_of_pos)
    #counting average in list of numbers
    average = math.ceil((n*(n+1)//2)/n)
    #create large number for comparison
    min_pos = 2**31
    #Go through list for average number of times from smallest number
    for i in range(min(array_of_pos), average + 1):
        pos = 0
        #go through each position in list
        for pos2 in array_of_pos:
            #asolute for difference between current number and average
            n1 = abs(pos2 -i)
            #sum abs number
            pos += (n1*(n1+1)//2)
        #See if pos is less than minimum pos
        min_pos = min(min_pos, pos)

    return min_pos



if __name__ == "__main__":
    amount_of_fuel = Day7Problem(sys.argv[1])
    print("amount of fuel, to travel " + str(amount_of_fuel))
