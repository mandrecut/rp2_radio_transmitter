from machine import Pin , ADC , PWM

pwm0 = PWM (Pin(0))
pwm0.freq (31250000)
pwm0.duty_u16(32768)

pwm = PWM(Pin(2))
pwm.freq(1000000)

adc = ADC(27)
while True :
    pwm.duty_u16(adc.read_u16())
