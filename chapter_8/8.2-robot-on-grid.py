def robot_on_grid(arr):
    moves = [[1,0], [0,1]]
    path = set()
    result = []
    def dfs(r, c):
        nonlocal result
        if r>=len(arr) or c>=len(arr[0]) or arr[r][c]==-1 or (r, c) in path:
            return 0

        path.add((r,c))
        if r==(len(arr)-1) and c==(len(arr[0])-1):
            result = list(path)
            return 1
        for n_r, n_c in moves:
            cur_path = dfs(r+n_r, c+n_c)
            if cur_path:
                return 1
        
        path.remove((r,c))
        return 0
    
    dfs(0, 0)
    return sorted(result)


def robot_on_grid_paths(arr): #number of ways
    moves = [[1, 0], [0, 1]]
    memo = [[-1]*len(arr[i]) for i in range(len(arr))]
    def dfs(r, c):
        if r >= len(arr) or c >= len(arr[0]) or arr[r][c] == -1:
            return 0
        
        if r == (len(arr) - 1) and c == (len(arr[0]) - 1):
            return 1
        
        if memo[r][c]>=0:
            return memo[r][c]
        memo[r][c] = 0
        for n_r, n_c in moves:
            memo[r][c] += dfs(r + n_r, c + n_c)
        
        return memo[r][c]
        
    
    result = dfs(0, 0)
    print(memo)
    return result
    
# 0, 0, -1, -1
# 0, -1, 0, -1
# 0, 0, 0, 0
# -1, -1, 0, 0

    
arr = [[0,0,-1,-1], [0,0,0,-1], [0 ,0 ,0,0], [-1,-1,0,0]]
print(robot_on_grid(arr))
print(robot_on_grid_paths(arr))