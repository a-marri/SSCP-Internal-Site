# electrical-fundamentals

## SSCP - Electrical Fundamentals

## Electrical Fundamentals

Thoughts After WSC2011

* If it isn't broken, don't fix it. Most of Xenith's electrical system works fine. We'll need to send out incremental revisions of some boards. We can also simplify: for example, our driver display can consist of a backlit 7-seg speed readout plus a tiny rearview cam screen. Our current electrical system draw about 20 watts quiescient, mostly due to the HUD and the Vicors; that needs to change.Also, we'll need to design in an easier way to test and debug systems. We should fix Ben's telemetry playback board. We shouldn't need BPS to test other boards on the car."Testing: last time we were going to put all of the electronics on Apogee and do a lot of testing. To my knowledge, this didn't happen early enough. The electrical team should build on the work on Xenith's electronics and test new revisions of the boards on Xenith until the new car is rolling."Paul sam and Bryant will build a better discharge modelAnalyze how contacts and welds of pack conductRamp up embedded codeHave a schedulerElectrical bug fix (duh)Code clean upRachel doesn't like writing over CAN. Sasha says to just have better functionality so it is easy to program over CAN. Then you can leave hardware in the vehicle and you can debug.Should freeze boards just like you freeze codeHave duplicates of boards. Even if you have to debug one board you can propagate the changes to the other boards.Put a test point on every rail and every signal, so you don't have to yellow wire in order to test your boardsHave all boards built so you can power logic over USB. No one wants to wait for the car to be available to test their boardsHave electronics be bench testableUse Phoenix A-coded connectorsDon't use micro-A USB for anythingMake good Phoenix to CAN adaptersBefore you send out a board with a new component you should take the physical component and make sure that the component will fit on the board and that the pins will fit. Just print out the board.Use a PID to control cruise controlRedo the Tridium's cruise controlGet a better battery modelHave two battery packs(Especially for electrical/code projects) Always keep a working copy of the project and write new code/test new hacks on a different copy.  That way a gamble or an attempt to implement the next feature doesn't stop the whole car from running.
* Paul sam and Bryant will build a better discharge model
* Analyze how contacts and welds of pack conduct
* Ramp up embedded code
* Have a scheduler
* Electrical bug fix (duh)
* Code clean up
* Rachel doesn't like writing over CAN. Sasha says to just have better functionality so it is easy to program over CAN. Then you can leave hardware in the vehicle and you can debug.
* Should freeze boards just like you freeze code
* Have duplicates of boards. Even if you have to debug one board you can propagate the changes to the other boards.
* Put a test point on every rail and every signal, so you don't have to yellow wire in order to test your boards
* Have all boards built so you can power logic over USB. No one wants to wait for the car to be available to test their boards
* Have electronics be bench testable
* Use Phoenix A-coded connectors
* Don't use micro-A USB for anything
* Make good Phoenix to CAN adapters
* Before you send out a board with a new component you should take the physical component and make sure that the component will fit on the board and that the pins will fit. Just print out the board.
* Use a PID to control cruise control
* Redo the Tridium's cruise control
* Get a better battery model
* Have two battery packs
* (Especially for electrical/code projects) Always keep a working copy of the project and write new code/test new hacks on a different copy.  That way a gamble or an attempt to implement the next feature doesn't stop the whole car from running.

If it isn't broken, don't fix it. Most of Xenith's electrical system works fine. We'll need to send out incremental revisions of some boards. We can also simplify: for example, our driver display can consist of a backlit 7-seg speed readout plus a tiny rearview cam screen. Our current electrical system draw about 20 watts quiescient, mostly due to the HUD and the Vicors; that needs to change.Also, we'll need to design in an easier way to test and debug systems. We should fix Ben's telemetry playback board. We shouldn't need BPS to test other boards on the car."Testing: last time we were going to put all of the electronics on Apogee and do a lot of testing. To my knowledge, this didn't happen early enough. The electrical team should build on the work on Xenith's electronics and test new revisions of the boards on Xenith until the new car is rolling."

* Paul sam and Bryant will build a better discharge model
* Analyze how contacts and welds of pack conduct
* Ramp up embedded code
* Have a scheduler
* Electrical bug fix (duh)
* Code clean up
* Rachel doesn't like writing over CAN. Sasha says to just have better functionality so it is easy to program over CAN. Then you can leave hardware in the vehicle and you can debug.
* Should freeze boards just like you freeze code
* Have duplicates of boards. Even if you have to debug one board you can propagate the changes to the other boards.
* Put a test point on every rail and every signal, so you don't have to yellow wire in order to test your boards
* Have all boards built so you can power logic over USB. No one wants to wait for the car to be available to test their boards
* Have electronics be bench testable
* Use Phoenix A-coded connectors
* Don't use micro-A USB for anything
* Make good Phoenix to CAN adapters
* Before you send out a board with a new component you should take the physical component and make sure that the component will fit on the board and that the pins will fit. Just print out the board.
* Use a PID to control cruise control
* Redo the Tridium's cruise control
* Get a better battery model
* Have two battery packs
* (Especially for electrical/code projects) Always keep a working copy of the project and write new code/test new hacks on a different copy.  That way a gamble or an attempt to implement the next feature doesn't stop the whole car from running.

Paul sam and Bryant will build a better discharge model

Analyze how contacts and welds of pack conduct

Ramp up embedded code

Have a scheduler

Electrical bug fix (duh)

Code clean up

Rachel doesn't like writing over CAN. Sasha says to just have better functionality so it is easy to program over CAN. Then you can leave hardware in the vehicle and you can debug.

Should freeze boards just like you freeze code

Have duplicates of boards. Even if you have to debug one board you can propagate the changes to the other boards.

Put a test point on every rail and every signal, so you don't have to yellow wire in order to test your boards

Have all boards built so you can power logic over USB. No one wants to wait for the car to be available to test their boards

Have electronics be bench testable

Use Phoenix A-coded connectors

Don't use micro-A USB for anything

Make good Phoenix to CAN adapters

Before you send out a board with a new component you should take the physical component and make sure that the component will fit on the board and that the pins will fit. Just print out the board.

Use a PID to control cruise control

Redo the Tridium's cruise control

Get a better battery model

Have two battery packs

(Especially for electrical/code projects) Always keep a working copy of the project and write new code/test new hacks on a different copy.  That way a gamble or an attempt to implement the next feature doesn't stop the whole car from running.
