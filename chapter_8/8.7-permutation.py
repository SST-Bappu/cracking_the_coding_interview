def permutation(s):
    
    def permute(cur_s):
        if not cur_s:
            return []
        left = cur_s[0]
        rest = permute(cur_s[1:])
        if not rest:
            return [left]
        result = []
        for sub_s in rest:
            result+= merge_permuted_string(left, sub_s)
        
        return result
     
    
    # bc, cb
    #abc, bac, bca
    def merge_permuted_string(left, rest):
        result = []
        for i in range(len(rest)+1):
            result.append(rest[:i]+left+rest[i:])
        
        return result
    
    return permute(s)

def permutation_optimized():
    pass

permutations = permutation('abcd')
print(len(list(permutations)))