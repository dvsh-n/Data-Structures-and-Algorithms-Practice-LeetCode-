import random

from torch import rand

nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def quick_sort(nums):
    pivot_idx = random.randint(0, len(nums)-1)
    pivot = nums[pivot_idx]
