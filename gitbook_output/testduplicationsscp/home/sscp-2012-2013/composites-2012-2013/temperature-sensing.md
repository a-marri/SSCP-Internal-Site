# temperature-sensing

## SSCP - Temperature Sensing

## Temperature Sensing

### Introduction

### Sensors

#### Pinout

&#x20;White/Orange

&#x20;+5V

&#x20;Whitle/Blue

&#x20;Ground

&#x20;White

&#x20;Output

#### Sensor Construction

The Sensor consists of an LM35 temperature sensor in a siliconed in a brass tube connected to high temperature (396F) wire.&#x20;

[LM35](http://www.ti.com/lit/ds/symlink/lm35.pdf)

#### Output

The sensor has a valid output from 0-150C (0-300F) and is calibrated in centigrade where each 10mV = 1C with no offset factor so multiplying the sensor output voltage by 100x yields the temperature in Centigrade.&#x20;

### Labjack U3

* Download the U3 software from the Labjack websiteInstall the U3 DriverOpen the LJStreamUD Plug the sensors into to the FIOChange the Range to U\_rgUNI2p5V for unipolar 2.5V Range
* Download the U3 software from the Labjack website
* Install the U3 Driver
* Open the LJStreamUD&#x20;
* Plug the sensors into to the FIO
* Change the Range to U\_rgUNI2p5V for unipolar 2.5V Range

1. Download the U3 software from the Labjack website
2. Install the U3 Driver
3. Open the LJStreamUD&#x20;
4. Plug the sensors into to the FIO
5. Change the Range to U\_rgUNI2p5V for unipolar 2.5V Range

Download the U3 software from the Labjack website

[website](http://labjack.com/support/software)

Install the U3 Driver

Open the LJStreamUD&#x20;

Plug the sensors into to the FIO

Change the Range to U\_rgUNI2p5V for unipolar 2.5V Range
