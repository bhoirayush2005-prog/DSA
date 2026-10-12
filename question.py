# find middle node and delete it

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


# Find and delete middle node
slow = head
fast = head
prev = None

while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next

# Delete middle node
prev.next = slow.next


# Print linked list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
