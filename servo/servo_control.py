# servo_control.py
import smbus2, time

bus = smbus2.SMBus(1)
ADDR = 0x40

def init_pwm(freq=50):
    prescale = int(round(25000000.0 / (4096 * freq) - 1))
    oldmode = bus.read_byte_data(ADDR, 0x00)
    bus.write_byte_data(ADDR, 0x00, (oldmode & 0x7F) | 0x10)  # sleep
    bus.write_byte_data(ADDR, 0xFE, prescale)                 # prescale
    bus.write_byte_data(ADDR, 0x00, oldmode)                  # wake
    time.sleep(0.005)
    bus.write_byte_data(ADDR, 0x00, oldmode | 0xA1)           # restart + auto-inc

def set_servo(channel, tick):
    reg = 0x06 + 4 * channel
    on = 0
    off = tick
    bus.write_i2c_block_data(ADDR, reg, [on & 0xFF, on >> 8, off & 0xFF, off >> 8])

def set_angle(channel, angle):
    # 204 ≈ 1.0 ms, 410 ≈ 2.0 ms, 307 ≈ 1.5 ms
    pulse_min, pulse_max = 204, 410
    tick = int(pulse_min + (angle / 180.0) * (pulse_max - pulse_min))
    set_servo(channel, tick)

# Initialize once at startup
init_pwm()
