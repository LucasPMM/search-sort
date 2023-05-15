import sys
import timeit
from Algorithms import * 

if __name__ == '__main__':
    algorithm = sys.argv[1]
    size = int(sys.argv[2])
    print_enabled = sys.argv[-1] == 'PRINT'

    initial = None
    if size > 0:
        initial = list(map(int, sys.argv[3:3+size]))

    start = timeit.default_timer()

    if algorithm == 'B':
        print('BFS')
        search = BFS(initial)
    elif algorithm == 'I':
        print('IDS')
        search = IDS(initial)
    elif algorithm == 'U':
        print('UCS')
        search = UCS(initial)
    elif algorithm == 'Uh':
        print('UCS_heap')
        search = UCS_heap(initial)
    elif algorithm == 'A':
        print('A*')
        search = A_STAR(initial)
    elif algorithm == 'Ah':
        print('A_heap*')
        search = A_STAR_heap(initial)
    elif algorithm == 'G':
        print('GREEDY')
        search = GREEDY(initial)
    elif algorithm == 'Gh':
        print('GREEDY')
        search = GREEDY_heap(initial)

    cost, expansions, path = search.start()
    end = timeit.default_timer()

    # Print results:
    print(cost, expansions)
    if print_enabled:
        for state in path:
            print(*state)
    
    # Only for tests purposes
    print('Duration: %f' % (end - start))

