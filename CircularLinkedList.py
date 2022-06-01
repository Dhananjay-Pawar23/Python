class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class CLinkedList:
    def __init__(self):
        self.head=None
    def print_cll(self):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.ref==self.head:
            print(self.head.data)
            return
        print(self.head.data)
        n=self.head.ref
        while n is not self.head:
            
            print(n.data)
            n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.ref=self.head
            return
        n=self.head
        new_node.ref=self.head
        while n.ref is not self.head:
            n=n.ref
        n.ref=new_node
        self.head=new_node
        print('addded')
    def add_after(self,x,data):
        if self.head is None:
            print('Linked list is empty what to delete')    
            return
        n=self.head
        while n.ref is not self.head:
            if n.data==x:
                break
            n=n.ref
        if n.ref is self.head:
            print('the value is not found in LL')
            return
        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node
    def add_before(self,x,data):
        if self.head is None:
            print('Linked list is empty what to delete')    
            return
        n=self.head    
        while n.ref is not self.head:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is self.head:
            print('the value is not found in LL')
            return
        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node
        
            
                
ll=CLinkedList()  
'''
ll.add_begin(2)
ll.add_begin(4)
ll.add_begin(30)
ll.add_after(4,10)'''
ll.add_before(10,30)
ll.print_cll()          
        