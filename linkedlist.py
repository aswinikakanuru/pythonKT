'''LinkedList

A Linked List is a collection of nodes, where each node contains:
#Data
#A link/reference to the next node
Python doesn't have a built-in Linked List like list.

We can create our own Node class.'''



class Node:
    def __init__(self,data):
          self.data=data
          self.next=None
node1= Node(10)
node2= Node(20)
node3= Node(30)
node1.next=node2
node2.next=node3

current = node1

while current is not None:
        print(current.data)
        current = current.next


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(100)
node2=Node(200)
node3=Node(300)
node4=Node(400)

node1.next=node2
node2.next=node3
node3.next=node4

current=node1
while current is not None:
    print(current.data)
    current=current.next

#Inserting the first Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        

        current=self.head

        while current.next is not None:
            current=current.next

        current.next=newnode

            
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        
ll=LinkedList()
ll.insert(15)
ll.insert(20)
ll.insert(45)

ll.traverse()
