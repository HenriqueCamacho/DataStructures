def swap(arr, n1, n2):
    save = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = save
    return arr

class Node():
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

class priorityQueue():
    def __init__(self):
        self.values = []
        
    def enqueue(self, value, priority):
        newnode = Node(value, priority)
        self.values.append(newnode)
        i = len(self.values)-1
        while i>=1 and self.values[i].priority < self.values[(i-1)//2].priority:
            print("entrou")
            swap(self.values, i, (i-1)//2 )
            i = (i-1)//2
                    
    def dequeue(self):
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
                leftchild = self.values[leftchildidx].priority
                if leftchild < element.priority:
                    troca = leftchildidx
                 
            if rightchildidx < length:
                rightchild = self.values[rightchildidx].priority
                if (troca == None and rightchild < element.priority) or (troca != None and rightchild < leftchild) : 
                    troca = rightchildidx
                    
            if troca == None:
                break
            else:
                self.values[idx] = self.values[troca]
                self.values[troca] = element
                idx = troca

pqueue = priorityQueue()
pqueue.enqueue("Drunk",5)
pqueue.enqueue("Concussion",2)
pqueue.enqueue("Low Fever",4)
pqueue.enqueue("Exploded Head",1)
pqueue.enqueue("Flu",3)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
print(pqueue.dequeue().val)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
print(pqueue.dequeue().val)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
print(pqueue.dequeue().val)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
print(pqueue.dequeue().val)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
print(pqueue.dequeue().val)
ls = []
for value in pqueue.values:
    ls.append(value.val)
print(ls)
