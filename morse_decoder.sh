nc -l -u 7355 | sox -r 48000 -t raw -b 16 -c 1 -e signed-integer /dev/stdin -r 22000 -t raw -b 16 -c 1 -e signed-integer - | multimon-ng -t raw -a MORSE_CW /dev/stdin
