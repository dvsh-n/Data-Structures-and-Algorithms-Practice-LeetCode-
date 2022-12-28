def maximumBags(capacity, rocks, additionalRocks):
    result = 0
    data = {}
    for i in range(len(capacity)):
        diff_i = capacity[i] - rocks[i]
        if diff_i not in data:
            data[diff_i] = 1
        else:
            data[diff_i] += 1

    for i in sorted(data.keys()):
        total = data[i] * i # no. of bags where i rocks can be filled * i
        if total <= additionalRocks:
            additionalRocks -= total
            result += data[i]
        else:
            ratio = additionalRocks/total # ratio of additionalRocks over total space
            result += (int)(ratio*data[i]) # ratio * no. of bags gives (float) no. of bags required, floor that to get no. of bags filled to max
            additionalRocks = 0 # all rocks empty
            break

    return result
    
print(maximumBags([10,1000000000], [10,0], 1000000000))