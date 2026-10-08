class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def delete(self, pos):
        # Delete first node
        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        p = 1

        # Move to node before the position
        while p < pos - 1:
            temp = temp.next
            p += 1

        # Delete the node
        temp.next = temp.next.next

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
list = LinkedList()

list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)

print("Before deletion:")
list.display()

# Delete node at position 3
list.delete(3)

print("After deletion:")
list.display()