from machine import Pin,PWM
import time

MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/',  
}

def morse_encode(text):
    x,dt = [],0.05
    for ch in text:
        print(ch," ",end="")
        for c in MorseCode[ch]:
            if c == '-':
                x.append([1,3*dt])
                x.append([0,dt])            
            elif c == '.':
                x.append([1,dt])
                x.append([0,dt])            
            elif c == '/':
                x.append([0,6*dt])                    
            print(c,end='')
        x.append([0,2*dt])                    
    return x

def morse_broadcast(encoded_text):    
#    led = Pin(25, Pin.OUT) # Pico
    led = Pin("LED", Pin.OUT) # Pico W
    for x in encoded_text:
        if x[0] == 1:
            led.on()
            pwm1.duty_u16(32767)
        else:
            led.off()
            pwm1.duty_u16(0)
        time.sleep(x[1])
        
text = 'Hello World! '
text = text.upper()
print(text)
encoded_text = morse_encode(text)
print(encoded_text)

pwm0 = PWM(Pin(0))
pwm0.freq(31250000)
pwm0.duty_u16(32767)

pwm1 = PWM(Pin(2))
pwm1.duty_u16(32768)
pwm1.freq(600)

while True:
    morse_broadcast(encoded_text)
