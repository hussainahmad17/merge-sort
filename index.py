def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left,right):
    result = []
    i,j=0,0
    n,m = len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i +=1
        else:   
            result.append(right[j])
            j +=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j < m:
            result.append(right[j])
            j+=1
    return result


array = [90,34,78,23,1,349,2,3,4]
array = merge_sort(array)
print(array)