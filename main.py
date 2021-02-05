import cv2
from Imagen import segmento
from Median import median
from Operations import WOS, MDM
from mapeo_colores import mapeo
from Cubo import Media
import picamera
import time

def lectura_cara(n,M):

    img1, img2, img3, img4, img5, img6, img7, img8, img9= segmento(n)

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
    wos_1 = WOS(m1, M)
    wos_2 = WOS(m2, M)
    wos_3 = WOS(m3, M)
    wos_4 = WOS(m4, M)
    wos_5 = WOS(m5, M)
    wos_6 = WOS(m6, M)
    wos_7 = WOS(m7, M)
    wos_8 = WOS(m8, M)
    wos_9 = WOS(m9, M)

    # Aplicando el algoritmo MDM
    mdm_1 = MDM(wos_1, M)
    mdm_2 = MDM(wos_2, M)
    mdm_3 = MDM(wos_3, M)
    mdm_4 = MDM(wos_4, M)
    mdm_5 = MDM(wos_5, M)
    mdm_6 = MDM(wos_6, M)
    mdm_7 = MDM(wos_7, M)
    mdm_8 = MDM(wos_8, M)
    mdm_9 = MDM(wos_9, M)

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

M=Media()

#Revolver
input("esperando a que se revuelva, presione enter para continuar")
camera=picamera.PiCamera()
camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
camera.framerate = 24
time.sleep(2)
camera.capture('Cara1.jpg') #captura de foto
lectura_cara('Cara1.jpg', M)

input("gire el cubo")
#camera=picamera.PiCamera()
#camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
#camera.framerate = 24
time.sleep(2)
camera.capture('Cara2.jpg') #captura de foto
lectura_cara('Cara2.jpg', M)

input("gire el cubo")
#camera=picamera.PiCamera()
#camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
#camera.framerate = 24
time.sleep(2)
camera.capture('Cara3.jpg') #captura de foto
lectura_cara('Cara3.jpg', M)

input("gire el cubo")
#camera=picamera.PiCamera()
#camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
#camera.framerate = 24
time.sleep(2)
camera.capture('Cara4.jpg') #captura de foto
lectura_cara('Cara4.jpg', M)

input("gire el cubo")
#camera=picamera.PiCamera()
#camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
#camera.framerate = 24
time.sleep(2)
camera.capture('Cara5.jpg') #captura de foto
lectura_cara('Cara5.jpg', M)

input("gire el cubo")
#camera=picamera.PiCamera()
#camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
#camera.framerate = 24
time.sleep(2)
camera.capture('Cara6.jpg') #captura de foto
lectura_cara('Cara6.jpg', M)

