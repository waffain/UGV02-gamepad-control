# UGV02 Gamepad Control

A Python script that allows you to control the Waveshare UGV02 robot using a gamepad/joystick (tested with ROG Ally built-in controls).

## Features

- Control UGV02 robot movement using the left joystick
- Tank drive control system (forward/backward + steering)
- Real-time HTTP JSON command communication
- Automatic speed scaling and clamping for safe operation

## Requirements

- Python 3.6+
- pygame library
- requests library
- UGV02 robot by Waveshare

## Installation

1. Clone this repository:
```bash
git clone https://github.com/waffain/UGV02-gamepad-control.git
cd UGV02-gamepad-control
```

2. Install required Python packages:
```bash
pip install pygame requests
```

3. Connect to the robot's WiFi network:
   - SSID: `UGV`
   - Password: `12345678`

## Usage

1. Power on your UGV02 robot
2. Connect your computer to the robot's WiFi network
3. Connect your joystick/gamepad to your computer
4. Run the control script:
```bash
python UGV02-gamepad-control.py
```

## Controls

- **Left Joystick**: Robot movement control
  - Push forward/backward: Move robot forward/backward
  - Push left/right: Turn robot left/right
  - Diagonal movements: Create curved paths

- **Ctrl+C**: Exit the program

## Configuration

The script uses the following default settings:
- Robot IP: `192.168.4.1` (AP mode)
- Speed range: -0.5 to 0.5 (as per UGV02 specifications)
- Update frequency: 10Hz (100ms delay)

To use a different IP address (e.g., when robot is in STA mode), modify the `ROBOT_IP` variable in the script.

## How It Works

The script:
1. Initializes pygame and connects to the first available joystick
2. Reads left analog stick values (X and Y axes)
3. Converts joystick input to tank drive commands (left wheel + right wheel speeds)
4. Sends JSON commands via HTTP to the robot using the format: `{"T":1,"L":left_speed,"R":right_speed}`
5. Repeats every 100ms to maintain smooth control

## Troubleshooting

- **No joystick found**: Ensure your gamepad is connected and recognized by the system
- **Connection errors**: Verify you're connected to the robot's WiFi network and the robot is powered on
- **Robot not responding**: Check that the robot's IP address matches the one in the script
- **Jerky movement**: The robot has a 3-second timeout for movement commands, so continuous commands are sent every 100ms

## Technical Details

This project uses the UGV02's JSON command interface for robot control. The robot supports various communication methods including WiFi, ESP-NOW, and serial communication.

### JSON Command Format
```json
{"T":1,"L":left_speed,"R":right_speed}
```
- `T`: Command type (1 for speed control)
- `L`: Left wheel speed (-0.5 to 0.5)
- `R`: Right wheel speed (-0.5 to 0.5)

## Source Documentation

For complete UGV02 documentation and additional features, refer to the official Waveshare wiki:
https://www.waveshare.com/wiki/UGV02


## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.
