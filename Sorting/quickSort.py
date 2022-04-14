def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save


def pivot_helper(start, end, arr):
    pivot = arr[start]
    pivot_index = start
    for i in range(start+1, end):
        if arr[i]<pivot:
            pivot_index += 1
            if i!=pivot_index:
                swap(arr, i, pivot_index)
        #print(arr)
    swap(arr, start, pivot_index)
    
    return pivot_index
    
def quickSort(arr, left, right):
    if left<right:
        
        pivot_index = pivot_helper(left, right, arr)
    
        quickSort(arr, left, pivot_index)
        quickSort(arr, pivot_index+1, right)
    return arr
    
    
ls = [100,-3,2,4,6,9,1,2,5,3,23]
quickSort(ls, 0, len(ls))
print(ls)
