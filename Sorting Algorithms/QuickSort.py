import random

nums = [3,7,8,5,2,1,9,5,4]
n = [5,8,9,5,7]

def quick_sort(nums):
    sorted  = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            sorted = False

    if sorted:
        return nums
    else:
        # pivot_idx = random.randint(0, len(nums)-1)
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
        return (nums), pivot_idx

print(quick_sort(nums))