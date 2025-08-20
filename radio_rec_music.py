import time
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm0.freq(31250000)
pwm0.duty_u16(16384)

pwm1 = PWM(Pin(2))
pwm1.freq(1000000)

buf = bytearray(4096)
for t in range(20):
    f = open("mgm_music.raw","rb")
    while f.readinto(buf) > 0:
        for sample in buf:
            pwm1.duty_u16(sample<<8)
            time.sleep_us(85)
    f.close()
