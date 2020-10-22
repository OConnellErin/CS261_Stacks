# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Erin O'Connell

class Stack:

    def __init__(self):
        self.next_index = 0
        self.data = []
        pass

    def is_empty(self):
        if self.next_index == 0:
            return True
        else: 
            return False    

    def pop(self):
        self.next_index -= 1
        if self.next_index < 0:
            raise IndexError
        return self.data[self.next_index]

    def peek(self):
        if self.next_index == 0:
            raise IndexError
        return self.data[self.next_index-1]

    def push(self,value):
        # if number > self.next_index or number < 0:
        #     raise IndexError
        self.data.append(value)     
        self.next_index += 1

        