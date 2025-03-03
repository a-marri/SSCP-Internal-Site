# SSCP - Tire Pressure Monitoring

# Tire Pressure Monitoring

Project Owner: Vincent Sparacio

Overview:

This board is responsible to monitoring the pressure of all the vehicle tires and sending out CAN messages to convey this to telemetry.

How this is done needs to be figured out. How will it measure the tire pressure? How will it convey this to the rest of the car? If it's wirelessly, does it have good signal even in the EMI of the car? How will the sensor be powered?

Proposed Solutions:

RF Link

    After doing tests with 2.4ghz wireless, no issues were detected from running the car with very close proximity to transmitters/receivers. In order to maintain a simplistic approach, and evaluating the pros and cons of a discreet transceiver chip, decided to use the SPZB32W1x2.1 instead of a Nordic Transceiver. First among the considerations was wireless viability. There was no meaningful difference between the two, so other factors had to be evaluated. Size and power consumption were the other two concerns. Size has to be small due to placement in machined recesses in the rims.This encouraged the use of a single chip. Lastly the power consumption of just the Nordic chip was higher the SPZB32W1x2.1, without the added issue of still needing an on board microcontroller. Thus the SPZB32W1x2.1 was settled on.

Pressure Sensor 

    MS5541-CM from Measurement Specialties. With an absolute maximum of 435 pounds per inch and an operating temperature of up to 185 degrees should be perfectly suitable for the conditions inside the tire. 

Power Concerns

    The sensor must be extremely low power consumption in order to provide constant data without need of replacement. While sleeping, the sensors would consume ~500 nanoamps. for the 2 milliseconds required to collect data at ~7.5 milliamps, and 2 milliseconds to transmit is at ~32 milliamps. Cycling at the rate associate with the pressure-pros of 5 minutes, means that a 47 milliamp-hour coin cell battery would last almost indefinitely. For size-constraint issues, a 10mm diameter coin cell battery was chosen for the sensor. This equates to a 30 milliamp-hour battery as opposed to 47 milliamp-hour. This should still be more than enough and replacement is trivial due to the placement of the battery holder at the top of the module. Due to the low current output of the battery, several capacitors have been connected in parallel to supply needed current to the module.

Bringup: 

The power concerns appeared in force: The battery chosen has a nominal output current of 0.1 mA and its source resistance increases greatly as the board tries to draw more power. In particular, as the SPZB32W1x2.1 and sensor draw mA+ before they're configured, and the capacitors draw a large inrush of current, the battery voltage was dropping rapidly (approximately 100mV/second). Because the nominal output voltage of the battery is 3V, and the minimum input voltage of the SPZB32W1x2.1 is 2.8V, this quickly resulted in an inoperable system. When powered by 3.3V off of a Xantrex, the board is programmable via IAR. We also had to solder the programming wires directly to the SPZ package pins, due to the difficulty in crimping programming connectors and potential SWD pinout errors.

Suggested changes: It may be worthwhile to replace the coin cell with a larger lithium ion polymer battery, for instance, this battery from Tenergy. It's larger (21mm x 12mm x 5mm) and heavier (2g) but can source 16mA continuous up to 80mA in pulses (as we'd be doing).  However, I'd be more worried about the discharge temperature range at this point. Also, since this cell is rechargeable (even if we wouldn't be using it as such) I'd need to verify it with the rules. 

[ this battery from Tenergy](http://www.tenergy.com/Tenergy-Lithium-Ion-Polymer-3-7V-80mAh-501221-Rechargeable-Battery)

If we have to stick with the current battery, we'd need to find a way to charge a large capacitance slowly (.1mA) at the start, and do the data gathering and transmitting very slowly and separately. (with 20+ second waits between any operation). With the 32mA current draw and 2 millisecond time, and wanting a drop of less than 150mV from 3V (to stay above the 2.8V minimum), at least 440uF of capacitance are required. If a 30K ohm resistor is chosen to limit the short circuit inrush current to the capacitor, the RC time constant of this circuit is 13.2 seconds. This means that at startup, the circuit will need 45+ seconds to charge without sensing or transmission, and will need 13 seconds or so between any high-current operation to give the caps time to recharge.  

Size:

750x1315mil

Batteries:

http://www.digikey.com/product-detail/en/CR-1025%2FBN/P031-ND/269738

http://www.digikey.com/product-detail/en/CR1025/N031-ND/704849

Battery Holder:

http://www.digikey.com/product-detail/en/BHX1-1025-SM/BHX1-1025-SM-ND/2194753

[](https://drive.google.com/folderview?id=13GaqvaQTKjf0SczwgKZrjJ8Jm08lQ2ED)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=13GaqvaQTKjf0SczwgKZrjJ8Jm08lQ2ED#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=13GaqvaQTKjf0SczwgKZrjJ8Jm08lQ2ED#list" frameborder="0"></iframe>

