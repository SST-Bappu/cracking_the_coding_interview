""""
11101
01111

10000
01111

101010

"""


def conversion(a: int, b: int) -> int:
    """
    number of bits required to be flipped to convert a to b
    """
    c = a ^ b
    result = 0
    while c:
        result += 1
        c = c & (c - 1) # it will clear the least significant bit every time
    
    return result

print(conversion(29, 15))
