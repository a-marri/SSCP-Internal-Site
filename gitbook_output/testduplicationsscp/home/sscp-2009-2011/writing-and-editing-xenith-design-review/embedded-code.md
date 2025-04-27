# embedded-code

## SSCP - Embedded code

## Embedded code

Boards on the car:

* BMSLightsDriver controlsTritium sideElmo sideMPPTsEmail Sasha and Greg if there's still nothing herePressure ProTelemetryHMDKent display
* BMS
* Lights
* Driver controlsTritium sideElmo side
* Tritium side
* Elmo side
* MPPTsEmail Sasha and Greg if there's still nothing here
* Email Sasha and Greg if there's still nothing here
* Pressure Pro
* Telemetry
* HMD
* Kent display
* BMS
* Lights
* Driver controlsTritium sideElmo side
* Tritium side
* Elmo side
* MPPTsEmail Sasha and Greg if there's still nothing here
* Email Sasha and Greg if there's still nothing here
* Pressure Pro
* Telemetry
* HMD
* Kent display

BMS

Lights

Driver controls

* Tritium side
* Elmo side

Tritium side

Elmo side

MPPTs

* Email Sasha and Greg if there's still nothing here

Email Sasha and Greg if there's still nothing here

[Sasha](mailto:s.zbrozek@gmail.com)

[Greg](mailto:ghall1@stanford.edu)

Pressure Pro

Telemetry

HMD

Kent display

BPS

Lessons and Improvements from last cycle

The centralized control board and the switch to STM32 processors on the new BMS meant that the code had to completely change.  Additionally, a focus on improving critical systems such as current measurement allowed us to do much more sophisticated data analysis on the board and improved telemetry back to the convoy.  Since all our monitoring was done with one chip, we could do significantly better state of charge estimation than ever before.

Software Architecture

The BPS software had a rudimentary scheduler architecture that enables the system to round-robin through available tasks as they needed to happen.  This was much simpler than a full-blown RTOS as most "tasks" were encapsulated as run-once functions and were never pre-empted, apart from interrupts.  This was inspired by a similar system used on several of the Apogee boards (but written from scratch).  For the module architecture, most hardware devices were split into their own separate "driver" files.

Problems found and solutions

One of the more crippling problem encountered during pre-race testing was the issue where the STM32 would lose SPI contact with the chips.  To fix this, a routine was added that would reset the SPI/DMA interface as soon as data stopped coming out of the interface.  This took an exceptionally long time to debug and was the cause for most of the BMS-related headaches before the race.  Most of these were due to the ability to discover the problem by detecting a side-effect (loss of new voltage readings), but without knowing the root cause the best that could be done would be to turn the pack off as a precaution.  This meant that after some arbitrary amount of time the pack would randomly shut off.&#x20;

Another major issue was that the temperature sensor on the board rose during use of the car, as current through the shunt and heat from the various ICs would heat the board up.  The solution was to use the less accurate LTC6803-3 temperature inputs which allowed us to use off-board thermistors.

Most of the issues during the bringup process for BMS were due to a combination of hardware and software issues.  Improving the design review process to avoid mistakes such as misrouted or unrouted lines to critical chips (like current sense, etc) would save a lot of time in terms of software debugging as well.

Race performance

Array Sensor Glitch

The array sensor was extremely noisy, which caused our algorithm to trip with a negative voltage fault as soon as we stepped on the accelerator.  This required periodic resetting of the battery pack to reactivate the array FET.  At the end of day 1, we fixed the problem by removing this fault condition.  Based on data analysis later, it's clear that we should have fixed the issue immediately instead of being more conservative with the software updates.  The extra power we would have gained, especially towards the end of the day when the current spikes had more of an impact as the array voltage was already low, was significant.

SOC

The tesla data was wrong due to their batteries being modified to exclude the PTC caps, which meant their internal resistance was lower than expected and caused our lift/sag predictions to be bad. &#x20;

Battery and current measurements were somewhat out of sync which caused lift/sag to be a bit worse than it should have been.

Suggestions for the future include better synchronize measurements (less of a big deal) and use better cruise control to limit the situations where this is a problem.  With close to constant current draw this won't be an issue in the future.

Remaining software

The rest of the pack seemed to work fine for the duration of the race.  We did not have any major issues.  The sensors worked as advertised.  The biggest improvements here could be in documentation and code commenting / style.  Given the number of rockstars consumed here over the summer this was obviously not an emphasis versus functionality, but should be in the future.

