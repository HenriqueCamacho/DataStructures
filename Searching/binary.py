def binary_search(arr, value):
    left = 0
    right = len(arr)-1
    while(left<=right):
        middle = (left+right)//2
        if (arr[middle]==value):
            return middle
        elif(arr[middle]<value):
            left = middle+1
        else:
            right = middle-1
    return -1


ls = [5,9,20,65,214,300]
value = 5

index = binary_search(ls,value)
if(index==-1):
    print("Value not in the array")
else:
    print("Index of "+str(value)+ " = "+ str(index))

def rec_binary_search(arr, value, left, right):
    middle = (left+right)//2
    if left>right:
        return -1
    elif arr[middle] == value:
        return (middle)
    elif arr[middle]<value:
        return rec_binary_search(arr, value, middle+1, right)

    return rec_binary_search(arr, value, left, middle-1 )    

ls = [5,9,20,65,214,300]
value = 214

index = rec_binary_search(ls,value, 0, len(ls)-1)
if(index==-1):
    print("Value not in the array")
else:
    print("Index of "+str(value)+ " = "+ str(index))
    
