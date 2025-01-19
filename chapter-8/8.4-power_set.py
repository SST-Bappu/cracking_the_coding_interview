from copy import deepcopy


def power_set(arr):
    result = [[]]
    
    for num in arr:
        for i in range(len(result)):
            new = deepcopy(result[i])
            new.append(num)
            result.append(new)
        
    
    return result


arr = [1,2,3]

print(power_set(arr))