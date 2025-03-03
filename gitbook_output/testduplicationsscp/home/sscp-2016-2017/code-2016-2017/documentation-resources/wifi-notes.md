# SSCP - Wifi Notes

# Wifi Notes

11/17/2016: WiFi Discussion w/ Eric

Present: Harrison, Eric

WiFi Infrastructure: https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2014-2015/code-2014-2015/wifi-infrastructure

[ https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2014-2015/code-2014-2015/wifi-infrastructure](/stanford.edu/testduplicationsscp/home/sscp-2014-2015/code-2014-2015/wifi-infrastructure)

* Hardware Overview: we use PicoStation2HP, AKA Ubiquiti instance, as source of WiFi communicationIMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)Testing Ubiquiti instances? we have at least three or four in the shop, we can search for themAlternatively, find a new, updated version from Ubiquiti itselfUbiquiti instances: they are high-powered wireless access pointsHow can we potentially reduce power?
* Hardware Overview: we use PicoStation2HP, AKA Ubiquiti instance, as source of WiFi communicationIMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)Testing Ubiquiti instances? we have at least three or four in the shop, we can search for themAlternatively, find a new, updated version from Ubiquiti itselfUbiquiti instances: they are high-powered wireless access pointsHow can we potentially reduce power?
* IMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.
* Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)
* IMU address (10.0.0.2)
* Ubiquiti (10.0.0.3)
* Testing Ubiquiti instances? we have at least three or four in the shop, we can search for them
* Alternatively, find a new, updated version from Ubiquiti itself
* Ubiquiti instances: they are high-powered wireless access points
* How can we potentially reduce power?

1. Hardware Overview: we use PicoStation2HP, AKA Ubiquiti instance, as source of WiFi communicationIMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)Testing Ubiquiti instances? we have at least three or four in the shop, we can search for themAlternatively, find a new, updated version from Ubiquiti itselfUbiquiti instances: they are high-powered wireless access pointsHow can we potentially reduce power?
2. IMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.
3. Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)
4. IMU address (10.0.0.2)
5. Ubiquiti (10.0.0.3)
6. Testing Ubiquiti instances? we have at least three or four in the shop, we can search for them
7. Alternatively, find a new, updated version from Ubiquiti itself
8. Ubiquiti instances: they are high-powered wireless access points
9. How can we potentially reduce power?

Hardware Overview: we use PicoStation2HP, AKA Ubiquiti instance, as source of WiFi communication

1. IMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.
2. Two IP addresses:IMU address (10.0.0.2)Ubiquiti (10.0.0.3)
3. IMU address (10.0.0.2)
4. Ubiquiti (10.0.0.3)
5. Testing Ubiquiti instances? we have at least three or four in the shop, we can search for them
6. Alternatively, find a new, updated version from Ubiquiti itself
7. Ubiquiti instances: they are high-powered wireless access points
8. How can we potentially reduce power?

IMU board communicates over ethernet to Ubiquiti instance WiFi router. Computers can connect to Ubiquiti instance to transmit packets.

Two IP addresses:

1. IMU address (10.0.0.2)
2. Ubiquiti (10.0.0.3)

IMU address (10.0.0.2)

Ubiquiti (10.0.0.3)

Testing Ubiquiti instances? we have at least three or four in the shop, we can search for them

Alternatively, find a new, updated version from Ubiquiti itself

Ubiquiti instances: they are high-powered wireless access points

How can we potentially reduce power?

* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficient
* companies don’t really optimize for this
* We need to look into power draw

* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficient
* companies don’t really optimize for this
* We need to look into power draw

* Access point is inherently power inefficientcompanies don’t really optimize for thisWe need to look into power draw
* Access point is inherently power inefficient
* companies don’t really optimize for this
* We need to look into power draw

1. Access point is inherently power inefficient
2. companies don’t really optimize for this
3. We need to look into power draw

Access point is inherently power inefficient

companies don’t really optimize for this

We need to look into power draw

* Other low-power options (some things to consider)
* Other low-power options (some things to consider)
* Other low-power options (some things to consider)

1. Other low-power options (some things to consider)
2. Other low-power options (some things to consider)

1. Other low-power options (some things to consider)

Other low-power options (some things to consider)

* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radio
* A drop in replacement for Ubiquiti (WiFi router that happens to be low power)
* Change access point on car to client-modeHowever, can this potentially increase delay?
* However, can this potentially increase delay?
* Dropping in WiFi module (Internet of things explosion)

* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radio
* A drop in replacement for Ubiquiti (WiFi router that happens to be low power)
* Change access point on car to client-modeHowever, can this potentially increase delay?
* However, can this potentially increase delay?
* Dropping in WiFi module (Internet of things explosion)

