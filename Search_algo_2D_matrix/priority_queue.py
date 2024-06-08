"""sumary_line:-
   - Priority Queue is a type of Data Structure.
   - Which is build on heap data sturcture.
   - It has get, put, is_empty, peek operations
   - get is used for retriving the item with highest priority.
   - put is used for adding item into priority queue.

Keyword arguments:
argument -- description
Return: return_description
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return not self.items
    
    def get(self):
        return heapq.heappop(self.items)[1]
    
    def put(self, item, priority):
        heapq.heappush(self.items,(priority, item))
    
    def __str__(self) -> str:
        return str(self.items)
        