
# A node represents one element in a singly linked list.
# Each node stores its data and a pointer to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# This class defines the operations for a singly linked list.
# It keeps track of the first node using the head pointer.
class SinglyLinkedList:
    def __init__(self):
        # head points to the first node in the list.
        self.head = None

    # 1. Create a linked list from a list of values.
    # It adds each value to the end of the list.
    def create(self, values):
        for value in values:
            self.insert_end(value)

    # Insert a new node at the end of the list.
    def insert_end(self, data):
        new_node = Node(data)

        # If the list is empty, the new node becomes the first node.
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node and attach the new node.
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Traverse and print the values in the linked list.
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert a node at a specific position using 0-based indexing.
    # For position 0, insert at the beginning of the list.
    def insert_at_position(self, data, position):
        new_node = Node(data)

        # A negative position is invalid.
        if position < 0:
            print("Invalid position")
            return

        # Insert at the beginning.
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Move to the node before the target position.
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        # If the target position is beyond the end of the list, it is invalid.
        if temp is None:
            print("Invalid position")
            return

        # Insert between temp and temp.next.
        new_node.next = temp.next
        temp.next = new_node

    # 4. Find the middle node of the list using the slow/fast pointer technique.
    def find_middle(self):
        slow = fast = self.head

        # The slow pointer moves one node at a time.
        # The fast pointer moves two nodes at a time.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If the list is not empty, print the middle node.
        if slow:
            print("Middle node:", slow.data)
        else:
            print("List is empty")

    # 5. Delete the first node whose value matches the given key.
    def delete_node(self, key):
        temp = self.head

        # Case 1: Delete the head node.
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Case 2: Traverse the list and remove the matching node.
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    # 6. Reverse the linked list by changing each node's next pointer.
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 7. Print the sum of every two consecutive nodes.
    # Example: 10 + 20 = 30
    def consecutive_sums(self):
        temp = self.head

        while temp and temp.next:
            print(
                temp.data, "+", temp.next.data, "=",
                temp.data + temp.next.data
            )
            temp = temp.next


# Main program starts here.
# Create a linked list object.
ll = SinglyLinkedList()

# Read input values and build the list.
values = list(map(int, input("Enter node values separated by spaces: ").split()))
ll.create(values)

# Display the original list.
print("\nOriginal linked list:")
ll.display()

# Insert a new value at a user chosen position.
position = int(input("\nEnter position to insert: "))
value = int(input("Enter value to insert: "))
ll.insert_at_position(value, position)
ll.display()

# Find and print the middle node.
ll.find_middle()

# Delete a value entered by the user.
key = int(input("\nEnter value to delete: "))
ll.delete_node(key)
ll.display()

# Reverse the list and display it.
print("\nReversed linked list:")
ll.reverse()
ll.display()

# Display the sum of each pair of adjacent values.
print("\nSum of consecutive node values:")
ll.consecutive_sums()
