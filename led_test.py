import Jetson.GPIO as GPIO
import time

# Pin Definitions
output_pin = 19  # BCM pin 19 (physical pin 35) connected to the LED

# Set up the GPIO channel
GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

try:
    print("Lighting up the LED for 2 seconds")
    GPIO.output(output_pin, GPIO.HIGH)  # Turn on LED
    time.sleep(2)  # Keep the LED on for 2 seconds
    GPIO.output(output_pin, GPIO.LOW)  # Turn off LED
    print("LED turned off")

except KeyboardInterrupt:
    print("Exiting gracefully")

finally:
    # Ensure the pin is set to LOW before cleaning up
    GPIO.output(output_pin, GPIO.LOW)
    # Clean up the GPIO pins before exiting
    GPIO.cleanup()
