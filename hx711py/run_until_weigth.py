#! /usr/bin/python2

import time
import sys
import argparse

EMULATE_HX711 = False

referenceUnit = -487.11

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711


def cleanAndExit():
    print("Cleaning...")
    motor.stop()

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()



parser = argparse.ArgumentParser(description='Weight measurement.')
parser.add_argument('target_weight', metavar='N',
                    type=int, help='The target weight')
args = parser.parse_args()

pi = pigpio.pi()
pi.set_mode(25, pigpio.OUTPUT)

print("mode: ", pi.get_mode(25))


hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()
print("Tare done! Add weight now...")

target_weight = args.target_weight  # finish weight

while True:
    try:
        val = hx.get_weight(5)
        print(val)

        if val >= target_weight:
            print("Target weight reached!")
            break

        print("setting to: ", pi.set_servo_pulsewidth(25, 1000))
        print("set to: ", pi.get_servo_pulsewidth(25))

        time.sleep(1)

        print("setting to: ", pi.set_servo_pulsewidth(25, 2000))
        print("set to: ", pi.get_servo_pulsewidth(25))

        time.sleep(1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
