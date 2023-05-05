import sys
from queue import Queue

class SearchSort:
    def __init__(self):
        self.array = []
        self.goal = []
        self.algorithm = None
        self.print_enabled = False

    def _expand_child(self, current, visited, costs):
        n = len(self.array)
        elements = []
        for i in range(n):
            for j in range(i+1, n):
                new_cost = 2 if abs(i-j) == 1 else 4
                new_array = current.copy()
                new_array[i], new_array[j] = new_array[j], new_array[i]
                if tuple(new_array) not in visited and new_array[i] < new_array[j]:
                    costs[tuple(new_array)] = costs[tuple(current)] + new_cost
                    visited[tuple(new_array)] = tuple(current)
                    elements.append(new_array)
        return elements

    def bfs(self):
        queue = Queue()
        queue.put(self.array)
        visited = set()
        visited = {tuple(self.array): None}
        costs = {tuple(self.array): 0}
        expansions = 0
        while not queue.empty():
            current = queue.get()
            expansions += 1
            if self.goal == current:
                # Constrói o caminho percorrido
                path = [current]
                while current != None and current != self.array:
                    current = visited[tuple(current)]
                    if current != None:
                        path.append(current)

                return costs[tuple(self.goal)], expansions, path[::-1]
            elements = self._expand_child(current, visited, costs)
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
                    # Constrói o caminho percorrido
                    path = [current]
                    while current != None and current != self.array:
                        current = visited[tuple(current)]
                        if current != None:
                            path.append(current)

                    return costs[tuple(self.goal)], expansions, path[::-1]
                # No early goal test (?)
                expansions += 1
                elements = self._expand_child(current, visited, costs)
                for el in elements:
                    stack.append((el,depth+1))

            depth_limit += 1

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

    if search.algorithm == 'B':
        print('BFS')
        search.result(*search.bfs())
    elif search.algorithm == 'I':
        print('IDS')
        search.result(*search.ids())
    elif search.algorithm == 'U':
        print('UCS')
    elif search.algorithm == 'A':
        print('A*')
    elif search.algorithm == 'G':
        print('GREEDY')