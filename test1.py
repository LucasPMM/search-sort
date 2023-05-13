import os

types = ['B','I','U','A','G']

for type in reversed(types):
    for i in range(10):
        print('==> T', i+1)
        arr = list(reversed(range(1, i+2)))
        arr_str = ' '.join(map(str, arr))

        os.system(f"python3 TP1.py {type} {i+1} {arr_str} PRINT >> ./tests1/t-{type}.txt")
