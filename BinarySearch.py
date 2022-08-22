

from re import S
import re

#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
#If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.

def find_target(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1
        
nums = [1, 1, 2, 3, 34, 45]
target = 
print(find_target(nums, target))