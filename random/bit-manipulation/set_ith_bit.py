"""
(8, 3) -> 12
1000 -> if we set the third bit, it will be 1100 (12)

(2,1) -> 2
"""

def set_ith_bit(num, i):
    mask = 1<<(i-1)
    
    return num | mask

print(set_ith_bit(8, 3))