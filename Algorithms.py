from Search import Search
from Node import Node
from queue import PriorityQueue
from heapq import *

class BFS(Search):
    def __init__(self, initial):
        super().__init__(initial, 'B')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = [node]

    def frontier_push(self, node, _):
        if node.state in self.frontier or node.state in self.explored:
            return
        self.frontier.append(node)
        
class IDS(Search):
    def __init__(self, initial):
        super().__init__(initial, 'I')

    def start_frontier(self):
        node = Node(self.initial, None, 0, 0)
        self.frontier = [node]

    def frontier_push(self, node, _):
        if node.state in self.frontier:
            return
        self.frontier.append(node)
    
    def start(self):
        depth_limit = 0
        while True:
            self.reset()
            self.start_frontier()
            while not self.empty_frontier():
                node = self.next_node()
                if node.depth > depth_limit:
                    continue

                if node.state == self.goal:
                    return node.cost, self.stored_expansions + self.expansions, node.solution_path()
                
                self.set_explored(node)
                self.expand(node)

            depth_limit += 1
    
# Using queue

class UCS(Search):
    def __init__(self, initial):
        super().__init__(initial, 'U')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((0, 0, node))

    def frontier_push(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((node.cost, iterator, node))

class GREEDY(Search):
    def __init__(self, initial):
        super().__init__(initial, 'G')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((self.hamming_distance(node), 0, node))

    def frontier_push(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((self.hamming_distance(node), iterator, node))

class A_STAR(Search):
    def __init__(self, initial):
        super().__init__(initial, 'A')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = PriorityQueue()
        self.frontier.put((self.hamming_distance(node), 0, node))

    def frontier_push(self, node, iterator):
        if node.state in self.explored:
            return
        self.frontier.put((node.cost + self.hamming_distance(node), iterator, node))
    
# Using heapq:

class UCS_heap(Search):
    def __init__(self, initial):
        super().__init__(initial, 'U')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        self.frontier = [(node.cost, node)]

    def frontier_push(self, node, _):
        if node.state in self.explored:
            return

        if tuple(node.state) in self.frontier_control:
            # Check costs
            index = list(map(lambda x: x[1], self.frontier)).index(node)
            cost = self.frontier[index][1].cost
            better_cost = node.cost < cost
            if not better_cost:
                return
            self.frontier.pop(index)

        heappush(self.frontier, (node.cost, node))
        self.frontier_control.add(tuple(node.state))


class GREEDY_heap(Search):
    def __init__(self, initial):
        super().__init__(initial, 'G')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        heuristic_cost = self.hamming_distance(node)
        node.set_heuristic_cost(heuristic_cost)
        self.frontier = [(heuristic_cost, node)]

    def frontier_push(self, node, _):
        if node.state in self.explored:
            return

        cost = self.hamming_distance(node)
        if tuple(node.state) in self.frontier_control:
            # Check costs
            index = list(map(lambda x: x[1], self.frontier)).index(node)
            old_cost = self.frontier[index][1].heuristic_cost
            better_cost = cost < old_cost
            if not better_cost:
                return
            self.frontier.pop(index)

        node.set_heuristic_cost(cost)
        heappush(self.frontier, (cost, node))
        self.frontier_control.add(tuple(node.state))

class A_STAR_heap(Search):
    def __init__(self, initial):
        super().__init__(initial, 'A')

    def start_frontier(self):
        node = Node(self.initial, None, 0)
        heuristic_cost = self.hamming_distance(node)
        node.set_heuristic_cost(heuristic_cost)
        self.frontier = [(heuristic_cost + node.cost, node)]

    def frontier_push(self, node, _):
        if node.state in self.explored:
            return
        
        heuristic_cost = self.hamming_distance(node)
        if tuple(node.state) in self.frontier_control:
            # Check costs
            index = list(map(lambda x: x[1], self.frontier)).index(node)
            old_node = self.frontier[index][1]
            better_cost = node.cost + heuristic_cost < old_node.cost + old_node.heuristic_cost
            if not better_cost:
                return
            self.frontier.pop(index)

        node.set_heuristic_cost(heuristic_cost)
        heappush(self.frontier, (node.cost + heuristic_cost, node))
        self.frontier_control.add(tuple(node.state))
