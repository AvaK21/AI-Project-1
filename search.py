"""
Ava Kirkland
Uninformed and informed search on the course map.

MY HEURISTIC CHOICE: ___Euclidean distance___
Justification (2-3 sentences): is it admissible on this map? is it consistent?
why?

Yes Euclidean distance is admissible on this map and it is consistent. 
Euclidean distance provides the displacement between two locations so the algorithm can not overestimate the distance.
Also the roman_map is set up synthesically in euclidean distance in mind. The distance is just a number, no differiation of top/down and left/right moves. 

Implement the functions below. Do not rename them or change their signatures.
Do not modify romania_map.py.

Each search returns a 3-tuple:

    (path, cost, expanded)

    path      list of city names from start to goal, inclusive.
              None if no path exists.
    cost      total cost of that path, an integer. None if no path exists.
    expanded  number of nodes your search expanded. See the handout for the
              exact counting rule -- this is graded.

If no path exists, a search returns (None, None, 0).

Run the public tests with:   python run_tests.py
"""
# TODO help on visited structure of breadth first search
# TODO implement deep first is needed for U and A*?
# TODO BIGGEST: for first breadth first search got expanded 3, expected 5 I don't understand what correct answer is 5
import heapq
from collections import deque

import numpy as np

from romania_map import GRAPH, COORDS


# --------------------------------------------------------------- distances
def coords_of(city):
    """Return a city's (x, y) from COORDS as a length-2 numpy array of floats."""
    return np.array(COORDS.get(city), dtype=float)


       


def euclidean(a, b):
    """Euclidean (L2) distance between two length-2 numpy arrays.

    Write the formula yourself with numpy operations. Do not call
    numpy.linalg.norm, math.dist, or scipy.
    """
    pa = np.array(a)
    pb = np.array(b)

    pdiff = pb - pa
    ppow = pdiff ** 2
    psqrt = np.sqrt(sum(ppow))
    return psqrt



def manhattan(a, b):
    """Manhattan (L1) distance between two length-2 numpy arrays."""
    pa = np.array(a)
    pb = np.array(b)

    pdiff = pb-pa
    pabs = np.abs(pdiff)

    return np.sum(pabs)


def chebyshev(a, b):
    """Chebyshev (L-infinity) distance between two length-2 numpy arrays."""
    pa = np.array(a)
    pb = np.array(b)

    pdiff = pb - pa
    pabs = np.abs(pdiff)
    pmax = np.max(pabs)
    return pmax


def heuristic(city, goal):
    """Estimated distance from `city` to `goal`, as a float.

    Call coords_of() for each city, then return the result of ONE of
    euclidean / manhattan / chebyshev.

    YOU CHOOSE which one. Read the handout first -- one of the three can
    overestimate the true remaining cost on this map, which breaks A*'s
    optimality guarantee.

    Must return 0.0 when city == goal.
    Your astar() must CALL this function -- do not inline the formula.
    """

    # TODO will need to look up bu think chebyshev will overestimate, idk about manhatten
    # I know ecludian won't estimate because it returns displacement 
    if city == goal:
        return 0.0
    else:
        return euclidean( coords_of(city), coords_of(goal))

#-----------------------------Helper functions
def bfsGoalPathAndCost(cities:dict,goal)-> tuple:
    """After the goal city has been found in Breadth-first search, pass visited dictionary to 
    determine path from goal to start
    # Args:
    # cities (visited) structure: dict({city:(parent:cost)})
    # goal: goal city that was just seen when expanded last entry of visited dictionary
    # 
    # Returns:
    # ([path], cost) - Path from start to goal, and cost of that path"""
    #TODO
    path = [goal]
    found_start = False
    total_cost = 0
    parent = None
    current_position = goal
    while not found_start:
        (parent, cost) = cities.get(current_position)
        if parent is None:
            # values are placed in reverse order 

            # reverse order to be correct with start index 0
            path = path[::-1]
            total_cost += cost
            found_start = True
            return(path,total_cost)
        else:
            #get city to front of the path, to be in correct order
            path.append(parent)
            total_cost += cost
            current_position = parent


    # get the last dictionary entry

    last_city, (last_parent,city_cost)  = cities.popitem()



