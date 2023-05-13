import os
import random

types = ['B','I','U','A','G']

for i in range(11, 20):
    arr = list(reversed(range(1, i+2)))
    arr = random.sample(arr, len(arr))
    for type in types:
        arr_str = ' '.join(map(str, arr))
        print('Test:', i+1, type, arr_str)
        os.system(f"python3 TP1.py {type} {i+1} {arr_str} PRINT >> ./tests2/t-{type}.txt")
