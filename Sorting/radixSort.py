import math
import itertools

def getDigit(number, position):
    '''if position>len(str(number)):
        return 0
    return int(str(number)[len(str(number))-position])'''
    #Or
    return (math.floor(abs(number) / math.pow(10,position)) )% 10
    
    
print(getDigit(7323,3))

def digitCount(number):
    '''
    return len(str(number))'''
    #Or
    if number==0:
        return 1
    return math.floor(math.log10(abs(number))) +1
    
print(digitCount(7323))
    
def mostDigits(arr):
    '''return digitCount(max(arr))'''
    #Or
    menor = 0
    for n in arr:
        if digitCount(n)>menor:
            menor = digitCount(n)
    return menor
    
print(mostDigits([732233,56,1,123,0]))

def radixSort(arr):
    n_digits = mostDigits(arr)
    for i in range(n_digits):
        buckets = [[] for k in range(10)]
        for numb in arr:
            buckets[getDigit(numb, i)].append(numb)
        print(buckets)
        arr = list(itertools.chain.from_iterable(buckets))
    return arr
    
print(radixSort([732233,56,1,123,0,7,900,512]))
        
        
        
        
        
