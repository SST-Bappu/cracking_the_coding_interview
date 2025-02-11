"""
---get next number---
110110
 ----> 111110 -> 111000 -> 111001
 
0111
-----> 1111 -> 1000 -> 1011

--- get previous number ---
1011
-------> 0011 -> 0000 -> 0111

"""


def next_number(num: int):
    def get_next(num: int) -> int:
        c0 = c1 = 0
        
        c = num
        while c and not (c & 1):
            c0+=1
            c= c>>1
        
        while c & 1:
            c1+=1
            c = c>>1
        p = c0+c1  # position of right most non-trailing zero
        
        num |= 1<<p # flip right most non-trailing zero (0111 -> 1111)
        
        num &= ~((1<<p)-1) #clear all bits to the right of p (1111 -> 1000)
        
        num |= (1<<(c1-1))-1 # insert c1-1 ones (1000 ->1011)
        
        return num
    """
    --- get previous number ---
    1011
    -------> 0011 -> 0000 -> 0111
    
    10110
    -------> 10100 -> 10100 -> 10101
    """
    def get_prev(num: int) ->int:
        c1 = c0 = 0
        c = num
        while c and (c & 1):
            c1+=1
            c= c>>1
        while c and not (c & 1):
            c0+=1
            c = c>>1
        if not c0:
            return -1 # if number is 1111, there's no previous number with same number of zeroes
        
        p = c1+c0
        num &= (~0)<<(p+1) # clear all the bits to the right starting from the position p (111001 -> 110000)
        mask = (1<<(c1+1))-1
        mask = mask << (c0-1)
        num |= mask # insert c1+1 ones starting from the position c0-1
        return num

    print(get_next(num))

    
    print(get_prev(num))


next_number(54)






