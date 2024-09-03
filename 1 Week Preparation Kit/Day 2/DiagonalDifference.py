def DiagonalDifference(arr):
    leftSum = 0
    rightSum = 0
    for i in range(0, len(arr)):
        #Calculate diagonal from top left to bottom right
        leftSum += arr[i][i]

        #Calculate diagon from top right to bottom left
        rightSum += arr[i][len(arr) - 1 - i]
    
    return abs(leftSum - rightSum)


arr2d = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

print(DiagonalDifference(arr2d))