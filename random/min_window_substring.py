import heapq
from collections import Counter
def min_window_substring(s, t):
    heap = []
    left = min_left = -1
    min_length = float('inf')
    count = len(t)
    char_count = Counter(t)
    for right in range(len(s)):
        if s[right] in char_count:
            char_count[s[right]]-=1
            if left==-1:
                left = right
            if left!=right:
                heapq.heappush(heap, right)
            if char_count[s[right]]==0:
                count -=1
        
        while count==0:
            if min_length>(right-left+1):
                min_length = (right-left+1)
                min_left = left
            char_count[s[left]]+=1
            if char_count[s[left]]>0:
                count+=1
            if heap:
                left = heapq.heappop(heap)
            

    return s[min_left: min_left+min_length]



print(min_window_substring('ADOBECODEBANC', 'ABC'))
print(min_window_substring('a', 'a'))