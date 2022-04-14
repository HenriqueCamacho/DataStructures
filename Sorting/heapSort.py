def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save
    return arr

class Minbinaryheap():
    def __init__(self):
        self.values = []
    
    def insert(self, value):
        self.values.append(value)
        i = len(self.values)-1
        while i>=1 and self.values[i]<self.values[(i-1)//2]:
            print("entrou")
            swap(self.values, i, (i-1)//2 )
            i = (i-1)//2
        
    def extractMin(self):
        if len(self.values) == 0:
            return -1
        minn = self.values[0]
        end = self.values.pop()
        if len(self.values)>0:
            self.values[0] = end
            self.sinkdown()
            
        return minn
        
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
                if leftchild < element:
                    troca = leftchildidx
                 
            if rightchildidx < length:
                rightchild = self.values[rightchildidx]
                if (troca == None and rightchild < element) or (troca != None and rightchild < leftchild) : 
                    troca = rightchildidx
                    
            if troca == None:
                break
            else:
                self.values[idx] = self.values[troca]
                self.values[troca] = element
                idx = troca
 
def heapSort(heap):
    sorteed = []
    element = heap.extractMin()
    while element !=-1:
        sorteed.append(element)
        element = heap.extractMin()
    return sorteed
 
arr = [5.1.15.18.100.75.42] 
heap = Minbinaryheap()
heap.insert(5)
heap.insert(1)
heap.insert(15)
heap.insert(18)
heap.insert(100)
heap.insert(75)
heap.insert(42)
print(heap.values)
print(heapSort(heap))
