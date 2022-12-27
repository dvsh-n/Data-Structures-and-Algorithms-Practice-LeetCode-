nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def selection_sort(nums):
    for i in range(len(nums)):
        min_val = (nums[i], None, False)
        for j in range(i, len(nums)):
            if nums[j] < min_val[0]:
                min_val = (nums[j], j, True)
        if min_val[2]:
            nums[i], nums[min_val[1]] = nums[min_val[1]], nums[i]
    return nums

print(selection_sort(nums))
