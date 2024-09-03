def FlippingMatrix(arr):
    sum = 0
    #left quadrant size
    maxInd = len(arr) - 1 

    for i in range(int(len(arr)/2)):
        for j in range(int(len(arr)/2)):
            sum += max([arr[i][j], arr[i][maxInd - j], arr[maxInd - i][j], arr[maxInd - i][maxInd - j]])

    return sum


arr2d = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
]
print(FlippingMatrix(arr2d))