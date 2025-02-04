"""
1 -> 001 -> 1
4 -> 100 -> 3
5 -> 101 -> -1
6 -> 110 -> -1

return the set bit only if there's 1 set bit, else return -1
"""

def find_set_bit(num):
    cnt = 0
    
    while num:
        cnt+=1
        if num & 1:
            break
        num = num>>1
    
    return cnt if num==1 else -1


print(find_set_bit(4))
