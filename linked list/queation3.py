#delete alternate node in sll

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_alternate(head):
    # If the list is empty or has only one node, nothing to delete
    if not head or not head.next:
        return head
    
    current = head
    while current and current.next:
        # Save the node to be deleted
        node_to_delete = current.next
        
        # Link current node to the node after the deleted node
        current.next = node_to_delete.next
        
        # Move current to the next valid node in the modified list
        current = current.next
        
    return head
