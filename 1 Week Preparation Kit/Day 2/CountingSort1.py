def CountingSort1(arr):
    freqArr = [0] * 100

    for i in arr:
        freqArr[i] += 1

    return freqArr

print(CountingSort1([1, 1, 3, 2, 1]))