# ------------------------------------------------------------------ search
def bfs(start, goal):
    """Breadth-first search. Goal-test children as they are GENERATED.
    return: (path, cost, expanded)
    path - inclusive list
    cost - total cost of path (integer)
    expanded - number of types expanded (not incremented when find goal bc stop when in expanded/frontier)

    For edge cases, if start or goal not in GRAPH, or start == goal or (else) if there is no path
    Normal case
    visit start node and add all neighbors to frontier, (city, parent, cost) tuple alpebetically sorted, 
    - pop node 
    - check if goal, else add neighbors to frontier (if not already visited) 
    once goal is found, use visited dictionary to backtrack from goal to start to get path and cost 
    return path, cost, expanded

    While the goal is added to visited dictionary, it is not expqnded
    Expanded is when you pop the city and add its neighbors to the frontier

    breadth-first search is graph search or going from a node, layer by layer til get to goal.

    """
    if start not in GRAPH or goal not in GRAPH:
        return (None, None,0)
    elif start == goal:
        ([start], 0,0)
    else:
        #initialization
        path = []
        cost = 0
        expanded = 1
        meet_goal = False
        visited = dict({start:(None,0)}) # city: (parent,cost)
        #once get to goal, go back through dictionary to get path based on parent and cost 

        frontier = deque([])
        #for expanding the first value

        for city, city_cost in sorted(GRAPH[start].items()):
            if city == goal:
                path.append(start)
                path.append(city)
                cost += city_cost
                return (path, cost,expanded)
            else:
                frontier.append((city, start, city_cost))
        while (frontier and not meet_goal):
            #Pop top of stack (alphebetically lowest value of recent adding to frontier from a city neighbors)
            # Expanding
            current, parent, c_cost = frontier.popleft()
            if current in visited: continue
            expanded += 1
            
            visited[current] = (parent, c_cost)
            
            #Exploring new frontier values 
            for city, city_cost in sorted(GRAPH[current].items()):
                if city == goal:
                    visited[city] = (current, city_cost)
                    # TODO goal finder
                    (finished_path, total_cost) = bfsGoalPathAndCost(visited,city)
                    path = finished_path
                    cost = total_cost
                    meet_goal = True
                    return (path, cost,expanded)
                elif city not in visited:
                    frontier.append((city, current, city_cost))

                    # changed frontier city, parent and cost, 
                    # path and cost is still incorrect, should be determined at the end once goal is found
                    #  did - on the else above change to elif city not in visited

                

        

    #if there is no connection from start to goal
    return (None, None, 0)
    raise NotImplementedError


def dfs(start, goal):
    """Depth-first graph search. Never expand a city twice.

    Push successors in reverse alphabetical order so the alphabetically
    first neighbour is popped first.
    """
    if start not in GRAPH or goal not in GRAPH:
        return (None, None,0)
    elif start == goal:
        ([start], 0,0)

    #if there is no connection from start to goal
    return (None, None, 0)
    raise NotImplementedError


def ucs(start, goal):
    """Uniform-cost search. Goal-test nodes as they are EXPANDED."""
    if start not in GRAPH or goal not in GRAPH:
        return (None, None,0)
    elif start == goal:
        ([start], 0,0)


    return (None, None, 0)
    raise NotImplementedError


def astar(start, goal):
    """A* search using heuristic(city, goal)."""
    if start not in GRAPH or goal not in GRAPH:
        return (None, None,0)
    elif start == goal:
        ([start], 0,0)

    #if there is no connection from start to goal
    return (None, None, 0)
    raise NotImplementedError
