#concatenate 2 SLL
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to concatenate two linked lists
def concatenate(head1, head2):
    if head1 is None:
        return head2

    temp = head1

    # Go to the last node of the first list
    while temp.next is not None:
        temp = temp.next

    # Connect the last node to the second list
    temp.next = head2

    return head1

# Function to display the linked list
def display(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# First linked list: 10 -> 20 -> 30
head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)

# Second linked list: 40 -> 50
head2 = Node(40)
head2.next = Node(50)

print("First Linked List:")
display(head1)

print("Second Linked List:")
display(head2)

# Concatenate both lists
head1 = concatenate(head1, head2)

print("After Concatenation:")
display(head1)