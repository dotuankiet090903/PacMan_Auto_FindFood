from fringe import Stack, Queue, PriorityQueue
from problems import MultiFoodSearchProblem as MFSP, SingleFoodSearchProblem as SFSP
import copy
def backtrace(parent, start, end):
    path = []
    node = end
    while node != start:
        move, parent_node = parent[node]
        path.append(move)
        node = parent_node
    path.reverse()
    path.append("Stop")
    return path
#Uninformed search
def dfs(problem):
    curr_problem = copy.deepcopy(problem)
    remain_goal = copy.deepcopy(curr_problem.end)
    if isinstance(problem,SFSP):
        x,y = remain_goal
        remain_goal = set()
        remain_goal.add((x,y))
    
    path = []
    start = copy.deepcopy(curr_problem.start) # get starting position
    while remain_goal:
        stack = Stack()
        stack.push(start)
        parent = dict()
        expanded = []
        break_loop = False
        while not stack.is_empty() and not break_loop:
            curr_pos = stack.pop()
            expanded.append(curr_pos)
            if curr_pos in remain_goal:
                remain_goal.remove(curr_pos)
                path = path[:-1] + backtrace(parent, start, curr_pos)
                start = curr_pos
                break_loop = True
                break
            
            for move, v in problem.AL.get(curr_pos, []):
                if v not in expanded:
                    stack.push(v)
                    parent[v] = (move, curr_pos)
    
    return path  
def bfs(problem):
    curr_problem = copy.deepcopy(problem)
    remain_goal = copy.deepcopy(curr_problem.end)
    if isinstance(problem,SFSP):
        x,y = remain_goal
        remain_goal = set()
        remain_goal.add((x,y))
    path = []
    start = copy.deepcopy(curr_problem.start) # get starting position
    while remain_goal:
        queue = Queue()
        queue.enqueue(start)
        parent = dict()
        expanded = []
        break_loop = False
        while not queue.is_empty() and not break_loop:
            curr_pos = queue.dequeue()
            expanded.append(curr_pos)
            if curr_pos in remain_goal:
                remain_goal.remove(curr_pos)
                path = path[:-1] + backtrace(parent, start, curr_pos)
                start = curr_pos
                break_loop = True
                break
            
            for move, v in problem.AL.get(curr_pos, []):
                if v not in expanded:
                    queue.enqueue(v)
                    parent[v] = (move, curr_pos)
    
    return path
def ucs(problem):
    curr_problem = copy.deepcopy(problem)
    remain_goal = copy.deepcopy(curr_problem.end)
    if isinstance(problem,SFSP):
        x,y = remain_goal
        remain_goal = set()
        remain_goal.add((x,y))
    path = []
    start = copy.deepcopy(curr_problem.start) # get starting position
    while remain_goal:
        pQueue = PriorityQueue()
        pQueue.enqueue(start,0)
        parent = dict()
        expanded = []
        break_loop = False
        while not pQueue.is_empty() and not break_loop:
            cost, curr_pos = pQueue.dequeue()
            expanded.append(curr_pos)
            if curr_pos in remain_goal:
                remain_goal.remove(curr_pos)
                path = path[:-1] + backtrace(parent, start, curr_pos)
                start = curr_pos
                break_loop = True
                break
            
            for move, v in problem.AL.get(curr_pos, []):
                if v not in expanded:
                    total_cost = cost + 1
                    pQueue.enqueue(v,total_cost)
                    parent[v] = (move, curr_pos)
    
    return path
#Best First search
def a_star(problem,fn_heuristic):
    curr_problem = copy.deepcopy(problem)
    remain_goal = copy.deepcopy(curr_problem.end)
    if isinstance(problem,SFSP):
        x,y = remain_goal
        remain_goal = set()
        remain_goal.add((x,y))
    path = []
    start = copy.deepcopy(curr_problem.start) # get starting position
    while remain_goal:
        pQueue = PriorityQueue()
        pQueue.enqueue(start,fn_heuristic(start,remain_goal))
        parent = dict()
        expanded = []
        cost = dict()
        cost[start] = 0 
        break_loop = False
        while not pQueue.is_empty() and not break_loop:
            heu, curr_pos = pQueue.dequeue()
            expanded.append(curr_pos)
            if curr_pos in remain_goal:
                remain_goal.remove(curr_pos)
                path = path[:-1] + backtrace(parent, start, curr_pos)
                start = curr_pos
                break_loop = True
                break
            
            for move, v in problem.AL.get(curr_pos, []):
                if v not in expanded:
                    parent[v] = (move,curr_pos)
                    h = fn_heuristic(v,remain_goal)
                    cost[v] = cost[curr_pos] + 1
                    total = cost[v] + h
                    pQueue.enqueue(v,total)
    
    return path
def gbfs(problem,fn_heuristic):
    curr_problem = copy.deepcopy(problem)
    remain_goal = copy.deepcopy(curr_problem.end)
    if isinstance(problem,SFSP):
        x,y = remain_goal
        remain_goal = set()
        remain_goal.add((x,y))
    path = []
    start = copy.deepcopy(curr_problem.start) # get starting position
    while remain_goal:
        pQueue = PriorityQueue()
        pQueue.enqueue(start,fn_heuristic(start,remain_goal))
        parent = dict()
        expanded = []
        break_loop = False
        while not pQueue.is_empty() and not break_loop:
            heu, curr_pos = pQueue.dequeue()
            expanded.append(curr_pos)
            if curr_pos in remain_goal:
                remain_goal.remove(curr_pos)
                path = path[:-1] + backtrace(parent, start, curr_pos)
                start = curr_pos
                break_loop = True
                break
            
            for move, v in problem.AL.get(curr_pos, []):
                if v not in expanded:
                    parent[v] = (move,curr_pos)
                    h = fn_heuristic(v,remain_goal)
                    pQueue.enqueue(v,h)
    
    return path
# thu = MFSP('pacman_multi04.txt')
# path = a_star(thu,thu.get_heu_multi)
# thu.print_move(path)
thu = MFSP('Task1-2\maze\pacman_multi02.txt')
path = bfs(thu)
thu.animate(path)