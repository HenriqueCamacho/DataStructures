class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
       
    #Add node to the end of the list/Add a new tail    
    def push(self, value):
        newnode = Node(value)
        if self.length==0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        
        self.length+=1
        
    #Remove node from the end of the list    
    def pop(self):
        copy = self.tail
        if self.length == 0:
            return None   
            
        elif self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            copy.prev = None           
                    
        self.length -=1
        return copy
    
    #Remove node from the beginning of the list
    def shift(self):
        copy = self.head
        if self.length == 0:
            return None
            
        elif self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            copy.next = None            

        self.length -=1
        return copy
        
    #Add node to the beggining of the list/a new head    
    def unshift(self, val):
        newnode = Node(val)
        if self.length ==0:
            self.head = newnode
            self.tail = newnode
    
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        
        self.length+=1

    #Get return a number in a certain position
    def get(self, position):
        if position<0 or position>=self.length:
            return None
    
        elif position<= self.length-1-position:
            currnode = self.head
            i = 0
            while i<position:
                currnode= currnode.next
                i+=1
        else:
            currnode = self.tail
            i=0
            while i<self.length-1-position:
                currnode = currnode.prev
                i+=1
                
        return currnode      
    
    #Change the value of a position   
    def set(self, position, value):
        node = self.get(position)
        if node!= None:
            node.value = value
            return True
        else:
            return False   
    
    #Insert a node from a certain position        
    def insert(self, position, value):
        if position<0 or position>self.length:
            return False
        elif position==0:
            self.unshift(value)
        elif position == self.length:
            self.push(value)
        else:
            newnode = Node(value)
            currnode = self.get(position-1)
            newnode.next = currnode.next
            newnode.prev = currnode
            currnode.next.prev = newnode
            currnode.next = newnode
            self.length +=1    
        return True
        
    #Remove a node from a certain position    
    def remove(self, position):
        if position<0 or position>self.length-1:
            return None
        elif position == 0:
            return self.shift()
        elif position == self.length-1:
            return self.pop()
        else:
            currnode = self.get(position)
            currnode.prev.next = currnode.next
            currnode.next.prev = currnode.prev
            currnode.next = None
            currnode.prev = None
            self.length -=1
            return currnode
            

    def printValues(self):
        currnode = self.head
        print(str(self.length) + " Elements ")
        for i in range(self.length):
            print(currnode.value)
            currnode = currnode.next
       
    def printReverse(self):
        currnode = self.tail
        print(str(self.length)+" Elements in reverse")
        for i in range(self.length, 0, -1):
            print(currnode.value)
            currnode = currnode.prev
            
lk = DoublyLinkedList()
lk.push(15)
lk.push(20)
lk.push(28)
lk.push(32)
lk.push(50)
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
print("Pop "+str(lk.pop().value))
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
print("Shift aka remove head "+str(lk.shift().value ) )
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
value = 7
lk.unshift(value)
print("Unshift aka add to the head the value "+str(value))
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
position = 3
print("Value at position "+str(position)+" = "+str(lk.get(position).value ) )
position = 3
value = 750
print("Set aka changingthe value at position "+str(position)+ " to be "+str(value)+" = "+ str(lk.set(position,value)))
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
value = 65
position = 3
print("Inserting value "+str(value)+" at position "+str(position)+" = "+str(lk.insert(position,value)))
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
position = 4
print("Removing position "+str(position)+" = "+str(lk.remove(position).value ))
lk.printValues()
lk.printReverse()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
