#write a function to delete fist & last node of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_first_last(head):
    # If list is empty or has only one node
    if head is None or head.next is None:
        return None

    # Delete first node
    head = head.next

    # If only one node remains, return it
    if head.next is None:
        return head

    # Find second-last node
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    # Delete last node
    temp.next = None

    return head

