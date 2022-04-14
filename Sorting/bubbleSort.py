'''We dont need a function to do that'''
def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save
    return arr

def bubbleSort(arr):
    for i in range(len(arr), 0, -1):
        aux = True
        for j in range(i - 1):
            if arr[j]>arr[j+1]:
                arr = swap(arr, j, j+1)
                aux = False
        if aux==True:
            break
    return arr

ls = [15,1,2,4,10,14,11]
print("Bubble sort = "+ str(bubbleSort(ls)) )
