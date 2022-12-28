def maximumBags(capacity, rocks, additionalRocks):
    result = 0
    max = 0
    data = {}
    for i in range(len(capacity)):
        diff_i = capacity[i] - rocks[i]
        if diff_i > max:
            max = diff_i
        if diff_i not in data:
            data[diff_i] = 1
        else:
            data[diff_i] += 1

    for i in range(max+1):
        if i not in data:
            continue
        total = data[i] * i # no. of bags where i rocks can be filled * i
        if total <= additionalRocks:
            additionalRocks -= total
            result += data[i]
        else:
            ratio = additionalRocks/total # ratio of additionalRocks over total space
            result += (int)(ratio*data[i]) # ratio * no. of bags gives (float) no. of bags required, floor that to get no. of bags filled to max
            additionalRocks = 0 # all rocks empty
            break

    return result, max, data, additionalRocks
    
print(maximumBags([91,54,63,99,24,45,78], [35,32,45,98,6,1,25], 17))