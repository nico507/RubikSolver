
"""Aquí se hara el procesamiento de las imagenes"""

import cv2

def segmento(img):
 
   image = cv2.imread(img)
   S1= image[6:25, 4:22] #segmentos
   S2= image[25:44, 4:22]
   S3= image[44:63, 4:22]
   S4= image[6:25, 22:40]
   S5= image[25:44, 22:40]
   S6= image[44:63, 22:40]
   S7= image[6:25, 40:60]
   S8= image[25:44, 40:60]
   S9= image[44:63, 40:60]
   ##cv2.imwrite('S1', S1)
   ##cv2.imwrite('S2', S2)
   ##cv2.imwrite('S3', S3)
   ##cv2.imwrite('S4', S4)
   ##cv2.imwrite('S5', S5)
   ##cv2.imwrite('S6', S6)
   ##cv2.imwrite('S7', S7)
   ##cv2.imwrite('S8', S8)
   ##cv2.imwrite('S9', S9)

   return S1, S2, S3, S4, S5, S6, S7, S8, S9