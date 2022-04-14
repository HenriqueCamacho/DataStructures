def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save
    return arr


def selectionSort(arr):
    for i in range(len(arr)-1):
        menor = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[menor]:
                menor = j
        if menor!=i:
            arr = swap(arr, i, menor)
    return arr

ls = [3,7,2,4,3,10,15,11,4,1]
print("Selection sort = "+ str(selectionSort(ls)) )        
