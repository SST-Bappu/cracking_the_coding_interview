"""
1 -> 001
2 -> 010 011
1 -> 001 001
"""

def number_of_flip(a, b):
    flips = 0
    while a or b:
        if (a & 1) != (b & 1):
            flips+=1
        a = a>>1
        b = b>>1
    
    return flips

print(number_of_flip(7, 15))