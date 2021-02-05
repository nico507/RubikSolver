import numpy as nmp

def Mean(img):

    pxlQuant = width*height
    meanOut = nmp.zeros(3)
    width = img.shape[0]
    height = img.shape[1]

    for k in range(3):

        for i in range(1, width):

            for j in range(1, height):

                meanOut[k] = meanOut[k] + img[i, j, k]

        meanOut[k] = meanOut[k]/pxlQuant

    return meanOut