* Zigbee: low-power radioA drop in replacement for Ubiquiti (WiFi router that happens to be low power)Change access point on car to client-modeHowever, can this potentially increase delay?Dropping in WiFi module (Internet of things explosion)
* Zigbee: low-power radio
* A drop in replacement for Ubiquiti (WiFi router that happens to be low power)
* Change access point on car to client-modeHowever, can this potentially increase delay?
* However, can this potentially increase delay?
* Dropping in WiFi module (Internet of things explosion)

1. Zigbee: low-power radio
2. A drop in replacement for Ubiquiti (WiFi router that happens to be low power)
3. Change access point on car to client-modeHowever, can this potentially increase delay?
4. However, can this potentially increase delay?
5. Dropping in WiFi module (Internet of things explosion)

Zigbee: low-power radio

A drop in replacement for Ubiquiti (WiFi router that happens to be low power)

Change access point on car to client-mode

1. However, can this potentially increase delay?

However, can this potentially increase delay?

Dropping in WiFi module (Internet of things explosion)

* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPI
* Could drop requirement for ethernet interface, which uses a bit of power

* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPI
* Could drop requirement for ethernet interface, which uses a bit of power

* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPI
* Could drop requirement for ethernet interface, which uses a bit of power

* Have the module communicate over IsoSPICould drop requirement for ethernet interface, which uses a bit of power
* Have the module communicate over IsoSPI
* Could drop requirement for ethernet interface, which uses a bit of power

1. Have the module communicate over IsoSPI
2. Could drop requirement for ethernet interface, which uses a bit of power

Have the module communicate over IsoSPI

Could drop requirement for ethernet interface, which uses a bit of power

* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate

* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate

* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate
* TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate

1. TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate

TODO: measure the power draw at different states, e.g. when it is idle or when it is transmitting at full rate

* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant
* One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

1. One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

One experiment in past: run the ubiquiti instance with lower transmit power (i.e. lower range), use a directional antenna. These changes decreased usage by a few watts, but not too significant

* How to test ubiquiti instace:
* How to test ubiquiti instace:
* How to test ubiquiti instace:

1. How to test ubiquiti instace:
2. How to test ubiquiti instace:

1. How to test ubiquiti instace:

How to test ubiquiti instace:

* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMU
* Ubiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24V
* Voltage conversion may cause inefficiencies
* Power regulator, which may convert 24V to something lower
* The instance itself uses 24V
* Power over ethernet injector

* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMU
* Ubiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24V
* Voltage conversion may cause inefficiencies
* Power regulator, which may convert 24V to something lower
* The instance itself uses 24V
* Power over ethernet injector

* We should measure power draw of IMUUbiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24VPower over ethernet injector
* We should measure power draw of IMU
* Ubiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24V
* Voltage conversion may cause inefficiencies
* Power regulator, which may convert 24V to something lower
* The instance itself uses 24V
* Power over ethernet injector

1. We should measure power draw of IMU
2. Ubiquiti is powered over ethernetVoltage conversion may cause inefficienciesPower regulator, which may convert 24V to something lowerThe instance itself uses 24V
3. Voltage conversion may cause inefficiencies
4. Power regulator, which may convert 24V to something lower
5. The instance itself uses 24V
6. Power over ethernet injector

We should measure power draw of IMU

Ubiquiti is powered over ethernet

1. Voltage conversion may cause inefficiencies
2. Power regulator, which may convert 24V to something lower
3. The instance itself uses 24V

Voltage conversion may cause inefficiencies

Power regulator, which may convert 24V to something lower

The instance itself uses 24V

Power over ethernet injector

* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet input
* Ethernet input
* Power input
* Power over ethernet input
* IMU board has power over ethernet injector circuit, built in
* Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector
* Baseline: test IMU without Ubiquiti attached
* Test would measure power draw of Ubiquiti + ethernet setup on IMU board

* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet input
* Ethernet input
* Power input
* Power over ethernet input
* IMU board has power over ethernet injector circuit, built in
* Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector
* Baseline: test IMU without Ubiquiti attached
* Test would measure power draw of Ubiquiti + ethernet setup on IMU board

* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet input
* Ethernet input
* Power input
* Power over ethernet input
* IMU board has power over ethernet injector circuit, built in
* Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector
* Baseline: test IMU without Ubiquiti attached
* Test would measure power draw of Ubiquiti + ethernet setup on IMU board

* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet inputIMU board has power over ethernet injector circuit, built inWant to test power draw of IMU since it has different power circuit compared to power over ethernet injectorBaseline: test IMU without Ubiquiti attachedTest would measure power draw of Ubiquiti + ethernet setup on IMU board
* AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet input
* Ethernet input
* Power input
* Power over ethernet input
* IMU board has power over ethernet injector circuit, built in
* Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector
* Baseline: test IMU without Ubiquiti attached
* Test would measure power draw of Ubiquiti + ethernet setup on IMU board

1. AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)Ethernet inputPower inputPower over ethernet input
2. Ethernet input
3. Power input
4. Power over ethernet input
5. IMU board has power over ethernet injector circuit, built in
6. Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector
7. Baseline: test IMU without Ubiquiti attached
8. Test would measure power draw of Ubiquiti + ethernet setup on IMU board

AC adaptor into this injector (there’s a separate thing made by Ubiquiti, which we never used)

1. Ethernet input
2. Power input
3. Power over ethernet input

Ethernet input

Power input

Power over ethernet input

IMU board has power over ethernet injector circuit, built in

Want to test power draw of IMU since it has different power circuit compared to power over ethernet injector

Baseline: test IMU without Ubiquiti attached

Test would measure power draw of Ubiquiti + ethernet setup on IMU board

* AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti
* AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti
* AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti

1. AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti
2. AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti

1. AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti

AirOS: stripped down linux distribution that Ubiquiti maintains. Runs on the ARM microcontroller on the Ubiquiti

* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interface
* Used to specify parameters for the Ubiquiti instance

* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interface
* Used to specify parameters for the Ubiquiti instance

* Main selling point: web interfaceUsed to specify parameters for the Ubiquiti instance
* Main selling point: web interface
* Used to specify parameters for the Ubiquiti instance

1. Main selling point: web interface
2. Used to specify parameters for the Ubiquiti instance

Main selling point: web interface

Used to specify parameters for the Ubiquiti instance

* Software
* Software

1. Software

Software

* Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP libraryOur code
* Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP libraryOur code
* Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP library
* LwIP: provides layers for communicationnetconf.c: also part of the LwIP library
* netconf.c: also part of the LwIP library
* Our code

* Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP libraryOur code
* Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP library
* LwIP: provides layers for communicationnetconf.c: also part of the LwIP library
* netconf.c: also part of the LwIP library
* Our code

1. Library codeLwIP: provides layers for communicationnetconf.c: also part of the LwIP library
2. LwIP: provides layers for communicationnetconf.c: also part of the LwIP library
3. netconf.c: also part of the LwIP library
4. Our code

Library code

1. LwIP: provides layers for communicationnetconf.c: also part of the LwIP library
2. netconf.c: also part of the LwIP library

LwIP: provides layers for communication

1. netconf.c: also part of the LwIP library

netconf.c: also part of the LwIP library

Our code

* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instance
* LwIP: provides layers for communication. Use UDP to send
* We don’t have IP address for Ubiquiti instance within in code

* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instance
* LwIP: provides layers for communication. Use UDP to send
* We don’t have IP address for Ubiquiti instance within in code

* EthWriter: communicating over ethernet to the Ubiquiti instanceLwIP: provides layers for communication. Use UDP to sendWe don’t have IP address for Ubiquiti instance within in code
* EthWriter: communicating over ethernet to the Ubiquiti instance
* LwIP: provides layers for communication. Use UDP to send
* We don’t have IP address for Ubiquiti instance within in code

1. EthWriter: communicating over ethernet to the Ubiquiti instance
2. LwIP: provides layers for communication. Use UDP to send
3. We don’t have IP address for Ubiquiti instance within in code

EthWriter: communicating over ethernet to the Ubiquiti instance

LwIP: provides layers for communication. Use UDP to send

We don’t have IP address for Ubiquiti instance within in code

* Ubiquiti details
* Ubiquiti details
* Ubiquiti details

* Ubiquiti details
* Ubiquiti details

1. Ubiquiti details

Ubiquiti details

* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly

* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly

* If everything has unique IP address, everything should just run correctly
* If everything has unique IP address, everything should just run correctly

1. If everything has unique IP address, everything should just run correctly

If everything has unique IP address, everything should just run correctly

* Total procedure
* Total procedure
* Total procedure

* Total procedure
* Total procedure

1. Total procedure

Total procedure

* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernet
* Difference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* Over ethernet:when we use UDP multicast, there’s retransmit if someone gets it
* when we use UDP multicast, there’s retransmit if someone gets it
* Over wifi:

* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernet
* Difference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* Over ethernet:when we use UDP multicast, there’s retransmit if someone gets it
* when we use UDP multicast, there’s retransmit if someone gets it
* Over wifi:

* IMU broadcasts UDP packets over ethernetDifference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* IMU broadcasts UDP packets over ethernet
* Difference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
* Over ethernet:when we use UDP multicast, there’s retransmit if someone gets it
* when we use UDP multicast, there’s retransmit if someone gets it
* Over wifi:

