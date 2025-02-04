"""
16 -> True,
15 -> False
"""

def is_power_of_2(num):
    if num and (num & (num-1))==0:
        return True
    return False


print(is_power_of_2(16))
