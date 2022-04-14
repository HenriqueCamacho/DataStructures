def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save
    return arr

class Maxbinaryheap():
    def __init__(self):
        self.values = []
    
    def insert(self, value):
        self.values.append(value)
        i = len(self.values)-1
        while i>=1 and self.values[i]>self.values[(i-1)//2]:
            print("entrou")
            swap(self.values, i, (i-1)//2 )
            i = (i-1)//2
            
    def extractMax1(self):
        if len(self.values)==0:
            return -1
        else:
            copy = self.values[0]
            self.values[0] = self.values[len(self.values)-1]
            self.values.pop()
            i = 0
            left =  (i*2)+1  
            right =  (i*2)+2  
            
            while True :
                change = False
                if left>len(self.values)-1 and right>len(self.values) -1:
                    break
                elif right> len(self.values)-1:
                    if self.values[i] < self.values[left]:
                        swap(self.values, i, left)  
                        change = True          
                        i = left
                    else:
                        i = right
                else:
                    if self.values[left] > self.values[right] :
                        if self.values[i] < self.values[left]:
                            swap(self.values, i, left)
                            i = left
                            change = True
                    else:
                        if self.values[i] < self.values[right]:
                            swap(self.values, i, right)
                            i = right
                            change = True
                if change == False:
                    break
                left = i*2+1 
                right = i*2+2
        return copy
        
    def extractMax(self):
        maxx = self.values[0]
        end = self.values.pop()
        if len(self.values)>0:
            self.values[0] = end
            self.sinkdown()
            
        return maxx
        
    def sinkdown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftchildidx = idx*2+1
            rightchildidx = idx*2+2
            troca = None
            
            if leftchildidx < length:
                leftchild = self.values[leftchildidx]
                if leftchild > element:
                    troca = leftchildidx
                 
            if rightchildidx < length:
                rightchild = self.values[rightchildidx]
                if (troca == None and rightchild > element) or (troca != None and rightchild > leftchild) : 
                    troca = rightchildidx
                    
            if troca == None:
                break
            else:
                self.values[idx] = self.values[troca]
                self.values[troca] = element
                idx = troca
                    
heap = Maxbinaryheap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
print(heap.values)
heap.insert(55)
heap.insert(1)
heap.insert(45)
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)
'''print(heap.extractMax())
print(heap.values)
print(heap.extractMax())
print(heap.values)'''