Conclusions

BPS this cycle was reliable during the race (with a couple of small issues) and did not result in the hindrance of the team in any notable way.  We got reasonably good data, including better state of charge data than ever before, but there is definite room for improvement (5% error over one cycle is fairly significant).

HMD

The HMD was inspired by three things - making an extremely awesome display system, making a display system that could also do rear-view, and making a display system that would work during a race.  Those goals were accomplished at the expense of another - power consumption.

For the design, we used a modified version of Angstrom Linux and configured the system to automatically boot to the HMD program, which received data over the serial port and output 800x600 VGA.

Major issues with the HMD included unreliable CAN->serial bridging due to a number of factors, the least of which is a microcontroller-depth serial buffer on the TI OMAP chips which does not play well with a complex operating system such as Linux.  The low capacity of these buffers meant that during a context switch away from say our CAN program, data could get dropped as the buffer would overflow.  Even with proper serial port configuration this was a major issue.  The suggestion is to switch to USB for future boards that use a Gumstix.

Power consumption was hurt substantially by the HDMI->VGA bridge that was necessary to use with the HMD.  This used almost a watt by itself.  In the future, we should use HDMI, Composite Video, or LVDS, all of which can be found more readily on embedded boards.

Telemetry

Telemetry for Xenith was inspired by two issues from the Apogee telemetry system.  The first was the low reliability of the Zigbee link and the telemetry systems' tendency to fail after relatively short periods of time.  The second was the reliance on an external USB receiver which had the tendency to be lost during critical moments by team members.

Significant debate occurred over the choice of using low-power WiFi for the telemetry system.  This was proven to be justified by objective testing - We used palm drive as an example and got approximately 0.6 mile range before notable signal degradation by using a large, high gain WiFi antenna on the receiver / wireless router.

The telemetry board was the first board to be brought up for Xenith and worked reasonably well.  For the architecture we chose to use a STM32 and a WiFly serial module.  In effect, the STM32 simply served to convert serial data to CAN and CAN data to serial.  This worked reasonably well, but we had a handful of issues that should be addressed in the next iteration.  First and foremost, there is at least one race condition in the telemetry software that causes packets on occasion to be stomped on by the next piece of incoming data.  This is a good opportunity to use FreeRTOS as then we will have validated locks and threading, which is a plus.  The contention on the shared data from both CAN and Serial interrupts likely caused the race condition.

Additionally, it would be good to have an accurate real time clock on the board so that we can sort packets in the database by transmitted time and not received time.  A GPS would also help for the purposes of location stamping our packets.

Light boards

* Set LED brightness based on messages from driver controlsUpdated state directly from CAN messagesControl blinker timing and coordinating hazardsProtect LEDs from overheatingTemperature sensor connected to an ADCOnly turn on temperature sensor when lights are onNot implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.Code was written by John Bolander, based on Apogee code by Ben Stabler
* Set LED brightness based on messages from driver controlsUpdated state directly from CAN messages
* Updated state directly from CAN messages
* Control blinker timing and coordinating hazards
* Protect LEDs from overheatingTemperature sensor connected to an ADCOnly turn on temperature sensor when lights are onNot implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.
* Temperature sensor connected to an ADC
* Only turn on temperature sensor when lights are on
* Not implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.
* Code was written by John Bolander, based on Apogee code by Ben Stabler
* Set LED brightness based on messages from driver controlsUpdated state directly from CAN messages
* Updated state directly from CAN messages
* Control blinker timing and coordinating hazards
* Protect LEDs from overheatingTemperature sensor connected to an ADCOnly turn on temperature sensor when lights are onNot implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.
* Temperature sensor connected to an ADC
* Only turn on temperature sensor when lights are on
* Not implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.
* Code was written by John Bolander, based on Apogee code by Ben Stabler

Set LED brightness based on messages from driver controls

* Updated state directly from CAN messages

Updated state directly from CAN messages

Control blinker timing and coordinating hazards

Protect LEDs from overheating

* Temperature sensor connected to an ADC
* Only turn on temperature sensor when lights are on
* Not implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.

Temperature sensor connected to an ADC

Only turn on temperature sensor when lights are on

Not implemented on Xenith; implemented by new members in Winter 2012, but not yet on the car.