1. IMU broadcasts UDP packets over ethernet
2. Difference between ethernet/wifiOver ethernet:when we use UDP multicast, there’s retransmit if someone gets itOver wifi:
3. Over ethernet:when we use UDP multicast, there’s retransmit if someone gets it
4. when we use UDP multicast, there’s retransmit if someone gets it
5. Over wifi:

IMU broadcasts UDP packets over ethernet

Difference between ethernet/wifi

1. Over ethernet:when we use UDP multicast, there’s retransmit if someone gets it
2. when we use UDP multicast, there’s retransmit if someone gets it
3. Over wifi:

Over ethernet:

1. when we use UDP multicast, there’s retransmit if someone gets it

when we use UDP multicast, there’s retransmit if someone gets it

Over wifi:

* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss

* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss

* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss

* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss

* When we use, no retransmit. A lot of packet loss
* When we use, no retransmit. A lot of packet loss

1. When we use, no retransmit. A lot of packet loss

When we use, no retransmit. A lot of packet loss

* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instance
* Finally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it

* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instance
* Finally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it

* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instanceFinally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it
* Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instance
* Finally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it

1. Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instance
2. Finally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it

Code doesn’t care about where the packet is being sent. It multicasts to everything on network… which is just Ubiquiti instance

Finally, Ubiquiti instance simply forwards the packet from IMU to computers connected to it

* Extra considerations
* Extra considerations
* Extra considerations

* Extra considerations
* Extra considerations

1. Extra considerations

Extra considerations

* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%
* Protobufs:May need to keep packet sizes small
* May need to keep packet sizes small
* NRF chip:

* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%
* Protobufs:May need to keep packet sizes small
* May need to keep packet sizes small
* NRF chip:

* Need to make sure packets are robust to drops; packet drop rate could reach 50%Protobufs:May need to keep packet sizes smallNRF chip:
* Need to make sure packets are robust to drops; packet drop rate could reach 50%
* Protobufs:May need to keep packet sizes small
* May need to keep packet sizes small
* NRF chip:

1. Need to make sure packets are robust to drops; packet drop rate could reach 50%
2. Protobufs:May need to keep packet sizes small
3. May need to keep packet sizes small
4. NRF chip:

Need to make sure packets are robust to drops; packet drop rate could reach 50%

Protobufs:

1. May need to keep packet sizes small

May need to keep packet sizes small

NRF chip:

* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers
* May be good to talk with Sasha over NRF code
* Sasha also has experience splitting packets for udp

* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers
* May be good to talk with Sasha over NRF code
* Sasha also has experience splitting packets for udp

* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers
* May be good to talk with Sasha over NRF code
* Sasha also has experience splitting packets for udp

* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computersMay be good to talk with Sasha over NRF codeSasha also has experience splitting packets for udp
* NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers
* May be good to talk with Sasha over NRF code
* Sasha also has experience splitting packets for udp

1. NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers
2. May be good to talk with Sasha over NRF code
3. Sasha also has experience splitting packets for udp

NRF: hardware retransmit, point to point, leading to fewer dropped packets. But, we would have to have one telemetry computer transmit to other computers

May be good to talk with Sasha over NRF code

Sasha also has experience splitting packets for udp

* TODO:
* TODO:

1. TODO:

TODO:

* Figure out how to incorporate protobufs into UDP packetsUpdate ethernet transmission code to work with the vehicle computerTalk with Sasha about NRF code/potentially splitting packets for UDP
* Figure out how to incorporate protobufs into UDP packetsUpdate ethernet transmission code to work with the vehicle computerTalk with Sasha about NRF code/potentially splitting packets for UDP
* Figure out how to incorporate protobufs into UDP packets
* Update ethernet transmission code to work with the vehicle computer
* Talk with Sasha about NRF code/potentially splitting packets for UDP

* Figure out how to incorporate protobufs into UDP packetsUpdate ethernet transmission code to work with the vehicle computerTalk with Sasha about NRF code/potentially splitting packets for UDP
* Figure out how to incorporate protobufs into UDP packets
* Update ethernet transmission code to work with the vehicle computer
* Talk with Sasha about NRF code/potentially splitting packets for UDP

1. Figure out how to incorporate protobufs into UDP packets
2. Update ethernet transmission code to work with the vehicle computer
3. Talk with Sasha about NRF code/potentially splitting packets for UDP

Figure out how to incorporate protobufs into UDP packets

Update ethernet transmission code to work with the vehicle computer

Talk with Sasha about NRF code/potentially splitting packets for UDP

