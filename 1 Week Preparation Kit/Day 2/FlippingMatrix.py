def FlippingMatrix(arr):
    sum = 0
    #left quadrant size
    maxInd = len(arr) - 1 


    #only certain values can be moved into the top left quadrant of the square matrix with only flipping rows or columns.abs
    #ie [1, 2, 2, 1]
    #   [3, 4, 4, 3]
    #   [3, 4, 4, 3]
    #   [1, 2, 2, 1]
    #in this matrix, the numbers above show the groups of numbers that must be compared to determine what will show up in the top left submatrix.
    #ie. only the values in the "1" group ever show up in the top left corner of the submatrix.  This means that we just need to find the max value in 
    #that group and add it to a running sum
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