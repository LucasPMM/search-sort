from Node import Node

class Search():

    def __init__(self, initial, algorithm):
        self.initial = initial
        self.goal = sorted(initial)
        self.algorithm = algorithm
        
        self.explored = []
        self.frontier = None
        self.frontier_control = set()
        self.frontier_control.add(tuple(initial))
        self.expansions = 0
        self.stored_expansions = 0

    def frontier_push(self, node, iterator=None):
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
        for idx, el in enumerate(elements):
            self.frontier_push(el, idx+1+self.expansions)
        self.expansions += 1

    def hamming_distance(self, node):
        """
        Number of elements on the wrong position
        """
        return sum(1 for i in range(len(node.state)) if node.state[i] != self.goal[i])

    def start_frontier(self):
        pass

    def next_node(self):
        pass

    def reset(self):
        self.stored_expansions += self.expansions
        self.expansions = 0
        self.explored = []
        self.frontier = None
        self.frontier_control = set()

    def set_explored(self, node):
        self.explored.append(node.state)

    def start(self):
        self.start_frontier()

        while not self.empty_frontier():
            node = self.next_node()
            if node.state == self.goal:
                if self.algorithm in ['U', 'G', 'A']:
                    self.expansions += 1
                return node.cost, self.expansions, node.solution_path()
            
            if self.algorithm in ['U', 'A'] and node.state in self.explored:
                # If node was already explored (with better cost) on those algorithms, skip
                # If the heuristic is admissible the best path to the node has already been found when it is explored (A*)
                # If the best cost node was already explored, there is no need to explore it again (UCS)
                continue

            self.set_explored(node)
            self.expand(node)