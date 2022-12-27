nums = [13, 24, 26, 36, 43, 46, 65, 79, 87, 98, 214, 876]

def binary_search(target, nums):
    try:
        center = len(nums)//2
        i = nums[center]
    except IndexError:
        return False

    if i == target:
        return True
    elif i < target:
        return binary_search(target, nums[center+1:])
    elif i > target:
        return binary_search(target, nums[:center])

print(binary_search(87, nums))