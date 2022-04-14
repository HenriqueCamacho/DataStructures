class Node():
    def __init__(self, value):
        self.value = value
        self.next = None    
    
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Push insert at the end
    def push(self, val):
        #Initializing the node
        newnode = Node(val)
        #If the List is empty, then head and tail are the same
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length+=1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.length+=1
        print(str(val) +" inserted with sucess!!")
        
    #Pop removes from the end
    def pop(self):
        #Just one element removes node
        if self.length ==0:
            return None
        elif self.length==1:
            copy = self.head
            del self.head
            self.head = None
            self.tail = None    
            self.length = 0
            return copy
        else:
            currnode = self.head
            while currnode.next.next != None :   
                currnode = currnode.next
            copy = currnode.next
            del currnode.next
            currnode.next = None
            self.tail = currnode
            self.length -= 1
            return copy
            
    #Removes head
    def shift(self):
        copy = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length =0
        else:
            self.head = self.head.next
            self.length -=1
        return copy
        
    #Add to the beggining, head    
    def unshift(self, val):
        if self.length == 0:
            self.push(val)
        else:    
            newnode = Node(val)
            newnode.next = self.head
            self.head = newnode  
            self.length += 1      

    def printValues(self):
        currnode = self.head
        print(str(self.length) + " Elementos ")
        for i in range(self.length):
            print(currnode.value)
            currnode = currnode.next
    
    #Get node at certain position        
    def get(self, position):
        if position>=self.length or position<0:
            print("Position bigger than list number of elements")
            return None
        else:
            currnode = self.head
            i = 0
            while i<position:
                currnode = currnode.next
                i+=1
        return currnode
        
    #Change the value of a node of a certain position    
    def set(self, position, val):
        node = self.get(position)
        if node==None:
            return False
        else:
            node.value = val
            return True
         
    #Insert a node at a certain position        
    def insert(self, position, val):
        if position<0 or position>self.length:
            return False
        elif position == 0:
            self.unshift(val)
            return True
        elif position == self.length:
            self.push(val)
            return True
        else:
            newnode = Node(val)
            prevnode = self.get(position-1)
            newnode.next = prevnode.next
            prevnode.next = newnode
            self.length+=1
            return True
            
    #Remove a node from a certain position        
    def remove(self, position):
        if position<0 or position>self.length-1:
            return None
        elif position==0:
            return self.shift()
        elif position==self.length-1:
            return self.pop()
        else:
            prevnode = self.get(position-1)
            copy = prevnode.next
            prevnode.next = prevnode.next.next
            self.length -=1
            return copy

    def reverse(self):
        prevnode = self.head
        currnode = prevnode.next
        for i in range(self.length-1):
            aux = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = aux
        aux = self.head
        self.head = self.tail
        self.tail = aux
        self.tail.next = None

lk = SinglyLinkedList()
lk.push(10)
lk.push(16)
lk.push(17)
lk.push(20)
lk.push(25)
lk.printValues()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
print("Pop " + str(lk.pop().value ))
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
print("Shifted aka fuck head "+str(lk.shift().value))
lk.printValues()
lk.push(100)
lk.printValues()
print("Unshift aka add to the head")
lk.unshift(13)
lk.printValues()
position = 4
print("Node at position "+ str(position) + "= "+str(lk.get(position).value))
lk.push(200)
position = 5
print("Node at position " + str(position) + " = "+str(lk.get(position).value))
position = 3
val = 21
print("Setting the " + str(position) + " position to be " + str(val) + " = "+str(lk.set(position, val)))
lk.printValues()
position = 4
val = 55
print("Inserting" + str(val) + "at position"+ str(position) + "= "+str(lk.insert(position,val)))
lk.printValues()
position = 6
print("Removing at position "+ str(position) +" = "+str(lk.remove(position).value))
lk.printValues()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
lk.reverse()
print("Reversing the list")
lk.printValues()
print("Head " +str(lk.head.value))
print("Tail " +str(lk.tail.value))
