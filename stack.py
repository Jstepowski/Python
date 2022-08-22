class Stack:

    def __init__(self):
        self.stack = list()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        print ("in pop")
        if self.stack:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if self.stack:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
    
    def clear_stack(self):
        while self.stack:
            print (f"Stack in loop: {self.stack}")
            self.pop()

    def reverse_list(self, list_to_reverse):
        new_stack = Stack()
        while list_to_reverse:
            new_stack.push(list_to_reverse.pop())
        return new_stack


stack = Stack()

for i in range (1, 11):
    stack.push(i)

# print (stack)
# stack.clear_stack()
# print (stack)

l = [1 ,2, 3, 4, 5]
reversed = stack.reverse_list(l)
print (reversed)

print (stack)


