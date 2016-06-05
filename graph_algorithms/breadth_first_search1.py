from implementation import draw_grid
import sys
import heapq
import random
import time

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def neighbors(self,id):
        return self.edges[id]

class Queue:
    def __init__(self):
        self.internal = []
    def is_empty(self):
        return self.internal == []
    def push(self,data):
        self.internal.insert(0,data)
    def pop(self):
        return self.internal.pop()

class SquareGrid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self,id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.weights = {}

    def cost(self,from_node, to_node):
        return self.weights.get(to_node,1)

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self,item,priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def get_min_distance_index(F,distances):
    minimum = sys.float_info.max
    cur_index = 0
    for ind,elem in enumerate(F):
        if distances[elem] < minimum:
            minimum = distances[elem]
            cur_index = ind
    return cur_index
    
def dijkstra(graph,start,goal):
    distances = {}.fromkeys(graph.keys(),sys.float_info.max)
    distances[start] = 0
    #F is set of nodes that are yet to get final distance estimates
    F = [vertex for vertex in distances.keys() if vertex != 0]
    D = [] #set of all nodes that have final distances
    while F != []:
        current = F[get_min_distance_index(F,distances)]
        
        if current == goal:
            break
        for node in graph.neighbors(current):
            distances[node] = min(distances[node],distances[current] + graph.cost(current,node))
        F.remove(current)
        D.append(current)
    return D,distances

def dijkstra2(graph,start,goal,total_grid):
    already_seen = PriorityQueue()
    already_seen.put(start,0)
    distances = {}.fromkeys(total_grid,float("inf"))
    distances[start] = 0
    came_from = {}
    cost_so_far = {}.fromkeys(total_grid,0)
    came_from[start] = None
    already_processed = []
    while not already_seen.empty():
        current = already_seen.get()
        already_processed.append(current)
        if current == goal:
            break

        min_distance = []
        for next in graph.neighbors(current):
            if next not in already_processed:
                distances[next] = min(distances[next],distances[current] + graph.cost(current,next))
                min_distance.append((next,distances[next]))
        if min_distance == []: continue
        min_distance = sorted(min_distance,key=lambda t:t[1])
        cost_so_far[current] += min_distance[0][1]
        already_seen.put(*min_distance[0])
        came_from[min_distance[0][0]] = current
            
    return came_from,cost_so_far
        
def dijkstra_search(graph,start,goal):
    already_seen = PriorityQueue()
    already_seen.put(start,0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not already_seen.empty():
        current = already_seen.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current,next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                already_seen.put(next,priority)
                came_from[next] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start,goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def bfs(start,goal,graph):
    q = Queue()
    came_from = {}
    came_from[start] = None
    q.push(start)
    while not q.is_empty():
        current = q.pop()
        if current == goal:
            break
        for node in graph.neighbors(current):
            if not node in came_from.keys():
                q.push(node)
                came_from[node] = current
    return came_from

grid = """
. . . . . . . . . . . . . . . . . . . . . ####. . . . . . . 
. . . . . . . . . . . . . . . . . . . . . ####. . . . . . . 
. . . . . . . . . . . . . . . . . . . . . ####. . . . . . . 
. . . ####. . . . . . . . . . . . . . . . ####. . . . . . . 
. . . ####. . . . . . . . ####. . . . . . ####. . . . . . . 
. . . ####. . . . . . . . ####. . . . . . ##########. . . . 
. . . ####. . . . . . . . ####. . . . . . ##########. . . . 
. . . ####. . . . . . . . ####. . . . . . . . . . . . . . . 
. . . ####. . . . . . . . ####. . . . . . . . . . . . . . . 
. . . ####. . . . . . . . ####. . . . . . . . . . . . . . . 
. . . ####. . . . . . . . ####. . . . . . . . . . . . . . . 
. . . ####. . . . . . . . ####. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . ####. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . ####. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . ####. . . . . . . . . . . . . . .
"""

def process_grid(grid):
    grid = [line.split(' ') for line in grid.split("\n")]
    grid = [[x for x in line if x != '']for line in grid]
    grid = [line for line in grid if line != []]

    walls = []
    x_offset = 0
    for y,line in enumerate(grid): 
        for x,elem in enumerate(line): 
            if "#" in elem:
                tmp = []
                for i in range(len(elem)):
                    if i % 2  == 0:
                        i //= 2
                        tmp.append((x_offset+i+x,y))
                walls += tmp[:-1]
                x_offset += len(elem)//2
        x_offset = 0
    return walls

def gen_grid(width,height):
    total_grid = []
    for y in range(height):
        for x in range(width):
            total_grid.append((x,y))
    return total_grid
    
def grid_excluding_walls(width,height,walls):
    total_grid = []
    for y in range(height):
        for x in range(width):
            total_grid.append((x,y))
    [total_grid.remove(wall) for wall in walls]
    return total_grid
    
g = GridWithWeights(30,15)
g.walls = process_grid(grid)
walls = {loc:50 for loc in g.walls}
other_weights = {loc:random.randint(2,17) for loc in grid_excluding_walls(30,15,g.walls)}
weights = other_weights
weights.update(walls)       
g.weights = weights

total_grid = gen_grid(30,15)
came_from, cost_so_far = dijkstra(g, (1, 4), (7, 8),total_grid)
if (7,8) in came_from:
    print("found")
print(" -> ".join([",".join([str(elem[0]),str(elem[1])]) for elem in came_from]))
#for key in cost_so_far:
#    print(str(key)+":"+str(cost_so_far[key]))
# draw_grid(g, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
# print()
# draw_grid(g, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
# print()
# draw_grid(g, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))

#parents = bfs((8,7),(17,2),g)
#draw_grid(g,width=2,point_to=parents,start=(8,7),goal=(17,2))
