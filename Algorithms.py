from Search import Search
from Node import Node
from queue import PriorityQueue

class BFS(Search):
    def __init__(self, initial):
        super().__init__(initial, 'B')

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = [node]

    def add_to_frontier(self, node, _):
        if node.state in self.frontier or node.state in self.explored:
            return
        self.frontier.append(node)

    def empty_frontier(self):
        return len(self.frontier) == 0
    
    def next_node(self):
        return self.frontier.pop(0)
    
class IDS(Search):
    def __init__(self, initial):
        super().__init__(initial, 'I')

    def init_frontier(self):
        node = Node(self.initial, None, 0, 0)
        self.frontier = [node]

    def add_to_frontier(self, node, _):
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
        super().__init__(initial, 'U')

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((0, 0, node))

    def add_to_frontier(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((node.cost, iterator, node))

    def empty_frontier(self):
        return self.frontier.empty()
    
    def next_node(self):
        _, _, node = self.frontier.get()
        return node

class GREEDY(Search):
    def __init__(self, initial):
        super().__init__(initial, 'U')

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((self.hamming_distance(node), 0, node))

    def add_to_frontier(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((self.hamming_distance(node), iterator, node))

    def empty_frontier(self):
        return self.frontier.empty()
    
    def next_node(self):
        _, _, node = self.frontier.get()
        return node

class A_STAR(Search):
    def __init__(self, initial):
        super().__init__(initial, 'U')

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((self.hamming_distance(node), 0, node))

    def add_to_frontier(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((node.cost + self.hamming_distance(node), iterator, node))

    def empty_frontier(self):
        return self.frontier.empty()
    
    def next_node(self):
        _, _, node = self.frontier.get()
        return node