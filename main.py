import time
import Jetson.GPIO as GPIO
from sensor import is_sensor_triggered
from camera import capture_frame
from backend import send_frame_to_backend

# Pin Definitions
input_pin = 17  # BCM pin 17 (GPIO 17)
output_pin = 18  # BCM pin 18 (GPIO 18)

def main():
    # Set up the GPIO channels
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
    
    try:
        print("Waiting for sensor trigger...")
        while True:
            if is_sensor_triggered(input_pin):
                print("Sensor triggered!")
                frame = capture_frame()
                response = send_frame_to_backend(frame)
                
                if response['action'] == 'open':
                    GPIO.output(output_pin, GPIO.HIGH)
                    print("Output signal sent: OPEN")
                else:
                    GPIO.output(output_pin, GPIO.LOW)
                    print("Output signal sent: CLOSE")
                
                time.sleep(1)  # Adjust based on your needs
                GPIO.output(output_pin, GPIO.LOW)
                
                # Add a delay to avoid multiple triggers
                time.sleep(2)  # Adjust this delay based on your needs
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Exiting gracefully")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
