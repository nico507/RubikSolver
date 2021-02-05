import cv2
from Image import segmento
from Median import median
from operations import wos, mdm
from mapeo_colores import mapeo
from Cubo import Media


def lectura_cara(n,M):

    img1, img2, img3, img4, img5, img6, img7, img8, img9= get_the_video(n)

    colors = []

    # Calculando la mediana de cada cuadrado
    m1 = median(img1)
    m2 = median(img2)
    m3 = median(img3)
    m4 = median(img4)
    m5 = median(img5)
    m6 = median(img6)
    m7 = median(img7)
    m8 = median(img8)
    m9 = median(img9)

    # Aplicando el algoritmo WOS
    wos_1 = wos(m1, M)
    wos_2 = wos(m2, M)
    wos_3 = wos(m3, M)
    wos_4 = wos(m4, M)
    wos_5 = wos(m5, M)
    wos_6 = wos(m6, M)
    wos_7 = wos(m7, M)
    wos_8 = wos(m8, M)
    wos_9 = wos(m9, M)

    # Aplicando el algoritmo MDM
    mdm_1 = mdm(wos_1, M)
    mdm_2 = mdm(wos_2, M)
    mdm_3 = mdm(wos_3, M)
    mdm_4 = mdm(wos_4, M)
    mdm_5 = mdm(wos_5, M)
    mdm_6 = mdm(wos_6, M)
    mdm_7 = mdm(wos_7, M)
    mdm_8 = mdm(wos_8, M)
    mdm_9 = mdm(wos_9, M)

    colors.append(mapeo(mdm_1))
    colors.append(mapeo(mdm_2))
    colors.append(mapeo(mdm_3))
    colors.append(mapeo(mdm_4))
    colors.append(mapeo(mdm_5))
    colors.append(mapeo(mdm_6))
    colors.append(mapeo(mdm_7))
    colors.append(mapeo(mdm_8))
    colors.append(mapeo(mdm_9))

    print(colors)
    cv2.imwrite("img1.jpg", img1)

    cv2.imwrite("wos_1.jpg", wos_1)
    cv2.imwrite("mdm_1.jpg", mdm_1)
    cv2.imwrite("wos_final.jpg", wos_final)
    cv2.imwrite("mdm_final.jpg", mdm_final)


M=Media()

camera=picamera.PiCamera()
camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
camera.framerate = 24
time.sleep(2)
camera.capture('Cara1.jpg') #captura de foto
lectura_cara('Cara1.jpg')
