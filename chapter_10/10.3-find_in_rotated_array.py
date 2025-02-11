arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

def find_in_rottated_array(arr, target):
    def modified_binary_search(left, right):
        if left>right:
            return -1
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        
        if arr[mid]>target:
            if arr[left]>=target:
                return modified_binary_search(left, mid-1)
            else:
                return modified_binary_search(mid+1, right)
        else:
            if arr[right]>=target:
                return modified_binary_search(mid + 1, right)
            else:
                return modified_binary_search(left, mid-1)

                
    
    
    return modified_binary_search(0, len(arr)-1)

print(find_in_rottated_array(arr, 14))