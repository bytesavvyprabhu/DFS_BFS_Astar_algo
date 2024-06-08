
"""sumary_line:-
   - This Stack is used to ake a Stack Data Structure. Which should have push(), pop(), is_empty() and peek() operation.
   - Stack follow the rule of Last IN FIrst Out(LIFO).

Keyword arguments:
argument -- description
Return: return_description
"""


class Stack:
    def __init__(self):
        self.items = []
        
    # put() is used to add element in Stack
    def push(self, item):
        return self.items.append(item)

    # pop() is used to delete element from right hand side 
    def pop(self):
        return self.items.pop()
    
    # peek() is used to return the peek element of stack which is last element
    def peek(self):
        return self.items[-1]
    
    # is_empty() is used to check whether stack is empty or not
    def is_empty(self):
        return not self.items
    
    
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())