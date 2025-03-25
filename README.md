# PacMan Auto Find Food using Search Algorithms 

This project implements search algorithms for solving Pacman maze problems, where Pacman must find food in a grid-based world. The AI solves Single-Food Search and Multi-Food Search problems using various search strategies.

## Features
Search algorithms used in this project:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A Search (A*)*
- Greedy Best-First Search (GBFS)

More information about this project:
- Supports single-food and multi-food search problems.
- Uses heuristics (Manhattan, Euclidean) for A* and GBFS.
- Efficient data structures: Stack, Queue, and PriorityQueue.

## Project Structure
pacman-search
 ├── fringe.py          # Stack, Queue, PriorityQueue implementations
 ├── problems.py        # Defines search problems (SingleFood & MultiFood)
 ├── searchAgent.py     # Search algorithms (DFS, BFS, UCS, A*, GBFS)
 ├── maze.txt           # Sample maze file for Pacman navigation
 ├── README.md          # Project documentation

## Maze Format
P → Pacman (Start Position)

. → Food (Goal)

\# → Wall (Obstacle)

(space) → Empty Path

## Usage 
### How to make Pacman start 
- Run the searchAgent.py file
- The code will inform the position of Pacman and the foods.
- Pressing Enter to see the process of Pacman
- Program end when all the food is eaten
  
### Changing Algorithm
You can run different search algorithms by modifying searchAgent.py:
#### Import the problem
from problems import SingleFoodSearchProblem

from searchAgent import dfs, bfs, ucs, a_star, gbfs

#### Load the maze
problem = SingleFoodSearchProblem("maze.txt")

#### Run a search algorithm
solution = a_star(problem, problem.get_hue_man())  # A* with Manhattan heuristic

print(solution)

### Changing maps
You can change different map by modifying the path to map in searchAgent.py file:

For example changing the "\maze\pacman_multi02.txt" with the desire map's path in this piece of code.

thu = MFSP("\maze\pacman_multi02.txt")

path = bfs(thu)


