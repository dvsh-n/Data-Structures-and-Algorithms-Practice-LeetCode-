nums = [26,79,13,65,24,46,876,43,214,87,36,98]

def merge_sort(nums):
    if len(nums) == 1:
        return nums

    center = len(nums)//2
    left = nums[:center]
    right = nums[center:]

    return comparator(merge_sort(left), merge_sort(right))

def comparator(left, right):
    result = []
    i,j = 0,0

    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        result += right[j:]
    else:
        result += left[i:]
    
    return result

print(merge_sort(nums))