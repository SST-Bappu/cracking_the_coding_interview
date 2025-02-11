def pairwise_swap(num: int)->int:
    """
    this will swap bits between odd and even spots.
    this solution is for 32 bits integer
    """
    odd_mask = 0xAAAAAAAA # 10101010101010101010101010101010
    even_mask = 0x55555555 # 01010101010101010101010101010101
    
    even_bits = (even_mask & num) << 1
    odd_bits = (odd_mask & num) >> 1
    
    return even_bits | odd_bits

# 101010
# 010101
print(pairwise_swap(42))

