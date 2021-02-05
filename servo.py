import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)

pwm=gpio.PWM(12, 50)
pwm.start(0)

sleep(7)
pwm.ChangeDutyCycle(3) #0 grados
sleep(2)
pwm.ChangeDutyCycle(5) #90 grados
sleep(5)
pwm.ChangeDutyCycle(7) #180 grados
sleep(5)
pwm.ChangeDutyCycle(0)

pwm.stop()
gpio.cleanup()