Code was written by John Bolander, based on Apogee code by Ben Stabler

Kent display

The Kent display was a low power display that is essentially e-ink: the image persists after the power is turned off.

* Display state of battery pack in a easily accessible locationRemove the need to go through telemetry or open up the pack to get basic information about the state of the carRemove the need to turn the car on to get some basic informationCode was written by Rachel Fenichel
* Display state of battery pack in a easily accessible location
* Remove the need to go through telemetry or open up the pack to get basic information about the state of the car
* Remove the need to turn the car on to get some basic information
* Code was written by Rachel Fenichel
* Display state of battery pack in a easily accessible location
* Remove the need to go through telemetry or open up the pack to get basic information about the state of the car
* Remove the need to turn the car on to get some basic information
* Code was written by Rachel Fenichel

Display state of battery pack in a easily accessible location

Remove the need to go through telemetry or open up the pack to get basic information about the state of the car

Remove the need to turn the car on to get some basic information

Code was written by Rachel Fenichel

Technical details: Communicated with the Kent display over SPI; used DMA internally to manage SPI.  The kent display takes messages with an address and a byte of data to put in the next 8 bits: whether each should be on or off.  Fonts were generated as bitmaps and stored on the device for lookup--it would probably be less wasteful to not be storing all of the letters and characters in the alphabet, or to store only capital letters.  To simplify figuring out when to write consecutive bytes of memory, the Kent display MCU just keeps a memory map of all of the positions on the display and their values.  It updates this map when it needs to write more data, and continuously sends the data in the map to the Kent display until all updates have been sent out.  Again, this is wasteful.  It limited the size of the Kent display that the board would work with, because the MCU couldn't hold all of the data for larger displays.  One of the new members is currently working on updating this code and making it more flexible, as a way to work with SPI.

Driver controls

Overview:

Driver controls was the board that dealt with all the things that the driver touched.  It originally had one microcontroller on it.  We later changed it to have two microcontrollers: one to manage rear wheel steering, and the other to deal with everything else: speed of the car, lights, and audio.  Driver controls code was split roughly into two sections, of which only one part was truly new.  The rear wheel steering code and algorithms were built from scratch.  The primary problems with code were 1) calibrating responses to encoders and 2) pointer problems for sending messages to the Elmo which caused nondeterministic behaviour.  The more complex part of the project was algorithmic--in particular, managing transitions between the two steering modes.  These algorithms were roughly laid out during Winter Quarter 2011 by Rachel Fenichel and Nathan Hall-Snyder as a research project under Chris Gerdes.  They were later updated in response to testing on and off the car.  Ultimately they were made to be as simple as possible for safety, though more sophisticated behaviour may have been possible had the nondeterminism in the code been resolved earlier in the cycle.

Driver controls specifications:

