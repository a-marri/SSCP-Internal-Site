# SSCP - Picking Parts

# Picking Parts

Selecting parts can be a rather difficult thing for beginners. Digikey provides a great place to pick most passive component. Here a just a few things you should consider when picking parts :

[ Digikey](http://www.digikey.com/)

### Capacitors:

[](#h.oe372lk67h36)

Rated Capacitance

Package: should be 0805 unless there is a good reason for something else.

Rated Voltage: at least 20% above the desired voltage rail voltag

Material: Ceramic (probably want this), Electrolytic, etc.

Instantaneous current sourcing/ESR

Breakdown situation: Get automotive rated caps

### Resistors:

[](#h.kuh18j5gwry0)

Package: should be 0805 unless there is a good reason for something else.

Resistance

Power Dissipation

Tolerance (probably 1% or 5%) -how accurate does this resistor need to be?

Struggling to find the right ratio? Try this. Use E96 values.

[ this](http://jansson.us/resistors.html)

### Inductors:

[](#h.mkib3fnezlng)

Inductance

Core Material: Probably want ferrite core

Saturation Current: Above the max current through the inductor

DCR: Resistance at DC

### Fets:

[](#h.ax2oqknkg76h)

Voltage rating: Vds

Current Rating: Ids

Type: p or n channel

On resistance

Not as big of a concern:

Gate capacitance, Response time

### Diodes:

[](#h.mwi5pq2d2655)

Forward voltage drop

Reverse break down voltage

Type: Zener, Shotcky

Power Rating

Reverse recovery time

### Op Amps:

[](#h.l9nobvx4h23i)

For general use the LTC1678 has good all around performance specs.

For applications that require excellent DC performance where the gain bandwidth product is not important use the LTC2051

For Instrumentation Amplifiers: The LTC2053 is a instrumentation amp with good dc performance and high CMRR

### Linear Regulator:

[](#h.yj8ziaz3ijg7)

Probably want this one.

[ this](http://www.ti.com/product/tps7a4901)

There is a matched negative regulator for bipolar supplies. 

ICs:

Input/output voltage

Control signals

Complexity of design/topology

Power draw

Pin arrangement: No BGAs, avoid DFN and try to avoid QFN

### Voltage References:

[](#h.ehxv92l7tdwf)

For general applications, or powering the analog rail on an STM use a LT1461, if you need the

[LT1461](http://cds.linear.com/docs/Datasheet/1461f.pdf)

best voltage reference made by mankind use the LTC6655. Current sense on BMS is the only 

[ LTC6655](http://cds.linear.com/docs/Datasheet/6655fa.pdf)

application that requires this kind of performance. 

### PGA:

[](#h.jiolt1jtuljq)

Zero Drift TI PGA

[ TI PGA](http://www.ti.com/lit/ds/symlink/pga112.pdf)

Linear Regulators for Analog Applications:

Since there are many components on the car which are hard switching (MPPTs, Vicor, Motorcontroller) there is quite a bit of switching noise that propagates onto the LV bus. The most important characteristic then of picking a good LDO for analog applications is the PSSR of the linear regulator. Currently the recommended LDOs for analog applications are the TI TPS7A49xx for the positive rails and the complimentary TPS7A30xx for the negative rails. 

