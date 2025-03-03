# SSCP - Driver Controls

# Driver Controls

LEDs

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

Pedal Calibration

Uncomment PEDAL_CONFIGURATION in global.h

This starts a task that will record the max and min positions of both pedals for 15 seconds and then use that to configure the pedals.

You can mash the pedals and it will print the limits if debug is enabled.

Debug

Uncomment DEBUG in global.h to enable printf

Driver Controls Design - this is super old

======================

#### main.c

##### tasks

Drive

- Read inputs from GPIO, CAN messages

- Read current DriveState

- Add to the the moving average

- produce an output based on DriveState

- control lights

- add a TritiumCommandT to tritium_queue

TritiumOutput

- Read TritiumCommandT[] from tritium_queue

- send CAN messages to the tritiums

tritium_queue

- queue of TritiumCommandT's

##### settings

DriveSettingsT drive_state

- Cruise control PID constants

TritiumStateT tritium_states[2]

- represents each individual tritium

#### drive.c

produce an output based on a DriveInputT and drive_state

Cruise

- Calculate next command speed based on PID constants

ManualControl

- linear map from throttle to command speed

Rear lights are set from either function when brake is applied.

#### tritium.c

Abstracts communication with the Tritiums over CAN.

Initialize tritium states and then send a message encoded in a TritiumCommandT.

##### structs

TritiumStateT

- condition of an individual Tritium

TritiumCommandT

- desired speed

