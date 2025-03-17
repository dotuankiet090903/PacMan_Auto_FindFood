import os
from math import sqrt
class SingleFoodSearchProblem:
    moves = {
        'N': (-1,0),
        'S': (1,0),
        'E': (0,1),
        'W': (0,-1)
    }
    def __init__(self, filename: str) -> None:
        self.load_from_file(filename)
        self.AL = {}
        for i in range(1,len(self.maze)-1):
            for j in range(1,len(self.maze[0])-1):
                if self.maze[i][j] != '%':
                    self.successor(i,j)
    
    def successor(self,x: int,y: int) -> None:
        self.AL[(x,y)] = []
        for move, (dx,dy) in self.moves.items():
          new_x, new_y = x + dx, y + dy
          if self.maze[new_x][new_y] != '%':
            self.AL[(x,y)].append((move,(new_x,new_y)))

    def load_from_file(self, filename: str) -> None:
        self.start,self.end = None, None
        with open(filename,'r') as f:
            maze = f.read().split('\n')
            self.maze = maze
            for i in range(1, len(maze) - 1):
                for j in range(1, len(maze[0]) - 1):
                    if maze[i][j] == 'P':
                       self.start = (i,j)
                    if maze[i][j] == '.':
                       self.end = (i,j)
            if self.start == None or self.end == None:
                raise Exception("There is no start or end in this maze")
            
            
    def print_maze(self):
        for r in self.maze:
            print(r)

    def print_move(self,steps: list[str]):
        maze = [list(row) for row in self.maze]
        x,y = self.start
        for step in steps:
            if step == 'Stop':
                break
            dx,dy = self.moves[step]
            x , y = x + dx, y + dy
            if (x,y) == self.end:
                maze[x][y] = '!'
            elif (x,y) == self.start:
                maze[x][y] = 'P'
            else:    
                maze[x][y] = "-"
        for r in maze:
            print(''.join(r))

    def goal_test(self,curr_pos):
        return curr_pos == self.end
    
    def animate(self,steps:list[str]):
        os.system('cls')
        maze = [list(row) for row in self.maze]
        x,y = self.start
        self.print_maze()
        print(f"Pacman:{self.start}")
        print(f"Food:{self.end}")
        input("Press Enter to continue")
        for step in steps:
            os.system('cls')
            if step == 'Stop':
                break
            dx,dy = self.moves[step]
            x,y = x+dx,y + dy
            if (x,y) == self.end:
                maze[x][y] = '!'
            else:
                maze[x][y] = '-'
            for r in maze:
                print(''.join(r))
            print(f"Pacman:{(x,y)}")
            print(f"Food:{self.end}")
            input('Press Enter to continue')
        for r in maze:
            print(''.join(r))
        print("Pacman has reached his food")
    def get_hue_man(self,curr_pos,end):
        for i in end:#Manhattan distance D*(abs(dx-x) + abs(dy-y)) \\ D is 1 in this function
            x,y = curr_pos              #For an admissible heruristic set D to the lowest cost between adjacent squares    
            dx,dy = i
            return abs(dx-x) + abs(dy-y)
    def get_hue_eucli(self,curr_pos,end):#Euclidean distance D * sqrt(dx * dx + dy * dy) \\ D is 1 in this function
        for i in end:
            x,y = curr_pos               #Shorter than man but not effective for this type of maze because you can't move diag
            dx,dy = i           #And not admissible in this maze because it underestimate the distance 
            fx = abs(x-dx)
            fy = abs(y-dy)
            return sqrt((fx*fx) + (fy*fy))

        
class MultiFoodSearchProblem:
    moves = {
        'N': (-1,0),
        'S': (1,0),
        'E': (0,1),
        'W': (0,-1)
    }
    def __init__(self,filename:str) -> None:
        self.load_from_file(filename)
        self.AL = {}
        for i in range(1,len(self.maze)-1):
            for j in range(1,len(self.maze[0])-1):
                if self.maze[i][j] != '%':
                    self.successor(i,j)      
    def successor(self,x: int,y: int) -> None:
        self.AL[(x,y)] = []
        for move, (dx,dy) in self.moves.items():
          new_x, new_y = x + dx, y + dy
          if self.maze[new_x][new_y] != '%':
            self.AL[(x,y)].append((move,(new_x,new_y)))

    def load_from_file(self, filename: str) -> None:
        self.start,self.end = None, None
        with open(filename,'r') as f:
            maze = f.read().split('\n')
            self.maze = maze
            food = set()
            for i in range(1, len(maze) - 1):
                for j in range(1, len(maze[0]) - 1):
                    if maze[i][j] == 'P':
                       self.start = (i,j)
                    if maze[i][j] == '.':
                       food.add((i,j))
            self.end = food
            if self.start == None or self.end == None:
                raise Exception("There is no start or end in this maze")
            
    def print_maze(self):
        for r in self.maze:
            print(r)

    def print_move(self,steps: list[str]):
        maze = [list(row) for row in self.maze]
        x,y = self.start
        for step in steps:
            if step == 'Stop':
                break
            dx,dy = self.moves[step]
            x , y = x + dx, y + dy
            if (x,y) in self.end:
                maze[x][y] = '!'
            elif (x,y) == self.start:
                maze[x][y] = 'P'
            else:    
                maze[x][y] = "-"
        for r in maze:
            print(''.join(r))

    def goal_test(self,curr_pos, end_pos):
       return curr_pos in end_pos
    
    def animate(self,steps:list[str]):
        os.system('cls')
        maze = [list(row) for row in self.maze]
        x,y = self.start
        end = self.end
        self.print_maze()
        print(f"Pacman:{self.start}")
        print(f"Food:{end}")
        input("Press Enter to continue")
        for step in steps:
            os.system('cls')
            if step == 'Stop':
                break
            dx,dy = self.moves[step]
            x,y = x+dx,y + dy
            if (x,y) in end:
                maze[x][y] = "!"
                end.remove((x,y))
            elif (x,y) == self.start:
                maze[x][y] ='P'
            else:
                if maze[x][y] == '-':
                    maze[x][y] = '+'
                elif maze[x][y] == '!':
                    continue
                else:
                    maze[x][y] = '-'
            for r in maze:
                print(''.join(r))
            print(f"Pacman:{(x,y)}")
            print(f"Food:{end}")
            input('Press Enter to continue')
        for r in maze:
            print(''.join(r))
        print("Pacman has reached all of his foods")
    def get_man(self,curr_pos,end):
        x,y = curr_pos
        dx,dy = end
        return abs(dx-x) + abs(dy-y)
    def get_hue_multi(self,curr_pos,end):
        h = []
        for i in end:
            h1 = self.get_man(curr_pos,i)
            h.append(h1)
        return min(h)


    

