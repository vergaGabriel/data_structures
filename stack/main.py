def length(stack):
    value = 0 
    for item in stack:
        value = value + 1
        
    return value


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[length(self.items) - 1]

    def size(self):
        return length(self.items)

stack = Stack()
stack.push(8)
stack.push(10)
stack.push(9)

print(stack.peek())

