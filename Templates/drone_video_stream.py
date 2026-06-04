from pysimverse import Drone
from time import sleep
from keyboard_control import get_keyboard_input
import cv2

drone = Drone()

try:
    # Connect
    drone.connect()
    sleep(1)

    # Start stream
    drone.streamon()
    sleep(1)

    # Takeoff
    drone.take_off()
    sleep(2)

    while True:

        # 1. GET CONTROL INPUT
        left_right, forward_backward, up_down, yaw = get_keyboard_input()

        # Safety fallback
        if left_right is None:
            left_right = forward_backward = up_down = yaw = 0

        # 2. SEND CONTROL SIGNAL
        drone.send_rc_control(
            left_right,
            forward_backward,
            up_down,
            yaw
        )

        # 3. GET VIDEO FRAME
        frame, is_success = drone.get_frame()

        if is_success:
            cv2.imshow("Drone Feed", frame)

        # 4. EXIT CONDITION
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    print("Landing drone safely...")

    drone.send_rc_control(0, 0, 0, 0)  # stop motion first
    sleep(1)

    drone.land()
    drone.streamoff()
    drone.disconnect()

    cv2.destroyAllWindows()