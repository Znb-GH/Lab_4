class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (bottom -> top):", self.items)
text = input("Enter a string: ")
s = Stack()
for char in text:
    s.push(char)
reversed_text = ""
while not s.is_empty():
    reversed_text += s.pop()
print("Original: ", text)
print("REVERSED : ", reversed_text)
    