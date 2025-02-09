def is_power_of_two(n: int)-> bool:
    if not (n & (n-1)):
        return True # n is power of 2
    return False


print(is_power_of_two(32))