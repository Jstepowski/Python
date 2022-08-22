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
        if self.head is None:
            self.head = Node(data, None)
        i = self.head
        while i.next:
            i = i.next
            
        i.next = Node(data, None)
    
    def insert_values(self, values):
        self.head = None
        for value in values:
            self.insert_at_beginning(value)
            
    def print(self):
        if self.head is None:
            print ("Empty list")
            return
        s = ""
        while self.head:
            s += str(self.head.data) + '---->'
            self.head = self.head.next
        print(s)
    
    def len(self):
        i = self.head
        counter = 1
        while i.next:
            counter +=1
            i = i.next
        return counter
    
    def remove_node_by_index(self, i):
        if i < 0 or i >= self.len():
            raise Exception ("Not a valid index")
        if i == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == i - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self, index, item):
        if index < 0 or index > self.len():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(0)
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(item, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1 
        




if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_values([1, 2, 3])
    length = linked_list.len()
    linked_list.print()
    print (f"{length = }")
    