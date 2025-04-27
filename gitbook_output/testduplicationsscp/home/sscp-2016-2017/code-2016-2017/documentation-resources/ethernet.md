# ethernet

## SSCP - Ethernet

## Ethernet

We use ethernet as the main communication protocol between boards.

Each board maintains an internal and an external state (except for vehicle computer):

* The internal state contains variables originating from a board itselfThe external state contains variables copied over from other boards
* The internal state contains variables originating from a board itself
* The external state contains variables copied over from other boards
* The internal state contains variables originating from a board itself
* The external state contains variables copied over from other boards

The internal state contains variables originating from a board itself

The external state contains variables copied over from other boards

Vehicle computer:

* Only has internal state Sends speed, battery current, voltages, temperature, ?? to steering wheelSends all data over WiFiReceives from Steering WheelReceives from BMS
* Only has internal state&#x20;
* Sends speed, battery current, voltages, temperature, ?? to steering wheel
* Sends all data over WiFi
* Receives from Steering Wheel
* Receives from BMS
* Only has internal state&#x20;
* Sends speed, battery current, voltages, temperature, ?? to steering wheel
* Sends all data over WiFi
* Receives from Steering Wheel
* Receives from BMS

Only has internal state&#x20;

Sends speed, battery current, voltages, temperature, ?? to steering wheel

Sends all data over WiFi

Receives from Steering Wheel

Receives from BMS

Steering wheel:

* Sends complete internal state to vehicle computerReceives from vehicle computer
* Sends complete internal state to vehicle computer
* Receives from vehicle computer
* Sends complete internal state to vehicle computer
* Receives from vehicle computer

Sends complete internal state to vehicle computer

Receives from vehicle computer

BMS:

* Sends complete internal state to vehicle computer
* Sends complete internal state to vehicle computer
* Sends complete internal state to vehicle computer

Sends complete internal state to vehicle computer
