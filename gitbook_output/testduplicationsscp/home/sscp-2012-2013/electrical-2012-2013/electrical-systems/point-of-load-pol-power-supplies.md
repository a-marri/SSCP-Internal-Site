# SSCP - Point-of-Load (POL) Power Supplies

# Point-of-Load (POL) Power Supplies

Requirements

The solar car CAN bus provides power at a higher voltage than is convenient for microprocessors and their supporting hardware. Point of load down-conversion of that power to a lower voltage is relatively efficient and ensures that the power delivered to sensitive loads is well-regulated and clean.

Currently there are no fixed requirements for load current or output voltage. A reasonable expectation is that different instances of the power supply hardware will be asked to supply from 1.8 to 12 volts for various car systems. It's not unreasonable to have several point-of-load power supply designs that span a range of output currents, enabling the use of the most efficient design for a particular load.

POL supplies should operate from a nominal input that is 24 to 28 volts, but that can swing from 18 to 36 volts and suffer high voltage inductive and ESD transients. The designs should be available as schematic and layout blocks ready to copy-and-paste in to another design with minimal modification (ie, changing a feedback resistor).

A mechanism must exist for the target device to report, at minimum, its load current. Preferably it will also measure its input voltage and compute its power consumption.

Spice and Validation:

The output ripple of the power supplies should stay within 3% of the desired operating voltage under unchanging conditions. The output should not vary more than 5% when a load transient occurs. To meet these specs, more capacitance may be added to the output.

The output should also be monitored during turn on and turn off, making sure the above specs are met whether the load on the output is nothing or the full load the system can handle. It is also not a bad idea to monitor the input during these conditions to ensure nothing strange happens. Another condition to test for it what happens when there is a short on the output side (does the short detect work and how fast).

Power Modules

We currently have two discreet power modules for dropping into other circuit layouts:

* The Low Current Module provides up to 100 mAThe Medium Current Module provides up to 1A using the LT3695 bucking regulator.
* The Low Current Module provides up to 100 mA
* The Medium Current Module provides up to 1A using the LT3695 bucking regulator.

* The Low Current Module provides up to 100 mA
* The Medium Current Module provides up to 1A using the LT3695 bucking regulator.

The Low Current Module provides up to 100 mA

[ Low Current Module](/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/low-current)

The Medium Current Module provides up to 1A using the LT3695 bucking regulator.

[ Medium Current Module](/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/medium-current)

Module Pinout:

The modules fit in a standard 600-mil DIP24 socket. They each have the same standardized pinout, corresponding to the diagram below:

The diagram corresponds to a DIP24 socket as seen from above (looking down on the socket, on the side the module plugs into).

Module Voltage Selection

Placing a resistor from FB to GND external to the module will select the regulator output voltage. DO NOT USE the medium module without the feedback resistor! Doing so will lead to undefined output behavior and can destroy your circuit. Please choose your feedback resistor carefully, and as always check the output voltage of the module before installing it in your final circuit.

