

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)


    def is_empty(self):
        return not self.stack
    
    def pop(self):
        if self.is_empty:
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.is_empty:
            return None
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


def idontcareaboutit(filename):
    stack = Stack()

    filename = 'stacks.txt'

    with open(filename, 'r') as file:
        print(file.read)
        for line in file:
            words = line.split
            for word in words:
                stack.push(word)

reverse_stack = []
pri


    

        