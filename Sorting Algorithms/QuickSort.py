import random

nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def quick_sort(nums):
    sorted  = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            sorted = False

    if sorted:
        return nums
    else:
        pivot_idx = random.randint(0, len(nums)-1)
        pivot = nums[pivot_idx]
        i = 0
        while i < pivot_idx:
            pass