* Read pedal inputs and button inputs and set speed of the car (in cruise control or out)There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.Read button inputs and send out messages to turn lights on and off(Extensions not implemented on the race): Manage audioSwitching between mp3 and radio output to driver headphonesNot implemented due to hardware problemsNoise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problemsThe audio side of driver controls was unpopulated during the raceControl rear wheel steeringChoose mode (dynamic or sailing) based on buttonsDo not allow the driver to change between modes in unsafe conditionsCommunicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel positionSet speed on rear wheel steering movementCode was written by Rachel Fenichel.  Tritium code was legacy code pulled in from Apogee, which may in turn have been pulled from older cars.Managing the cruise control PID loop on driver controls instead of letting the Tritium control it was discussed but never implementedNew members in Winter 2012 are currently working on this project
* Read pedal inputs and button inputs and set speed of the car (in cruise control or out)There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.
* There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.
* Read button inputs and send out messages to turn lights on and off
* (Extensions not implemented on the race): Manage audioSwitching between mp3 and radio output to driver headphonesNot implemented due to hardware problemsNoise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problemsThe audio side of driver controls was unpopulated during the race
* Switching between mp3 and radio output to driver headphonesNot implemented due to hardware problems
* Not implemented due to hardware problems
* Noise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problems
* Not implemented due to hardware and software problems
* The audio side of driver controls was unpopulated during the race
* Control rear wheel steeringChoose mode (dynamic or sailing) based on buttonsDo not allow the driver to change between modes in unsafe conditionsCommunicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel positionSet speed on rear wheel steering movement
* Choose mode (dynamic or sailing) based on buttons
* Do not allow the driver to change between modes in unsafe conditions
* Communicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel position
* Set speed on rear wheel steering movement
* Code was written by Rachel Fenichel.  Tritium code was legacy code pulled in from Apogee, which may in turn have been pulled from older cars.
* Managing the cruise control PID loop on driver controls instead of letting the Tritium control it was discussed but never implementedNew members in Winter 2012 are currently working on this project
* New members in Winter 2012 are currently working on this project
* Read pedal inputs and button inputs and set speed of the car (in cruise control or out)There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.
* There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.
* Read button inputs and send out messages to turn lights on and off
* (Extensions not implemented on the race): Manage audioSwitching between mp3 and radio output to driver headphonesNot implemented due to hardware problemsNoise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problemsThe audio side of driver controls was unpopulated during the race
* Switching between mp3 and radio output to driver headphonesNot implemented due to hardware problems
* Not implemented due to hardware problems
* Noise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problems
* Not implemented due to hardware and software problems
* The audio side of driver controls was unpopulated during the race
* Control rear wheel steeringChoose mode (dynamic or sailing) based on buttonsDo not allow the driver to change between modes in unsafe conditionsCommunicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel positionSet speed on rear wheel steering movement
* Choose mode (dynamic or sailing) based on buttons
* Do not allow the driver to change between modes in unsafe conditions
* Communicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel position
* Set speed on rear wheel steering movement
* Code was written by Rachel Fenichel.  Tritium code was legacy code pulled in from Apogee, which may in turn have been pulled from older cars.
* Managing the cruise control PID loop on driver controls instead of letting the Tritium control it was discussed but never implementedNew members in Winter 2012 are currently working on this project
* New members in Winter 2012 are currently working on this project

Read pedal inputs and button inputs and set speed of the car (in cruise control or out)

* There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.

There are encoders in each of the pedals to give the absolute positions of the pedals.  These send PWM signals to the board.

Read button inputs and send out messages to turn lights on and off

(Extensions not implemented on the race): Manage audio

* Switching between mp3 and radio output to driver headphonesNot implemented due to hardware problems
* Not implemented due to hardware problems
* Noise cancelling with two microphones for driver output to radioNot implemented due to hardware and software problems
* Not implemented due to hardware and software problems
* The audio side of driver controls was unpopulated during the race

Switching between mp3 and radio output to driver headphones

* Not implemented due to hardware problems

Not implemented due to hardware problems

Noise cancelling with two microphones for driver output to radio

* Not implemented due to hardware and software problems

Not implemented due to hardware and software problems

The audio side of driver controls was unpopulated during the race

Control rear wheel steering

* Choose mode (dynamic or sailing) based on buttons
* Do not allow the driver to change between modes in unsafe conditions
* Communicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel position
* Set speed on rear wheel steering movement

Choose mode (dynamic or sailing) based on buttons

Do not allow the driver to change between modes in unsafe conditions

Communicate with the Elmo to set the rear wheel position based on either button presses or the steering wheel position

Set speed on rear wheel steering movement

Code was written by Rachel Fenichel.  Tritium code was legacy code pulled in from Apogee, which may in turn have been pulled from older cars.

Managing the cruise control PID loop on driver controls instead of letting the Tritium control it was discussed but never implemented

* New members in Winter 2012 are currently working on this project

New members in Winter 2012 are currently working on this project

Technical details:  Driver controls has two MCUs.  The rear wheel steering MCU is the "Elmo MCU"; the other is the "Tritium MCU".  Both MCUs are on a single board so that they can share all of the button inputs, allowing buttons to be easily remapped.  In all other ways they act as though they were on separate boards: they communicate only over CAN, so there is no state that is shared between the two MCUs that is not shared with every other board on the CAN bus.  Each micro is also connected to a second CAN bus to the motor controller that it manages.  Switching to two microcontrollers also meant that utterly breaking one part of driver controls would leave the other part intact: for instance, once tritium code worked we could be confident that the car could still be driven even if the rear wheel steering code were broken.  We could merely disable rear wheel steering entirely if necessary.

Tritium Code

