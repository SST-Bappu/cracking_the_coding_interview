"""
(8,4) -> True
1000 -> 4'th bit is set
(12, 4) -> True
(12,4) -> False
"""

def check_ith_bit(num, i):
    mask = 1<<(i-1)
    if mask & num:
        return True
    
    return False

print(check_ith_bit(12, 2))