import copy
'''
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''
def n_queens(n):
    grid = [[''] * n for _ in range(n)]
    result = []
    def is_valid_pos(r, c):
        for i in range(r-1, -1, -1):
            
            d = r-i
            if grid[i][c]=='Q' or (c-d>=0 and grid[i][c-d]=='Q') or (c+d<n and grid[i][c+d]=='Q'):
                return False
        
        return True
        
        
    def backtrack(i):
        if i==n:
            result.append(copy.deepcopy(grid))
            return
        
        for j in range(n):
            if is_valid_pos(i,j):
                grid[i][j] = 'Q'
                backtrack(i+1)
                grid[i][j] = ''
    
    backtrack(0)
    return result


result = n_queens(8)

for r in result:
    print('->>>>>>>>>')
    for c in r:
        print(c)
