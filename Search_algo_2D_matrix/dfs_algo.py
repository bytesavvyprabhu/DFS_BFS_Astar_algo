from stack import Stack
from healper import offset, is_valid_path, get_path

"""sumary_line:-
   - Dfs algo stand for Depth First Search. which is used to find the sortest path in 2D matrix.
   - It is also know as aggressive algorithm either it found the target or it will end on there path.

Keyword arguments:
argument -- 2D matrix, Start co-ordinate and target co-ordinate.
Return: path till target, if target in 2D matrix
"""

def dfs(matrix, start, target):
    s = Stack()
    s.push(start)
    predecessors = {start:None}
    
    while not s.is_empty():
        current_cell = s.pop()
        if current_cell == target:
            return get_path(predecessors,start, target)
        
        for direction in ["up", "right", "down", "left"]:
            x_offset, y_offset = offset[direction]
            neighbour = (current_cell[0]+x_offset, current_cell[1]+y_offset)

            if is_valid_path(matrix, neighbour) and neighbour not in predecessors:
                s.push(neighbour)
                predecessors[neighbour] = current_cell
    return None
                
    