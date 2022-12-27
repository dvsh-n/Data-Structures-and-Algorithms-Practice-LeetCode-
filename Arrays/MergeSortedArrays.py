def merge_arrays(nums1, nums2):

    merged_arr = []
    i = 0
    j = 0
    total_len = len(nums1) + len(nums2)

    while len(merged_arr) != total_len:

        if i < len(nums1) and j < len(nums2):
            temp1 = nums1[i]
            temp2 = nums2[j]

            if temp1 <= temp2:
                merged_arr.append(temp1)
                i = i + 1
            else:
                merged_arr.append(temp2)
                j = j + 1

        else:
            if i == len(nums1):
                merged_arr = merged_arr + nums2[j:]
            else:
                merged_arr = merged_arr + nums1[i:]
            return merged_arr

    return merged_arr
        
print(merge_arrays([1,4,9,25,30,41],[5,7,10,20,25,30]))


