def MiniMaxSum(arr):
    arrSum = sum(arr)
    minVal = arr[0]
    maxVal = arr[0]

    for i in range (1, len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]

        if arr[i] > maxVal:
            maxVal = arr[i]

    print(f"{arrSum - maxVal} {arrSum - minVal}")

MiniMaxSum([5, 4, 3, 2, 1])