The code for talking to the Tritium was pulled from the Apogee driver controls and remains essentially untouched, with the exception of some additions for sending out light messages at the correct times.  The Tritium code and light code were essentially finished by the time we shipped to Australia.  (There may have been a problem with hazards when we first arrived in Darwin, but this was not a mission-critical problem.)  The speed that the Tritium reported (and the speed used for cruise control) was not entirely accurate because it was based on an inaccurate tire diameter.  This mean that the conversion from RPM to KPH was inaccurate, if predictably so.

Calibrating the pedals was a royal pain, and involved changing constants until the range was right.  They had to be recalibrated whenever the pedals were changed or repositioned.  This made one of our test drives pretty useless, because the calibration was wrong and the car kept kicking out of cruise control.

Elmo Code

The code for talking to the Elmo, and the algorithms for rear wheel steering, were completely new.  Rachel Fenichel and Nathan Hall-Snyder worked together on designing the algorithms for research units under Chris Gerdes in Winter 2011.  The algorithms continued to be updated as we understood more nuances about how the car would drive.  The last bugs in the Elmo side code were hammered out two days before the race.  During the race this code was unchanged except for constants related to the size of the tire.

Elmo CAN

Talking to the Elmo involved understanding the Elmo CAN protocol.  Once this layer was fully understood and set up it was not touched again: one could call ElmoSendMessage with arguments related to sending a new position and trust that the message would be set up and sent appropriately.

This almost worked, and worked well enough that it seemed that all messages were being sent.  But there were so many messages to send to set up a simple movement that it could overrun the three mailboxes on the STM32, and the solution to this was to make a bigger circular message buffer and send messages from that buffer whenever a new message could be sent.  This was implemented with pointer failures that were not caught until a code review in Darwin four days before the race; the buffer failures caused a lot of nondeterministic behaviour in the months leading up to the race, and would probably have been caught much earlier with a thorough code review earlier in the process.  Nondeterminism in a steering system is particularly bad, and the steering code was simplified over time in part because we could not seem to get rid of these potentially dangerous bugs.  Steering could probably have been more sophisticated if this bug had been caught earlier.

This also meant that messages with speed, etc. were sent every 100 ms or so instead of being sent once when they were changed, because we were never sure that the Elmo had actually received the messages the first time they were sent.

Rear wheel steering algorithms

There were two possible modes for rear wheel steering: dynamic, where the rear wheel would track the position of the steering wheel, and sailing, where the rear wheel's position could be set with buttons and would remain fixed regardless of what the steering wheel did.  The first mode allowed us to meet the turning radius requirement without movable fairings; the second allowed us to drive sideways into the wind.  Whether sailing was worthwhile is discussed elsewhere in this documentation.

The car always turned on to sailing mode.  This meant that the position of the rear wheel was completely deterministic on start-up.  Sailing mode and dynamic mode were each fairly easy to set up--the transition between the two was where most of the algorithmic work came in.

Sailing mode moved the rear wheel slowly--around five seconds per degree moved.  Dynamic mode moved the rear wheel as quickly as possible, because lag between the steering wheel and the rear wheel could cause us to fail the figure-eight test (and would be potentially dangerous).  One problem we encountered with making this code run quickly was that the STM32F107 does not have a built in float type.  This means that math involving decimals takes many clock cycles to run.  This was part of the reason to switch to two microcontrollers: so that the math involved in rear wheel steering would not lag out the tritium code.  The eventual solution to this problem was to use fixed-point math as much as possible; even so, some of the drivers reported noticeable lag.  (The programmer did not notice any such lag.) &#x20;

We tried to be lazy and avoid doing encoder math (which involved floats) unless the car was in dynamic mode.  This failed because it meant that the position that the rear wheel should go to when switching out of sailing was just the position it had been at before it entered sailing.

The transition from sailing to dynamic was problematic because it was possible for the rear wheel to be fixed all the way on one side of the range (e.g. all the way to the left) when the steering wheel position meant that it should be all the way to the right.  If the driver tried to switch from sailing to dynamic they needed to cover this entire range (the size of which would be unknown, because the driver could turn the steering wheel while it was transitioning) slowly enough to not throw the car around, but fast enough to eventually catch up to the steering wheel position.  This transition was never as smooth as we would have liked.  We tried a few different ways to get around this, including moving the wheel toward the steering wheel position at sailing speed (slowly) and constantly querying to see if the positions matched.  This failed, but it may have failed in part due to the buffer problems mentioned above.

Failsafes in the rear wheel steering system:

