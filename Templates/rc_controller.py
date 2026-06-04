from pysimverse import Drone
from keyboard_control import get_keyboard_input
from time import sleep

drone = Drone()

drone.connect()

sleep(1)

drone.take_off()

while True:

    left_right, forward_backward, up_down, yaw = get_keyboard_input()

    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )

    sleep(0.05)