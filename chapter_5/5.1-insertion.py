"""

Input: N 10000100000, M 10011, i 2, j 6
Output:N = 10001001100

"""
def insert_bits_optimized(n, m, i, j):
    all_ones = ~0
    
    left = all_ones << (j+1) #11110000000
    right = (1<<i) -1 # 00000000011
    left_right_comb = left | right # 11110000011
    n_cleared = n & left_right_comb #10000000000
    m_positioned = m<<i # 1001100
    
    return n_cleared | m_positioned

def insert_bits(n, m, i, j):
    
    def insert_bits(mask, is_set):
        nonlocal n
        if is_set:
            n = n|mask #we are inserting a set bit here (1000 | 0010) -> 1010
        else:
            n = n & mask # insert a unset bit, the mask is inverted in this case
            
    for k in range(i, j + 1):
        mask = 1
        if m & mask:
            mask = mask<<k
            insert_bits(mask, 1)
        else:
            mask = mask<<k
            insert_bits(~mask, 0)
        m = m>>1
    
    return n
    

print(insert_bits(128, 6, 2, 4))
print(insert_bits_optimized(128, 6, 2, 4))