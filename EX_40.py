'''
40. Feladat
Írjon olyan metódust, amely olyan 2X2-es mátrixokat generál, amelynek determinánsa
10 és 20 közé esik.
'''

import numpy as np

matrix_szam=0
while matrix_szam!=5:
    b=np.random.rand(2,2)
    matrix=np.random.randint(10,size=(2,2))
    det=int(round(np.linalg.det(matrix)))
    if 10<=det and 20>=det:
        matrix_szam=matrix_szam+1
        print(matrix)
        print(det)