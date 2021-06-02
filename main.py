from hw5 import *
import math
import numpy as np
import matplotlib.pyplot as plt

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def mins(nums, how_many):
    if len(nums) <= 3:
        return nums
    least_ = []
    for num in nums:
        if len(least_) < how_many:  # not full yet
            least_.append(num)
        else:   # full
            if least_[-1] <= num:   # keep going
                continue
            else:   # replace the last one, and resort
                least_[-1] = num
                least_.sort()

    return least_


def plus(a, b):
    return (a * 10**(int(math.log10(b))+1)) + b


def min_combination(nums, used, sum, left):
    # recursion
    if left == 0:
        # print('return ', sum)
        return sum

    smallest = math.inf
    for i in range(len(nums)):
        if used[i] == 0:    # not used yet
            used[i] = 1     # mark as used
            small = min_combination(nums, used, plus(sum, nums[i]), left-1)
            smallest = min(smallest, small)
            used[i] = 0
            # print(small, smallest, sum)

    return smallest


def seq(num):
    valid = [(num, num)]
    for start in range(num, 1, -1):    # start with each number smaller than original num
        sum_ = start
        for j in range(start-1, 0, -1):  # from start to 0
            sum_ += j

            # print(start, j, sum_)

            if sum_ == num:
                valid.append((start, j))    # find a solution
            elif sum_ > num:     # sum is bigger than original number
                break
    return valid

def form_output(start2ends):
    output = ""
    for start2end in start2ends:
        start, end = start2end[0], start2end[1]
        output += str(start2ends[0][0]) + '='
        for i in range(end, start+1):
            output += str(i)
            if i < start:
                output += '+'
        output += '\n'
    return output + "Result:" + str(len(start2ends))


def probmapping():
    lim_low = 50
    lim_up = 950
    x = np.arange(lim_low, lim_up)
    x = x / 1000
    y = x / (1 -x)
    log_y = np.log(y)
    # print(y)
    print(x[-1])
    plt.plot(x, y)
    plt.show()

    plt.plot(x, log_y)
    plt.show()

def oneMapping2zeor():
    lim_low = 500
    lim_up = 2000
    x = np.arange(lim_low, lim_up)
    x = x / 1000
    log_y = np.log(x)
    print(x[-1])
    plt.plot(x, log_y)
    plt.show()


def cross_entropy(y=0.5, y_expect=0.5):
    loss = -y_expect*math.log2(y) - (1-y_expect)*math.log2(1-y)

    return loss




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = 5.2
    b = 2.0
    print(a % b)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

