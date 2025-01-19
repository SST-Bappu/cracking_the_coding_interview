def recursive_multiply(a, b):
    if a==0 or b==0:
        return 0
    
    a, b = max(a,b), min(a,b)
    
    odd = a%2
    
    left = recursive_multiply(a>>1, b)
    result = left+left
    if odd:
        result+=b
    
    return result

print(recursive_multiply(-10, -40))