
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # create a new node for the list
        self.head = node
    
    def insert_at_end(self, data):
        if not self.head:
            node = Node(data, None)
            self.head = node
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data, None)
    
    def print_list(self):
        if self.head == "None":
            print ("Empty List")
            pass
        i = self.head
        s = ""
        while i:
            s += str(i.data) + "--->"
            i = i.next
        print(s)


        

linked_list = LinkedList()
linked_list.print_list()

linked_list.insert_at_beginning(1)
linked_list.print_list()
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.insert_at_end(4)

linked_list.print_list()

        

