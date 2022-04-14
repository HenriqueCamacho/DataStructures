func = lambda val:(val%2)!=0
gtr = lambda val:val>10

def someRecursive(arr, callback):
    if len(arr)==0:
        return False
    elif(callback(arr[0])):
        return True;
    return someRecursive(arr[1:], callback)

print(someRecursive([2,2,11,2], gtr))
