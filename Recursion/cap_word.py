def cap_first(arr):
    if(len(arr)==1):
        return [(arr[0].upper())]
    return [(arr[0].upper())] + cap_first(arr[1:])

print(cap_first(['ola','mundo','como','esta']))
