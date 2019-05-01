'''
2. Feladat
Írjon függvényt, amely egy paraméterként adott 2D-s mátrixról eldönti, hogy alsó
háromszög mátrix-e.
'''

def alsoharomszog_vizsgalat(matrix):
    for i in range(0,len(matrix)):
        for j in range(i+1,len(matrix)):
            if(matrix[i][j])!=0:
                return False
    return True


matrix1=[[4,0,0,0,0],
         [3,6,0,0,0],
         [8,2,7,0,0],
         [3,9,4,5,0],]

matrix2=[[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],]

print(alsoharomszog_vizsgalat(matrix1))

print(alsoharomszog_vizsgalat(matrix2))