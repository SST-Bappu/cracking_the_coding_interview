from collections import Counter
def permutations(s):
    cnt = Counter(s)
    result = []
    def permute(prefix, remaining):
        if remaining==0:
            result.append(prefix)
            return
        
        for key in cnt.keys():
            if cnt[key]>0:
                cnt[key]-=1
                permute(prefix+key, remaining-1)
                cnt[key]+=1
    
    permute('', len(s))
    return result

result = permutations('aabbcc')
print(result)

