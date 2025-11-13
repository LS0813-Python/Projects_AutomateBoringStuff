def concat_list(lstString) :
    concatString = ''
    for i in range(len(lstString) - 2) :
        concatString += lstString[i]
        concatString += ','
    concatString += lstString[-2] + ' and ' + lstString[-1]
    return concatString

def grid_join(gridLists) : 
    lstString = []
    for i in range(len(grid[0])) :
        str = ''
        for j in range(len(grid)) :
            str += grid[j][i]
        lstString.append(str)
    return lstString


glstTest = ['Banana', 'Apple', 'Pear', 'Cherry', 'Apricot']

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(concat_list(glstTest))

strList = grid_join(grid)
for strItem in strList :
    print(strItem)