"""sumary_line:-
    - This Queue class is used to make a queue DataStructure. Which follow the rule of First in First Out.
    - This Queue Data structure has enqueue(new item insert) and dequeue(remove item).
    - enqueue will be happen at the tail of list.
    - dequeue will be happen at the head of list.
    - peek will be used to retun the head of element from queue.
    - size is used to get the size of queue
Keyword arguments:
argument -- description
Return: return_description
"""

# deque is a data structure which is stand for double ended queue, by which we can do insertion and deletion 
# at both end.
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
        
    def is_empty(self):
        return not self.items
    
    def peek(self):
        return self.items[0]
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return  self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    
if __name__ == "__main__":
    q = Queue()
    print(q)