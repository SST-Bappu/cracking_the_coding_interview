def paintFill(grid, x,y, color):
    old_color = grid[x][y]
    if color==old_color:
        return
    moves = [[0,1], [1,0], [0,-1], [-1,0]]
    def dfs(r, c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=old_color:
            return
        
        grid[r][c] = color
        for n_r, n_c  in moves:
            dfs(r+n_r, c+n_c)
        
    dfs(x,y)
    

    
    
    
grid = [[0, 0, 0, 1],[1, 1, 1, 1],[0, 0, 1, 0],[1, 0, 1, 1]]

paintFill(grid, 0, 3, 2)

for row in grid:
    print(row)
