# SSCP - Sundae Code Testing Checklist

# Sundae Code Testing Checklist

Checklist of items to double check when testing board functionality.

BEFORE UNVEILING (JULY 1)

* VC read ADCs correctlyVC handle ADC readings correctly --> send correct message to tritiumVC correctly send and receive over ethernetVC correctly send over CANVC correctly forward messages from steering wheelBMS read current senseBMS read voltage senseBMS send info over ethernet to VC
* VC read ADCs correctly
* VC handle ADC readings correctly --> send correct message to tritium
* VC correctly send and receive over ethernet
* VC correctly send over CAN
* VC correctly forward messages from steering wheel
* BMS read current sense
* BMS read voltage sense
* BMS send info over ethernet to VC

* VC read ADCs correctly
* VC handle ADC readings correctly --> send correct message to tritium
* VC correctly send and receive over ethernet
* VC correctly send over CAN
* VC correctly forward messages from steering wheel
* BMS read current sense
* BMS read voltage sense
* BMS send info over ethernet to VC

VC read ADCs correctly

VC handle ADC readings correctly --> send correct message to tritium

VC correctly send and receive over ethernet

VC correctly send over CAN

VC correctly forward messages from steering wheel

BMS read current sense

BMS read voltage sense

BMS send info over ethernet to VC

BEFORE TEST DRIVE 1 (JULY 15)

* Fill out entire protobuf variable listSteering wheel read all buttons correctlySteering wheel display on screen correctlyVC write protobuf to SD cardVC read all IMU sensors and populate protobufVC send over ethernet to telemetryBMS all states correct
* Fill out entire protobuf variable list
* Steering wheel read all buttons correctly
* Steering wheel display on screen correctly
* VC write protobuf to SD card
* VC read all IMU sensors and populate protobuf
* VC send over ethernet to telemetry
* BMS all states correct

* Fill out entire protobuf variable list
* Steering wheel read all buttons correctly
* Steering wheel display on screen correctly
* VC write protobuf to SD card
* VC read all IMU sensors and populate protobuf
* VC send over ethernet to telemetry
* BMS all states correct

Fill out entire protobuf variable list

Steering wheel read all buttons correctly

Steering wheel display on screen correctly

VC write protobuf to SD card

VC read all IMU sensors and populate protobuf

VC send over ethernet to telemetry

BMS all states correct

Individual Boards

Vehicle Computer

* SD Card writing: VC board should periodically write internal protobuf structure to its SD card.IMU: VC board should read IMU state (GPS, velocity, etc.) and store in internal protobuf structureDriver Controls: VC board should correctly determine motor output given the current driving state.
* SD Card writing: VC board should periodically write internal protobuf structure to its SD card.
* IMU: VC board should read IMU state (GPS, velocity, etc.) and store in internal protobuf structure
* Driver Controls: VC board should correctly determine motor output given the current driving state.

* SD Card writing: VC board should periodically write internal protobuf structure to its SD card.
* IMU: VC board should read IMU state (GPS, velocity, etc.) and store in internal protobuf structure
* Driver Controls: VC board should correctly determine motor output given the current driving state.

SD Card writing: VC board should periodically write internal protobuf structure to its SD card.

IMU: VC board should read IMU state (GPS, velocity, etc.) and store in internal protobuf structure

Driver Controls: VC board should correctly determine motor output given the current driving state.

Steering Wheel

* SPI screen output should be visible.Other fun goodies.
* SPI screen output should be visible.
* Other fun goodies.

* SPI screen output should be visible.
* Other fun goodies.

SPI screen output should be visible.

Other fun goodies.

BMS

* State Diagram.Other fun goodies.
* State Diagram.
* Other fun goodies.

* State Diagram.
* Other fun goodies.

State Diagram.

Other fun goodies.

Communication between Systems

Vehicle Computer/BMS

* BMS should send ethernet packets which the VC board receives.
* BMS should send ethernet packets which the VC board receives.

* BMS should send ethernet packets which the VC board receives.

BMS should send ethernet packets which the VC board receives.

Vehicle Computer/Steering Wheel

* Steering wheel should send ethernet packets to the VC board.VC board should send ethernet packets to the steering wheel board.
* Steering wheel should send ethernet packets to the VC board.
* VC board should send ethernet packets to the steering wheel board.

* Steering wheel should send ethernet packets to the VC board.
* VC board should send ethernet packets to the steering wheel board.

Steering wheel should send ethernet packets to the VC board.

VC board should send ethernet packets to the steering wheel board.

Vehicle Computer/WiFi Router

* VC board should send ethernet packets to the wireless access point.Dragonfly's packet parser should read Protobuf packets from the VC board.
* VC board should send ethernet packets to the wireless access point.
* Dragonfly's packet parser should read Protobuf packets from the VC board.

* VC board should send ethernet packets to the wireless access point.
* Dragonfly's packet parser should read Protobuf packets from the VC board.

VC board should send ethernet packets to the wireless access point.

Dragonfly's packet parser should read Protobuf packets from the VC board.

Vehicle Computer/Tritium motor controllers

* VC board should send CAN commands to the Tritiums, sending motor rpm/currentVC board should receive CAN messages from the Tritiums, reading a bunch of measurements
* VC board should send CAN commands to the Tritiums, sending motor rpm/current
* VC board should receive CAN messages from the Tritiums, reading a bunch of measurements

* VC board should send CAN commands to the Tritiums, sending motor rpm/current
* VC board should receive CAN messages from the Tritiums, reading a bunch of measurements

VC board should send CAN commands to the Tritiums, sending motor rpm/current

VC board should receive CAN messages from the Tritiums, reading a bunch of measurements

Vehicle Computer/ADCs

* VC board should be able to read pedal input values and store them accordingly
* VC board should be able to read pedal input values and store them accordingly

* VC board should be able to read pedal input values and store them accordingly

VC board should be able to read pedal input values and store them accordingly

BMS/MPPT Solar Array

* BMS board should send CAN commands to the MPPTs to turn them on.BMS board should receive CAN messages from the MPPTs to store voltages, currents, etc.
* BMS board should send CAN commands to the MPPTs to turn them on.
* BMS board should receive CAN messages from the MPPTs to store voltages, currents, etc.

* BMS board should send CAN commands to the MPPTs to turn them on.
* BMS board should receive CAN messages from the MPPTs to store voltages, currents, etc.

BMS board should send CAN commands to the MPPTs to turn them on.

BMS board should receive CAN messages from the MPPTs to store voltages, currents, etc.

