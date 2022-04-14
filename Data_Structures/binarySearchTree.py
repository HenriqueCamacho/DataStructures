class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    #Find the right place to insert
    def insert(self, value):
        newnode = Node(value)
        #Tree is empty
        if self.root==None:
            self.root = newnode
        else:
            currnode = self.root
            while True:
                if value < currnode.value:
                    #Found the right place
                    if currnode.left == None:
                        currnode.left = newnode
                        break
                    else:
                        currnode = currnode.left
                else:
                    #Found the right place
                    if currnode.right == None:
                        currnode.right = newnode
                        break
                    else:
                        currnode = currnode.right
 
    #Search if a value is in the tree
    def search(self, value):
        if self.root == None:
            return None
        else:
            currnode = self.root
            while True:
                if currnode.value == value:
                    return currnode
                elif value < currnode.value:
                    if currnode.left == None:
                        return None
                    else:
                        currnode = currnode.left
                else:
                    if currnode.right == None:
                        return None
                    else:
                        currnode = currnode.right
                  
    def findMinatRight(self, currnode):
        prevnode = currnode
        node = currnode.right
        while node.left != None:
            prevnode = currnode
            node = node.left
        return node,prevnode                  
        
                        
    def remove(self, node):
        # Base Case
        pass
        
    def Bfs(self):
        visited = []
        queue = [self.root]
        while len(queue)>0:
            element = queue.pop(0)
            visited.append(element.value)
            if element.left!=None:
                queue.append(element.left)
            if element.right!=None:
                queue.append(element.right)
        return visited
        
    def Dps_PreOrder(self):
        visited = []
        node = self.root
        def helper(node):
            visited.append(node.value)
            if node.left != None:
                helper(node.left)
            if node.right!=None:
                helper(node.right)
        helper(node)
        return visited
                
    def Dps_PostOrder(self):
        visited = []
        node = self.root
        def helper(node):
            if node.left != None:
                helper(node.left)
            if node.right!=None:
                helper(node.right)
            visited.append(node.value)
        helper(node)
        return visited
        
    def Dps_InOrder(self):
        visited = []
        node = self.root
        def helper(node):
            if node.left != None:
                helper(node.left)
            visited.append(node.value)
            if node.right!=None:
                helper(node.right)
        helper(node)
        return visited
    
    
bs = BinarySearchTree()
bs.insert(12)
bs.insert(5)
bs.insert(3)
bs.insert(1)
bs.insert(7)
bs.insert(9)
bs.insert(8)
bs.insert(11)
bs.insert(14)
bs.insert(13)
bs.insert(17)
bs.insert(20)
bs.insert(18)
#12
print(bs.root.value)
#5
print(bs.root.left.value)
#3
print(bs.root.left.left.value)
#1
print(bs.root.left.left.left.value)
#7
print(bs.root.left.right.value)
#9
print(bs.root.left.right.right.value)
#8
print(bs.root.left.right.right.left.value)
#11
print(bs.root.left.right.right.right.value)
#14
print(bs.root.right.value)
#13
print(bs.root.right.left.value)
#17
print(bs.root.right.right.value)
#20
print(bs.root.right.right.right.value)
#18
print(bs.root.right.right.right.left.value)
value = 18
print("Is the value "+str(value)+" at the tree? = "+str(bs.search(value).value))
print("Bfs "+str(bs.Bfs()))
print("DPS Pre order "+str(bs.Dps_PreOrder()))
print("DPS Post order "+str(bs.Dps_PostOrder()))
print("DPS In Order "+str(bs.Dps_InOrder()))

