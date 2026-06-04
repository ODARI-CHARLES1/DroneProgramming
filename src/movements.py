from pysimverse import Drone
from time import sleep

drone=Drone()

drone.connect()
drone.take_off()

#movements up and down 
drone.move_forward(100)
drone.move_backward(100)
drone.move_left(100)
drone.move_right(100)
drone.move_left(100)
drone.move_up(100)
drone.move_down(100)
drone.land()
