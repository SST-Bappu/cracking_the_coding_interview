a = [1,2,3,8,22,30,35]
b = [7, 8,25,38]

def merge_sorted_arrays(A, B):
    b_pointer = 0
    
    i=0
    while i<len(A) and b_pointer<len(B):
        if A[i]>B[b_pointer]:
            A.insert(i,B[b_pointer])
            b_pointer+=1
        i+=1
    
    A+=B[b_pointer:]
    
    return A

print(merge_sorted_arrays(a,b))