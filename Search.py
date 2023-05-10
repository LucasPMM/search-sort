from Node import Node

class Search():

    def __init__(self, initial):
        self.initial = initial
        self.goal = sorted(initial)
        self.explored = []
        self.frontier = None
        self.expansions = 0
        self.stored_expansions = 0

    def add_to_frontier(self, node):
        # Each search will define their rules
        pass

    def empty_frontier(self):
        return False

    def expand(self, node):
        n = len(self.initial)
        current = node.state
        elements = []
        for i in range(n):
            for j in range(i+1, n):
                new_cost = 2 if abs(i-j) == 1 else 4
                new_array = current.copy()
                new_array[i], new_array[j] = new_array[j], new_array[i]

                new_cost += node.cost
                branch_reducer_conditional = new_array[i] < new_array[j]
                if branch_reducer_conditional:
                    new_node = Node(new_array, node, new_cost, self.expansions+1)
                    elements.append(new_node)
        for el in elements:
            self.add_to_frontier(el)
        self.expansions += 1

    def hamming_distance(self, node):
        """
        Number of elements on the wrong position
        """
        return sum(1 for i in range(len(node)) if node[i] != self.goal[i])

    def init_frontier(self):
        pass

    def next_node(self):
        pass

    def reset(self):
        self.stored_expansions += self.expansions
        self.expansions = 0
        self.explored = []
        self.frontier = None

    def set_explored(self, node):
        self.explored.append(node.state)

    def start(self):
        self.init_frontier()

        while not self.empty_frontier():
            print('FRONTIER', self.frontier)
            node = self.next_node()
            print('CURRENT', node)
            if node.state == self.goal:
                return node.cost, self.expansions, node.solution_path()
            
            self.set_explored(node)
            self.expand(node)