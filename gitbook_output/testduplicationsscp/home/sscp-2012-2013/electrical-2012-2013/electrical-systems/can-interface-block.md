# SSCP - CAN interface block

# CAN interface block

Requirements

In addition to providing a CAN transceiver, the CAN block needs to protect the transceiver against ESD and provide an optional 120 ohm split termination. Some form of edge slew control must be used to reduce EMI. Unlike in previous iterations, the interface block will provide no galvanic isolation.

Proposed solutions

CAN transceiver

TI is surprisingly good at making interface chips and their CAN transceivers are no exception. The SN65HVD235 offers a convenient 3.3v logic level while being 5v tolerant, but also offers programmable slew rates and a standby mode. Now that isolation is no longer a requirements, it's feasible to use the standby pin to reduce power consumption when a board is not transmitting. In almost all applications a 10k slew rate limiting resistor is appropriate.

[ SN65HVD235](http://www.ti.com/product/sn65hvd235)

ESD protection

A low-cost packaged CAN bus ESD suppression diode makes meeting this requirement easy.

[ ESD suppression diode](http://search.digikey.com/us/en/products/PESD2CAN,215/568-4147-1-ND/1589996)

Optional split termination

We never know when a board is going to be the end node of a CAN bus, so it's convenient to be able to flip a switch and change termination. Split termination means using two resistors with a capacitor to ground to make the termination resistance. CAN is terminated with two 60.4 ohm resistors in series with a 10nF capacitor to ground.

[ switch](http://search.digikey.com/us/en/products/204-211ST/CT204211ST-ND/267310)

