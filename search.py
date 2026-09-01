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



# ------------------------------------------------------------------ search
def bfs(start, goal):
    """Breadth-first search. Goal-test children as they are GENERATED.
    return: (path, cost, expanded)
    path - inclusive list
    cost - total cost of path (integer)
    expanded - number of types expanded (not incremented when find goal bc stop when in expanded/frontier)
    """
    if start not in GRAPH or goal not in GRAPH:
        return (None, None,0)
    elif start == goal:
        ([start], 0,0)
    else:
        #initialization
        path = [start]
        cost = 0
        expanded = 1
        meet_goal = False
        #TODO Not sure about visisted structre city: (how many actions to get there, cost) (parent ? mentioned in Readme don't understand that part)
        visited = dict({start:(0,0)}) # city: (how many actions to get there, cost)
        frontier = deque([])
        #for expanding the first value

        for city, city_cost in sorted(GRAPH[start].items(),reverse =True):
            if city == goal:
                path.append(city)
                cost += city_cost
                return (path, cost,expanded)
            else:
                frontier.append((city, city_cost))
        while (frontier and not meet_goal):
            #Pop top of stack (alphebetically lowest value of recent adding to frontier from a city neighbors)
            # Expanding
            current, c_cost = frontier.pop()
            if current in visited: continue
            expanded += 1
            cost += c_cost 
            visited[current] = (expanded, c_cost)
            path.append(current)
            #Exploring new frontier values 
            for city, city_cost in sorted(GRAPH[current].items(), reverse=True):
                if city == goal:
                    path.append(city)
                    cost += city_cost
                    return (path, cost,expanded)
                else:
                    frontier.append((city, city_cost))

                

        

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
