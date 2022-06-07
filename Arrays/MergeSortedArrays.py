from logging import PlaceHolder


def merge_arrays(arr1, arr2):

    merged_arr = []
    i = 0
    j = 0
    total_len = len(arr1) + len(arr2)

    while len(merged_arr) != total_len:
        if i == len(arr1):
            num1 = num2 + 1
        else:
            num1 = arr1[i]

        if j == len(arr2):
            num2 = num1 + 1
        else:
            num2 = arr2[j]

        if num1 <= num2:
            merged_arr.append(num1)
            i = i + 1
        else:
            merged_arr.append(num2)
            j = j + 1

    return merged_arr

print(merge_arrays([1,5,9,20,30,34], [4,7,10,30,50,80]))

