class Node():
    
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

    def soluction_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return path
