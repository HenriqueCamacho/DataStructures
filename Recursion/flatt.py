def flatt(arr):
    newarr = []
    for i in arr:
        if isinstance(i,list):
            newarr+= (flatt(i))
        else:
            newarr.append(i)
    return newarr
print(flatt([5,6,[7,8]]) )
