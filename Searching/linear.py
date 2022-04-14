def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i
    return -1

ls = [1,2,3,4,5]
value = 5

index = linear_search(ls,value)
if(index==-1):
    print("Value not in the array")
else:
    print("Index of "+str(value)+ " = "+ str(index))
