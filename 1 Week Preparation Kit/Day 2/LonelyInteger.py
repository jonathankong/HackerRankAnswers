def LonelyInteger(arr):
    intOccurances = {}

    for i in arr:
        if i not in intOccurances:
            intOccurances[i] = 1
        else:
            intOccurances[i] += 1

    return [key for key, value in intOccurances.items() if value == 1][0]
     
print(LonelyInteger([1, 2, 3, 4, 3, 2, 1]))