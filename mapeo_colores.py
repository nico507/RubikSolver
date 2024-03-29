import numpy as np
from Cubo import Media

# M=Media()

##M = [[67, 92, 79],  # Blanco
##     [118, 61, 65],  # Rojo
#     [81, 118, 71],  # Amarillo
#     [128, 86, 73],  # Naranja
#     [12, 132, 81],  # Verde
#     [34, 129, 133],  # Azul
#     [27, 55, 17]
#    ]  # Fondo

def mapeo(img, M):
    w = np.shape(img)[0]
    h = np.shape(img)[1]

    count = np.zeros(6)

    for i in range(w):
        for j in range(h):

            if img[i, j, 2] == M[0][0] and img[i, j, 1] == M[0][1] and img[i, j, 0] == M[0][2]:
                count[0] = count[0] + 1

            if img[i, j, 2] == M[1][0] and img[i, j, 1] == M[1][1] and img[i, j, 0] == M[1][2]:
                count[1] = count[1] + 1

            if img[i, j, 2] == M[2][0] and img[i, j, 1] == M[2][1] and img[i, j, 0] == M[2][2]:
                count[2] = count[2] + 1

            if img[i, j, 2] == M[3][0] and img[i, j, 1] == M[3][1] and img[i, j, 0] == M[3][2]:
                count[3] = count[3] + 1

            if img[i, j, 2] == M[4][0] and img[i, j, 1] == M[4][1] and img[i, j, 0] == M[4][2]:
                count[4] = count[4] + 1

            if img[i, j, 2] == M[5][0] and img[i, j, 1] == M[5][1] and img[i, j, 0] == M[5][2]:
                count[5] = count[5] + 1


    moda = max(count)
    indice = 0

    for i in range(6):
        if count[i] == moda:
            indice = i

    if indice == 0:
        return 'U'
    if indice == 1:
        return 'F'
    if indice == 2:
        return 'D'
    if indice == 3:
        return 'B'
    if indice == 4:
        return 'L'
    if indice == 5:
        return 'R'
    if indice == 6:
        return 'X'
