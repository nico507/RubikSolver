import numpy as nmp


M = [[17, 109, 149],  # Azul ya
     [246, 83, 20],  # Rojo ***
     [69, 205, 84],  # Verde pálido
     [242, 129, 20],  # Naranja ya
     [183, 178, 52],  # Amarillo ***
     [158, 176, 130],  # Blanco
     [4, 17, 2]
    ]  # Fondo


M2 = [[0, 0, 255],  # Azul
            [255, 0, 0],  # Rojo
            [0, 255, 0],  # Verde
            [255, 128, 0],  # Naranja
            [255, 255, 0],  # Amarillo            [255, 255, 255],  # Blanco
            [0, 0, 0]]  # Fondo


def MDM(img, M):

    Classes = nmp.shape(M)[0]
    width = img.shape[0]
    height = img.shape[1]

    MDM_out = nmp.zeros((width, height, 3))

    for i in range(width):

        for j in range(height):

            D = []

            for p in range(6):

                dist = nmp.sqrt(
                    pow((img[i, j, 0] - M[p][0]), 2) +
                    pow((img[i, j, 1] - M[p][1]), 2) +
                    pow((img[i, j, 2] - M[p][2]), 2)
                    )
                D.append(dist)

            minD = min(D)

            for r in range(Classes):

                if D[r] == minD:

                    MDM_out.itemset((i, j, 0), M[r][0])
                    MDM_out.itemset((i, j, 1), M[r][1])
                    MDM_out.itemset((i, j, 2), M[r][2])

    return MDM_out

def WOS(img, M):

    Classes = nmp.shape(M)[0]
    width = img.shape[0]
    height = img.shape[1]

    WOS_out = nmp.zeros((width, height, 3))

    for k in range(3):

        for i in range(width):

            for j in range(height):

                delta = []

                for p in range(Classes):

                    dist = abs(img[i, j, k] - M[p][k])
                    delta.append(dist)

                minDelta = min(delta)

                for r in range(Classes):

                    if delta[r] == minDelta:

                        WOS_out.itemset((i, j, k), M[r][k])

    return WOS_out
