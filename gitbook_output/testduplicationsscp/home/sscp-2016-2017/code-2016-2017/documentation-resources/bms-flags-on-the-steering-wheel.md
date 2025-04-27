# bms-flags-on-the-steering-wheel

## SSCP - BMS Flags on the Steering Wheel

## BMS Flags on the Steering Wheel

The steering wheel displays 3 BMS flags and the BMS state (a number corresponding to the a state) on the right hand side of the screen. To indicate a flag is on, the letter corresponding to the flag appears. Otherwise "\_" is displayed. The flags are as follows:

R - Indicates if regen is enabled. Regen is disabled when the BMS indicates charge is disabled (at top of pack).&#x20;

V - Indicates if the pack total voltage is below 97V (bottom of pack).

C - Indicates if the difference between the highest and lowest cell voltage is greater than .1. This can indicate a problem with the pack welds.

BMS State Mappings:

&#x20; 0 - STARTUP

&#x20; 1 - PRECHARGE

&#x20; 2 - STARTUPFAIL

&#x20; 3 - HIGHSIDEDELAY

&#x20; 4 - NOMINAL

&#x20; 5 - ABOVENOMTEMP

&#x20; 6 - OVERCHARGED

&#x20; 7 - UNDERCHARGED

&#x20; 8 - OVERTEMPERATURE

&#x20; 9 - UNRESPONSIVE

&#x20; 10 - OVERCURRENT
