import smbus2, time

class PCA9685:
    def __init__(self, bus_num=1, address=0x40, freq=50):
        self.bus = smbus2.SMBus(bus_num)
        self.addr = address
	# Wake up the chip
        self.write(0x00, 0x00)       # clear sleep bit
        time.sleep(0.005)
        self.set_pwm_freq(freq)

    def write(self, reg, val):
        self.bus.write_byte_data(self.addr, reg, val)

    def read(self, reg):
        return self.bus.read_byte_data(self.addr, reg)

    def set_pwm_freq(self, freq):
        prescale = int(round(25000000.0 / (4096 * freq) - 1))
        oldmode = self.read(0x00)
        self.write(0x00, (oldmode & 0x7F) | 0x10)
        self.write(0xFE, prescale)
        self.write(0x00, oldmode)
        time.sleep(0.005)
        self.write(0x00, oldmode | 0xa1)

    def set_pwm(self, channel, on, off):
        self.bus.write_i2c_block_data(self.addr, 0x06+4*channel,
            [on & 0xFF, on >> 8, off & 0xFF, off >> 8])

    def set_servo_angle(self, channel, angle):
        # map 0-180° → 204-410 ticks (~1ms–2ms)
        pulse = int(204 + (angle/180.0) * (410-204))
        self.set_pwm(channel, 0, pulse)
