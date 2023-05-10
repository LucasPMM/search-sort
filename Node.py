class Node():
    
    def __init__(self, state, parent, cost, depth=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = None
        self.depth = depth

    # Rewrite some functions to print data rightely
    def __eq__(self, node):
        return self.state == node
    def __lt__(self, node): 
        return self.cost < node.cost
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str('<' + str(self.state) + ', ' + str(self.cost) + '>')

    def set_heuristic_cost(self, cost):
        self.heuristic_cost = cost

    def solution_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return reversed(path)
