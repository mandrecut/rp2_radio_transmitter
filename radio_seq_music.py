from buzzer_music import music
from time import sleep
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm0.freq(31250000)
pwm0.duty_u16(16384)

song = open("seq_music.txt", "r").read()
mySong = music(song[25:-2], pins=[Pin(2)])

while True:
    print(mySong.tick())
    sleep(0.04)

