from pysimverse import Drone

drone=Drone()
drone.connect()
drone.take_off()

drone.move_forward(250)
drone.move_right(250)

drone.land()

