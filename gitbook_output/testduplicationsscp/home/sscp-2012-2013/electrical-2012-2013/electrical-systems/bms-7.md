# bms-7

## SSCP - BMS 7

## BMS 7

A Note to the Reader

Each designer has different reasons for putting endless hours into SSCP. My reasons are: learning, and being involved in a cool project. Past generations of designers have re-invented the wheel for the sake of "innovation," or because "it is the only way to learn." I don't think it's necessary to start from scratch to learn something.

Thus, the BMS I set out to design is not intended to be novel, but reliable and maintainable. Designing a circuit from scratch may mean more experience in selecting parts and feel like more understanding is gained; however, this does not mean that less is learned through iterating on a design. Iteration forces consideration of prior design decisions and requires a more in-depth understanding of each circuit block, if improvement is to be made. I could have thrown out all work done on Solar Car BMS's before, but I chose to rethink Greg's BMS 6, with a focus on modernizing parts selections, eliminating unnecessary components (especially those that are failure-prone, like connectors, power supplies, or capacitors), and characterizing / testing the final product.

The bottom line: if you're the person tasked with "building" a BMS for the next car, and you're starting from scratch without a clear reason for changing the architecture of the BMS, then I haven't met my design goals. In the interest of progressing forward with a reliable and functional design (and giving more time for other projects on the car), this BMS is intended to only require changes that will help adapt to the architecture of the next car. I've made every attempt to keep parts modern and simplify the design. Consider this before throwing out the countless hours I've put into a BMS - your time is finite. Each hour you spend reinventing what I've done here (that does not clearly improve over the current design) is an hour that won't go to another section of the car.

Happy Solar Car Racing!

\--Max Praglin, Class of 2014-ish

What Worked Well, and What Didn't

&#x20;  The Good

* Overall power architecture of the car
* Turn-on circuit. Very simple, worked intuitively!
* Duplicated current sensing for motor, solar, car, and net battery. Provided good data during the race.
* Placement of BMS outside the high current loop formed by the batteries. The high current path on BMS 7 is on the edge of the board closest to the cells, too.Isolating all of the LT chip circuits. There were no PEC errors after this decisoinPrecharge check: consisted of comparator (in hardware), voltage sensing in MCU, and time-outNo array switch - with the rules change requiring contacting the array output, there was no need for a switch in the battery boxPackaging: there is no need for a BMS enclosure separate from the battery pack. There is no time you ever are working on the battery pack and don't want to make connections to the board. In fact, enclosing the board in its own box could lead to thermal problems.Micro-fit connectors. Strain-relieved a couple inches behind the connector (zip tying all the wires together works well), and with all leads the same length, there are no problems with vibe, cycle life, waterproofing, resistance, etc. There is no need for a bulky connector inside of a theoretically waterproof battery pack!Keystone terminals for high current, with Belleville washers.Board form-factor: it's large, but trying to make the board smaller would probably just be a waste of  time. It's really not that large in the grand scheme of the car...
* Isolating all of the LT chip circuits. There were no PEC errors after this decisoin
* Precharge check: consisted of comparator (in hardware), voltage sensing in MCU, and time-out
* No array switch - with the rules change requiring contacting the array output, there was no need for a switch in the battery box
* Packaging: there is no need for a BMS enclosure separate from the battery pack. There is no time you ever are working on the battery pack and don't want to make connections to the board. In fact, enclosing the board in its own box could lead to thermal problems.
* Micro-fit connectors. Strain-relieved a couple inches behind the connector (zip tying all the wires together works well), and with all leads the same length, there are no problems with vibe, cycle life, waterproofing, resistance, etc. There is no need for a bulky connector inside of a theoretically waterproof battery pack!
* Keystone terminals for high current, with Belleville washers.
* Board form-factor: it's large, but trying to make the board smaller would probably just be a waste of  time. It's really not that large in the grand scheme of the car...

Overall power architecture of the car