* The range of the rear wheel was limited to avoid encoder rollover, rather than trying to do faintly complicated math to deal with the rollover.The driver had to hold down the transition button for at least three seconds to switch from sailing mode to dynamic mode, and had to be below a certain speed limit.  It is a non-trivial endeavour to accidentally depress a button in the lower half of the steering wheel momentarily, let alone for three full secondsIt is possible to turn rear wheel steering off entirely, by sending a message to the battery pack to turn off power to the Elmo.  The button to do this is a toggle button, not a momentary switch.  It is possible to say if it is on or off either by looking at the button or by feeling whether it is depressed.  When rear wheel steering is turned back on it always turns on in sailing mode, which does not move the rear wheel.  Driver controls reads the position of the rear wheel on startup and uses that to set its internal state.The buttons for rear wheel steering were placed at the bottom of the steering wheel and on the side of the dashboard so that they are not easy to hit without the intention of doing so.The Elmo itself was designed so that the rear wheel steering actuator cannot be moved or turned unless the brake is powered.  This means that in the event of a complete power loss or power cycle the rear wheel is locked into its position at the moment of the power loss.  Additionally, the front wheels have a greater range of motion than the rear wheel, meaning that even if the rear wheel is completely locked to one side the driver can still drive straight, steer, and safely stop.The actuator's brake is always applied during sailing mode, unless the driver pressed a button telling the rear wheel to steer.  Then the brake stays off for the duration of that movement and a few seconds after it.  The brake is also turned off to save power.The code is written so that state changes are generally not considered permanent unless the Elmo has responded with a message acknowledging the change.The transitional mode was removed to make the behaviour of the car more predictable.We carefully tuned the speed at which the rear wheel is allowed to turn in sailing mode so that it is painfully slow at low speeds and slow enough to not throw the driver around at high speeds.  This also means that accidentally pressing a steering button at speed does not cause a fast twitch of the rear wheel
* The range of the rear wheel was limited to avoid encoder rollover, rather than trying to do faintly complicated math to deal with the rollover.
* The driver had to hold down the transition button for at least three seconds to switch from sailing mode to dynamic mode, and had to be below a certain speed limit.  It is a non-trivial endeavour to accidentally depress a button in the lower half of the steering wheel momentarily, let alone for three full seconds
* It is possible to turn rear wheel steering off entirely, by sending a message to the battery pack to turn off power to the Elmo.  The button to do this is a toggle button, not a momentary switch.  It is possible to say if it is on or off either by looking at the button or by feeling whether it is depressed.  When rear wheel steering is turned back on it always turns on in sailing mode, which does not move the rear wheel.  Driver controls reads the position of the rear wheel on startup and uses that to set its internal state.
* The buttons for rear wheel steering were placed at the bottom of the steering wheel and on the side of the dashboard so that they are not easy to hit without the intention of doing so.
* The Elmo itself was designed so that the rear wheel steering actuator cannot be moved or turned unless the brake is powered.  This means that in the event of a complete power loss or power cycle the rear wheel is locked into its position at the moment of the power loss.  Additionally, the front wheels have a greater range of motion than the rear wheel, meaning that even if the rear wheel is completely locked to one side the driver can still drive straight, steer, and safely stop.
* The actuator's brake is always applied during sailing mode, unless the driver pressed a button telling the rear wheel to steer.  Then the brake stays off for the duration of that movement and a few seconds after it.  The brake is also turned off to save power.
* The code is written so that state changes are generally not considered permanent unless the Elmo has responded with a message acknowledging the change.
* The transitional mode was removed to make the behaviour of the car more predictable.
* We carefully tuned the speed at which the rear wheel is allowed to turn in sailing mode so that it is painfully slow at low speeds and slow enough to not throw the driver around at high speeds.  This also means that accidentally pressing a steering button at speed does not cause a fast twitch of the rear wheel
* The range of the rear wheel was limited to avoid encoder rollover, rather than trying to do faintly complicated math to deal with the rollover.
* The driver had to hold down the transition button for at least three seconds to switch from sailing mode to dynamic mode, and had to be below a certain speed limit.  It is a non-trivial endeavour to accidentally depress a button in the lower half of the steering wheel momentarily, let alone for three full seconds
* It is possible to turn rear wheel steering off entirely, by sending a message to the battery pack to turn off power to the Elmo.  The button to do this is a toggle button, not a momentary switch.  It is possible to say if it is on or off either by looking at the button or by feeling whether it is depressed.  When rear wheel steering is turned back on it always turns on in sailing mode, which does not move the rear wheel.  Driver controls reads the position of the rear wheel on startup and uses that to set its internal state.
* The buttons for rear wheel steering were placed at the bottom of the steering wheel and on the side of the dashboard so that they are not easy to hit without the intention of doing so.
* The Elmo itself was designed so that the rear wheel steering actuator cannot be moved or turned unless the brake is powered.  This means that in the event of a complete power loss or power cycle the rear wheel is locked into its position at the moment of the power loss.  Additionally, the front wheels have a greater range of motion than the rear wheel, meaning that even if the rear wheel is completely locked to one side the driver can still drive straight, steer, and safely stop.
* The actuator's brake is always applied during sailing mode, unless the driver pressed a button telling the rear wheel to steer.  Then the brake stays off for the duration of that movement and a few seconds after it.  The brake is also turned off to save power.
* The code is written so that state changes are generally not considered permanent unless the Elmo has responded with a message acknowledging the change.
* The transitional mode was removed to make the behaviour of the car more predictable.
* We carefully tuned the speed at which the rear wheel is allowed to turn in sailing mode so that it is painfully slow at low speeds and slow enough to not throw the driver around at high speeds.  This also means that accidentally pressing a steering button at speed does not cause a fast twitch of the rear wheel

