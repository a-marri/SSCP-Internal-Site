# SSCP - Pack Charging Procedure

# Pack Charging Procedure

Relevant snippets from power supply manual:

http://www.programmablepower.com/dc-power-supply/XPF/downloads/XPF_60-10D-DP_Operation_Manual_M370633-01_rvA.pdf

[http://www.programmablepower.com/dc-power-supply/XPF/downloads/XPF_60-10D-DP_Operation_Manual_M370633-01_rvA.pdf](http://www.programmablepower.com/dc-power-supply/XPF/downloads/XPF_60-10D-DP_Operation_Manual_M370633-01_rvA.pdf)

The output is protected from reverse voltages by a diode; the continuous reverse current must not exceed 3 Amps, although transients can be much higher.

However, in common with all precision bench power supplies, a capacitor is connected across the output to maintain stability and good transient response. This capacitor charges to the output voltage and short-circuiting of the output will produce a current pulse as the capacitor discharges which is independent of the current limit setting.

Battery Datasheet:

http://na.industrial.panasonic.com/sites/default/pidsa/files/ncr18650b.pdf

[http://na.industrial.panasonic.com/sites/default/pidsa/files/ncr18650b.pdf](http://na.industrial.panasonic.com/sites/default/pidsa/files/ncr18650b.pdf)

Pack precharge current at full pack is 113.4V / 500 ohm = 227 mA

Things needed:

* 2x Sorensen power supply + something to plug in to1x charging cable
* 2x Sorensen power supply + something to plug in to
* 1x charging cable

1. 2x Sorensen power supply + something to plug in to
2. 1x charging cable

2x Sorensen power supply + something to plug in to

1x charging cable

Procedure:

* Turn off carTurn off power suppliesUnplug 1x motor controllerSet power supply voltage limit to 113.4V (4x 28.35V)Set one power supply current limits to 0.01ATurn on all power suppliesTurn on carWait for precharge to complete
* Turn off car
* Turn off power supplies
* Unplug 1x motor controller
* Set power supply voltage limit to 113.4V (4x 28.35V)
* Set one power supply current limits to 0.01A
* Turn on all power supplies
* Turn on carWait for precharge to complete
* Wait for precharge to complete

1. Turn off car
2. Turn off power supplies
3. Unplug 1x motor controller
4. Set power supply voltage limit to 113.4V (4x 28.35V)
5. Set one power supply current limits to 0.01A
6. Turn on all power supplies
7. Turn on carWait for precharge to complete
8. Wait for precharge to complete

Turn off car

Turn off power supplies

Unplug 1x motor controller

Set power supply voltage limit to 113.4V (4x 28.35V)

Set one power supply current limits to 0.01A

Turn on all power supplies

Turn on car

1. Wait for precharge to complete

Wait for precharge to complete

* Increase current limit to 6ACharge until total current drops to 0.975A
* Increase current limit to 6A
* Charge until total current drops to 0.975A

1. Increase current limit to 6A
2. Charge until total current drops to 0.975A

Increase current limit to 6A

Charge until total current drops to 0.975A

