import RPi.GPIO as GPIO
import subprocess
import time

# sudo modprobe snd_bcm2835
# sudo amixer cset numid=3 1

def main():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.IN)

    prev_input = False

    while True:
        input = GPIO.input(17)
        print input
        if input != prev_input:
            prev_input = input
            if input:
                print "Playing"
                subprocess.call(['aplay', 'siren.wav'])

        time.sleep(.1)

if __name__ == '__main__':
    main()
