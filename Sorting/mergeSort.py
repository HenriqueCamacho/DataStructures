from math import floor
import time
import random


def merge(arr1, arr2):
    arr3 = [0 for i in range(len(arr1)+len(arr2))]
    i = 0
    j = 0
    while True:
        if i>(len(arr1)-1):
            arr3[i+j:] = arr2[j:]
            break                        
        elif j>(len(arr2)-1):
            arr3[j+i:] = arr1[i:]
            break  
        elif arr1[i]<=arr2[j]:
            arr3[i+j] = arr1[i]
            i+=1
        else:
            arr3[i+j] = arr2[j]
            j+=1
    return arr3

print(merge([2,3,14,99,100,200,200],[1,10,50,200,500]))

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    return merge( mergeSort(arr[:(len(arr))//2]), mergeSort(arr[(len(arr)//2):]) ) 


def mergeSort2(arr):
    if len(arr)<=1:
        return arr
    mid = floor(len(arr)/2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge( left, right ) 

def mergeSort3(a):
     
    current_size = 1
     
    # Outer loop for traversing Each
    # sub array of current_size
    while current_size < len(a) - 1:
         
        left = 0
        # Inner loop for merge call
        # in a sub array
        # Each complete Iteration sorts
        # the iterating sub array
        while left < len(a)-1:
             
            # mid index = left index of
            # sub array + current sub
            # array size - 1
            mid = min((left + current_size - 1),(len(a)-1))
             
            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(a)-1
            # else len(a)-1
            right = ((2 * current_size + left - 1,
                    len(a) - 1)[2 * current_size
                        + left - 1 > len(a)-1])
                             
            # Merge call for each sub array
            mmerge(a, left, mid, right)
            left = left + current_size*2
             
        # Increasing sub array size by
        # multiple of 2
        current_size = 2 * current_size
 
# Merge Function
def mmerge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


ls = [random.randint(1, 10000000) for i in range(1000000)]


start = time.time()
mergeSort(ls)
end = time.time()
print("Tempo com minha implementação = "+str(end-start))


start = time.time()
mergeSort2(ls)
end = time.time()
print("Tempo com a implementação do Colt = "+str(end-start))

start = time.time()
mergeSort3(ls)
end = time.time()
print("Tempo com minha implementação iterativa = "+str(end-start))
