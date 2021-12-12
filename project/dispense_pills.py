import time
from adafruit_servokit import ServoKit
import busio
import board
from i2c_button import I2C_Button
import json
from datetime import datetime
import os

# SERVO: Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# SERVO: Name and set up the servo according to the channel you are using.
servos = [kit.servo[i] for i in range(2)]

# SERVO: Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
for servo in servos:
    servo.set_pulse_width_range(500, 2500)

while True:
    try:
        with open('face_detected.txt') as f:
            face_detected = bool(f.read())
        if face_detected:
            os.system("./verbal_asking_script.sh")
            with open("found_name.txt") as f:
                name = f.read()
                if name != 'jack':
                    os.system("./incorrect_name.sh")
                    with open('face_detected.txt', 'w') as f:
                        f.write('')
                    time.sleep(5)
                else:
                    with open('data.txt') as f:
                        data = json.load(f)
                        out_dict = {int(k): v for k, v in data.items()}
                    print(out_dict)
                    curr_day = datetime.today().weekday()
                    desired = out_dict[curr_day]
                    print('desired: ',desired)
                    for idx, num_turns in enumerate(desired):
                        # Set the servo to 180 degree position
                        servo = servos[idx]
                        print('servo: ',idx,' num_turns:',num_turns)
                        for _ in range(num_turns):
                            servo.angle = 90
                            time.sleep(0.5)
                            servo.angle = 0
                            time.sleep(2)
                        time.sleep(0.5)
                    with open('face_detected.txt', 'w') as f:
                        f.write('')
                    time.sleep(1)
    except KeyboardInterrupt:
        for servo in servos:
            # Once interrupted, set the servo back to 0 degree position
            servo.angle = 0
            time.sleep(0.5)
            break
