# SSCP - Digital Current Sense

# Digital Current Sense

Purpose

Every board should have the capability of measuring and reporting its power draw for power optimisation and debugging purposes.

Specifications

This is a block that will be integrated into every power module and report over I2C. The highest power module of which this is intended to be a part is the high power one, which outputs 3.3V at 4A. Including a margin of error, this current sense needs to be capable of measuring 0.75A.

Design decisions

The circuit is a high side current sense. Since all on-board converters downstream of BMS are non-isolated, there is no particular reason to use a high-side current sense other than the availability of a convenient chip. In this case we used a LTC4151 owing to its extremely simple interface and suitability for our high side voltage (its operation region is 7-80V), in conjunction with a sense resistor whose value depends on the highest expected current (3.3 Ohms in the case of the low power module).

Interface

The sense resistor is the only external component required for this block to work, and should be placed between Vcc and Vsense-.

