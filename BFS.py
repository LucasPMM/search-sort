from Search import Search
from Node import Node
from heapq import *

class BFS(Search):
    def __init__(self, initial):
        super().__init__(initial)

    def init_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = [(0, node)]

    def add_to_frontier(self, node):
        if node.state in self.frontier or node.state in self.explored:
            return
        
        cost = self.hamming_distance(node.state)
        heappush(self.frontier, (cost, node))

    def empty_frontier(self):
        return len(self.frontier) == 0
    
    def next_node(self):
        return heappop(self.frontier)[1]