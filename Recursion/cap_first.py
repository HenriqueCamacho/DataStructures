def cap_first(arr):
    if(len(arr)==1):
        return [(arr[0][0].upper()+arr[0][1:])]
    return [(arr[0][0].upper()+arr[0][1:])] + cap_first(arr[1:])

print(cap_first(['ola','mundo','como','esta']))
