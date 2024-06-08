"""sumary_line:- 
   - BFS stand for breadth first search. Which is used to find the sortest path till the target in 2D Matrix.
   - It work like water is sperading on the floor. means it will search to all his neighbour element.

Keyword arguments:
argument -- 2D matrix, start(co-ordinate), target(co-ordinate).
Return: list of co-ordinate which is path to the target.
"""

from queue_my import Queue
from healper import offset, is_valid_path, get_path
def bfs(matrix, start, target):
    q = Queue()
    q.enqueue(start)
    predecessors = {start : None}
    
    
    while not q.is_empty():
        current_cell = q.dequeue()
        if current_cell == target:
            return get_path(predecessors, start, target)
        
        for direction in ["up", "right", "down", "left"]:
            x_offset, y_offset = offset[direction]
            neighbour = (current_cell[0]+x_offset, current_cell[1]+y_offset)
            
            if is_valid_path(matrix, neighbour) and neighbour not in predecessors:
                q.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None