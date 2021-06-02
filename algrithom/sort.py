#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sort.py    
@Github  :   https://github.com/StrikerCC

@Modify Time      @Author       @Version    @Desciption
------------      -------       --------    -----------
5/13/2021 1:38 PM   Cheng Chen    1.0         None
'''

# import lib
import numpy as np
import random


def heap_sort(nums):
    if not nums:
        return nums

    len_sorted = 1
    while len_sorted < len(nums):

        """sort every len_sorted * 2"""
        for i in range(0, len(nums), len_sorted*2):
            left, right = i, i + len_sorted
            left_lim = right
            right_lim = min(i + 2 * len_sorted, len(nums))
            nums_sorted = []

            """heap insort smallest ele of two list into nums_sorted"""
            while left < left_lim or right < right_lim:
                if right >= right_lim:
                    nums_sorted += nums[left:left_lim]
                    left = left_lim
                elif left >= i + len_sorted:
                    nums_sorted += nums[right:right_lim]
                    right = right_lim
                elif nums[left] < nums[right]:    # move left forward
                    nums_sorted.append(nums[left])
                    left += 1
                else:
                    nums_sorted.append(nums[right])
                    right += 1

            """overwrite ele"""
            nums[i:i+len_sorted*2] = nums_sorted
        len_sorted *= 2

    return nums


def quick_sort(nums):
    if not nums: return nums
    len_sort = len(nums)

    """try to sort len_sort from mid"""
    while len_sort > 1:

        for i in range(0, len(nums), len_sort):
            left, right = i, min(i+len_sort, len(nums))
            mid = int((left+right)/2)

            """put smaller ele to left, bigger ele to right"""
            nums_left, nums_right = [], []
            for j in range(left, right):
                """sort"""
                if j == mid:
                    continue
                if nums[j] > nums[mid]:
                    nums_right.append(nums[j])
                else:
                    nums_left.append(nums[j])
            print(nums_left, nums[mid], nums_right)
            nums[left:right] = nums_left + [nums[mid]] + nums_right
        len_sort = int(len_sort / 2)


def quick_sort_helper(nums, left, right):
    if not nums:
        return
    if left == right:
        return
    """try to sort len_sort from mid"""
    mid = int((left+right)/2)

    """put smaller ele to left, bigger ele to right"""
    nums_left, nums_right = [], []
    for j in range(left, right):
        """sort"""
        if j == mid:
            continue
        if nums[j] > nums[mid]:
            nums_right.append(nums[j])
        else:
            nums_left.append(nums[j])
    print(left, mid, right)
    print(nums_left, nums[mid], nums_right)

    nums[left:right] = nums_left + [nums[mid]] + nums_right
    quick_sort_helper(nums, left, left+len(nums_left))
    quick_sort_helper(nums, left+len(nums_left)+1, right)


def part():
    pass


def main():
    nums = [i for i in range(10)]
    random.shuffle(nums)

    print(nums)
    quick_sort_helper(nums, 0, len(nums))
    print(nums)


if __name__ == '__main__':
    main()
