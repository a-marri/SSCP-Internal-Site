# current-sensing-block

## SSCP - Current Sensing Block

## Current Sensing Block

Note: although this page is written in the present tense, this module does not yet exist.

The current sensing module is based upon the LT6102 Current Sense Amplifier coupled with a LT6002 opamp. The current sense amplifier measures the voltage drop across a shunt (currently spec'd at 500mOhm). This shunt resistor can be shared with the shunt resistor for the LT4356 surge stopper found on the medium / high current versions of the power module.&#x20;

[LT6102 Current Sense Amplifier](http://www.linear.com/product/LTC6102)

[LT6002 opamp](http://www.linear.com/product/LT6002)

[LT4356 surge stopper](http://www.linear.com/product/LT4356-1%20and%20-2)

TODO: create a table of resistor values for different maximum current draws

An alternative is to use the  LTC4151 that reports the current draw of the system over I2C. TI also makes one: INA219

[ LTC4151](http://cds.linear.com/docs/Datasheet/4151fc.pdf)

[INA219](http://www.ti.com/lit/ds/symlink/ina219.pdf)

A current sensing module is intended to be paired with every power module; however, it is encouraged to use the current sensing module on boards that host multiple power-hungry devices (i.e. GPS, WiFly module, camera, etc) so that power consumption can be reported by device.
