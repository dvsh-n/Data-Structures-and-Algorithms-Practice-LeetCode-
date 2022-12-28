def maximumBags(capacity, rocks, additionalRocks):
    result = 0
    diff = []
    max = 0
    for i in range(len(capacity)):
        diff_i = capacity[i] - rocks[i]
        if diff_i > max:
            max = diff_i
        diff.append(diff_i)
    print(max)

    data = [0 for j in range(max+1)]
    print(data)
    print(diff)

    for i in diff:
        data[i] += 1
    print(data)

    for i in range(len(data)):
        if  i == 0:
            result += data[i]
        else:
            total = data[i] * i # no. of bags where i rocks can be filled * i
            if total <= additionalRocks:
                additionalRocks -= total
                result += data[i]
            else:
                remainder = total % additionalRocks
                if remainder == 0:
                    result += data[i]
                else:
                    result += data[i] - 1
                additionalRocks = 0
                break

    return result

print(maximumBags([2,3,4,5], [1,2,4,4], 2))