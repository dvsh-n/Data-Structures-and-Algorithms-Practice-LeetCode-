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
        pivot_idx = len(nums) - 1
        pivot = nums[pivot_idx]
        i = 0
        while i < pivot_idx:
            if nums[i] > pivot:
                temp = nums[i]
                nums[i] = nums[pivot_idx - 1]
                nums[pivot_idx - 1] = pivot
                nums[pivot_idx] = temp
                pivot_idx -= 1
            if nums[i] < pivot:
                i += 1
    return quick_sort(nums[:pivot_idx]) + [nums[pivot_idx]] + quick_sort(nums[pivot_idx + 1:]) 

print(quick_sort(nums))