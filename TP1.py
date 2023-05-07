import sys
from queue import Queue, PriorityQueue
import timeit

class SearchSort:
    def __init__(self):
        self.array = []
        self.goal = []
        self.algorithm = None
        self.print_enabled = False

    def _expand_child(self, current, visited, frontier, costs, type):
        n = len(self.array)
        elements = []
        for i in range(n):
            for j in range(i+1, n):
                new_cost = 2 if abs(i-j) == 1 else 4
                new_array = current.copy()
                new_array[i], new_array[j] = new_array[j], new_array[i]

                new_cost += costs[tuple(current)]

                skip_visited_conditional = (tuple(new_array) not in visited)
                branch_reducer_conditional = new_array[i] < new_array[j]
                conditional = branch_reducer_conditional
                
                if type == 'bfs' or type == 'ids':
                    conditional = conditional and skip_visited_conditional
                if type == 'ucs':
                    on_frontier = tuple(new_array) in frontier
                    better_cost_conditional = (tuple(new_array) not in costs or new_cost < costs[tuple(new_array)])
                    # Add element if is not visited or is on the frontier with higher cost
                    conditional = conditional and (skip_visited_conditional or (better_cost_conditional and on_frontier))

                if conditional:
                    costs[tuple(new_array)] = new_cost
                    visited[tuple(new_array)] = tuple(current)
                    elements.append(new_array)
        return elements
    
    def _hamming_distance(self, state):
        """
        Calcula a heurística que consiste na quantidade de elementos fora de sua posição ordenada.
        """
        return sum(1 for i in range(len(state)) if state[i] != self.goal[i])

    def _heuristic_sum_distances(self, state):
        """
        Calcula a heurística que consiste na soma das distâncias dos elementos do vetor v até a sua posição ordenada.
        """
        return sum([abs(i - self.goal.index(e)) for i, e in enumerate(state)])


    def _soluction_path(self, current, visited):
        # Constrói o caminho percorrido
        path = [current]
        while current != None and current != self.array:
            current = visited[tuple(current)]
            if current != None:
                path.append(current)
        return path[::-1]

    def bfs(self):
        queue = Queue()
        queue.put(self.array)
        visited = {tuple(self.array): None}
        costs = {tuple(self.array): 0}
        if self.goal == self.array:
            return 0, 0, [self.array]
        expansions = 0
        while not queue.empty():
            current = queue.get()
            expansions += 1
            if self.goal == current:
                path = self._soluction_path(current, visited)
                return costs[tuple(self.goal)], expansions, path
            elements = self._expand_child(current, visited, queue.queue, costs, 'bfs')
            for el in elements:
                queue.put(el)

    def ids(self):
        depth_limit = 0
        expansions = 0

        while True:
            stack = [(self.array, 0)]
            visited = {tuple(self.array): None}
            costs = {tuple(self.array): 0}
            while len(stack) != 0:
                current, depth = stack.pop()

                if depth > depth_limit:
                    continue

                if self.goal == current:
                    path = self._soluction_path(current, visited)
                    return costs[tuple(self.goal)], expansions, path
                # No early goal test (?)
                expansions += 1
                elements = self._expand_child(current, visited, stack, costs, 'ids')
                for el in elements:
                    stack.append((el,depth+1))

            depth_limit += 1

    def ucs(self):
        queue = PriorityQueue()
        frontier = PriorityQueue()
        queue.put((0, 0, self.array))
        frontier.put((self.array))
        visited = {tuple(self.array): None}
        costs = {tuple(self.array): 0}
        expansions = 0

        while not queue.empty():
            _, _, current = queue.get()
            expansions += 1
            if self.goal == current:
                path = self._soluction_path(current, visited)
                return costs[tuple(self.goal)], expansions, path
            elements = self._expand_child(current, visited, frontier.queue, costs, 'ucs')
            for idx, el in enumerate(elements):
                queue.put((costs[tuple(el)], idx+1+expansions, el))
                frontier.put((el))

    def greedy(self):
        queue = PriorityQueue()
        queue.put((self._heuristic_sum_distances(self.array), 0, self.array))
        visited = {tuple(self.array): None}
        costs = {tuple(self.array): 0}
        expansions = 0

        while not queue.empty():
            _, _, current = queue.get()
            expansions += 1
            if self.goal == current:
                path = self._soluction_path(current, visited)
                return costs[tuple(self.goal)], expansions, path
            elements = self._expand_child(current, visited, queue.queue, costs, 'greedy')
            for idx, el in enumerate(elements):
                queue.put((self._heuristic_sum_distances(el), idx+1+expansions, el))

    def a_star(self):
        queue = PriorityQueue()
        queue.put((self._heuristic_sum_distances(self.array), 0, self.array))
        visited = {tuple(self.array): None}
        costs = {tuple(self.array): 0}
        expansions = 0

        while not queue.empty():
            _, _, current = queue.get()
            expansions += 1
            if self.goal == current:
                path = self._soluction_path(current, visited)
                return costs[tuple(self.goal)], expansions, path
            elements = self._expand_child(current, visited, queue.queue, costs, 'astar')
            for idx, el in enumerate(elements):
                queue.put((costs[tuple(el)] + self._heuristic_sum_distances(el), idx+1+expansions, el))


    def result(self, costs, expansions, states):
        print(costs, expansions)
        if self.print_enabled:
            for state in states:
                print(*state)

if __name__ == '__main__':
    search = SearchSort()

    search.algorithm = sys.argv[1]
    size = int(sys.argv[2])
    search.print_enabled = sys.argv[-1] == 'PRINT'
    if size > 0:
        search.array = list(map(int, sys.argv[3:3+size]))
        search.goal = sorted(search.array)

    start = timeit.default_timer()

    if search.algorithm == 'B':
        print('BFS')
        search.result(*search.bfs())
    elif search.algorithm == 'I':
        print('IDS')
        search.result(*search.ids())
    elif search.algorithm == 'U':
        print('UCS')
        search.result(*search.ucs())
    elif search.algorithm == 'A':
        print('A*')
        search.result(*search.a_star())
    elif search.algorithm == 'G':
        print('GREEDY')
        search.result(*search.greedy())

    end = timeit.default_timer()
    print ('Duration: %f' % (end - start))