Turn-on circuit. Very simple, worked intuitively!

Duplicated current sensing for motor, solar, car, and net battery. Provided good data during the race.

Placement of BMS outside the high current loop formed by the batteries. The high current path on BMS 7 is on the edge of the board closest to the cells, too.

* Isolating all of the LT chip circuits. There were no PEC errors after this decisoin
* Precharge check: consisted of comparator (in hardware), voltage sensing in MCU, and time-out
* No array switch - with the rules change requiring contacting the array output, there was no need for a switch in the battery box
* Packaging: there is no need for a BMS enclosure separate from the battery pack. There is no time you ever are working on the battery pack and don't want to make connections to the board. In fact, enclosing the board in its own box could lead to thermal problems.
* Micro-fit connectors. Strain-relieved a couple inches behind the connector (zip tying all the wires together works well), and with all leads the same length, there are no problems with vibe, cycle life, waterproofing, resistance, etc. There is no need for a bulky connector inside of a theoretically waterproof battery pack!
* Keystone terminals for high current, with Belleville washers.
* Board form-factor: it's large, but trying to make the board smaller would probably just be a waste of  time. It's really not that large in the grand scheme of the car...

Isolating all of the LT chip circuits. There were no PEC errors after this decisoin

Precharge check: consisted of comparator (in hardware), voltage sensing in MCU, and time-out

No array switch - with the rules change requiring contacting the array output, there was no need for a switch in the battery box

Packaging: there is no need for a BMS enclosure separate from the battery pack. There is no time you ever are working on the battery pack and don't want to make connections to the board. In fact, enclosing the board in its own box could lead to thermal problems.

Micro-fit connectors. Strain-relieved a couple inches behind the connector (zip tying all the wires together works well), and with all leads the same length, there are no problems with vibe, cycle life, waterproofing, resistance, etc. There is no need for a bulky connector inside of a theoretically waterproof battery pack!

Keystone terminals for high current, with Belleville washers.

Board form-factor: it's large, but trying to make the board smaller would probably just be a waste of  time. It's really not that large in the grand scheme of the car...

&#x20;   The Bad

* HVA-280 connector on the outside of the battery pack. It's a great connector for a lower cycle life application. The plastic retainer (red clip) on the HVA-280 began sticking once we got to Australia. This may not be worth the trouble of changing on the next battery pack, though.
* 24 to +/-5v converter is inefficient.
* 5v to 5v converter is inefficient and does not have a well-regulated output (I had to put a zener on the output)
* 7-seg LEDs are too bright and cause the 3.3v LDO to get very hot

HVA-280 connector on the outside of the battery pack. It's a great connector for a lower cycle life application. The plastic retainer (red clip) on the HVA-280 began sticking once we got to Australia. This may not be worth the trouble of changing on the next battery pack, though.

24 to +/-5v converter is inefficient.

5v to 5v converter is inefficient and does not have a well-regulated output (I had to put a zener on the output)

7-seg LEDs are too bright and cause the 3.3v LDO to get very hot

Bring-up and Testing

The bring-up log for both hardware and software between BMS 7-0-0 and BMS 7-1-1 can be found here.

