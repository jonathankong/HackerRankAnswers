import sys 

def superDigit(n, k):
    #since dealing with converting a large string into an int is annoying and slow
    #I'll instead break apart the string into each character, multiply it and add it to a running sum
    
    #this should only happen once because the input is a string and we don't need k afterwards
    if isinstance(n, str):
        sum = 0
        for num in n:
            sum += int(num) * k
        
        return superDigit(sum, k)
        
    #end case    
    if n % 10 == n:
        return n
    
    #get sum 
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    
    #recursively get super digit
    return superDigit(sum, k)

print(superDigit("861568688536788", 100000))