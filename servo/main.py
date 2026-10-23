from flask import Flask, redirect, url_for
from pca9685 import PCA9685

app = Flask(__name__)
servo = PCA9685(bus_num=1, address=0x40)

# Define servo channels (add more later)
SERVOS = {
    "printer": 0
}

HOME_ANGLE = 0
OPEN_ANGLE = 180

# Start all in home
for ch in SERVOS.values():
    servo.set_servo_angle(ch, HOME_ANGLE)

@app.route("/servo/<name>/open", methods=["POST"])
def open_servo(name):
    servo.set_servo_angle(SERVOS[name], OPEN_ANGLE)
    return f"{name} opened\n"

@app.route("/servo/<name>/home", methods=["POST"])
def home_servo(name):
    servo.set_servo_angle(SERVOS[name], HOME_ANGLE)
    return f"{name} homed\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
