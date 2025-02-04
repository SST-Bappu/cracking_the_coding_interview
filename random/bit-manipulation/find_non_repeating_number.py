"""
all the repeated elements in the array are present in pair,(11, 1111, but not 111)
and there's one non-repeated number.
we have to find that out

010
101 -> 010 -> 001
111
010
"""

def find_non_repeating_number(arr):
    result = arr[0]
    
    for i in range(1, len(arr)):
        result = result ^ arr[i]
        
    return result

def find_first_set_bit(num):
    cnt = 0
    while num:
        if num & 1:
            return cnt
        num = num>>1
        cnt+=1
    return -1
def find_bit(num, cnt):
    while cnt:
        num = num>>1
        cnt-=1
    return num & 1
def find_two_non_repeating_number(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result = result ^ arr[i]
    
    part1 = []
    part2 = []
    set_bit = find_first_set_bit(result)
    for num in arr:
        cur_set_bit = find_bit(num, set_bit)
        if cur_set_bit:
            part1.append(num)
        else:
            part2.append(num)
    print(part1)
    print(part2)
    result = (find_non_repeating_number(part1), find_non_repeating_number(part2))
    return result
    
# print(find_non_repeating_number([1,2,1,2,5,3,4,3,4]))
print(find_two_non_repeating_number([1,2,1,2,5,7,3,4,3,4]))
