"""
abc -> a,b,c,ab,bc,ac,abc
'', 'a', 'b', 'ab','c', 'ac','bc','abc'
"""
import datetime


def string_subsequence_optimized(s):
    result = [s[0]]
    for i in range(1, len(s)):
        result.append(s[i])
        for j in range(len(result)-1):
            sub = result[j]+s[i]
            result.append(sub)
    return result
def string_subsequences_bit_manipulation(s):
    n = 2**len(s)
    result = []
    
    for i in range(1,n):
        x = i
        j=0
        sub_sequence = ''
        while x:
            if x & 1:
                sub_sequence+=s[j]
            j+=1
            x = x>>1
        result.append(sub_sequence)
    
    return result

start_time = datetime.datetime.now()
print(string_subsequences_bit_manipulation('abcdefgh'))
print(datetime.datetime.now()-start_time)
start_time = datetime.datetime.now()
print(string_subsequence_optimized('abcdefgh'))
print(datetime.datetime.now()-start_time)