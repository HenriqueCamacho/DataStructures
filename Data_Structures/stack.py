class Node():
    def __init__(self, value):
        self.value = value
        self.next = None    
    
class Stack():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    #Push to top the stack    
    def push(self, value):
        node = Node(value)
        if self.size == 0:
            self.first = node
            self.last = node
        else:    
            node.next = self.first
            self.first = node
            
        self.size +=1
        return self.size
        
    #Remove from the top of the stack
    def pop(self):
        if self.size == 0:
            return None
        elif self.size==1:
            copy = self.first
            self.first = None
            self.last = None
        else:
            copy = self.first
            self.first = self.first.next
            copy.next = None
        
        self.size -=1    
        return copy
        
    def printStack(self):
        print("Printing Stack")
        print('"""""')
        curr = self.first
        for i in range(self.size):
            print(" "+str( curr.value))
            curr = curr.next
        print('"""""')
            
    
pilha = Stack()
pilha.push(5)
pilha.push(7)
pilha.push(9)
print(pilha.push(12)) 
pilha.printStack()
print()
print("First "+str(pilha.first.value))
print("Last "+str(pilha.last.value))
print()
print("First pop = " +str(pilha.pop().value))
print("First "+str(pilha.first.value))
print("Last "+str(pilha.last.value))
print()
print("Second pop = " +str(pilha.pop().value))
print("First "+str(pilha.first.value))
print("Last "+str(pilha.last.value))
pilha.printStack()
