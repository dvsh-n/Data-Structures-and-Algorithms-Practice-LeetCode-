nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(bubble_sort(nums))