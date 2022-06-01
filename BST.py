class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
            if self.key==data:
                print('This is present in bst')
                return
            if self.key>data:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    print('This element is not present')
            else:
                if self.rchild:
                    self.rchild.search(data)
                else:
                    print('This element is not present')
             
                 
root=BST(8)
li=[6,3,1,2,98,9]
for i in li:
    root.insert(i)    
root.insert(7)                    
root.search(98)   
root.search(8)                 
                
                
            
        
        
         	
         	