The range of the rear wheel was limited to avoid encoder rollover, rather than trying to do faintly complicated math to deal with the rollover.

The driver had to hold down the transition button for at least three seconds to switch from sailing mode to dynamic mode, and had to be below a certain speed limit.  It is a non-trivial endeavour to accidentally depress a button in the lower half of the steering wheel momentarily, let alone for three full seconds

It is possible to turn rear wheel steering off entirely, by sending a message to the battery pack to turn off power to the Elmo.  The button to do this is a toggle button, not a momentary switch.  It is possible to say if it is on or off either by looking at the button or by feeling whether it is depressed.  When rear wheel steering is turned back on it always turns on in sailing mode, which does not move the rear wheel.  Driver controls reads the position of the rear wheel on startup and uses that to set its internal state.

The buttons for rear wheel steering were placed at the bottom of the steering wheel and on the side of the dashboard so that they are not easy to hit without the intention of doing so.

The Elmo itself was designed so that the rear wheel steering actuator cannot be moved or turned unless the brake is powered.  This means that in the event of a complete power loss or power cycle the rear wheel is locked into its position at the moment of the power loss.  Additionally, the front wheels have a greater range of motion than the rear wheel, meaning that even if the rear wheel is completely locked to one side the driver can still drive straight, steer, and safely stop.

The actuator's brake is always applied during sailing mode, unless the driver pressed a button telling the rear wheel to steer.  Then the brake stays off for the duration of that movement and a few seconds after it.  The brake is also turned off to save power.

The code is written so that state changes are generally not considered permanent unless the Elmo has responded with a message acknowledging the change.

The transitional mode was removed to make the behaviour of the car more predictable.

We carefully tuned the speed at which the rear wheel is allowed to turn in sailing mode so that it is painfully slow at low speeds and slow enough to not throw the driver around at high speeds.  This also means that accidentally pressing a steering button at speed does not cause a fast twitch of the rear wheel

Rear wheel steering did not fail during the race.

Problems with this code:

It was really easy to remap the buttons, meaning that other drivers were not always aware of what the buttons did.  This was mostly true during testing in America, when we were experimenting with things like current controlled cruise control.  In Australia the button behaviours were standardized and there was a document emailed to all drivers, the team lead, and parts of the race team laying out what each button on the dash and steering wheel did.  The buttons were ultimately organized by colour: Green buttons governed lights (blinkers and headlights), white buttons governed the Tritium (reverse, cruise up, and cruise down), black buttons governed rear wheel steering (degree changes and mode changes), and the blue buttons were used in testing for current cruise control and entirely disabled on the race.

The Elmo was able to send out fault and error messages.  None of these were ever handled fully, but this was done knowingly.  Rachel Fenichel and Ben Stabler reviewed the list of fault and error codes and decided that most of the faults were related to operational modes that we were not moving, and the others were either irrelevant or would not occur due to the constraints of the car.  The main response to faults and errors would have been to forward those codes up through telemetry and let the strategy team decide about them.
