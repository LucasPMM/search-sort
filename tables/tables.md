### 1. Testando arrays em ordem decrescente:

Aplicação de todos algoritmos com arrays em ordem decrescente
Ex: [X1,...,Xn], X1 <= ... <= Xn

###### Python sort

|  N  | Tempo(s) |
| :-: | -------- |
|  1  | 0.000007 |
|  2  | 0.000008 |
|  3  | 0.000007 |
|  4  | 0.000007 |
|  5  | 0.000009 |
|  6  | 0.000008 |
|  7  | 0.000009 |
|  8  | 0.000008 |
|  9  | 0.000007 |

###### BFS

|  N  | Custo | Expansões | Tempo (s)   |
| :-: | :---: | :-------: | ----------- |
|  1  |   0   |     0     | 0.000009    |
|  2  |   2   |     1     | 0.000016    |
|  3  |   4   |     2     | 0.000025    |
|  4  |   6   |    15     | 0.000132    |
|  5  |   8   |    33     | 0.000837    |
|  6  |  10   |    273    | 0.041138    |
|  7  |  12   |    694    | 0.619046    |
|  8  |  14   |   7403    | 72.974005   |
|  9  |  16   |   20561   | 1270.301665 |

###### IDS

|  N  | Custo | Expansões | Tempo (s) |
| :-: | :---: | :-------: | --------- |
|  1  |   0   |     0     | 0.000010  |
|  2  |   2   |     2     | 0.000022  |
|  3  |   4   |     3     | 0.000034  |
|  4  |  14   |    40     | 0.000330  |
|  5  |  32   |    328    | 0.006057  |
|  6  |  50   |   1108    | 0.049908  |
|  7  |  72   |   3056    | 0.345815  |
|  8  |  98   |   7270    | 1.850486  |
|  9  |  128  |   15486   | 8.210359  |
| 10  |  162  |   30288   | 31.523385 |

###### UCS

|  N  | Custo | Expansões | Tempo (s)   |
| :-: | :---: | :-------: | ----------- |
|  1  |   0   |     1     | 0.000025    |
|  2  |   2   |     2     | 0.000052    |
|  3  |   4   |     4     | 0.000114    |
|  4  |   6   |    15     | 0.000212    |
|  5  |   8   |    60     | 0.001306    |
|  6  |  10   |    299    | 0.014475    |
|  7  |  12   |   1516    | 0.279619    |
|  8  |  14   |   9514    | 14.978700   |
|  9  |  16   |   59035   | 1253.012248 |

###### GREEDY

|  N  | Custo | Expansões | Tempo (s) |
| :-: | :---: | :-------: | --------- |
|  1  |   0   |     1     | 0.000026  |
|  2  |   2   |     2     | 0.000037  |
|  3  |   4   |     2     | 0.000044  |
|  4  |   6   |     3     | 0.000064  |
|  5  |   8   |     3     | 0.000085  |
|  6  |  10   |     4     | 0.000121  |
|  7  |  12   |     4     | 0.000162  |
|  8  |  14   |     5     | 0.000462  |
|  9  |  16   |     5     | 0.000444  |

###### A\*

|  N  | Custo | Expansões | Tempo (s) |
| :-: | :---: | :-------: | --------- |
|  1  |   0   |     1     | 0.000026  |
|  2  |   2   |     2     | 0.000038  |
|  3  |   4   |     2     | 0.000045  |
|  4  |   6   |     5     | 0.000106  |
|  5  |   8   |     9     | 0.000269  |
|  6  |  10   |    27     | 0.001161  |
|  7  |  12   |    93     | 0.006085  |
|  8  |  14   |    324    | 0.044251  |
|  9  |  16   |   1227    | 0.460286  |
| 10  |  18   |   4074    | 6.595554  |

### 2. Testando arrays aleatórios:

###### N = 10: [1 7 8 4 5 2 9 3 6 10]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  16   |   1226    | 1.009159  |
|     I     |  54   |   1382    | 0.093657  |
|     U     |  14   |   2031    | 0.544639  |
|     G     |  16   |     5     | 0.000204  |
|     A     |  14   |    162    | 0.011557  |

