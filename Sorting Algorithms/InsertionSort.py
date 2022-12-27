nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[0]:
            temp = nums[i]
            nums.remove(temp)
            nums.insert(0, temp)
        else:
            j = i - 1
            while nums[j] > nums[i]:
                j -= 1
            temp = nums[i]
            nums = nums[:i] + nums[i+1:]
            nums.insert(j+1, temp)
    return nums

print(insertion_sort(nums))