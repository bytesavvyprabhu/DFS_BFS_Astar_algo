

# Offset is used to calculate the neighbour 

offset = {
    "up"    : (-1,0),
    "left"  : (0,-1),
    "right" : (0, 1),
    "down"  : (1,0)
}

# this function is used to check whether the co-ordinate is within the matrix or not ?
def is_valid_path(matrix, current_position):
    x, y = current_position[0], current_position[1]
    return 0<= x <len(matrix) and 0<= y < len(matrix[0]) and matrix[x][y] != '*'

def get_path(predecessors, start, target):
    path = []
    current = target
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def heuristic(target, neighbour):
    x,y = neighbour
    x_t, y_t = target
    return abs(x_t-x) + abs(y_t-y)

def read_2d_matrix(file):
    with open(f'./maze_in_txt/{file}','r') as f:
        f = f.read()
    list_2d = [[cha for cha in line.strip("\n")] for line in f.splitlines()]
    len_1st_row = len(list_2d[0])
    for row in list_2d:
        if len(row) != len_1st_row:
            print("this maze is not a rectangle")
    return list_2d
