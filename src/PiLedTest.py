import time
from time import sleep
from hal import hal_input_switch as switch
from hal import hal_led as led

state = False
def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def read_switch():
    switch.init()
    return switch.read_slide_switch()

def main():

    count = 0

    while read_switch() == 1:
        blink_led(0.1)
    else:
        while read_switch() == 0:
            if count <= 50:
                blink_led(0.05)
                count += 1
            else:
                led.set_output(0, 0)

while True:
    if __name__ == "__main__":
        main()