print("Welcome in game of finding sortest path")
print("""
      Rule of playing this game:-
      Rule1:- Choose the file from given option to convert it into matrix. 
      RUle2:- Provide the target value like which should be present in the matrix.
      Rule3:- Select the Algorithm from option.
      """)

from utils import list_files
file = list_files('maze_in_txt')

from healper import read_2d_matrix
matrix = read_2d_matrix(file)
start = input("Enter the start position co-ordinate in (x,y) format: ")
x,y = start.split(',')
start = (int(x), int(y))
target = input("Enter the Target position co-ordinate in (x,y) format :")
x,y = target.split(',')
target = (int(x), int(y))

print("""
      Please Select the Algo to find the sortest path:-
      1:- DFS
      2:- BFS
      3:- A*
      """)
algo_option = int(input("Enter your option : "))

from dfs_algo import dfs
from bfs_algo import bfs
from a_star_algo import a_star
'''
dict = {
    '1': dfs(matrix, start, target),
    '2': bfs(matrix, start, target),
    '3': a_star(matrix, start, target)
}
print(dict[algo_option])
'''
if algo_option == 1:
    print(dfs(matrix, start, target))
elif algo_option == 2:
    print(bfs(matrix, start, target))
else:
    print(a_star(matrix, start, target))
    
