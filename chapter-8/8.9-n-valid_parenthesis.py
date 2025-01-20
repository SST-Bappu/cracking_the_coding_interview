# 3
# ((())), ()()(), (())(), ()(()),(()())

def parens(n):
    if not n:
        return []
    
    result = []
    def build_parens(paren, o, c):
        if not o and not c:
            result.append(paren)
            return
        if o>0:
            build_parens(paren+'(', o-1, c)
        if o<c:
            build_parens(paren+')', o, c-1)
    
    build_parens('', n, n)
    return result


print(parens(3))