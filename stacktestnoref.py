class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data, None)
    
    def delete_node(self, data):
        i = self.head

        while i.next:
            if i.next == 
            i = i.next


    
        