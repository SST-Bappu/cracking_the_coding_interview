import datetime


def count_ways(n):
    memo = {}
    def dfs(i, cur_total):
        if cur_total==n:
            return 1
        if cur_total>n or i>= len(coins):
            return 0
        key = (i, cur_total)
        if key not in memo:
            memo[key] = dfs(i, cur_total+coins[i]) + dfs(i+1, cur_total)
        
        return memo[key]
    
    return dfs(0,0)
    
def count_ways_2(n):
    memo = {}
    def make_change(amount, index):
        if amount==0:
            return 1
        if index>= len(coins):
            return 0
        key = (amount, index)
        if key not in memo:
            
            cur_coin = coins[index]
            i= 0
            ways = 0
            while i*cur_coin<=amount:
                remaining_amount = amount - (i*cur_coin)
                ways+= make_change(remaining_amount, index+1)
                i+=1
            
            memo[key] = ways
        
        return memo[key]
    
    return make_change(n,0)

coins = [1, 5, 10, 25]

start = datetime.datetime.now()
print(count_ways(300))
end = datetime.datetime.now()
print(end-start)

start = datetime.datetime.now()
print(count_ways_2(300))
end = datetime.datetime.now()
print(end-start)