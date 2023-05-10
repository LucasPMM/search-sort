from Search import Search
from Node import Node

class BFS(Search):
    def __init__(self, initial):
        super().__init__(initial)

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = [node]

    def add_to_frontier(self, node):
        if node.state in self.frontier or node.state in self.explored:
            return
        self.frontier.append(node)

    def empty_frontier(self):
        return len(self.frontier) == 0
    
    def next_node(self):
        return self.frontier.pop(0)
    
class IDS(Search):
    def __init__(self, initial):
        super().__init__(initial)

    def init_frontier(self):
        node = Node(self.initial, None, 0, 0)
        self.frontier = [node]

    def add_to_frontier(self, node):
        if node.state in self.frontier or node.state in self.explored:
            return
        self.frontier.append(node)

    def empty_frontier(self):
        return len(self.frontier) == 0
    
    def start(self):
        depth_limit = 0
        while True:
            self.reset()
            self.init_frontier()
            while not self.empty_frontier():
                node = self.next_node()
                if node.depth > depth_limit:
                    continue

                if node.state == self.goal:
                    return node.cost, self.stored_expansions + self.expansions, node.solution_path()
                
                self.set_explored(node)
                self.expand(node)

            depth_limit += 1
    
    def next_node(self):
        return self.frontier.pop()

class UCS(Search):
    def __init__(self, initial):
        super().__init__(initial)

    # def init_frontier(self):
    #     node = Node(self.initial, None, 0)
    #     self.frontier = [(0, node)]

    # def add_to_frontier(self, node):
    #     if node.state in self.frontier or node.state in self.explored:
    #         return
    #     cost = self.hamming_distance(node.state)
    #     heappush(self.frontier, (cost, node))

    # def empty_frontier(self):
    #     return len(self.frontier) == 0
    
    # def next_node(self):
    #     return heappop(self.frontier)[1]

class GREEDY(Search):
    def __init__(self, initial):
        super().__init__(initial)

    # def init_frontier(self):
    #     node = Node(self.initial, None, 0)
    #     self.frontier = [(0, node)]

    # def add_to_frontier(self, node):
    #     if node.state in self.frontier or node.state in self.explored:
    #         return
    #     cost = self.hamming_distance(node.state)
    #     heappush(self.frontier, (cost, node))

    # def empty_frontier(self):
    #     return len(self.frontier) == 0
    
    # def next_node(self):
    #     return heappop(self.frontier)[1]

class A_STAR(Search):
    def __init__(self, initial):
        super().__init__(initial)

    # def init_frontier(self):
    #     node = Node(self.initial, None, 0)
    #     self.frontier = [(0, node)]

    # def add_to_frontier(self, node):
    #     if node.state in self.frontier or node.state in self.explored:
    #         return
    #     cost = self.hamming_distance(node.state)
    #     heappush(self.frontier, (cost, node))

    # def empty_frontier(self):
    #     return len(self.frontier) == 0
    
    # def next_node(self):
    #     return heappop(self.frontier)[1]