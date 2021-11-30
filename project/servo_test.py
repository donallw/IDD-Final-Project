import time
from adafruit_servokit import ServoKit
import busio
import board
from i2c_button import I2C_Button

# BUTTON: initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# BUTTON: scan the I2C bus for devices
while not i2c.try_lock():
	pass
devices = i2c.scan()
i2c.unlock()
default_addr = 0x6f
if default_addr not in devices:
	print('warning: no device at the default button address', default_addr)

# BUTTON: initiatilize the button
button = I2C_Button(i2c)

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
        if button.last_click_ms < 1000:
            for servo in servos:
                # Set the servo to 180 degree position
                servo.angle = 180
                time.sleep(2)
                # Set the servo to 0 degree position
                servo.angle = 0
                time.sleep(2)
        
    except KeyboardInterrupt:
        for servo in servos:
            # Once interrupted, set the servo back to 0 degree position
            servo.angle = 0
            time.sleep(0.5)
            break
