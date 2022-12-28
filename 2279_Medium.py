def maximumBags(capacity, rocks, additionalRocks):
    result = 0
    diff = []
    max = 0
    for i in range(len(capacity)):
        diff_i = capacity[i] - rocks[i]
        if diff_i > max:
            max = diff_i
        diff.append(diff_i)

    data = [0 for j in range(max+1)]

    for i in diff:
        data[i] += 1

    for i in range(len(data)):
        total = data[i] * i # no. of bags where i rocks can be filled * i
        if total <= additionalRocks:
            additionalRocks -= total
            result += data[i]
        else:
            ratio = additionalRocks/total # ratio of additionalRocks over total space
            result += (int)(ratio*data[i]) # ratio * no. of bags gives (float) no. of bags required, floor that to get no. of bags filled to max
            additionalRocks = 0 # all rocks empty
            break

    return result, diff, max, data, additionalRocks
    
print(maximumBags([91,54,63,99,24,45,78], [35,32,45,98,6,1,25], 17))