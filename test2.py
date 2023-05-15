import os

types = ['B','I','U','A','G', 'Uh', 'Gh', 'Ah']

arrays = [[1,7,8,4,5,2,9,3,6,10],
[1,3,2,5,4,8,6,7,10,9,11],
[1,3,2,5,4,8,6,12,7,10,9,11],
[1,3,2,5,4,13,8,6,12,7,10,9,11],
[1,3,2,5,4,7,8,6,14,12,13,10,9,11],
[1,3,2,5,4,7,8,15,6,9,12,13,10,14,11],
[1,3,2,5,4,7,8,15,6,9,12,13,10,14,11,16],
[1,3,2,5,4,7,8,10,6,9,12,13,15,17,14,11,16],
[1,3,2,5,4,7,6,10,8,9,12,13,15,18,17,14,11,16],
[1,3,2,5,4,7,6,10,8,9,12,13,15,11,17,14,19,18,16],
[1,3,2,5,4,7,6,10,8,9,12,13,15,11,17,16,14,20,19,18]]

for idx, arr in enumerate(arrays):
    i = idx + 10
    arr_str = ' '.join(map(str, arr))
    for type in types:
        is_heap = 'h' in type
        type = type.replace('h', '')
        type_str = type + '-heap' if is_heap else type
        print('Test:', i, type, arr_str)
        os.system(f"python3 TP1.py {type} {i} {arr_str} PRINT >> ./tests2/t-{type_str}.txt")
