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

        # for i in range(len(capacity)):
        #     diff.append(capacity[i] - rocks[i])
        #     if diff[i] == 0:
        #         result += 1
        # for j in range(1,len(additionalRocks)):
            #     if j < additionalRocks:
            #         additionalRocks -= j
            #         result += 1
            #     else:
            #         if additionalRocks != 0:
            #             additionalRocks = 0
            #             result += 1
        # return result

# maximumBags([2,3,4,5], [1,2,4,4], 2)
# [0,0,0,0,2] 5
print(8%5)