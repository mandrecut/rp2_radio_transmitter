import time
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm0.freq(31250000)
pwm0.duty_u16(int(65536//4))
pwm1 = PWM(Pin(2))
pwm1.duty_u16(32768)

while True:
    for n in range(1,101):
        pwm1.freq(n*10+200)
        time.sleep(0.01)

