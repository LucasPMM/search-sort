import os

types = ['B','I','U','A','G', 'Uh', 'Gh', 'Ah']

for type in reversed(types):
    is_heap = 'h' in type
    type = type.replace('h', '')
    type_str = type + '-heap' if is_heap else type
    for i in range(9):
        print('==> T', i+1)
        arr = list(reversed(range(1, i+2)))
        arr_str = ' '.join(map(str, arr))
        os.system(f"python3 TP1.py {type} {i+1} {arr_str} PRINT >> ./tests1/t-{type_str}.txt")
