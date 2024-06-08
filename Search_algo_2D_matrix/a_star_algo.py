"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from priority_queue import PriorityQueue
from healper import offset, is_valid_path, get_path, heuristic, read_2d_matrix


def a_star(matrix, start, target):
    pq = PriorityQueue()
    priority = 0
    pq.put(start, priority)
    
    predecessors = {start : None}
    g_value = {start : 0}
    
    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == target:
            return get_path(predecessors, start, target)
            
        for direction in ["up","right", "down", "left"]:
            x_offset, y_offset = offset[direction]
            neighbour = (current_cell[0]+x_offset, current_cell[1]+y_offset)
            if is_valid_path(matrix, neighbour) and neighbour not in predecessors:
                new_cost = g_value[current_cell] + 1
                g_value[neighbour] = new_cost
                f_values = new_cost + heuristic(target, neighbour)
                pq.put(neighbour, f_values)
                predecessors[neighbour] = current_cell
    return None


if __name__ == "__main__":
    start = (0,0)
    target = (3,3)
    file = ""# give file name
    maze = read_2d_matrix(file)
    result = a_star(maze, start, target)