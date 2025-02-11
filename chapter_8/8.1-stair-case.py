memo = {}
def stair_case(n): #bottom-up approach
    if n==0:
        return 1
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    
    memo[n]=stair_case(n-1)+stair_case(n-2)+stair_case(n-3)
    return memo[n]

def stair_case2(n): #top-down approach
    result = [0]*(n+1)
    result[0] = 1
    keys = [-1, -2, -3]
    for i in range(1,n+1):
        
        for key in keys:
            if (i+key)>=0:
                result[i]+=result[i+key]
    
    return result[n]

def stair_case3(n): #bottom-up
    result = [0]*(n+1)
    result[n] = 1
    keys = [1, 2, 3]
    for i in range(n-1, -1, -1):
        for key in keys:
            if i+key<=n:
                result[i] += result[i+key]
    
    return result[0]
    


print(stair_case(3))
print(stair_case2(3))
print(stair_case3(3))