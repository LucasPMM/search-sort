class Node():
    
    def __eq__(self, node):
        return self.state == node

    def __init__(self, state, parent, cost, depth=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = 0
        self.depth = depth

    def __lt__(self, node): 
        return self.cost < node.cost

    def set_heuristic_cost(self, cost):
        self.heuristic_cost = cost

    def solution_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return reversed(path)
