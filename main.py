import cv2
from video_operations import get_the_video
from Median import median
from operations import wos, mdm
from mapeo_colores import mapeo


def lectura_cara(n):

    img1, img2, img3, img4, img5, img6, img7, img8, img9, final = get_the_video(n)

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
    final_m = median(final)

    # Aplicando el algoritmo WOS
    wos_1 = wos(m1)
    wos_2 = wos(m2)
    wos_3 = wos(m3)
    wos_4 = wos(m4)
    wos_5 = wos(m5)
    wos_6 = wos(m6)
    wos_7 = wos(m7)
    wos_8 = wos(m8)
    wos_9 = wos(m9)
    wos_final = wos(final_m)

    # Aplicando el algoritmo MDM
    mdm_1 = mdm(wos_1)
    mdm_2 = mdm(wos_2)
    mdm_3 = mdm(wos_3)
    mdm_4 = mdm(wos_4)
    mdm_5 = mdm(wos_5)
    mdm_6 = mdm(wos_6)
    mdm_7 = mdm(wos_7)
    mdm_8 = mdm(wos_8)
    mdm_9 = mdm(wos_9)
    mdm_final = mdm(wos_final)

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

lectura_cara(0)