"""
3 -> 011 -> set bit =2
5 -> 101 -> set bit = 2
4 -> 100 -> set bit = 1
"""

def count_set_bit(num):
    cnt = 0
    
    while num:
        if num & 1:
            cnt+=1
        num = num>>1
    
    return cnt


print(count_set_bit(10))