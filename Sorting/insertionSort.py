def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        num = arr[i]
        while arr[j]>num and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = num
    
    return arr

ls = [3,2,5,30,20,1]

print("Insertion sort= "+str(insertionSort(ls)))
