from gpiozero import Robot
import time as t

car = Robot(left=(7,8), right=(9,10))
car.forward(0.5)
t.sleep(5)
car.stop()

#car.left(1.0)
#t.sleep(5)
#car.stop

#car.right(1.0)
#t.sleep(2.11)
#car.stop()

#car.left(1.0)
#t.sleep(2.11)
#car.stop()

#car.backward(1.0)
#t.sleep(4)
#car.forward()
#t.sleep(8)
#car.right()
#t.sleep(10)
#car.left()
#t.sleep(8)
#car.right()
#t.sleep(10)
#car.stop()
