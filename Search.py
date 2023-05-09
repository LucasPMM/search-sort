from Node import Node

class Search():

    def __init__(self, initial):
        self.initial = initial
        self.goal = sorted(initial)
        self.explored = []
        self.frontier = None
        self.expanded = 0

    def init_frontier(self):
        pass

    def add_to_frontier(self, node):
        # Cada algoritmo terá suas regras de inserção na fronteira
        pass

    def empty_frontier(self):
        return False

    def next_node(self):
        pass

    def hamming_distance(self, node):
        """
        Calcula a heurística que consiste na quantidade de elementos fora de sua posição ordenada.
        """
        return sum(1 for i in range(len(node)) if node[i] != self.goal[i])

    def set_explored(self, node):
        self.explored.append(node.state)

    def solution(self, node):
        if node == None:
            return
        
        node.soluction_path()

    def expand(self, node):
        self.expanded += 1
        n = len(self.initial)
        print('vou expandir o node', node.state)
        current = node.state
        for i in range(n):
            for j in range(i+1, n):
                new_cost = 2 if abs(i-j) == 1 else 4
                new_array = current.copy()
                new_array[i], new_array[j] = new_array[j], new_array[i]

                new_cost += node.cost
                print('vou comparar', new_array[i], new_array[j])
                branch_reducer_conditional = new_array[i] < new_array[j]
                print('comparei')
                if branch_reducer_conditional:
                    new_node = Node(new_array, node, new_cost)
                    self.add_to_frontier(new_node)

    def start(self):
        self.init_frontier()

        while not self.empty_frontier():
            node = self.next_node()

            if node.state == self.goal:
                node.soluction_path()
                return
            
            self.set_explored(node)
            self.expand(node)