[here](https://docs.google.com/document/d/1L3fXiNaKfxoFQhZ9IejtqIhYrmxii28_H-cyHQc0or0/edit)

Architecture Decisions

Diagrams

Diagrams (that are hopefully easier to understand than the schematic) are attached below.

Distributed vs. Monolithic

In hindsight, this is not as significant of a design decision as everybody made it out to be (both architectures can work just fine). Time should be spent on testing (especially in-the-loop testing) rather than arguments about architecture.

A distributed BMS will have voltage/temperature measurement and cell bleeding as a separate circuit board that mounts on each cell. A monolithic BMS will have a central circuit board with wires to each cell.

This is a debate that has polarized BMS designers. Past distributed BMS's have: had a clean battery pack layout; had easy-to-test modules; been easy to swap out broken modules. Past monolithic BMS's have: used the LT6803, a well-understood BMS chip; had code in a single place; been easy to replace all the electronics in a pack.&#x20;

For BMS 7, I decided that a monolithic system was the best solution for the problem. Arguments for a distributed BMS included clean wiring, better voltage measurements, and simiplicity. I personally found a monolithic BMS simpler as there are fewer points of failure, and deemed any wiring tidiness problems as fixable. Without real analysis, I have a hard time believing that the length of signal lines is a more significant source of noise than wire placement or battery current ripple.  A distributed BMS may be more repairable because modules are quickly replaceable; however, in a race situation, it would be just as quick to swap a monolithic PCB for a spare and debug the broken board in the back of a van.&#x20;

A distributed system also may have higher power draw because 36 processors and CAN transceivers are required. Past distributed BMS's have used PIC microcontrollers on each of the battery-mounted PCBs. STM processors with CAN (the STM32F103 is the smallest) require approximately 7mA each. In order to use the lower current microcontrollers, we would not be able to maintain our current STM tool chain.

Current Sensing

In order to have an accurate model of State Of Charge (SOC), accurate measurement of current in and out of the pack is crucial. BMS 6 current sense (only for in and out of the pack) worked very well. The other current sense measurements using a LEM sensor were not entirely useful. BMS 7 will use the same sense circuitry for total pack current, and use a shunt + STM32 ADC for other current sensing.

BMS 6 used the AD7712 Sigma-Delta ADC; this ADC functioned well, but had a difficult-to-use interface. I considered the TI ADS1246, which has a much easier serial interface. Criteria for an ADC are:

* Able to measure voltages below analog ground (because current flows in both directions through the main shunt, meaning that no point is always "lowest" in the system) - unless some trick is used.
* Differential inputs preferred
* 3.3v digital, <3.0v analog preferred
* Adjustable gain to measure the full scale output of the shunt (50mV in the case of the Canadian shunts)
* Simple serial interface

Able to measure voltages below analog ground (because current flows in both directions through the main shunt, meaning that no point is always "lowest" in the system) - unless some trick is used.

Differential inputs preferred

3.3v digital, <3.0v analog preferred

Adjustable gain to measure the full scale output of the shunt (50mV in the case of the Canadian shunts)

Simple serial interface

The WSMS2906 series from Vishay would provide a very clean mechanical solution: PEM studs could come up through the main shunt terminals, combining a mechanical and electrical attachment into one. However, the temperature coefficient of these is nearly an order of magnitude worse than the Canadian Shunts used on BMS 6. Datasheet below. While we could calibrate out the inaccuracy with a thermistor attached to the shunt, this is more complexity to solve a fundamentally mechanical problem.

[WSMS2906](http://www.vishay.com/docs/30181/wsms2906.pdf)

Points at which BMS 7 will measure current (all on the low side of the battery pack): in/out of the pack;  to/from motor controller; from array; to DC/DC converter (i.e. Vicor).

A "sanity-check" current sense is provided on the 24V bus output using the simple ACS716 isolated current sense IC. It's nice to have values like this for telemetry that will give the race team an at-a-glance idea of the power required to control the car. High precision measurement is not needed here - each board should implement a more accurate current sense circuit. At the time of schematic drawing, the current sensing circuit on each board had not yet been implemented - while it could have been used here, it is not isolated (meaning that an I2C isolator would be required to feed the data into the MCU), and that I would be using an IC I had never seen function.

Update: as of 7-1-0, the I2C current sense IC is used to measure both car current draw as well as BMS board current draw.

Isolation Boundaries

BMS 6 had many numerous boundaries between the battery pack and any circuit board's 3.3V bus. BMS 7 will have the following two domains: battery pack ground (shared with motor controller, array, digital control electronics, and analog sensing); 24V ground (shared among the ground of all circuit boards on the car).

The 2013 WSC rules dictate very specific points at which mechanical isolation must be used. In order to accommodate these rules, mechanical isolation was used in three places: precharge, main contactor, and MPPT inlet. Placing a relay at the MPPT satisfies rule 2.68 ("The driver must be able to electrically isolate the solar panel from the rest of the Solar EV..."). Placing it at the inlet of the MPPT means that a lower voltage must be broken if the driver chooses to isolate the panel from the rest of the car while it is drawing current.

The most efficient solution for WSC 2013, should the rules allow it, would be a contactor separating the motor controller from the array (with the main contactor's output connected to the motor controller). If the MPPTs were to short their outputs by default (i.e. when powered off), the penalty of keeping a coil turned on is only payed once, rather than at each MPPT. However, the WSC officials explicitly stated in an email to us that a contactor inside the pack would not meet their requirements.

Precharge

For the sake of simplicity, BMS 7 uses a SPDT relay with the common contact tied to the HV bus. The NC state shorts the HV bus to ground through a large resistor, and the NO state shorts the HV bus to the battery pack through a massive NTC inrush limiter. A 5V relay was chosen so an extra opto-coupler would not be necessary to drive the coil from 24V.

While the processor can monitor battery and HV bus voltages, a hardware check exists in both BMS 6 and 7 to check if the HV bus is charged before the main contactor is opened. Charging to \~95% before closing the contactor is sufficient.

Note that a system which permanently connects the array and motor controller buses has the danger of the MPPT being enabled with the contactor closed, causing an inrush of current into the batteries. The precharge check comparator will register a "precharge done" even though the voltages are not equalized. We will prevent this in software.

Safety Interlocks

BMS 6 had an unintended behavior: when any cable carrying Emergency Disconnect ("Edisc") was disconnected, the battery pack turned on. In BMS 7, we opted to require that the Edisc lines (that travel through all CAN cables) be in a specific state for the car to run: the driver-operated on/off button must short Edisc to ground, and the external emergency stop button must be in a closed position. HVIL (high voltage interlock) is supported, as well - switches to override HVIL, the driver button, and the external button are present on BMS. Any break in the CAN harness between the pack and steering wheel, the two end points of our CAN bus, causes the car to immediately shut off - this provides a sanity check of "is everything plugged in," and also aids in safety: it will not be possible to expose high voltage outside the pack unless all control cables are plugged in properly. While it would require less components if the bottom shell Edisc line were to be required to short to ground for the car to start, unplugging a CAN cable would not shut off the car.

Update: Sunbad does not have a top shell, so there is only 1 CAN bus! The edisc circuitry has been absorbed onto BMS (as of 7-1-0). Also, the CAN architecture we chose for Sunbad necessitates that BMS and the steering wheel be the two end-nodes of the bus. The steering wheel shorts EDISC and GND as well as terminating the bus, so unplugging it will both turn off the car and de-terminate the bus.

I considered a Lid Closed switch that would require the lid to be closed in order to start the BMS. Because it would most likely be overridden, and the majority of falling objects on the pack would do damage to the PCB regardless of power running through it, the switch was deemed unnecessary.

BMS 7 includes a "perma-kill" relay that gives the processor the ability to turn off the battery pack (and reduce current draw to zero) if a serious condition is detected. An internal momentary button must be pressed in order to restart the car. This necessitates that a human look at the battery pack before it can be started after a fault. I considered having software-hardware undervoltage shutoff redundancy, but sensing undervoltage and transferring power and the signal to the perma-kill relay (across isolation boundaries) is not very clean. With regard to sensing: it is not sufficient to shut off the battery pack if the cell voltage average drops below 2.7v temporarily: at low SOC, hard acceleration can safely pull down the pack voltage temporarily. Thus, a filter with a long time constant (i.e. RC= >1 min) would be required on the input of the undervoltage comparator. High voltage sensing was added on BMS 7 because no isolation barrier must be crossed, so software can manage a SOC-based permakill.

BMS 6, as well as BMS 7 have an AND gate that prevents the main contactor from engaging until precharge has finished and the processor sends a signal to send high voltage to the rest of the car.

Engineering Decisions

Power Supplies

Power for the MCU arrives via the path: Pack->Vicor->Murata 24 to +/-5V converter-> LDO

Power for the analog section of the current measurement arrives via the path: Pack->Vicor->Murata 24 to +/-5V converter-> +/-2.7V Converter

Power for running CAN transceiver, I2C transceiver, fan controller, and recharging the supercapacitor arrives via the path: Pack->Vicor->24 to 5V buck converter

#### Shunts

Good shunts will have a good (small) temperature coefficient. Usually something in the range of 15ppm is considered good for high precision current measurement applications. For BMS 7 we considered shunts from Empro, Canadian Shunt, (made shunts for BMS 6), and Deltec. BMS 7 will use Canadian Shunt's 50 mV PCB-mount shunts.

[Empro](http://www.emproshunts.com/home.aspx)

[Canadian Shunt](http://www.cshunt.com/)

[Deltec](http://www.deltecco.com/)

[PCB-mount shunts](http://www.cshunt.com/pdf/pcb.pdf)

See calculations below for an understanding of how shunts were chosen. For both the main shunt and motor controller shunt, I chose a 150A shunt so we can capture the peaks of the Tritium's 100A RMS input. For the array, I chose a 50A shunt (see calculations below). For the Vicor, I chose the smallest PCB-mount shunt that Canadian makes, a 10A shunt.

Connectors

Since the mechanical design of the pack was multiple months from being mature at the time of the first revision of BMS 7, I opted to choose simply when it came to mechanical components. I used ring terminals for any connections to high voltage, and a single connector for all the cells. This one connector could plug into a board with many single cell battery holders, allowing us to test without a full-on pack.

BMS 7-1-1 includes both holes for #6 hardware and Keystone 7808 terminals, which do not stress the PCB through compression.

On BMS 7-0-0 and 7-1-0, JAE MX23 and MX47 connectors are used for cell sense, CAN connectivity, car power, etc. While the JAE MX23 and MX47 (essentially the same connector, just 2 vs 3 rows) are robust, watertight, and box-mountable, they are difficult (i.e. high removal force) to actuate once contacts are present, and require a lot of space because they are horizontally-mounting.&#x20;

I opted for Micro-fits (all through-hole, vertical-mount, with strain relief) on revision 7-1-1 because: they are vertical, allowing more space in the pack to be utilized. We own a proper crimping tool. The cycle life is high enough that we will likely not need to make a replacement connector over the lifetime of a pack. They are always in stock.&#x20;

Array Switching and Protection

It is advisable to have a means of disconnecting the MPPTs from the motor controller (and also prevent current from flowing back into the MPPT's output capacitance). For example, at the start of the race, when the batteries are fully charged, the MPPT output voltage will rise above a permissible if the output voltage is not limited. An ideal diode will prevent regenerative braking from pushing power into the MPPT's.

The ideal diode implementation means that the MPPT capacitance does not have to be precharged (because they precharge themselves).

The LTC4366 was considered as a way to protect the output of the MPPTs from high voltage spikes, and also to precharge by using the programmable slew rate of the connected FET. This is not a very clean solution and does not fulfill all the criteria given above. The LTC4359 has a ground that floats up to handle high voltages.&#x20;

[LTC4366](http://www.linear.com/product/LTC4366)

[LTC4359](http://cds.linear.com/docs/Datasheet/4359f.pdf)

Update: As of BMS 7-1-1, the array and motor controller share a positive rail. Thermal issues raised a concern of anything that dissipates power, and I was hoping to simplify / free up more space: connecting the two positive rails together means that no array switch is needed (eliminating the LTC4359 circuit, and two MOSFETs), and that no array discharge circuit is needed (eliminating a large power resistor and depletion N-FET). This saves both space and power dissipation.

24V Power and Sensing

Current sensing is provided for both the BMS and the rest of the car via the 24V bus. Power exiting the Vicor either:

* Reaches a 24V switch (with OV/UV/OC protection), followed by an isolated hall effect current sensor - to sense 24v power drawn by the rest of the car ("24v remote power")
* Or, is sensed with a LTC4151 I2C current sensor, followed by a Murata isolated 24-+/-5v converter. ("24v local power")

Reaches a 24V switch (with OV/UV/OC protection), followed by an isolated hall effect current sensor - to sense 24v power drawn by the rest of the car ("24v remote power")

Or, is sensed with a LTC4151 I2C current sensor, followed by a Murata isolated 24-+/-5v converter. ("24v local power")

The CAN transceiver (and the I2C current sensor) receive power from a buck converter that is powered off of the BMS's 24v local power. This power is available once the Vicor starts up, so it is suitable for recharging the 5V supercapacitor. A 24-5v LDO can be eliminated.

Calculations and Low-level Circuit Explanation

Calculations assume the following:

* 20mF capacitance on the high voltage bus
* Maximum= 160V battery stack due to Tritium input limit -> 36 cells in series, maximum.
* 1.5kW array power (overestimated)

20mF capacitance on the high voltage bus

Maximum= 160V battery stack due to Tritium input limit -> 36 cells in series, maximum.

1.5kW array power (overestimated)

Note!: These assumptions were made for Xenith's pack voltage

Resistive Power Losses (shunts and FETs)

At maximum pack draw (the Tritium Wave Sculptor 22 is rated to 100A RMS), a 150A 50mV shunt would dissipate 3.33W (R = V/I, P = I2R). At cruise, current draw is reduced to \~10-15A, meaning that losses are on the order of 100 mW.

If we were to run a 40V HV bus, at 1500W input, the maximum array output current would be 37.5A. This is an unlikely scenario, but shunts were chosen to accommodate this high of an array output current.

An array switch could be implemented with either a contactor or back-to-back FETs. A contactor in the range that we would use (i.e. a Gigavac GX11) has a maximum contact resistance of 0.0004 and uses 1.1W coil power. Very good MOSFETs (such as those we have gotten from IXYS directly) have a Rdson of 4.5 mOhm, for 9 mOhm total in back-to-back configuration. This document shows the power loss in each solution for different bus voltages. At 1500W and a bus voltage of <110V, a contactor is more efficient; however, at less than 100% array output, the contactor will rapidly become less efficient because it requires a constant coil current.

[Gigavac GX11](http://www.gigavac.com/products/contactors/datasheets/gx11/index.htm)

[This document](https://docs.google.com/spreadsheet/ccc?key=0AmVyg7HGPlLkdHZLUXFWWHlJNV93eDVjQmRtX3U4ZXc)

Resistive Power Losses (optimizing power loss and weight penalty)

I put together a calculator that helps find the right AWG (or conductor area, for bus bars) here.

[here](https://docs.google.com/spreadsheet/ccc?key=0AmVyg7HGPlLkdEtFcnpENVBxckJRaXlSN0VIY2ZGRHc#gid=0)

Backup Capacitor&#x20;

This capacitor will serve as the backup power supply on BMS 7. By E = 0.&#x35;_&#x43;_&#x56;2, at 5.0V and 1.5F, this holds 18.75J of energy, significantly less than the 10 Wh limit in the rules.

[This capacitor](http://industrial.panasonic.com/www-cgi/jvcr13pz.cgi?E+PZ+3+ABC0021+EECRG0V105H+7+WW)

Here's a rough calculation, assuming constant reverse leakage: The capacitor is charged through a Schottky diode. Assuming 100nA reverse leakage, half of the original charge (originally 7.5 Coulombs, by Q=CV) will be gone after 2.4 years (I=Q/t).

This cap is used on 7-1-0. It is 5V tolerant, meaning that the capacitor can be charged off of the 24-5v buck converter without an LDO.

[This](http://industrial.panasonic.com/www-cgi/jvcr13pz.cgi?E+PZ+3+ABC0002+EECS5R5H155+7+WW)

Precharge and Discharge

(The below 2 paragraphs are left over from Xenith calculations, but are still useful as an example)

The discharge circuit is simpler: it is a simple RC system. The time constant RC, with 20mF of capacitance on the HV bus (estimated, perhaps too high), a 500 Ohm resistor gives a RC of 10 seconds. By P=V2/R, Pmax = (4.2\*36)2/500 = 45.7W. A 30W resistor was chosen because the peak power is only seen for a short amount of time.

The precharge circuit utilizes an NTC thermistor as an inrush limiter. The high voltage bus has an energy of E=0.&#x35;_&#x43;_&#x56;2, or 225J. The thermistor is sized for at least double the energy stored in the HV bus.  It has a resistance of 20 Ohm at 25C. By I=V/R, Iinit = 150 / 20 = 7.5A. Although the resistance will decrease as temperature increases, leading to a higher current, the voltage difference is also decreasing, leading to smaller current. The NTC must be sized to balance the opposite trends of these two curves.

Update: As of 7-1-0, normal resistors for charge and discharge are used. The precharge and discharge times are not so significant that temperature dependence is a good idea.

Current Measurement: Analog Front-End

The sigma-delta modulator runs at a minimum of 32kHz. The input RCR network should have a corner frequency well below the modulator frequency to filter out this noise. Film capacitors are ideal for this location (non-piezoelectric, non-polarized), but are physically large. Using a combination of 22K Ohm resistors and a 47nF capacitor, a corner frequency of approximately 1kHz is attained.

The input impedance of the PGA is 5000 MOhm. At 50 mV maximum shunt voltage, by I=V/R, Iinput = 10^-11 A. Across a 22K Ohm resistor, this is a \~200nV error.

LTC6803 Turn-On Circuit

(Not used as of BMS 7-1-1, because of the switch to isolated stack monitors, but still may be useful to somebody trying to use the LTC6803-3)

The PFET has its VGS clamped to 15V to prevent overvoltage of this junction. Ignoring the RGS resistor, because current through it is negligible, the current to ground flows through a 4.7M Ohm resistor. In the worst case of the top stack, Presistor = (Vstack - Vzener)2/R = \~4 mW. Pzener = (

Vstack - Vzener) / R \* Vzener = \~450 nW. The resistors could be made smaller than 4.7M Ohm.

LED Cell Bleed Circuit

The diode curve of the red LED from CREE is shown on Page 9 of http://www.cree.com/\~/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/XlampMLE.pdf.

[http://www.cree.com/\~/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/XlampMLE.pdf](http://www.cree.com/~/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/XlampMLE.pdf)

This implies that bleed current is highest when the cell voltage is highest. With two LEDs in series, no current limiting resistor is required, meaning that energy bled from the cell is only dissipated through the inefficiency of the LEDs! Space and other materials in the pack with larger surface area will sink this heat.&#x20;

The minimum forward voltage of these LEDs is 1.6V, meaning that bleeding cannot be accomplished below 3.2V. This is in fact beneficial: at lower state of charge, the cells cannot be discharged through bleeding. As the cells rise in voltage during charging, the bleeding becomes more aggressive, which is beneficial, as cell voltage increases sharply near the top of the state of charge.

As of BMS 7-1-1, a power resistor and LED+current limiting resistor are used.

Power Conversion

To provide power to the on-board MCU and associated control circuitry, a Vicor Micro isolated switching power supply provides 24v. This is then converted to 5V referenced to battery ground (on which control circuitry sits). The 24 to +/-5V converter was chosen in stead of Xenith-era isolated power modules to eliminate the need for an additional cascaded power supply that provides a negative rail for the analog circuitry. Dropping 5V to 3.3V, if the Murata converter supplies its rated 600mA, P=(Vin - Vout) \* I = 1W. This is the WORST case scenario, and normal operation should never draw 600mA @ 3.3V.

Note that the Vicor VI-J00 or VI-200 series has a significantly lower quiescent draw than the Micro, and a footprint allowing either converter is on BMS 7-1-1 and later.

Voltage Sense

Because the MCU sits on the same ground as the battery pack as of BMS 7, measuring the voltages of the pack, HV bus, and array became simpler. The LTC6082 opamp, used as a buffer, was chosen for its low input bias current (with such large resistances in the voltage divider, in the range of 100k-1M Ohm, even a small input bias current on an op-amp leads to a large error. The output of the opamp buffer is sent to the precharge check circuitry (which uses a comparator that can have a reasonably large input current, because the sense circuitry is buffered). The output is also sent to analog input pins on the MCU, which require a large input current.

A filtering capacitor is placed on the output of the resistor divider. An RC for the filter is chosen such that switching noise is not amplified, and that it is significantly smaller than the RC of the precharge circuit (i.e. 2 orders of magnitude). 100 uSec is a reasonable RC constant. A 2.2nF capacitor is appropriate for this location.

ADC Effective Resolution

This link explains the difference between effective resolution and ENOB: http://www.edn.com/design/analog/4373658/Understanding-noise-ENOB-and-effective-resolution-in-ADCs

Noise measurements on the bench can be found here (for bms 7.0.0) and here (for bms 7.1.1).

[here](https://docs.google.com/spreadsheet/ccc?key=0AmVyg7HGPlLkdDVjOEJwdmphWmZJRlJwaGdTWnFKLWc\&usp=sharing)

[here](https://docs.google.com/spreadsheet/ccc?key=0AmVyg7HGPlLkdGpTc2FEVDFCbk1yVVVoeGt1em9kaEE\&usp=sharing)

Thermal Issues

Placing the board inside a waterproof box causes thermal concerns: See this link for calculations. Placed upside-down (with minimal load, drawing 49.5mA @ 141.5V) and at an ambient temperature of 25.4 C the Vicor's body rises to a temperature of 45.2 C. Drawing 50W output, .47A @ 138.7V, Tamb = 25.5, Tbody = 56. Under no load, this corresponds to \~2.8 K/W. Under load, this corresponds to \~2.3 K/W.

Sam suggests a 4-wire fan(s) for airflow through the pack. He is a believer in oversizing cooling for systems because you don't have to use all the fan power that you put in. He gave me a nice explanation of why a 4-wire fan is best:

A 4 wire fan is designed to be speed controlled. A 3 wire fan is not. A 4 wire fan is basically pinning out the gate control for the drive fets, so you can directly control how fast it's going, without turning off the fan controller itself. With a 2 or 3 wire fan, you really can't get speed feedback if you're pwming its power because you're simultaneously turning off the internal controller. Theres a turn on lag time when you are actually turning the power on and off to the fan as well, so you can only really do it at around 10hz or so, so you end up with an annoying pulsing sound. 4 wire fans tend to also be of much more robust design in general since their main market is for servers and not for consumer desktops. Bottom line is that the 4 wire fans are really designed for variable speed control and otherwise its kind of a hack.

This fan is nice because it is 4-wire, just slightly smaller than the height of the pack, and can run directly from the 24v bus. It may be too thick.

[This](http://www.digikey.com/product-detail/en/OD9238-24HBVXC10A/1053-1288-ND/2621193)

Ordering Parts

Parts not on the Altium BOM are listed here.

[here](https://docs.google.com/spreadsheet/ccc?key=0AmVyg7HGPlLkdDlmSG05THUyQ0VHWTNoS0ctUERBY1E\&usp=sharing)

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1zBqV4gAoI_pdw97xL8S_ppft0wYxGmzE#list)
