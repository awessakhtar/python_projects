import curses
from curses import wrapper
import queue
import time


'''
Maze discription: 
# obstacle, " " can be navigated, O start, X end point, 
'''
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*3, "X", RED)
            else:
                stdscr.addstr(i, j*3, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
        
    return None

def find_path (maze, stdscr):
    start = "O"
    end = "X" 
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][col] == end:
            return path
    
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue
        
            new_path = path + [neighbor]
            q.put(neighbor, new_path)
        

def find_neighbors(maze, row, col):
    neighbors= []

    if row > 0: # it will go up a node
        neighbors.append((row-1, col))
    
    if row + 1 < len(maze): # it will go down
        neighbors.append((row + 1, col))
    
    if col > 0: # it will go left
        neighbors.append((row, col - 1))
    
    if col + 1 < len(maze): # it will go right
        neighbors.append((row, col + 1))
    
    return neighbors
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # green_black_color = curses.color_pair(1)
    
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
