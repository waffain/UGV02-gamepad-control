import pygame
import requests
import time
import math

def init_controller():
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

def map_joystick_to_speeds(x, y):
    # Convert joystick values to left/right wheel speeds
    # x and y are in range -1 to 1
    left = y + x
    right = y - x
    
    # Clamp values to -0.5 to 0.5 (robot's speed range)
    left = max(min(left/2, 0.5), -0.5)
    right = max(min(right/2, 0.5), -0.5)
    
    return left, right

def main():
    # Robot IP address (when in AP mode)
    ROBOT_IP = "192.168.4.1"
    
    try:
        joystick = init_controller()
        print(f"Connected to {joystick.get_name()}")
        
        while True:
            pygame.event.pump()
            
            # Get left stick X and Y values
            x = joystick.get_axis(0)  # Left/Right on left stick
            y = -joystick.get_axis(1)  # Up/Down on left stick (inverted)
            
            # Convert to robot speeds
            left_speed, right_speed = map_joystick_to_speeds(x, y)
            
            # Create and send JSON command
            command = {"T": 1, "L": left_speed, "R": right_speed}
            url = f"http://{ROBOT_IP}/js?json={str(command)}"
            
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    print(f"Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Connection error: {e}")
            
            # Send commands every 100ms to prevent timeout
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()