class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class AvlTree():
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
        if self.root.left!= None or self.root.right!=None:
            self.balance_Tree()
            
        print(self.Dps_PreOrder() )         
            
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
        
    def balanceFactor(self, currnode):
        if self.root == None:
            return 0
        return self.height(currnode.left)- self.height(currnode.right)
        
    def height(self, currnode):
        if currnode == None:
            return -1
        iEsque = self.height(currnode.left)
        iDirei = self.height(currnode.right)
        if iEsque>iDirei:
            return iEsque+1
        else:
            return iDirei+1
            
    def balance_Tree(self):
        balance = self.balanceFactor(self.root)
        if balance>1:
           self.root = self.balanceLeft(self.root)
        elif balance<-1:
            self.root = self.balanceRight(self.root)
            
    def simple_LeftRotation(self, currnode):
        aux = currnode.right
        currnode.right = aux.left
        aux.left = currnode
        return aux
        
    def simple_RightRotation(self, currnode):
        aux = currnode.left
        currnode.left = aux.right
        aux.right = currnode
        return aux
        
    def balanceLeft(self, currnode):
        fb = self.balanceFactor(currnode.left)
        if fb >=0:
            currnode = self.simple_RightRotation(currnode)
        else:
            currnode.left = self.simple_LeftRotation(currnode.left)
            currnode = self.simple_RightRotation(currnode)
        return currnode
        
    def balanceRight(self, currnode):
        fb = self.balanceFactor(currnode.right)
        if fb <=0:
            currnode = self.simple_LeftRotation(currnode)
        else:
            currnode.right = self.simple_RightRotation(currnode.right)
            currnode = self.simple_LeftRotation(currnode)
        return currnode
                     
avl = AvlTree()
'''avl.insert(12)
avl.insert(8)
avl.insert(5)
avl.insert(4)
avl.insert(2)
avl.insert(7)
avl.insert(11)
avl.insert(18)
avl.insert(17)'''
'''avl.insert(2)
avl.insert(1)
avl.insert(4)
avl.insert(3)
avl.insert(5)
avl.insert(6)'''
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)
avl.insert(7)
avl.insert(8)
avl.insert(9)


print(avl.Dps_PreOrder())
print("Fb do "+str(avl.root.value)+" = "+str(avl.balanceFactor(avl.root) ) )
print(avl.Dps_PreOrder())
