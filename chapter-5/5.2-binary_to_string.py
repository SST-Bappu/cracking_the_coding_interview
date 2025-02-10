def binary_to_string(num: float) -> str:
    if num>=1 or num<=0:
        return 'ERROR'
    
    binary_string = '.'
    while num:
        if len(binary_string)>=32:
            return 'ERROR'
        
        print(binary_string, num)
        num = 2 * num
        if num>=1:
            binary_string+='1'
            num -= 1
        else:
            binary_string+='0'
    
    return binary_string

print(binary_to_string(0.5))
