import RPi.GPIO as GPIO
import time

# Pin Definitions
LED_PIN = 14
BUTTON_PIN = 10

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button as input with pull-up resistor

# PWM setup
pwm = GPIO.PWM(LED_PIN, 1000)  # Set frequency to 1kHz
pwm.start(0)  # Start PWM with 0% duty cycle (off)

brightness_levels = [0, 100, 75, 50, 25]
current_level = 0

try:
    button_pressed = False
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW and not button_pressed:  # Button is pressed
            button_pressed = True
            current_level = (current_level + 1) % len(brightness_levels)
            pwm.ChangeDutyCycle(brightness_levels[current_level])
            print(f"Brightness: {brightness_levels[current_level]}%")
        elif GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            button_pressed = False
        time.sleep(0.1)  # Small delay to debounce button
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
