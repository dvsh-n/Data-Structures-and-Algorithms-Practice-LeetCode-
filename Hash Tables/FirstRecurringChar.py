def first_recurring_char(arr):
    temp = {}
    for i in arr:
        if i not in temp:
            temp[i] = None
        else:
            return i
    return None

print(first_recurring_char([2,5,5,2,3]))