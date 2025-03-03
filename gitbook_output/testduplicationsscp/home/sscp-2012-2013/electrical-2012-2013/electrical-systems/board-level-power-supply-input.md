# SSCP - Board-level power supply input

# Board-level power supply input

Requirements

Bus-supplied power from the car is not tightly specified. Long, inductive cable runs, distributed loads, and user-access make the behavior of this bus somewhat unpredictable. It's important to offer reverse-polarity protection, overcurrent protection, ESD protection, and overvoltage protection to any power inlet that connects to this bus. Further, it's very helpful for diagnostics and systems-level understanding that a board be able to measure its own power consumption.

Proposed solutions

Simple overcurrent protection

A simple PTC fuse provides for basic protection while not being annoying to replace. Specifying them is tricky. Notice the the hold current is the leakage through the device when it has tripped, and that the trip times at the rated trip currents are measured in long seconds. Fuses are not really designed to protect against short-term overcurrents, but are really designed to prevent your wiring harnesses from going up in smoke.

[ PTC fuse](http://search.digikey.com/us/en/products/MF-USMF010-2/MF-USMF010-2CT-ND/1014929)

Simple reverse voltage protection

A basic Schottky diode can provide excellent reverse polarity protection on the input. Unfortunately, it also consumes power roughly proportionately to the load current at the bus voltage. In most boards this will not be a concern as they draw such a trivial amount of bus current as to make it inconsequential. All three power modules include reverse voltage protection.

[ Schottky diode](http://search.digikey.com/us/en/products/MBRA160T3G/MBRA160T3GOSCT-ND/920610)

Complicated UV/OV/OC/RV protection

Linear makes the LT4356, a convenient MOSFET controller that handles almost all of the error cases that can come down the line. It should be used where a diode drop for reverse voltage protection is unacceptable, or where there is a reasonable expectation that the bus will be sufficiently misbehaved that a TVS could not soak up all overvoltage transients. The medium and high current version of the power modules include the LT4356.

[ LT4356](http://www.linear.com/product/LT4356-1%2520and%2520-2)

EMI filtering

Depending on the expected load current, a simple integrated LC filter is likely the best bet. This will do some minor filtering of the line before it enters the board, preventing RF noise from propagating in either direction.

[ integrated LC filter](http://search.digikey.com/us/en/products/ELK-E103FA/P9878CT-ND/227675)

ESD filtering

A bidirectional TVS diode will clamp any spikes by dissipating power. In a true automotive system, these diodes would be rated for much higher voltages than the one linked. In a solar car, however, the bus is generally better regulated and the expected energy dissipation in a more tightly-rated TVS is low enough to make this selection practical.

[ TVS diode](http://search.digikey.com/us/en/products/SMA6J28CA-TR/497-7888-1-ND/1883785)

Current sensing

High side current-sense amplifiers with shunt resistors make it easy to do measuring and level shifting. Another option is an I2C voltage and current monitoring IC. Consider using the current sensing module; it integrates the LT6102 current sense amplifier and LT6004 opamp to provide a convenient analog output from 0-3.3v, proportional to the current draw.

[ current-sense amplifiers](http://www.linear.com/product/LT6106)

[ I2C voltage and current monitoring IC](http://www.linear.com/product/LTC4151)

[ current sensing module](/stanford.edu/testduplicationsscp/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/current-sensing-block)

