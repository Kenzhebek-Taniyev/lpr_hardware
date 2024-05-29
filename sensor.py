import Jetson.GPIO as GPIO

def is_sensor_triggered(input_pin):
    return GPIO.input(input_pin) == GPIO.HIGH
