### for city, city_cost in sorted(GRAPH[start].items()):
to get key and value from dictionary inside of dictionary based on alphebetical value
GRAPH  values is a dictionary of city: cost

- print(sorted(GRAPH[start])) - will get the key of second dictionary in alphabetical order


        frontier = []
        for city, city_cost in GRAPH[start].items():
            heapq.heappush(frontier, (city_cost, city, start)) # (cost from start, city, parent)
headq.heappush(___, () )   the first arg has to be a list, can't be a frontier = deque([])