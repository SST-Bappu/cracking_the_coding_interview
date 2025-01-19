def group_anagrams(arr):
    anagrams = {}
    for s in arr:
        anagram = ''.join(sorted(s))
        if anagram not in anagrams:
            anagrams[anagram] = []
        anagrams[anagram].append(s)
    
    result = []
    
    for key in anagrams:
        result+=anagrams[key]
    
    return result

str_list = ['dog', 'cat', 'god', 'tac', 'tar', 'act', 'listen', 'art', 'enlist', 'silent', 'rat']

print(group_anagrams(str_list))