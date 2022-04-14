class Node():
    def __init__(self, value):
        self.value = value
        self.next = None    
    
class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    #Add to the end of the queue
    def enqueue(self, value):
        node = Node(value)
        if self.size==0:
            self.first = node
            self.last = node
        else:
            self.last.next  = node
            self.last = node
        
        self.size+=1
        return self.size
    
    #Remove from the first position of the queue 
    def dequeue(self):
        copy = self.first
        if self.size == 0:
            return copy
        elif self.size == 1: 
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            copy.next = None
            
        self.size -=1    
        return copy
        
    def printQueue(self):
        node = self.first
        print("###Printing queue###")
        for i in range(self.size):
            print(node.value, end = " ")
            node = node.next
        print()
        
fila = Queue()
print("Size "+str(fila.enqueue(6)))
print("First "+ str(fila.first.value))
print("Last "+ str(fila.last.value))
print()
print("Size "+str(fila.enqueue(8)))
'''printt("Size "+str(fila.enqueue(11)))
printt("Size "+str(fila.enqueue(15)))'''
print("First "+ str(fila.first.value))
print("Last "+ str(fila.last.value))
fila.printQueue()
print()
print("Dequeu "+str(fila.dequeue().value))
fila.printQueue()
print("First "+ str(fila.first.value))
print("Last "+ str(fila.last.value))
