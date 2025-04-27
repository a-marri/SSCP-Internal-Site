# bms-7-design-reviews-change-log

## SSCP - BMS 7 Design Reviews & Change Log

## BMS 7 Design Reviews & Change Log

Changes made between 7-1-1 and 7-1-2

The medium power module and CAN modules use 0603 components :(

LTC4218 footprint could be more narrow

Add another 5V0 testpoint near the processor

Add testpoints on LTC6803 side of isolation barrier

Alignment of 3d model and outline for NDS6D2405C is slightly off - causes interference with capacitors

Need to shift silkscreen on the low 6803’s 4.22k resistors

C51 is 0603

C42 could be moved farther from high voltage

R81/82 are 0603

Consolidate: 10 ohm, 4.22/4.3/4.7k ohm,

No need for R17 - already a 100ohm resistor inline

Add designators to all 6803 blocks of components

Change fans to just be a FET

add thermistor to BOM

update LTC4151 component so digikey link works

Change the Vicor Fuse to 5A so the capacitance on the vicor doesn’t blow it up

Relay footprint needs fixing!

Change precharge resistor to 500 ohm to keep below current limit of relay

Add more thermistors

Remove discharge resistor on high voltage to avoid the possibility of burning power after czonka shutoff during charging

Change the schottky diodes on the 6803-4 comm to ones with lower forward voltage

Change the 5v dc-dc isolators to tighter toleranced ones

Add diode to bypass the supercap when board is running, allowing slower charge rate of supercap

Changes made between 7-1-0 and 7-1-1

The board is no longer in a box.

Multiple Vicor footprints supported

All connectors are vertical due to space constraints

Added HVIL option to turn-on circuit

Change to LTC6803-4 + isolators

Fan controller added

Using medium power module to support CAN transceiver, supercap recharge

New Layout

Schematic re-organization

Review 5 - Schematics (changes + overall)

1/7/2013

Shoot for \~3mA on the LEDs for longevity

Add in Harry’s debounce chip to buttons

Change the buttons to be a larger tactile switch

Look for a normally closed opto that would be used on hv diode and 24v switch - check under SSR’s as well

Or, could have a pull-down with an opto pulling the pin up

Shoot for 3mA (697 ohms)

Concern: when shut off, the ideal diode will be turned off. This means the discharge resistor won’t discharge the MPPT capacitance

Solution: Put a depletion FET + discharge resistor on the array input (the anode side)

Look into using a NC SSR instead of the driver+fet

Consider reducing the discharge rate

Note: I put this circuit on ARR-!

Want <5s for discharge to get to less than 30V

Use a common mode choke on the 6803 input. Also the node after the ferrite beads and resistors should be shared

Note: let's double check all of this. Also, this puts AC and 33ohm DC impedance between the HV- and LT-, which I think is okay. Only current flowing is for sensing.

Consider a different style of cabling for edisc button so it can’t be plugged into can.

Use a digital isolator + usual I2C current sense to figure out the power consumption of my board.

&#x20;   Should I fuse or OC protect the current sense / power conversion / CAN supply?

&#x20;   Eliminated a 5V LDO for charging the supercap - powered off of this supply now.

&#x20;   Need to use a medium power module: 70mA CAN, 30mA current sense, 150mA (max) supercap charge current?

Use the latching bulgin button: MP0045/1E

Will use a resistor + small LED as indicator instead of high power LEDs

Generally good practice to put a cap on the data line AFTER the sending resistor (on the reading side). RC time constant should be 10-20x the bit rate

Zener diodes on power rail - only one needed per rail. Doesn’t matter where the zener goes, probably near the regulator.

For protecting against ESD - put the TVS close to the connector (if there are multiple parts) or close to the chip (if there is just one part) on the line. Use something like a SMC for the vicor protection

Let's check the TVS + FB on the output of the 24V bus, as well as the edisc LED

Add a ferrite bead going into the vicor. This would be impedance for Vicor

PUT CAP BACK ON VICOR!

Use the VI-J00 for lower quiescent (note: unless more space in the pack appears and I want to do a new layout, the old vicor footprint will stay. More pressure on the vicor replacement project :P

Put my own CAN module circuitry on the board for future proofing

Tie the shield to 24V’s GND on this board!

Charger: can plug into the motor controller port

Mark alignment pins “no plate”

25mil sufficient clearance for high voltage? Look at IEC spec: 23mil

ADC input choke is rotated 90 degrees

Use a low-power module for the 24-5 conversion because CAN \~10mA

Switch to the 6803-4 and power the LT chips each from an isolated supply. We're tired of tweaking the same input power circuit and the inter-chip comm problems. This also means that communication is isolated and the MCU doesn't have to sit on the same ground as the LT chips, removing the ground loop between LT- and HV-!

Self-imposed Changelog between BMS7.0.0 and BMS7.1.0 (items not crossed out were suggested in design review)

Schematic Additions

Add kickback diode to czonka coil

Add current sense on the input of the 24 to +/-5v regulator so we know how much current this board draws? Or different part?

&#x20;           Use a digital isolator + usual I2C current sense to figure out the power consumption of my board.

Add a second ring terminal on +/- for motor controllers

Testpoint on 5v0, more testpoints on GND

TVS diode at every IC, as well as lines that exit the pack.

Add a 100ohm resistor on the output of the LT chip’s MISO line. Should go on right side

&#x20;           Generally good practice to put a cap on the data line AFTER the sending resistor (on the reading side). RC time constant should be 10-20x the bit rate

LED on each power rail

&#x20;           Shoot for \~3mA on the LEDs for longevity

A few buttons

&#x20;               Add in Harry’s debounce chip to buttons

&#x20;            Change the buttons to be a larger tactile switch

Schematic Changes

Anode and cathode of ideal diode swapped

Change all FET designators to Q (instead of U)

Depletion mode FET on the enable line for the 24v switch and HV ideal diode so it defaults to off

BSS159N H6906CT-ND

(used a normal FET inline with 24v line to avoid startup/retry issues. Same number of parts as a depletion switch)

&#x20;               Look for a normally closed opto that would be used on hv diode and 24v switch - check under SSR’s as well

&#x20;       Or, could have a pull-down with an opto pulling the pin up

PC comparator IN+ and IN- swapped

Use a TO-247 resistor for the precharge. Also change the precharge resistor to be a standard resistor

&#x20;           Want <5s for discharge to get to less than 30V

High voltage power path - precharge DIRECTLY across contactor

Place fuses immediately after the connector - so the LT chip power is fused. Change to \~250mA fuse

Bleed: want an efficiency figure on LEDs to see if it’s actually beneficial. Also, should have some resistor in case the LED fails short.

&#x20;           Will use a resistor + small LED as indicator instead of high power LEDs

Remove the backup battery and replace with FRAM?

Use smaller testpoints

Use CAN transceiver + regulator instead of modules?

&#x20;           Put my own CAN module circuitry on the board for future proofing

Delete R14 on LT chip power?

&#x20;           No need for it, but will keep for the pads.

Supply decoupling on both + and - of 6803, clamp V+ and V- of 6803

&#x20;           Use a common mode choke on the 6803 input. Also the node after the ferrite beads and resistors should be shared

Do anything with the shield on the CAN cabling?

&#x20;           Tie the shield to 24V’s GND on this board!

Pick a higher voltage supercap in order for the VGS of edisc circuit and the forward drop of optodriver to never be too low? (5V, P11342-ND)

Any connection on the board for charger? Or just on the output of the czonka?

Footprint Changes

Connectors - should the through holes without connectivity have any plating? How to do this?

Make sure all components are 0805 (except in bleed circuit perhaps)

1206 capacitors on the analog LDO’s should be changed

Fix fuse footprint soldermask

USB connector wrong

LTC6082 footprint may be too wide

AND gate footprint is too large for the part that was ordered

Diodes between the 6803’s are quite small. No need for this

Shunts should have less space between pad edge and shunt

TVS and C6 on bleed circuit have no soldermask cutout! Should use something slightly larger anyway.

LED footprint indicates that the notch on the corner should go toward the dot. it’s backwards if this is the case.

Changed zeners on ltc4359 to be smaller package and higher voltage

Ordering Changes

Standardize 0.1uF and 100nF capacitors when ratings are the same

Change edisc override switch to an in-stock part

Add screws + mounting holes as parts

Add mating connectors + contacts to schematics

Add MX connector front cap plug as well

Layout Changes

Think more about 6803 routing

Move pushbutton from high voltage section

Change from 50mil to 25mil HV clearance?

C0 Kelvin connection

Make a clear note that a cable using 39 wires straight through should not be plugged in, or shorting would result because of the thermistors!

Concern: when shut off, the ideal diode will be turned off. This means the discharge resistor won’t discharge the MPPT capacitance

Solution: Put a depletion FET + discharge resistor on the array input (the anode side)

Consider a different style of cabling for edisc button so it can’t be plugged into can.

Zener diodes on power rail - only one needed per rail. Doesn’t matter where the zener goes, probably near the regulator.

For protecting against ESD - put the TVS close to the connector (if there are multiple parts) or close to the chip (if there is just one part) on the line. Use something like a SMC for the vicor protection

&#x20;       Add a ferrite bead going into the vicor. This would be impedance for Vicor

Use the VI-J00 for lower quiescent

Review 4 - Schematics

9/16/2012

Isolation Boundaries - consider drawing only through power supplies that generate an isolation boundary

Power Module - note: should make the schematic symbol as descriptve as possible, so note the voltage there

24v net class - may not be necessary for such a low voltage (i.e. the normal 6mil minimum may be enough). Use these spacings: http://www.smpspowersupply.com/ipc2221pcbclearance.html

[http://www.smpspowersupply.com/ipc2221pcbclearance.html](http://www.smpspowersupply.com/ipc2221pcbclearance.html)

Reference

&#x20;   With Sasha's suggested LT1461, can put an RC on the input and run off the 5v supply.&#x20;

&#x20;   Opted to use the LT6655 because it has a better PSRR at low frequencies (by nearly 30 dB).

HV Precharge

&#x20;   Can use the 436x series for the gate charge pump SPICE model

&#x20;   Check on Figure 11 - 2k between OUT and the chip. Zener clamping OUT to VSS

&#x20;   Right now, I'm overpowering R98. Can either make it larger or make the zener drop larger. 147^2/100k = .2W, which is too much for the 0805

&#x20;   Zener vs TVS - TVS has less capacitance and is faster. Zeners are more precise but have more leakage. For D27, use TVS, for D28/29, use Zener

&#x20;   Consider using the resistor/diode/cap combo on figure 11. Not sure what it's there for...but it can't hurt to include? More research required.

Analog

&#x20;   Can't use a tantalum cap on the analog input - current flows in both directions on the shunt, no way to prevent reverse voltage on the cap.

&#x20;   C0G NP0 cap (http://www.tdk.com/pdf/automotive\_B11.pdf, 445-6947-1-ND) is very stable w.r.t. to piezoelectric effect. A film cap (399-6387-1-ND) would also work

[http://www.tdk.com/pdf/automotive\_B11.pdf](http://www.tdk.com/pdf/automotive_B11.pdf)

&#x20;   At 80% of the rated voltage, a ceramic cap can be as little as 20% of their rated capacitance. Film cap will be much more stable. Most ideal type of capacitor, but more expensive and larger. Try to use ceramics at half their rated voltage

6803

&#x20;   Better-specified zener for the turn-off circuit: try Comchip parts, like http://www.comchiptech.com/cms/UserFiles/CZRU52C2%20THRU%20CZRU52C39-RevB.pdf, or MicroCommercial, like http://61.222.192.61/mccsemi/up\_pdf/MMSZ5221-MMSZ5259(SOD123).pdf

[http://www.comchiptech.com/cms/UserFiles/CZRU52C2%20THRU%20CZRU52C39-RevB.pdf](http://www.comchiptech.com/cms/UserFiles/CZRU52C2%20THRU%20CZRU52C39-RevB.pdf)

[http://61.222.192.61/mccsemi/up\_pdf/MMSZ5221-MMSZ5259(SOD123).pdf](http://61.222.192.61/mccsemi/up_pdf/MMSZ5221-MMSZ5259\(SOD123\).pdf)

&#x20;   HV- is the vicor negative side. LT- will be the logic ground. Since the opamp of the ADC has such enormous impedance, even though the diagram technically has a ground loop, no current flows because of this impedance. In layout, since HV- and LT- are named differently, I won't actually connect them on the board. But they'll be at the same potential.&#x20;

&#x20;   Turn-on switch: doesn't matter what I use. A BJT has lower leakage, so I'll go with that. Find a BJT with leakage listed?

&#x20;   RENAME EVERYTHING TO LT-, except for the VICOR (as HV-)

&#x20;   Two Red LEDs in series may be the most efficient and not need a resistor. Check this!!

24v Switch

&#x20;   Recalculate voltage at UV, OV, FB pin and make note on schematic

&#x20;   Note that auto-retry is disabled

Turn-on

&#x20;   Make the zener always connected to the cathode of the turn-on optodriver. Also, a TVS is the proper part here. Put TVS from K to GND, and then maybe a 10 ohm resistor in series with EDISC\_TOP so the TVS is current-limited

Czonka

&#x20;   Will draw 5A on start-up. No need for a fuse - the vicor is output protected. The point of the 24v switch is to prevent a cascading failure from turning off BMS.

&#x20;   An AND gate is fine now that we've settled on the functionality of the circuit. Try this push-pull one: http://www.digikey.com/product-detail/en/SN74LVC1G08DCKR/296-11602-1-ND/385741

[http://www.digikey.com/product-detail/en/SN74LVC1G08DCKR/296-11602-1-ND/385741](http://www.digikey.com/product-detail/en/SN74LVC1G08DCKR/296-11602-1-ND/385741)

Precharge

&#x20;   Resistor for discharge, NTC with fuse (10A, slow-blow) for precharge

&#x20;   Can use PB1271-ND and not need an isolated switch! Put a pull-down resistor on the gate of the FET.

PC Check

&#x20;   Switch the Vicor on the high side, measure BATT+ after the switch so the pack is not always draining

&#x20;   Use 0.1% resistors for the dividers

&#x20;   R61 does nothing but waste power

&#x20;   Comparator is open drain...FAIL. Have a pull-up resistor instead of pull-down.

&#x20;   On the buffer - size the inputs to the opamp for 3.0v so I don't go too close to the rail.

Vicor

&#x20;   Size for the 1/4 brick Vicor - they are more efficient, leaves more room for the replacement

&#x20;   The EMI capacitors should connect to the base plate. Could use a pogo pin to connect to the base plate.&#x20;

Buzzer&#x20;

&#x20;   Put a 10-100k resistor on the gate of the FET even though I'll configure them as pull-downs

Review 3 - Schematics

9/11/2012

Schematics at the time of review are attached below under "bms\_7\_review\_3.pdf"

* naming - MC shunt, array shunt, etc...isolation - medium dashed line, blackLook into a different way to power the analog circuitry    Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails   Look at TDK and CUIAsk Sasha about the reference he uses - mine has some temperature drift5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.    Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)    Need an optocoupler to short between SHDN and VSS, not SHDN and GND    Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents    Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulatorAnalog page    Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)    Consider a tantalum cap on the input    Bypass the reference with a tantalum cap at the input of the chip    (Don't have ceramic capacitors on the reference because of piezoelectric effect)    Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHzLTC6803    Fix the JAE connector for the cells    Note: 50V between temp inputs may be pushing it. Probably OK between female pins    D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately    No reason for the PFET to be smaller than the abs max of the LTC6803    Could use a BJT instead of an optocoupler. But going to leave it.    Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat    Investigate     Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-Resistors - use 1% everywhere because it doesn't cost any more24v switch    Go ahead and connect the zero current reference    ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum    Ground the FAULT\_EN pin    Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4ATurn-on    Put a zener on the top shell edisc line - cathode can go very highCzonka fuse    500ma will blow up because of inrush    Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)    Put the 24v net on the other nets that have higher voltage    NAND gate - strange choice not to use a push-pull drive. Precharge    Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus    Also have HV indicator just below the fuse    Write the percentages on the schematic    Don't connect directly to BATT- - use both sides of the precharge resistor.    No reason to have the fusePiezo    Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create     Consider a magnetic buzzer so I can have a wider frequency responseFan    Rules don't say I need it, but it's worth keepingVicor    To just have pads for the resistors, uncheck the "fitted" box    Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)    Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-. MCU    Add small ceramic to the RTC battery    Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp    FIX THE DIGIT DISPLAY PFETS!!!!STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch
* isolation - medium dashed line, blackLook into a different way to power the analog circuitry    Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails   Look at TDK and CUIAsk Sasha about the reference he uses - mine has some temperature drift5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.    Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)    Need an optocoupler to short between SHDN and VSS, not SHDN and GND    Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents    Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulatorAnalog page    Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)    Consider a tantalum cap on the input    Bypass the reference with a tantalum cap at the input of the chip    (Don't have ceramic capacitors on the reference because of piezoelectric effect)    Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHzLTC6803    Fix the JAE connector for the cells    Note: 50V between temp inputs may be pushing it. Probably OK between female pins    D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately    No reason for the PFET to be smaller than the abs max of the LTC6803    Could use a BJT instead of an optocoupler. But going to leave it.    Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat    Investigate     Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-Resistors - use 1% everywhere because it doesn't cost any more24v switch    Go ahead and connect the zero current reference    ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum    Ground the FAULT\_EN pin    Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4ATurn-on    Put a zener on the top shell edisc line - cathode can go very highCzonka fuse    500ma will blow up because of inrush    Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)    Put the 24v net on the other nets that have higher voltage    NAND gate - strange choice not to use a push-pull drive. Precharge    Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus    Also have HV indicator just below the fuse    Write the percentages on the schematic    Don't connect directly to BATT- - use both sides of the precharge resistor.    No reason to have the fusePiezo    Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create     Consider a magnetic buzzer so I can have a wider frequency responseFan    Rules don't say I need it, but it's worth keepingVicor    To just have pads for the resistors, uncheck the "fitted" box    Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)    Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-. MCU    Add small ceramic to the RTC battery    Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp    FIX THE DIGIT DISPLAY PFETS!!!!STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch
* Look into a different way to power the analog circuitry
* &#x20;   Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails
* &#x20;  Look at TDK and CUI
* Ask Sasha about the reference he uses - mine has some temperature drift
* 5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.
* &#x20;   Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)
* &#x20;   Need an optocoupler to short between SHDN and VSS, not SHDN and GND
* &#x20;   Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents
* &#x20;   Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulator
* Analog page
* &#x20;   Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)
* &#x20;   Consider a tantalum cap on the input
* &#x20;   Bypass the reference with a tantalum cap at the input of the chip
* &#x20;   (Don't have ceramic capacitors on the reference because of piezoelectric effect)
* &#x20;   Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHz
* LTC6803
* &#x20;   Fix the JAE connector for the cells
* &#x20;   Note: 50V between temp inputs may be pushing it. Probably OK between female pins
* &#x20;   D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately
* &#x20;   No reason for the PFET to be smaller than the abs max of the LTC6803
* &#x20;   Could use a BJT instead of an optocoupler. But going to leave it.
* &#x20;   Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat
* &#x20;   Investigate&#x20;
* &#x20;   Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-
* Resistors - use 1% everywhere because it doesn't cost any more
* 24v switch
* &#x20;   Go ahead and connect the zero current reference
* &#x20;   ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum
* &#x20;   Ground the FAULT\_EN pin
* &#x20;   Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4A
* Turn-on
* &#x20;   Put a zener on the top shell edisc line - cathode can go very high
* Czonka fuse
* &#x20;   500ma will blow up because of inrush
* &#x20;   Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)
* &#x20;   Put the 24v net on the other nets that have higher voltage
* &#x20;   NAND gate - strange choice not to use a push-pull drive.&#x20;
* Precharge
* &#x20;   Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus
* &#x20;   Also have HV indicator just below the fuse
* &#x20;   Write the percentages on the schematic
* &#x20;   Don't connect directly to BATT- - use both sides of the precharge resistor.
* &#x20;   No reason to have the fuse
* Piezo
* &#x20;   Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create&#x20;
* &#x20;   Consider a magnetic buzzer so I can have a wider frequency response
* Fan
* &#x20;   Rules don't say I need it, but it's worth keeping
* Vicor
* &#x20;   To just have pads for the resistors, uncheck the "fitted" box
* &#x20;   Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)
* &#x20;   Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-.&#x20;
* MCU
* &#x20;   Add small ceramic to the RTC battery
* &#x20;   Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp
* &#x20;   FIX THE DIGIT DISPLAY PFETS!!!!
* STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch

naming - MC shunt, array shunt, etc...

* isolation - medium dashed line, blackLook into a different way to power the analog circuitry    Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails   Look at TDK and CUIAsk Sasha about the reference he uses - mine has some temperature drift5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.    Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)    Need an optocoupler to short between SHDN and VSS, not SHDN and GND    Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents    Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulatorAnalog page    Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)    Consider a tantalum cap on the input    Bypass the reference with a tantalum cap at the input of the chip    (Don't have ceramic capacitors on the reference because of piezoelectric effect)    Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHzLTC6803    Fix the JAE connector for the cells    Note: 50V between temp inputs may be pushing it. Probably OK between female pins    D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately    No reason for the PFET to be smaller than the abs max of the LTC6803    Could use a BJT instead of an optocoupler. But going to leave it.    Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat    Investigate     Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-Resistors - use 1% everywhere because it doesn't cost any more24v switch    Go ahead and connect the zero current reference    ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum    Ground the FAULT\_EN pin    Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4ATurn-on    Put a zener on the top shell edisc line - cathode can go very highCzonka fuse    500ma will blow up because of inrush    Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)    Put the 24v net on the other nets that have higher voltage    NAND gate - strange choice not to use a push-pull drive. Precharge    Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus    Also have HV indicator just below the fuse    Write the percentages on the schematic    Don't connect directly to BATT- - use both sides of the precharge resistor.    No reason to have the fusePiezo    Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create     Consider a magnetic buzzer so I can have a wider frequency responseFan    Rules don't say I need it, but it's worth keepingVicor    To just have pads for the resistors, uncheck the "fitted" box    Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)    Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-. MCU    Add small ceramic to the RTC battery    Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp    FIX THE DIGIT DISPLAY PFETS!!!!STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch
* Look into a different way to power the analog circuitry
* &#x20;   Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails
* &#x20;  Look at TDK and CUI
* Ask Sasha about the reference he uses - mine has some temperature drift
* 5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.
* &#x20;   Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)
* &#x20;   Need an optocoupler to short between SHDN and VSS, not SHDN and GND
* &#x20;   Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents
* &#x20;   Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulator
* Analog page
* &#x20;   Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)
* &#x20;   Consider a tantalum cap on the input
* &#x20;   Bypass the reference with a tantalum cap at the input of the chip
* &#x20;   (Don't have ceramic capacitors on the reference because of piezoelectric effect)
* &#x20;   Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHz
* LTC6803
* &#x20;   Fix the JAE connector for the cells
* &#x20;   Note: 50V between temp inputs may be pushing it. Probably OK between female pins
* &#x20;   D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately
* &#x20;   No reason for the PFET to be smaller than the abs max of the LTC6803
* &#x20;   Could use a BJT instead of an optocoupler. But going to leave it.
* &#x20;   Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat
* &#x20;   Investigate&#x20;
* &#x20;   Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-
* Resistors - use 1% everywhere because it doesn't cost any more
* 24v switch
* &#x20;   Go ahead and connect the zero current reference
* &#x20;   ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum
* &#x20;   Ground the FAULT\_EN pin
* &#x20;   Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4A
* Turn-on
* &#x20;   Put a zener on the top shell edisc line - cathode can go very high
* Czonka fuse
* &#x20;   500ma will blow up because of inrush
* &#x20;   Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)
* &#x20;   Put the 24v net on the other nets that have higher voltage
* &#x20;   NAND gate - strange choice not to use a push-pull drive.&#x20;
* Precharge
* &#x20;   Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus
* &#x20;   Also have HV indicator just below the fuse
* &#x20;   Write the percentages on the schematic
* &#x20;   Don't connect directly to BATT- - use both sides of the precharge resistor.
* &#x20;   No reason to have the fuse
* Piezo
* &#x20;   Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create&#x20;
* &#x20;   Consider a magnetic buzzer so I can have a wider frequency response
* Fan
* &#x20;   Rules don't say I need it, but it's worth keeping
* Vicor
* &#x20;   To just have pads for the resistors, uncheck the "fitted" box
* &#x20;   Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)
* &#x20;   Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-.&#x20;
* MCU
* &#x20;   Add small ceramic to the RTC battery
* &#x20;   Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp
* &#x20;   FIX THE DIGIT DISPLAY PFETS!!!!
* STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch

isolation - medium dashed line, black

* Look into a different way to power the analog circuitry
* &#x20;   Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails
* &#x20;  Look at TDK and CUI
* Ask Sasha about the reference he uses - mine has some temperature drift
* 5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.
* &#x20;   Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)
* &#x20;   Need an optocoupler to short between SHDN and VSS, not SHDN and GND
* &#x20;   Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents
* &#x20;   Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulator
* Analog page
* &#x20;   Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)
* &#x20;   Consider a tantalum cap on the input
* &#x20;   Bypass the reference with a tantalum cap at the input of the chip
* &#x20;   (Don't have ceramic capacitors on the reference because of piezoelectric effect)
* &#x20;   Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHz
* LTC6803
* &#x20;   Fix the JAE connector for the cells
* &#x20;   Note: 50V between temp inputs may be pushing it. Probably OK between female pins
* &#x20;   D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately
* &#x20;   No reason for the PFET to be smaller than the abs max of the LTC6803
* &#x20;   Could use a BJT instead of an optocoupler. But going to leave it.
* &#x20;   Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat
* &#x20;   Investigate&#x20;
* &#x20;   Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-
* Resistors - use 1% everywhere because it doesn't cost any more
* 24v switch
* &#x20;   Go ahead and connect the zero current reference
* &#x20;   ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum
* &#x20;   Ground the FAULT\_EN pin
* &#x20;   Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4A
* Turn-on
* &#x20;   Put a zener on the top shell edisc line - cathode can go very high
* Czonka fuse
* &#x20;   500ma will blow up because of inrush
* &#x20;   Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)
* &#x20;   Put the 24v net on the other nets that have higher voltage
* &#x20;   NAND gate - strange choice not to use a push-pull drive.&#x20;
* Precharge
* &#x20;   Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus
* &#x20;   Also have HV indicator just below the fuse
* &#x20;   Write the percentages on the schematic
* &#x20;   Don't connect directly to BATT- - use both sides of the precharge resistor.
* &#x20;   No reason to have the fuse
* Piezo
* &#x20;   Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create&#x20;
* &#x20;   Consider a magnetic buzzer so I can have a wider frequency response
* Fan
* &#x20;   Rules don't say I need it, but it's worth keeping
* Vicor
* &#x20;   To just have pads for the resistors, uncheck the "fitted" box
* &#x20;   Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)
* &#x20;   Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-.&#x20;
* MCU
* &#x20;   Add small ceramic to the RTC battery
* &#x20;   Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp
* &#x20;   FIX THE DIGIT DISPLAY PFETS!!!!
* STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch

Look into a different way to power the analog circuitry

&#x20;   Consider using an off the shelf module as opposed to a power module. Would proivde +/- rails

&#x20;  Look at TDK and CUI

Ask Sasha about the reference he uses - mine has some temperature drift

5-15 mF capacitance on the HV bus is the most I should expect. Sam's trackers are 2mF a piece, Tritium is 560uF.

&#x20;   Do some LTspice with this part, do math on how long it should take to turn on. Don't allow current to above 1/3 the external lead current (i.e. \~50A peak current)

&#x20;   Need an optocoupler to short between SHDN and VSS, not SHDN and GND

&#x20;   Try finding a zener for D26 that won't suck all the gate current. Look for a zener that is specified at very small currents

&#x20;   Look at the 200V schematic in the LT datasheet for vss resistor and the shunt regulator

Analog page

&#x20;   Use RCR filter, like before. Make sure that the corner of this filter is well below the internal sampling frequency of the sigma delta (100 ohms, 10nF, something like that)

&#x20;   Consider a tantalum cap on the input

&#x20;   Bypass the reference with a tantalum cap at the input of the chip

&#x20;   (Don't have ceramic capacitors on the reference because of piezoelectric effect)

&#x20;   Read the datasheet to see if I can use MCO to drive the ADC at 1-4.5MHz

LTC6803

&#x20;   Fix the JAE connector for the cells

&#x20;   Note: 50V between temp inputs may be pushing it. Probably OK between female pins

&#x20;   D5, etc should be rated for full pack voltage. Check on D4 - check zener voltage at low current. Check on the low current performance of the zener, size the resistors appropriately

&#x20;   No reason for the PFET to be smaller than the abs max of the LTC6803

&#x20;   Could use a BJT instead of an optocoupler. But going to leave it.

&#x20;   Use one large blue LED on the bleed circuit (possibly on the back side of the board) - very efficient, least amount of power burned in heat

&#x20;   Investigate&#x20;

&#x20;   Eliminate isolated supply and isolator. All of the logic ground will change to LT-. Perhaps put parallel and opposite diodes between HV- and LT-

Resistors - use 1% everywhere because it doesn't cost any more

24v switch

&#x20;   Go ahead and connect the zero current reference

&#x20;   ACS716 needs at least a 10k ohm load (so use a 2.2-4.7 so i'm not at the minimum

&#x20;   Ground the FAULT\_EN pin

&#x20;   Because the ISET pin is open, there is a 15mV limit - size the shunt to allow 4A

Turn-on

&#x20;   Put a zener on the top shell edisc line - cathode can go very high

Czonka fuse

&#x20;   500ma will blow up because of inrush

&#x20;   Sam likes vertical mount fuses from Schurter - saves board area. (http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)

[http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958](http://www.digikey.com/product-detail/en/3101.0040/486-1159-ND/1522958)

&#x20;   Put the 24v net on the other nets that have higher voltage

&#x20;   NAND gate - strange choice not to use a push-pull drive.&#x20;

Precharge

&#x20;   Put pads for this http://www.ametherm.com/datasheetspdf/SL2212103.pdf in parallel with my resistors - can precharge at a more constant current .Size the energy of the NTC at about twice the energy stored in the HV bus

[http://www.ametherm.com/datasheetspdf/SL2212103.pdf](http://www.ametherm.com/datasheetspdf/SL2212103.pdf)

&#x20;   Also have HV indicator just below the fuse

&#x20;   Write the percentages on the schematic

&#x20;   Don't connect directly to BATT- - use both sides of the precharge resistor.

&#x20;   No reason to have the fuse

Piezo

&#x20;   Need the protection resistor? make it a 10 ohm resistor. But put a TVS there because the piezo could create&#x20;

&#x20;   Consider a magnetic buzzer so I can have a wider frequency response

Fan

&#x20;   Rules don't say I need it, but it's worth keeping

Vicor

&#x20;   To just have pads for the resistors, uncheck the "fitted" box

&#x20;   Look at the recommended circuit for minimized EMI. (see Vicor Application Notes)

[Vicor Application Notes](http://www.vicorpower.com/cms/home/technical_resources/applications-information)

&#x20;   Put a high voltage capacitor between IN+ and OUT+ plus IN- and OUT-.&#x20;

MCU

&#x20;   Add small ceramic to the RTC battery

&#x20;   Opamp - Can do even better in terms of input bias current. Use the LTC6082 (quad), can put the comparator after the opamp and use any opamp

&#x20;   FIX THE DIGIT DISPLAY PFETS!!!!

STM pins - put a pull resistor to set the startup state and prevent jitter. I.e. pull-down on the czonka enable switch

Review 2 - Schematics

9/4/2012

Below is a list of suggested changes from the review with Sasha. The schematics at the time of review are attached under "bms\_7\_review\_2.pdf".

* Perhaps use a repeated schematic for the LT bleeder circuit using net ties
* Check thermistor values - lower (10k as opposed to 100k) is better for noise
* Isolated switch: use 390 ohm resistor for current limit. Also fix this in the array switch schematic.
* Analog block - just duplicate 4x to avoid compile errors with the buses
* Schematic block names - such as "pmic\_3v3"
* Consider WSMS2906 from Vishay - PEM studs can be mounted through the board and the shunt, meaning that separate shunt and mounting holes are note required.These have a 75 ppm/C accuracy, as opposed to the originally specified 15 ppm/C shunts. They will also take up more board real estate
* These have a 75 ppm/C accuracy, as opposed to the originally specified 15 ppm/C shunts. They will also take up more board real estate
* If temperature coefficient is a concern, perhaps put some thermistors in terminal lugs to measure the temperature
* OK to create a connector that will break out spare pins on the MCU for hacking/debugging
* Good schematic style: draw a dotted line in the top level schematic showing isolation boundaries
* Analog power block - Sasha: power supplies are failure generators. Eliminating supplies eliminates failures.Double check that the Recom supply can provide enough current to the regulatorsFerrite bead between analog and digital suppliesDon't collapse the positive and negative LDOs into one sheet - make a separate block for eachConsider the TI ADC as it is more modern and requires fewer power supplies. Ideally there would be one with 3.0v analog and 3.3v digital, to eliminate power supplies
* Double check that the Recom supply can provide enough current to the regulators
* Ferrite bead between analog and digital supplies
* Don't collapse the positive and negative LDOs into one sheet - make a separate block for each
* Consider the TI ADC as it is more modern and requires fewer power supplies. Ideally there would be one with 3.0v analog and 3.3v digital, to eliminate power supplies
* Consistency in naming: change "VIN+" to "VIN"
* Power moduleUse a 550kOhm feedback resistor. This should be double-checked once assembledDon't need an output capacitor on the power module. The Schottky diode is good, though.Check the schematic part! There should be two V+ pins
* Use a 550kOhm feedback resistor. This should be double-checked once assembled
* Don't need an output capacitor on the power module. The Schottky diode is good, though.
* Check the schematic part! There should be two V+ pins
* Array switchWe did some SPICE, a 1uF capacitor on the gate should make the peak current through the FETs lower.Precharging with the FET is possible because the PV FET Driver is a current source, outputting a very small current when shorted.
* We did some SPICE, a 1uF capacitor on the gate should make the peak current through the FETs lower.
* Precharging with the FET is possible because the PV FET Driver is a current source, outputting a very small current when shorted.
* AnalogRemove R1 from the analog page - it doesn't do anything except turn off the level translatorLevel translator: extreme schematic drawing fail...nothing lines up. LOL.Use 100nF bypass capacitor on each side of the translator. 100nF should be the default bypass capacitor valueUse the MCO output on the F4, assuming that the ADC will run properly on 8MHz. This way, the HSE can be configured to output as a square wave on the MCO pin.Common mode ferrite bead is ideal for the ADC input, rather than two separate beads. Something like this is good. Maybe also use this on the CAN lines in differential configuration?Put a 100nF capacitor across VSS and AVDD. Also a 100nF on digital supply pinJust use a single analog reference - fewer parts required, and you are only calibrating against one reference
* Remove R1 from the analog page - it doesn't do anything except turn off the level translator
* Level translator: extreme schematic drawing fail...nothing lines up. LOL.
* Use 100nF bypass capacitor on each side of the translator. 100nF should be the default bypass capacitor value
* Use the MCO output on the F4, assuming that the ADC will run properly on 8MHz. This way, the HSE can be configured to output as a square wave on the MCO pin.
* Common mode ferrite bead is ideal for the ADC input, rather than two separate beads. Something like this is good. Maybe also use this on the CAN lines in differential configuration?
* Put a 100nF capacitor across VSS and AVDD. Also a 100nF on digital supply pin
* Just use a single analog reference - fewer parts required, and you are only calibrating against one reference
* LTC6803Rethink the pinout of the cell connector!!! As-is, there are 150V between two pins. That being said, the connector will certainly change to something like the JAE MX47 seriesUse a different connector for the thermistor connections on each LT chip. Or, leave a pin between connections at different voltagesUse the PFET pull-down trick on the supplies for the LT6803's. The current optocoupler solution will have a junction drop, making the input supply lower than the top cell. The LT chip does not like this.Consider a different means of transmitting the SPI data: use an optocoupler isolator, the ADuM chips, or power an isolator from VReg. Or, consider no isolator?Put inline resistors (100Ohm) on the side of the SPI lines that transmits; i.e., on SCLK, CS, MOSI at the MCU side, and MISO on the LT chip side.
* Rethink the pinout of the cell connector!!! As-is, there are 150V between two pins. That being said, the connector will certainly change to something like the JAE MX47 series
* Use a different connector for the thermistor connections on each LT chip. Or, leave a pin between connections at different voltages
* Use the PFET pull-down trick on the supplies for the LT6803's. The current optocoupler solution will have a junction drop, making the input supply lower than the top cell. The LT chip does not like this.
* Consider a different means of transmitting the SPI data: use an optocoupler isolator, the ADuM chips, or power an isolator from VReg. Or, consider no isolator?
* Put inline resistors (100Ohm) on the side of the SPI lines that transmits; i.e., on SCLK, CS, MOSI at the MCU side, and MISO on the LT chip side.
* Leave termination to the CAN modules - eliminates uncertainty about what's supposed to be terminating.
* 24V Protection / SwitchBring this page to the top levelNO auto-retry. Also try pulling down UV to ground through an optocoupler in order to shut off the switchDon't use 0.1% resistors on the feedback (or anywhere, for that matter - there's no need.)Use a 24V current sense for sanity check: consider the ACS716Consider a larger value for the timer capacitorThe output FET is not large enough. Rule of thumb: select 3x the expected drain current on the FET. For all FETs, check the power dissipation and consider the package
* Bring this page to the top level
* NO auto-retry. Also try pulling down UV to ground through an optocoupler in order to shut off the switch
* Don't use 0.1% resistors on the feedback (or anywhere, for that matter - there's no need.)
* Use a 24V current sense for sanity check: consider the ACS716
* Consider a larger value for the timer capacitor
* The output FET is not large enough. Rule of thumb: select 3x the expected drain current on the FET. For all FETs, check the power dissipation and consider the package
* Turn-on circuitRemove R71Remove zener on Edisc\_top inletMove the zener on the PFET to Gate-SourceUse the other permakill coil/contact set to switch VBKUP - this way, you aren't discharging through the pull-up and gate of the PFETSimilarly, move the PFET above the VicorMake R70 larger (10k), put a 100nF from Gate-Source, inline resistor
* Remove R71
* Remove zener on Edisc\_top inlet
* Move the zener on the PFET to Gate-Source
* Use the other permakill coil/contact set to switch VBKUP - this way, you aren't discharging through the pull-up and gate of the PFET
* Similarly, move the PFET above the Vicor
* Make R70 larger (10k), put a 100nF from Gate-Source, inline resistor
* Specify all fuses as "mechanical" components so they show up on the BOM but not on the layout
* Name all sub-sheets for variants so it's clear which array switch is which
* CzonkaPick a Czonka coil drive FET for peak current. 200V isn't necessaryUse a NAND gate for the turn-on. This can be yellow-wired into any other type of gate!Drive the precharge coil with a Darlington Optocoupler - fewer parts, no high current needed.Check the pinout of the standard Czonka connector so I don't have to make a new connector
* Pick a Czonka coil drive FET for peak current. 200V isn't necessary
* Use a NAND gate for the turn-on. This can be yellow-wired into any other type of gate!
* Drive the precharge coil with a Darlington Optocoupler - fewer parts, no high current needed.
* Check the pinout of the standard Czonka connector so I don't have to make a new connector
* Precharge resistor divider: will not workFind lower bias current comparator or use smaller resistors. Or both. There will be 0.5v of error at the input with 2.8M and a bias current in the nano-amps!Unused comparator inputs will "chatter" if left unconnected. Should connect one to a high rail, one to a low rail, so the output stays in a fixed state
* Find lower bias current comparator or use smaller resistors. Or both. There will be 0.5v of error at the input with 2.8M and a bias current in the nano-amps!
* Unused comparator inputs will "chatter" if left unconnected. Should connect one to a high rail, one to a low rail, so the output stays in a fixed state
* Put a 100k resistor inline to the PC\_Done net so the processor cannot drive the output of the comparator due to bad MCU configuration
* BuzzerRename BUZ\_EN to BUZ\_PWMNo inline resistor, use a 10k pull-downFind a better buzzer with more documentation?A piezo is essentially a capacitor! Consider driving it by connecting one side to a MCU pin (push-pull), and the other to the middle of two capacitors dividing 3.3v and HV-. If the processor can drive the amount of current required for the buzzer, no need for an external driver!
* Rename BUZ\_EN to BUZ\_PWM
* No inline resistor, use a 10k pull-down
* Find a better buzzer with more documentation?
* A piezo is essentially a capacitor! Consider driving it by connecting one side to a MCU pin (push-pull), and the other to the middle of two capacitors dividing 3.3v and HV-. If the processor can drive the amount of current required for the buzzer, no need for an external driver!
* Fan: check the rules for the requirements - if it must always be on, no need to switch it
* 50V capacitor on the Vicor output. Maybe put 20uF on the outputAlso put pads for resistors that would allow adjusting the Vicor output voltage
* Also put pads for resistors that would allow adjusting the Vicor output voltage
* Label fuses versus fuse holders to avoid confusion
* Will run into a chicken-and-egg problem the first time I want to start the BMS: should put a 3-pin header (pwr-gnd-pwr, so it's hermaphroditic) that will charge the capacitor THROUGH the resistor
* Need power for the F4's RTC: non-rechargeable coin cell
* Need buffers on voltage sense because the ADC input current is huge! Move these pins to PA0,1,2 to use ADC0,1,2
* Interface: have 2 (or some small number of) LEDs, and one 8-segment display
* 100nF on JTAG port rather than the 10uF currently
* Sam Lenius: can't hurt to put the lightning protection diode on the low voltage rail.
* Isolated switch: rename to A,K rather than "CTRL" and "GND"
* Annotate schematics with useful values like precharge speed, etc.

Perhaps use a repeated schematic for the LT bleeder circuit using net ties

Check thermistor values - lower (10k as opposed to 100k) is better for noise

Isolated switch: use 390 ohm resistor for current limit. Also fix this in the array switch schematic.

Analog block - just duplicate 4x to avoid compile errors with the buses

Schematic block names - such as "pmic\_3v3"

Consider WSMS2906 from Vishay - PEM studs can be mounted through the board and the shunt, meaning that separate shunt and mounting holes are note required.

[WSMS2906](http://www.vishay.com/docs/30181/wsms2906.pdf)

* These have a 75 ppm/C accuracy, as opposed to the originally specified 15 ppm/C shunts. They will also take up more board real estate

These have a 75 ppm/C accuracy, as opposed to the originally specified 15 ppm/C shunts. They will also take up more board real estate

If temperature coefficient is a concern, perhaps put some thermistors in terminal lugs to measure the temperature

OK to create a connector that will break out spare pins on the MCU for hacking/debugging

Good schematic style: draw a dotted line in the top level schematic showing isolation boundaries

Analog power block - Sasha: power supplies are failure generators. Eliminating supplies eliminates failures.

* Double check that the Recom supply can provide enough current to the regulators
* Ferrite bead between analog and digital supplies
* Don't collapse the positive and negative LDOs into one sheet - make a separate block for each
* Consider the TI ADC as it is more modern and requires fewer power supplies. Ideally there would be one with 3.0v analog and 3.3v digital, to eliminate power supplies

Double check that the Recom supply can provide enough current to the regulators

Ferrite bead between analog and digital supplies

Don't collapse the positive and negative LDOs into one sheet - make a separate block for each

Consider the TI ADC as it is more modern and requires fewer power supplies. Ideally there would be one with 3.0v analog and 3.3v digital, to eliminate power supplies

Consistency in naming: change "VIN+" to "VIN"

Power module

* Use a 550kOhm feedback resistor. This should be double-checked once assembled
* Don't need an output capacitor on the power module. The Schottky diode is good, though.
* Check the schematic part! There should be two V+ pins

Use a 550kOhm feedback resistor. This should be double-checked once assembled

Don't need an output capacitor on the power module. The Schottky diode is good, though.

Check the schematic part! There should be two V+ pins

Array switch

* We did some SPICE, a 1uF capacitor on the gate should make the peak current through the FETs lower.
* Precharging with the FET is possible because the PV FET Driver is a current source, outputting a very small current when shorted.

We did some SPICE, a 1uF capacitor on the gate should make the peak current through the FETs lower.

Precharging with the FET is possible because the PV FET Driver is a current source, outputting a very small current when shorted.

Analog

* Remove R1 from the analog page - it doesn't do anything except turn off the level translator
* Level translator: extreme schematic drawing fail...nothing lines up. LOL.
* Use 100nF bypass capacitor on each side of the translator. 100nF should be the default bypass capacitor value
* Use the MCO output on the F4, assuming that the ADC will run properly on 8MHz. This way, the HSE can be configured to output as a square wave on the MCO pin.
* Common mode ferrite bead is ideal for the ADC input, rather than two separate beads. Something like this is good. Maybe also use this on the CAN lines in differential configuration?
* Put a 100nF capacitor across VSS and AVDD. Also a 100nF on digital supply pin
* Just use a single analog reference - fewer parts required, and you are only calibrating against one reference

Remove R1 from the analog page - it doesn't do anything except turn off the level translator

Level translator: extreme schematic drawing fail...nothing lines up. LOL.

Use 100nF bypass capacitor on each side of the translator. 100nF should be the default bypass capacitor value

Use the MCO output on the F4, assuming that the ADC will run properly on 8MHz. This way, the HSE can be configured to output as a square wave on the MCO pin.

Common mode ferrite bead is ideal for the ADC input, rather than two separate beads. Something like this is good. Maybe also use this on the CAN lines in differential configuration?

[this](http://www.tdk.co.jp/tefe02/e9711_act.pdf)

Put a 100nF capacitor across VSS and AVDD. Also a 100nF on digital supply pin

Just use a single analog reference - fewer parts required, and you are only calibrating against one reference

LTC6803

* Rethink the pinout of the cell connector!!! As-is, there are 150V between two pins. That being said, the connector will certainly change to something like the JAE MX47 series
* Use a different connector for the thermistor connections on each LT chip. Or, leave a pin between connections at different voltages
* Use the PFET pull-down trick on the supplies for the LT6803's. The current optocoupler solution will have a junction drop, making the input supply lower than the top cell. The LT chip does not like this.
* Consider a different means of transmitting the SPI data: use an optocoupler isolator, the ADuM chips, or power an isolator from VReg. Or, consider no isolator?
* Put inline resistors (100Ohm) on the side of the SPI lines that transmits; i.e., on SCLK, CS, MOSI at the MCU side, and MISO on the LT chip side.

Rethink the pinout of the cell connector!!! As-is, there are 150V between two pins. That being said, the connector will certainly change to something like the JAE MX47 series

Use a different connector for the thermistor connections on each LT chip. Or, leave a pin between connections at different voltages

Use the PFET pull-down trick on the supplies for the LT6803's. The current optocoupler solution will have a junction drop, making the input supply lower than the top cell. The LT chip does not like this.

Consider a different means of transmitting the SPI data: use an optocoupler isolator, the ADuM chips, or power an isolator from VReg. Or, consider no isolator?

Put inline resistors (100Ohm) on the side of the SPI lines that transmits; i.e., on SCLK, CS, MOSI at the MCU side, and MISO on the LT chip side.

Leave termination to the CAN modules - eliminates uncertainty about what's supposed to be terminating.

24V Protection / Switch

* Bring this page to the top level
* NO auto-retry. Also try pulling down UV to ground through an optocoupler in order to shut off the switch
* Don't use 0.1% resistors on the feedback (or anywhere, for that matter - there's no need.)
* Use a 24V current sense for sanity check: consider the ACS716
* Consider a larger value for the timer capacitor
* The output FET is not large enough. Rule of thumb: select 3x the expected drain current on the FET. For all FETs, check the power dissipation and consider the package

Bring this page to the top level

NO auto-retry. Also try pulling down UV to ground through an optocoupler in order to shut off the switch

Don't use 0.1% resistors on the feedback (or anywhere, for that matter - there's no need.)

Use a 24V current sense for sanity check: consider the ACS716

Consider a larger value for the timer capacitor

The output FET is not large enough. Rule of thumb: select 3x the expected drain current on the FET. For all FETs, check the power dissipation and consider the package

Turn-on circuit

* Remove R71
* Remove zener on Edisc\_top inlet
* Move the zener on the PFET to Gate-Source
* Use the other permakill coil/contact set to switch VBKUP - this way, you aren't discharging through the pull-up and gate of the PFET
* Similarly, move the PFET above the Vicor
* Make R70 larger (10k), put a 100nF from Gate-Source, inline resistor

Remove R71

Remove zener on Edisc\_top inlet

Move the zener on the PFET to Gate-Source

Use the other permakill coil/contact set to switch VBKUP - this way, you aren't discharging through the pull-up and gate of the PFET

Similarly, move the PFET above the Vicor

Make R70 larger (10k), put a 100nF from Gate-Source, inline resistor

Specify all fuses as "mechanical" components so they show up on the BOM but not on the layout

Name all sub-sheets for variants so it's clear which array switch is which

Czonka

* Pick a Czonka coil drive FET for peak current. 200V isn't necessary
* Use a NAND gate for the turn-on. This can be yellow-wired into any other type of gate!
* Drive the precharge coil with a Darlington Optocoupler - fewer parts, no high current needed.
* Check the pinout of the standard Czonka connector so I don't have to make a new connector

Pick a Czonka coil drive FET for peak current. 200V isn't necessary

Use a NAND gate for the turn-on. This can be yellow-wired into any other type of gate!

Drive the precharge coil with a Darlington Optocoupler - fewer parts, no high current needed.

Check the pinout of the standard Czonka connector so I don't have to make a new connector

Precharge resistor divider: will not work

* Find lower bias current comparator or use smaller resistors. Or both. There will be 0.5v of error at the input with 2.8M and a bias current in the nano-amps!
* Unused comparator inputs will "chatter" if left unconnected. Should connect one to a high rail, one to a low rail, so the output stays in a fixed state

Find lower bias current comparator or use smaller resistors. Or both. There will be 0.5v of error at the input with 2.8M and a bias current in the nano-amps!

Unused comparator inputs will "chatter" if left unconnected. Should connect one to a high rail, one to a low rail, so the output stays in a fixed state

Put a 100k resistor inline to the PC\_Done net so the processor cannot drive the output of the comparator due to bad MCU configuration

Buzzer

* Rename BUZ\_EN to BUZ\_PWM
* No inline resistor, use a 10k pull-down
* Find a better buzzer with more documentation?
* A piezo is essentially a capacitor! Consider driving it by connecting one side to a MCU pin (push-pull), and the other to the middle of two capacitors dividing 3.3v and HV-. If the processor can drive the amount of current required for the buzzer, no need for an external driver!

Rename BUZ\_EN to BUZ\_PWM

No inline resistor, use a 10k pull-down

Find a better buzzer with more documentation?

A piezo is essentially a capacitor! Consider driving it by connecting one side to a MCU pin (push-pull), and the other to the middle of two capacitors dividing 3.3v and HV-. If the processor can drive the amount of current required for the buzzer, no need for an external driver!

Fan: check the rules for the requirements - if it must always be on, no need to switch it

50V capacitor on the Vicor output. Maybe put 20uF on the output

* Also put pads for resistors that would allow adjusting the Vicor output voltage

Also put pads for resistors that would allow adjusting the Vicor output voltage

Label fuses versus fuse holders to avoid confusion

Will run into a chicken-and-egg problem the first time I want to start the BMS: should put a 3-pin header (pwr-gnd-pwr, so it's hermaphroditic) that will charge the capacitor THROUGH the resistor

Need power for the F4's RTC: non-rechargeable coin cell

Need buffers on voltage sense because the ADC input current is huge! Move these pins to PA0,1,2 to use ADC0,1,2

Interface: have 2 (or some small number of) LEDs, and one 8-segment display

100nF on JTAG port rather than the 10uF currently

Sam Lenius: can't hurt to put the lightning protection diode on the low voltage rail.

Isolated switch: rename to A,K rather than "CTRL" and "GND"

Annotate schematics with useful values like precharge speed, etc.

Review 1 - Architecture

8/10/2012

Move shunts off the board (for flexibility of packaging).

Shutting the board down to where physical changes are required to turn it back on will only happen in software (no hardware).

Bus voltage: 24V

Change: don’t put the MCU on the other side of an isolation barrier from the rest of the ICs.  It would give another layer of isolation, but isn’t worth the additional time and pain.  Put it in a box to protect it against derpers with wrenches instead.

Change the net naming conventions to conform to Sasha Style. Call the two ground GND and HV-.

Change port numbers to shorter and keep them upercase. (Each character above 8 incurs a penalty of one lashing)

Edisc switches the startup battery.

Consider: A supercap instead of a coin cell in some applications

FET on the vicor switch may be overkill

Put a capacitor on the input and output of the vicor to keep it stable.  If electrolytic, use solid polymers (good practice).  Input--film; output--ceramic

May not need fet to turn on photovoltaic optocoupler

Switch APV1121 to TLP190B

Have switches on the inputs and outputs of power supplies to turn on and off rails.

Separate switch to turn on the rest of the car after BMS boots.  Question: Turn on the MPPTs before or after this?

Don’t put too much capacitance on the output of a Vicor because you can crash it at start.

Everything related to power should be rated to 125C

Replace turnon fet to the car with a linear chip that has overcurrent protection and inrush current limiting. Sasha suggests LTC 4218--also to avoid an infinite reboot loop.

Consider sending fault pins from LTC

Change: No fuse to the Vicor?  Don’t use a resettable fuse--probably won’t get to the voltage rating you’re looking for.  They also blow to a holding current rather than open, and at solar car temperatures it’s possible for them to explode when they fail.  Can also break and then arc if you look at the AC rating instead of DC.

Don’t hook the array directly to the motor controller.

Possible failure modes:

Disconnect the contactor at full regen--(hint it involves dv/dt)

Running current back into the topshell through the high voltage line.

Regen->current to the topshell->seen by BPS as a failed MPPT.

“Lid open” is irrelevant because wrenches will damage BPS even if it’s off.

Prefer a common positive rail to a common ground for the latching relay: makes life simpler, requires fewer components.

Can have a stronger pull-up on the Permakill\_drive circuit, because it will be on only briefly (power consumption is a concern).

Edisc: want a mechanism where any number of nodes can turn off the car--currently only two: pushbutton on the steering wheel and the emergency stop button on the outside of the car.  Button on top is normally closed, driver button is normally open.

Pressing driver button closes a path that goes through both switches.  Separate edisc net for top and bottom shell.

Remove 0R reistors on can bridge and bridge in software instead.

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1DNgbEYxeRcauP5RysnBv3A4FEtbgU1vB#list)