According to the datasheet of the LT3695 (and matching the other modules' regulators):

We have standardized the low-, medium- and high-power boards to share the high-side resistor value of 316k. Thus the equation for Vout as a function of R2, the low-side resistor, becomes

Vout = 0.8V + (252.8k / R2)

or

R2 = 252.8k / (Vout - 0.8)

Here's a handy table of some commonly-needed feedback resistances:

Table of FB Resistances versus Regulator Output Voltage

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

The High-Current Power Supply

The high-current supply is not provided as a discreet module, due to the high current requirements that would overload standard socket connectors. Instead, it is a drop-in schematic and parts collection that you can incorporate into a board design that needs it.

[ high-current supply](/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/high-current)

Archived (Outdated) Plans for Modules:

Proposed solutions

Low Current (up to 100 mA)

[Low Current (up to 100 mA)](/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/low-current)

ICs / modules

    LTC3631-3.3 buck converter

[LTC3631](http://www.linear.com/product/LTC3631)

    Current sensing module

Discrete components

    TVS to protect bus spikes

[ TVS to protect bus spikes](http://search.digikey.com/us/en/products/SMA6J28CA-TR/497-7888-1-ND/1883785)

    TVS to protect against ESD

[ TVS to protect against ESD](http://search.digikey.com/us/en/products/SMAJ85CA/SMAJ85CABCT-ND/2253558)

    Schottky for reverse polarity protection

[ Schottky for reverse polarity protection](http://search.digikey.com/us/en/products/SS1150-LTP/SS1150-LTPMSCT-ND/2423310)

    ferrite bead and  input capacitor or integrated LC filter?

[ferrite bead](http://search.digikey.com/us/en/products/FBMH3225HM202NT/587-1754-1-ND/1147079)

[input capacitor](http://search.digikey.com/us/en/products/GCM188R72A103KA37D/490-4781-1-ND/1641700)

[ i](http://goog_1211727336)

[ntegrated LC filter](http://search.digikey.com/us/en/products/ELK-E103FA/P9878CT-ND/227675)

Medium Current (100-500mA)

ICs

    LT3502 buck converter 

[LT3502](http://www.linear.com/product/LT3502)

    Two alternatives:  LT3973 and LT3695 We will probably be using the LT3695.

[LT3973](http://cds.linear.com/docs/Datasheet/3973f.pdf)

[LT3695](http://cds.linear.com/docs/Datasheet/3695fa.pdf)

    LT4356 for voltage protection, as per fig. 7 & 8 of datasheet (possibly implemented as a module)

[LT4356](http://cds.linear.com/docs/Datasheet/4356fa.pdf)

    Current sensing module

Discrete components

    TVS to protect against ESD

[TVS to protect against ESD](http://search.digikey.com/us/en/products/SMAJ85CA/SMAJ85CABCT-ND/2253558)

    ferrite bead and input capacitor or integrated LC filter?

[ferrite bead](http://search.digikey.com/us/en/products/FBMH3225HM202NT/587-1754-1-ND/1147079)

[input capacitor](http://search.digikey.com/us/en/products/GCM188R72A103KA37D/490-4781-1-ND/1641700)

[i](https://sites.google.com/site/susolarcar/goog_1211727336)

[ntegrated LC filter](http://search.digikey.com/us/en/products/ELK-E103FA/P9878CT-ND/227675)

High Current (up to 5A)

ICs

    LT3690 buck converter 

[LT3690](http://www.linear.com/product/LT3690)

    LT4356 for voltage protection, as per fig. 7 & 8 of datasheet (possibly implemented as a module)

[LT4356](http://cds.linear.com/docs/Datasheet/4356fa.pdf)

    Current sensing module

Discrete components

    TVS to protect against ESD

[TVS to protect against ESD](http://search.digikey.com/us/en/products/SMAJ85CA/SMAJ85CABCT-ND/2253558)

    ferrite bead and input capacitor or integrated LC filter?

[ferrite bead](http://search.digikey.com/us/en/products/FBMH3225HM202NT/587-1754-1-ND/1147079)

[input capacitor](http://search.digikey.com/us/en/products/GCM188R72A103KA37D/490-4781-1-ND/1641700)

[i](https://sites.google.com/site/susolarcar/goog_1211727336)

[ntegrated LC filter](http://search.digikey.com/us/en/products/ELK-E103FA/P9878CT-ND/227675)

    

Proposed building blocks

Low current (100mA)

The LTC3631 is fairly efficient over a very wide output current range, is rated to 125°C and is extremely simple. It is a monolithic synchronous buck and thus requires only a few external components. One module would be used for each required output voltage. Most boards will only need 3.3 volts.

[LTC3631](http://www.linear.com/product/LTC3631)

Medium current (500mA)

The LT3502 is less efficient, particularly at low output current, but is very high frequency and should be able to make nice, clean power. It is available in easy-to-use packages and is rated to 125°C. The  LT3973 and LT3695 are more efficient at will probably be used instead of the LT3502.

[ LT3502](http://www.linear.com/product/LT3502)

[LT3973](http://cds.linear.com/docs/Datasheet/3973f.pdf)

[LT3695](http://cds.linear.com/docs/Datasheet/3695fa.pdf)

High current (4A)

The LT3690 is fairly efficient, but only with load currents >500mA. This might be useful for powering larger loads like a motor controller with fans.

[ LT3690](http://www.linear.com/product/LT3690)

Reverse voltage protection

Most boards will have a fairly minimal bus current draw; usually less than 100mA. This lends itself nicely to using a simple diode for reverse voltage blocking. For high current applications, using an arrangement like figure 7 or 8 (PDF) will be more appropriate.

[ diode](http://search.digikey.com/us/en/products/SS1150-LTP/SS1150-LTPMSCT-ND/2423310)

[ figure 7 or 8](http://cds.linear.com/docs/Datasheet/4356fa.pdf)

Overvoltage, undervoltage, and overcurrent protection

Surge stopping chips like the LT4356 make it easy to regulate the bus voltage to a safe level. This chip also protects again load overcurrent using a shunt. Window the steady-state operating range of the load from 18-30v with the undervoltage lockout and the overvoltage regulation. Pair the chip with an appropriate shunt to limit the input current to a safe level for the expected load.

[ LT4356](http://cds.linear.com/docs/Datasheet/4356fa.pdf)

EMI and ESD suppresion

A bidirectional TVS diode will suppress ESD and very high voltage inductive spikes. A ferrite bead and a very small input capacitor will suppress incoming and outgoing RF noise generated locally by switching edges and remotely by radio stations and other electronics.

[ bidirectional TVS diode](http://search.digikey.com/us/en/products/SMAJ85CA/SMAJ85CABCT-ND/2253558)

[ ferrite bead](http://search.digikey.com/us/en/products/FBMH3225HM202NT/587-1754-1-ND/1147079)

[ input capacitor](http://search.digikey.com/us/en/products/GCM188R72A103KA37D/490-4781-1-ND/1641700)

Input voltage and current measurement

The LTC6102HV will survive voltages just as high as the LT4356 protection chip and can use the same shunt. The resistor divider ratio should be scaled to ensure reasonable dynamic range on the output of the device for the expected load currents. Most boards will likely have a processor with an ADC scaled for a 3.3v input range.

[LTC6102HV](http://www.linear.com/product/LTC6102)

A simple resistor divider can scale down the input voltage. Measuring a range from 0-36v seems reasonable. Use 0.1% resistors to ensure accuracy and a small capacitor to filter the signal.

Both outputs will need to be buffered before going in to the ADC to avoid inaccuracy due to the input bias current on the ADC. A slow, rail-to-rail input and output opamp like the LT6004 will work nicely.

[ LT6004](http://www.linear.com/product/LT6004)

[](https://drive.google.com/folderview?id=1Wcb4ScdD7lpdp3R4CF0TLYxDHuYEw6fe)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1Wcb4ScdD7lpdp3R4CF0TLYxDHuYEw6fe#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1Wcb4ScdD7lpdp3R4CF0TLYxDHuYEw6fe#list" frameborder="0"></iframe>

