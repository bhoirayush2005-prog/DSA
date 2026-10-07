#singly linear linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))

list.print()


class linkedlist:
    def append(self,new node):
        temp = temp.next
    temp.next = new_node
class linkedlist:
    def insert(self,new_node,position):
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
           p = 1
           while(p!=position-1):
               temp = temp.next
               p += 1
            new_node.next = temp.next
            temp.next = new_node
            