from datetime import datetime

def magic_index_distinct(arr):
    def binary_search(l, r):
        if l>r:
            return -1
        
        mid = (l+r)//2
        if arr[mid]==mid:
            return mid
        if arr[mid]>mid:
            return binary_search(l, mid-1)
        return binary_search(mid+1, r)
    
    return binary_search(0, len(arr)-1)
def magic_index(arr):
    i = 0
    while i<len(arr):
        if arr[i]==i:
            return i
        elif arr[i]>i:
            i +=(arr[i]-i)
        else:
            i+=1
    
    return -1
def magic_index_bs(arr):
    def binary_search(l, r):
        try:
            if l>r:
                return -1
            # 0, 0, 1, 4, 5
            mid = (l+r)//2
            if arr[mid] == mid:
                return mid
            left_val = min(mid-1, arr[mid])
            left = binary_search(l,left_val)
            if left>=0:
                return left
            right_val = max(mid+1, arr[mid])
            right = binary_search(right_val, r)
            return right
        except Exception as e:
            print(e)
            print(l, r)
    return binary_search(0, len(arr)-1)
arr = [-2,-2,0,2,3,3,4,4,6,7,7,12,12]
time = datetime.now()
print(magic_index(arr))
time2 = datetime.now()
print(time2 - time)


time = datetime.now()
print(magic_index_bs(arr))
time2 = datetime.now()
print(time2 - time)


arr2 = [-23,-10,1,3,7,9]
# print(magic_index_distinct(arr2))