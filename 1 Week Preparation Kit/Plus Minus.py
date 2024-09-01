def plusMinus(n, arr):
    posCounter = 0
    negCounter = 0
    
    for val in arr:
        if val > 0: 
            posCounter += 1
        elif val < 0:
            negCounter += 1
    
    print(f"{posCounter/n:.6f}")
    print(f"{negCounter/n:.6f}")
    print(f"{(n - (posCounter + negCounter))/n:.6f}")


plusMinus(5, [1, 1, 0 , -1, -1])    

