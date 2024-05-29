import Jetson.GPIO as GPIO
import time

# Pin Definitions
input_pin = 17  # BCM pin 17 (GPIO 17) connected to the button
output_pin = 18  # BCM pin 18 (GPIO 18) connected to the LED

# Set up the GPIO channels
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

try:
    print("Press the button to light up the LED")
    while True:
        # Check if the button is pressed
        if GPIO.input(input_pin) == GPIO.HIGH:
            print("Button pressed!")
            GPIO.output(output_pin, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(output_pin, GPIO.LOW)  # Turn off LED
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting gracefully")

finally:
    # Clean up the GPIO pins before exiting
    GPIO.cleanup()
