# SSCP - Temperature Sensing

# Temperature Sensing

## Introduction

[](#h.nunyp0c1xjo)

## Sensors

[](#h.qa06ico7r6ru)

### Pinout

[](#h.o2o082d02ubc)

 White/Orange

 +5V

 Whitle/Blue

 Ground

 White

 Output

### Sensor Construction

[](#h.77lxl0jhf807)

The Sensor consists of an LM35 temperature sensor in a siliconed in a brass tube connected to high temperature (396F) wire. 

[ LM35](http://www.ti.com/lit/ds/symlink/lm35.pdf)

### Output

[](#h.1n5nadiamwb1)

The sensor has a valid output from 0-150C (0-300F) and is calibrated in centigrade where each 10mV = 1C with no offset factor so multiplying the sensor output voltage by 100x yields the temperature in Centigrade. 

## Labjack U3

[](#h.b5igrajcls8a)

* Download the U3 software from the Labjack websiteInstall the U3 DriverOpen the LJStreamUD Plug the sensors into to the FIOChange the Range to U_rgUNI2p5V for unipolar 2.5V Range
* Download the U3 software from the Labjack website
* Install the U3 Driver
* Open the LJStreamUD 
* Plug the sensors into to the FIO
* Change the Range to U_rgUNI2p5V for unipolar 2.5V Range

1. Download the U3 software from the Labjack website
2. Install the U3 Driver
3. Open the LJStreamUD 
4. Plug the sensors into to the FIO
5. Change the Range to U_rgUNI2p5V for unipolar 2.5V Range

Download the U3 software from the Labjack website

[ website](http://labjack.com/support/software)

Install the U3 Driver

Open the LJStreamUD 

Plug the sensors into to the FIO

Change the Range to U_rgUNI2p5V for unipolar 2.5V Range

