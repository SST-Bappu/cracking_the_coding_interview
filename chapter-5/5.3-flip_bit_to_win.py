"""
Input: 1775 (or: 11011101111)
110111111110
Output: 8
"""
def flip_bit_to_win(num : int) -> int :
    max_sequence = 0
    is_one_applied = False
    left = 0
    last_zero = -1
    right = 0
    while num:
        mask = 1
        mask = num & mask
        if mask or not is_one_applied:
            if not mask:
                is_one_applied = True
                last_zero = right
        else:
            max_sequence = max(max_sequence, (right-left))
            left = last_zero+1
            last_zero = right
        
        right +=1
        num = num >> 1
    
    return max(max_sequence, (right - left))

print(flip_bit_to_win(3582))
    