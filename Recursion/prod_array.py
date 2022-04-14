def prodarr(arr):
    if(len(arr)==0):
        return 0
    return arr[0]+prodarr(arr[1:])

print(prodarr([2,2,2,2]))
