# SSCP - BMS Flags on the Steering Wheel

# BMS Flags on the Steering Wheel

The steering wheel displays 3 BMS flags and the BMS state (a number corresponding to the a state) on the right hand side of the screen. To indicate a flag is on, the letter corresponding to the flag appears. Otherwise "_" is displayed. The flags are as follows:

R - Indicates if regen is enabled. Regen is disabled when the BMS indicates charge is disabled (at top of pack). 

V - Indicates if the pack total voltage is below 97V (bottom of pack).

C - Indicates if the difference between the highest and lowest cell voltage is greater than .1. This can indicate a problem with the pack welds.

BMS State Mappings:

  0 - STARTUP

  1 - PRECHARGE

  2 - STARTUPFAIL

  3 - HIGHSIDEDELAY

  4 - NOMINAL

  5 - ABOVENOMTEMP

  6 - OVERCHARGED

  7 - UNDERCHARGED

  8 - OVERTEMPERATURE

  9 - UNRESPONSIVE

  10 - OVERCURRENT

