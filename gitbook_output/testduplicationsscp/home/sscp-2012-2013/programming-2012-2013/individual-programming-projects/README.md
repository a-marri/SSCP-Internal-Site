# individual-programming-projects

## SSCP - Individual Programming Projects

## Individual Programming Projects

Auto-cancelling turn signals

* If the driver turned on the right turn signal, turned the steering wheel to the right, and then turned back to center the right turn signal would automatically turn off.  You'll have to figure out which microcontroller on the board should be sending those messages and what information the two micros will have to share to make that happen.  You shouldn't need to change code on the light boards themselves \[why not?].

If the driver turned on the right turn signal, turned the steering wheel to the right, and then turned back to center the right turn signal would automatically turn off.  You'll have to figure out which microcontroller on the board should be sending those messages and what information the two micros will have to share to make that happen.  You shouldn't need to change code on the light boards themselves \[why not?].

Kent display

* Hook the Kent display into the main CAN bus and have it display information from the battery pack. &#x20;
* Parse CAN messages, choose which are important to display and choose what information should be displayed on button presses.
* When the board is ready also move it into a box (grab a mech team person if you want).
* Have an electrical person make a new version of the Kent board in Altium with a Phoenix connector instead of DB-9.  The code should not change when the connector changes.

Hook the Kent display into the main CAN bus and have it display information from the battery pack. &#x20;

Parse CAN messages, choose which are important to display and choose what information should be displayed on button presses.

When the board is ready also move it into a box (grab a mech team person if you want).

Have an electrical person make a new version of the Kent board in Altium with a Phoenix connector instead of DB-9.  The code should not change when the connector changes.

Brake light fading

* Program the light boards and the tritium side of driver controls to make the brake lights' brightness vary with how far the brake pedal is depressed.&#x20;
* This code would not run on the car for race or road driving because it makes brakes less visible, but it's a good exercise with multiple parts.
* If we ever implement this on the car the brake lights and the headlights could pulse instead.
* Relevant sections of the California vehicle code: 25251.2.  Any motorcycle may be equipped with a means of modulating the upper beam of the headlamp between a high and a lower brightness at a rate of 200 to 280 flashes per minute. Such headlamps shall not be so modulated during darkness. (c) Any stoplamp or supplemental stoplamp required or permitted bySection 24603 may be equipped so as to flash not more than four times within the first four seconds after actuation by application of the brakes.&#x20;
* Any motorcycle may be equipped with a means of modulating the upper beam of the headlamp between a high and a lower brightness at a rate of 200 to 280 flashes per minute. Such headlamps shall not be so modulated during darkness.&#x20;
* (c) Any stoplamp or supplemental stoplamp required or permitted bySection 24603 may be equipped so as to flash not more than four times within the first four seconds after actuation by application of the brakes.&#x20;

Program the light boards and the tritium side of driver controls to make the brake lights' brightness vary with how far the brake pedal is depressed.&#x20;

This code would not run on the car for race or road driving because it makes brakes less visible, but it's a good exercise with multiple parts.

If we ever implement this on the car the brake lights and the headlights could pulse instead.

Relevant sections of the California vehicle code: 25251.2. &#x20;

* Any motorcycle may be equipped with a means of modulating the upper beam of the headlamp between a high and a lower brightness at a rate of 200 to 280 flashes per minute. Such headlamps shall not be so modulated during darkness.&#x20;
* (c) Any stoplamp or supplemental stoplamp required or permitted bySection 24603 may be equipped so as to flash not more than four times within the first four seconds after actuation by application of the brakes.&#x20;

Any motorcycle may be equipped with a means of modulating the upper beam of the headlamp between a high and a lower brightness at a rate of 200 to 280 flashes per minute. Such headlamps shall not be so modulated during darkness.&#x20;

(c) Any stoplamp or supplemental stoplamp required or permitted bySection 24603 may be equipped so as to flash not more than four times within the first four seconds after actuation by application of the brakes.&#x20;

Tritium Cruise Control

* Set up a PID loops to make the tritium cruise control better.

Set up a PID loops to make the tritium cruise control better.

Box CAN

* First rev of the board will not require programming, second rev will have eeprom, a display, buttons and possibly USB.

First rev of the board will not require programming, second rev will have eeprom, a display, buttons and possibly USB.

Audio

* Talk to the multiplexer on driver controls to switch between radio and mp3 player input.
* Beat the electrical team until they debug the circuit.
* The multiplexer is a LMV 1089.  Find the datasheet and figure out I2C communication.

Talk to the multiplexer on driver controls to switch between radio and mp3 player input.

Beat the electrical team until they debug the circuit.

The multiplexer is a LMV 1089.  Find the datasheet and figure out I2C communication.
