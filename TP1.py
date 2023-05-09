import sys
import timeit
from Algorithms import * 

# class SearchSort:

#     def _expand_child(self, current, visited, frontier, costs, type):
#         n = len(self.array)
#         elements = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 new_cost = 2 if abs(i-j) == 1 else 4
#                 new_array = current.copy()
#                 new_array[i], new_array[j] = new_array[j], new_array[i]

#                 new_cost += costs[tuple(current)]

#                 skip_visited_conditional = (tuple(new_array) not in visited)
#                 branch_reducer_conditional = new_array[i] < new_array[j]
#                 conditional = branch_reducer_conditional
                
#                 if type == 'bfs' or type == 'ids':
#                     conditional = conditional and skip_visited_conditional
#                 if type == 'ucs':
#                     on_frontier = tuple(new_array) in frontier
#                     better_cost_conditional = (tuple(new_array) not in costs or new_cost < costs[tuple(new_array)])
#                     # Add element if is not visited or is on the frontier with higher cost
#                     conditional = conditional and (skip_visited_conditional or (better_cost_conditional and on_frontier))

#                 if conditional:
#                     costs[tuple(new_array)] = new_cost
#                     visited[tuple(new_array)] = tuple(current)
#                     elements.append(new_array)
#         return elements
    
#     def ids(self):
#         depth_limit = 0
#         expansions = 0

#         while True:
#             stack = [(self.array, 0)]
#             visited = {tuple(self.array): None}
#             costs = {tuple(self.array): 0}
#             while len(stack) != 0:
#                 current, depth = stack.pop()

#                 if depth > depth_limit:
#                     continue

#                 if self.goal == current:
#                     path = self._soluction_path(current, visited)
#                     return costs[tuple(self.goal)], expansions, path
#                 # No early goal test (?)
#                 expansions += 1
#                 elements = self._expand_child(current, visited, stack, costs, 'ids')
#                 for el in elements:
#                     stack.append((el,depth+1))

#             depth_limit += 1

#     def ucs(self):
#         queue = PriorityQueue()
#         frontier = PriorityQueue()
#         queue.put((0, 0, self.array))
#         frontier.put((self.array))
#         visited = {tuple(self.array): None}
#         costs = {tuple(self.array): 0}
#         expansions = 0

#         while not queue.empty():
#             _, _, current = queue.get()
#             expansions += 1
#             if self.goal == current:
#                 path = self._soluction_path(current, visited)
#                 return costs[tuple(self.goal)], expansions, path
#             elements = self._expand_child(current, visited, frontier.queue, costs, 'ucs')
#             for idx, el in enumerate(elements):
#                 queue.put((costs[tuple(el)], idx+1+expansions, el))
#                 frontier.put((el))

#     def greedy(self):
#         queue = PriorityQueue()
#         queue.put((self._hamming_distance(self.array), 0, self.array))
#         visited = {tuple(self.array): None}
#         costs = {tuple(self.array): 0}
#         expansions = 0

#         while not queue.empty():
#             _, _, current = queue.get()
#             expansions += 1
#             if self.goal == current:
#                 path = self._soluction_path(current, visited)
#                 return costs[tuple(self.goal)], expansions, path
#             elements = self._expand_child(current, visited, queue.queue, costs, 'greedy')
#             for idx, el in enumerate(elements):
#                 queue.put((self._hamming_distance(el), idx+1+expansions, el))

#     def a_star(self):
#         queue = PriorityQueue()
#         queue.put((self._hamming_distance(self.array), 0, self.array))
#         visited = {tuple(self.array): None}
#         costs = {tuple(self.array): 0}
#         expansions = 0

#         while not queue.empty():
#             _, _, current = queue.get()
#             expansions += 1
#             if self.goal == current:
#                 path = self._soluction_path(current, visited)
#                 return costs[tuple(self.goal)], expansions, path
#             elements = self._expand_child(current, visited, queue.queue, costs, 'astar')
#             for idx, el in enumerate(elements):
#                 queue.put((costs[tuple(el)] + self._hamming_distance(el), idx+1+expansions, el))


if __name__ == '__main__':
    algorithm = sys.argv[1]
    size = int(sys.argv[2])
    print_enabled = sys.argv[-1] == 'PRINT'

    initial = None
    if size > 0:
        initial = list(map(int, sys.argv[3:3+size]))

    start = timeit.default_timer()

    if algorithm == 'B':
        print('BFS')
        search = BFS(initial)
    elif algorithm == 'I':
        print('IDS')
        search = IDS(initial)
    elif algorithm == 'U':
        print('UCS')
        search = UCS(initial)
    elif algorithm == 'A':
        print('A*')
        search = A_STAR(initial)
    elif algorithm == 'G':
        print('GREEDY')
        search = GREEDY(initial)

    cost, expansions, path = search.start()
    end = timeit.default_timer()

    # Print results:
    print(cost, expansions)
    if print_enabled:
        for state in path:
            print(*state)
    
    # Only for tests purposes
    print('Duration: %f' % (end - start))

