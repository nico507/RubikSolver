
import picamera
import time
import numpy as np

def captura():
      with picamera.PiCamera() as camera:
        camera.resolution = (64, 64) #ponemos la menor resolución posible para procesar más facilmente
        camera.framerate = 24
        time.sleep(2)
        output = np.empty((64, 64, 3), dtype=np.uint8) #formato de foto
        camera.capture(output, 'rgb') #captura de foto
        output = output[:64, :64]
      return output

def Valor_medio(picture):
    width = picture.shape[0] #ancho de la foto
    height = picture.shape[1] #alto de la foto

    size = width * height #area de la foto

    media = np.zeros(3)  #Vector sumatorias de rgb
    for k in range(3):
        for i in range(1, width):
            for j in range(1, height):
                if picture[i, j, k]>20:
                  media[k] = media[k] + picture[i, j, k]  #sumatoria
                else
        media[k] = media[k] / size

    return media

##Obtener valores del cubo resuelto

def Media():
  M=[]

  print("\nIniciando, ponga el cubo con la cara blanca arriba\n")
  input("presione una tecla para continuar")
  blanco=captura()
  M.append(Valor_medio(blanco))

  print("\nponga el cubo con la cara roja arriba\n")
  input("presione una tecla para continuar")
  rojo=captura()
  M.append(Valor_medio(rojo))

  print("\nponga el cubo con la cara amarillo arriba\n")
  input("presione una tecla para continuar")
  amarillo=captura()
  M.append(Valor_medio(amarillo))

  print("\nponga el cubo con la cara naranja arriba\n")
  input("presione una tecla para continuar")
  naranja=captura()
  M.append(Valor_medio(naranja))

  print("\nponga el cubo con la cara verde arriba\n")
  input("presione una tecla para continuar")
  verde=captura()
  M.append(Valor_medio(verde))

  print("\nponga el cubo con la cara azul arriba\n")
  input("presione una tecla para continuar")
  azul=captura()
  M.append(Valor_medio(azul))

  return M
#print(M)
