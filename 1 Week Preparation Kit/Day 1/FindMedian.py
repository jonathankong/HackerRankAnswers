def FindMedian(arr):
    arr.sort()
    return arr[int(len(arr) / 2)]

print(FindMedian([0, 1, 2, 4, 6, 5, 3]))