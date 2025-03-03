# SSCP - What we do

# What we do

## Embedded vs. PC

[](#h.rvwdqry48anf)

The embedded code team is responsible for code that runs on the car and makes the car drive from second to second. We write all of the code for the boards on the car: battery management, lights, driver controls, and data collection (telemetry).

The PC and strategy team is responsible for taking all of the data that comes off the car and building a model of the car: how much energy it takes to drive at a given speed, what the sources of losses on the car are and how important each one is, and what speed the car should drive during the race based on all of that information.

Broadly speaking the strategy team deals with data and the embedded team deals with bits and bytes. If the strategy team gets something wrong we might drive too fast and run out of energy or drive too slowly and overcharge. If the embedded team gets something wrong the car might not drive at all, the batteries might overheat, or the car might go in reverse when you hit the throttle.

The embedded team works in C, while the strategy team works with python, MATLAB, and whatever other languages they want.

## Hardware Details

[](#h.orddjcporaww)

The solar car runs on ARM processors, specifically the STM32F4 family of processors made by ST Microelectronics.

We use the F4s on all of the boards (button/steering wheel display, driver controls, lights, battery management system, IMU/telemetry) on the car.

We run FreeRTOS, an operating system which provides a task and queue abstraction (among other things), on the F4s.

We deal with inputs from real hardware and create output that controls real hardware. For example, on the battery management system board, voltage measurements go to the processor and the processor decides if it's necessary to turn off the relay that isolates the batteries from the rest of the car.  Communication between the F4 and the other chips on the same board is frequently over SPI or I2C.  Communication between boards on the car is over CAN.

One of the coolest boards on the car is the telemetry board which receives data from all other boards, receives GPS data, and broadcasts it over WiFi to the strategy laptop in another car.

