class node:
    def __init__(self,value):
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

    def append(self,new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp=temp.next
                temp.next = new_node
                new_node.prev = temp
            else : #first Node
                self.head=new_node
    def print(self):
        temp=self.head
        print("list elements:")
        while temp:
            print(temp.data," ")
            temp=temp.next
list=LinkedList()
list.append(node(22))
list.append(node(33))
list.append(node(44))
list.append(node(55))
