def GridChallenge(grid):
    #sort each row
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    
    #go through each column
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            #check if current letter is not in alphabetical order compared 
            #to the previous
            if grid[i][j] < grid[i - 1][j]:
                return "NO"
    return "YES"


grid = [
    ['m', 'p', 'x', 'z'],
    ['a', 'b', 'c', 'd'],
    ['w', 'l', 'm', 'f']
]

print(GridChallenge(grid))

