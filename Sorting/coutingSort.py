def countingSort(arr):
    minn = min(arr)
    maxx = max(arr)
    new_arr = [0 for l in range(len(arr))]
    aux_arr = [0 for k in range(minn, maxx+1) ]
    for i in arr:
        aux_arr[i-minn]+=1
    for i in range(1,len(aux_arr)):
        aux_arr[i] += aux_arr[i-1]
    aux_arr_2 = [0]
    for i in range(1,len(aux_arr)):
        aux_arr_2.append(aux_arr[i-1])
    del aux_arr
    for i in arr:
        new_arr[aux_arr_2[i-minn]] = i
        aux_arr_2[i-minn] +=1
        
    return new_arr
    
print(countingSort([2,3,0,0,2,3,9,2,7,10]))