###### N = 11: [1 3 2 5 4 8 6 7 10 9 11]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  10   |    31     | 0.000596  |
|     I     |  12   |    50     | 0.001004  |
|     U     |  10   |    32     | 0.000861  |
|     G     |  10   |     6     | 0.000179  |
|     A     |  10   |    24     | 0.000706  |

###### N = 12: [1 3 2 5 4 8 6 12 7 10 9 11]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  18   |    370    | 0.019322  |
|     I     |  26   |    258    | 0.008305  |
|     U     |  16   |    375    | 0.025681  |
|     G     |  18   |     8     | 0.000313  |
|     A     |  16   |    140    | 0.007230  |

###### N = 13: [1 3 2 5 4 13 8 6 12 7 10 9 11]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  24   |   7683    | 10.379428 |
|     I     |  52   |   1392    | 0.115073  |
|     U     |  22   |   8317    | 13.031302 |
|     G     |  26   |     9     | 0.000499  |
|     A     |  22   |   2776    | 1.164527  |

###### N = 14: [1 3 2 5 4 7 8 6 14 12 13 10 9 11]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  26   |   6722    | 8.121249  |
|     I     |  48   |   1392    | 0.121794  |
|     U     |  22   |   7193    | 10.073892 |
|     G     |  24   |     9     | 0.000556  |
|     A     |  22   |   2624    | 1.074254  |

###### N = 15: [1 3 2 5 4 7 8 15 6 9 12 13 10 14 11]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  28   |   18572   | 49.274218 |
|     I     |  48   |   1381    | 0.124233  |
|     U     |  22   |   16689   | 53.146751 |
|     G     |  32   |    11     | 0.000760  |
|     A     |  22   |   1716    | 0.495602  |

###### N = 16: [1 3 2 5 4 7 8 15 6 9 12 13 10 14 11 16]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  28   |   18572   | 49.977115 |
|     I     |  48   |   1381    | 0.131245  |
|     U     |  22   |   16689   | 53.040291 |
|     G     |  32   |    11     | 0.000801  |
|     A     |  22   |   1716    | 0.495602  |

###### N = 17: [1 3 2 5 4 7 8 10 6 9 12 13 15 17 14 11 16]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  38   |   9213    | 9.635667  |
|     I     |  38   |    930    | 0.074791  |
|     U     |  26   |   9150    | 16.448345 |
|     G     |  38   |    13     | 0.000921  |
|     A     |  26   |   3632    | 2.096421  |

###### N = 18: [1 3 2 5 4 7 6 10 8 9 12 13 15 18 17 14 11 16]

| Algoritmo | Custo | Expansões | Tempo (s)  |
| :-------: | :---: | :-------: | ---------- |
|     B     |  34   |   27440   | 106.069731 |
|     I     |  50   |   1659    | 0.190443   |
|     U     |  28   |   27620   | 193.607536 |
|     G     |  34   |    12     | 0.001106   |
|     A     |  28   |   12336   | 31.644904  |

###### N = 19: [1 3 2 5 4 7 6 10 8 9 12 13 15 11 17 14 19 18 16]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  34   |   12262   | 15.794709 |
|     I     |  36   |    927    | 0.085309  |
|     U     |  26   |   12244   | 31.057561 |
|     G     |  34   |    13     | 0.001083  |
|     A     |  26   |   4056    | 2.748947  |

###### N = 20: [1 3 2 5 4 7 6 10 8 9 12 13 15 11 17 16 14 20 19 18]

| Algoritmo | Custo | Expansões | Tempo (s) |
| :-------: | :---: | :-------: | --------- |
|     B     |  32   |   18121   | 38.557624 |
|     I     |  38   |   1138    | 0.118293  |
|     U     |  26   |   18349   | 76.174505 |
|     G     |  32   |    12     | 0.001040  |
|     A     |  26   |   4816    | 3.862979  |
