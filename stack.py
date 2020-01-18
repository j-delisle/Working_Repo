
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


stack = Stack()
expression = input('Input an expression: ')
bracket = []
# filter out chars that aren't bracketed type
for char in expression:
    if char in '({[]})':
        bracket.append(char)


def paren_match(b1, b2):
    if b1 == '(' and b2 == ')':
        return True
    elif b1 == '[' and b2 == ']':
        return True
    elif b1 == '{' and b2 == '}':
        return True
    else:
        return False


def isBalanced(b):
    index = 0
    is_balanced = True
    while index < len(b) and is_balanced:
        if b[index] in '({[':
            stack.push(b[index])
        else:
            if stack.isEmpty():
                is_balanced = False
            else:
                top_item = stack.pop()
                if not paren_match(top_item, b[index]):
                    is_balanced = False
        index += 1

    if stack.isEmpty() and is_balanced:
        return True
    else:
        return False


print(isBalanced(bracket))
