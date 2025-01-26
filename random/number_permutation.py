def permutation(arr):
    def permute(prefix, p):
        result = []
        for i in range(len(p)+1):
            result.append(p[:i]+[prefix]+p[i:])
        return result
    
    def dfs(i):
        if i==(len(arr)-1):
            return [[arr[i]]]
        
        prefix = arr[i]
        rest = dfs(i+1)
        result = []
        for r in rest:
            result+=permute(prefix, r)
        
        return result
    
    return dfs(0)


arr = [1,2,3,4]
result = permutation(arr)

for r in result:
    print(r)
    