import os
import random

types = ['B','I','U','A','G']

for i in range(10):
    for type in types:
        for j in range(10):
            arr = list(reversed(range(1, i+2)))
            arr = random.sample(arr, len(arr))
            arr_str = ' '.join(map(str, arr))
            os.system(f"python3 TP1.py {type} {i+1} {arr_str} PRINT >> ./tests2/t{i+1}-{type}.txt")
