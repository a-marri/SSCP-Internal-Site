# SSCP - Protection Circuit

# Protection Circuit

The protection circuit module is featured in all of the Point-of-Load power supplies (including those that do not feature a step-down buck converter). This circuit's purpose is to isolate components feeding off of the power supply from possibly damaging events such as: sustained overvoltage, overcurrent, undercurrent, reverse bias, and transient voltage spikes.

The protection circuit protects against over- and undervoltage situations by monitoring two voltages coming from resistor voltage dividers connected to the load line. When the voltage fluctuates past a limit set by the dividers, the IC goes into a warning state (of length determined by the timing capacitor) and then cuts off the load from the supply using the FETs on the load line. Protection against overcurrent situations is provided by monitoring the voltage across a sense resistor in series with the load line. When the voltage across this sense resistor exceeds a hard limit, the IC proceeds to go into the warning state and then shut off the current. By changing the values of these resistors, it is possible to change the voltage and current limits.

Additional protection is provided against transients by having low-pass filters on both the input and output as well as TVS diodes (which non-destructively break down and bypass current at a certain voltage).

### Input Ratings

[](#h.5czv0xclxp84)

Max/Min ratings describe the limit at which damage to module components will occur. Operating limits describe the range within which the protection circuitry does nothing (allows for normal operation of load). The operating voltage limits were designed to protect more sensitive components from being damaged, while allowing for some fluctuations without needlessly interrupting the power supply. Operating current settings depends heavily on the load as buck converters are more susceptible to overcurrent situations (they can handle wide voltage fluctuations without damage or performance degradation). 

VIN (Max): 45V (can handle transients higher than this)

VIN (Min): -60V

VIN (Operating): 18V-30V (can handle transients higher than this)

IIN (Max): 2.5A (Depends on ferrite bead, sense resistor, and FET selection.)

IIN (Operating): 1A (Depends on sense resistor selection.)

### Output Ratings

[](#h.nnk8nrtim1wy)

Output ratings are less robust since they are not connected to the typically higher voltage bus and therefore should only have to tolerate ESDs and reverse bias conditions. Current ratings are the same, since the protection IC draws a negligible amount of current from the main load line.

VOUT (Max): 30V (can handle transients higher than this)

VOUT (Min): -60V

VqOUT (Operating): 18V-30V (can handle transients higher than this)

IOUT (Max): 2.5A (Depends on ferrite bead, sense resistor, and FET selection.)

IOUT: 1A (Depends on sense resistor selection.)

### Layout Notes

[](#h.fxir57pv2lz4)

The protection module is incorporated into the 24-pin DIP packages of the low and medium power modules. For the high current module, a modified low or medium current module is plugged into a high current module that is integrated with the load circuit. The modifications required involve changing the sense resistor to set the proper overcurrent cutoff limits.

The schematic for the protection module features a port for an external sense resistor. This resistor determines the overcurrent cutoff limits and should be selected with the typical load currents in mind using the formula found in the LT4356 datasheet. Also, this resistor is used by the current sense module, so there must be a calibration of the current sense module to the specific sense resistor chosen.

### Component Selection Notes

[](#h.kikw0oxk5nn1)

This circuit utilizes an LT4356 integrated circuit to determine when these damaging events occur and to cutoff current utilizing back to back FETs. Any components located on the load line are required to be able to tolerate high currents (up to 2.5A) because the protection circuit could be connected to either a buck converter (in which case, <.5A would typically be pulled) or directly to a load (in which case, up to 2.5A could be pulled).

PFET: 2.5A Ids, 60V Vds

NFET: 3A Ids, 60V Vds (Note: Due to shortages, schematic part may not reflect actual part).

These FETs (a PFET and NFET) are of opposite channel types to allow for protection against reverse-bias situations. They should be able to withstand drain-source currents higher than required by the typical load power consumption as well as voltage transients up to the rating of the TVS diodes (they need to be able to withstand high voltages until the TVS diodes 'kick-in'

 and bypass them).

Input TVS Diode: 45V

Output TVS Diode: 30V

The TVS diodes are used bypass voltage transients that could damage the IC or FETs and are located on both the input and output as to protect from transients originating from either port.

Input/Output Ferrite Bead: 3A, 1.3K @ 100MHz

Output Capacitor: 10uF, 35V

The protection circuit also features LC filters on the input and output to provide a smoothing behavior to rapidly changing voltages.

Sense Resistor: 50mΩ (for 1A cutoff setting)

    Depends on host application, determined by the desired current limit. Use tight tolerance (especially important here) for accurate overcurrent limit setting.

    RSense= 50mV /  IOvercurrent

Overvoltage Fault Setting Resistors: 120K ±1% and 4.99K ±1%

    Selected depending on desired overvoltage limit. Use tight tolerance resistors for limit accuracy.

    R1 = (VOvervolt - 1.25V) * R2 / 1.25V

    R2 = 1.25V / IOvervolt R1 & R2

    IOvervolt R1 & R2 = 250μA

Timing Capacitor: 4.7uF

    Selected to set TR and TFALL to appropriate times.

    tWarning = (CTMR * 100mV) / 5μA

    tCooldown = (CTMR * .85V) / 2μA

Undervoltage Fault Setting Resistors: 68K ±1% and 4.99K ±1%

    Selected depending on desired undervoltage limit. Use tight tolerance resistors for limit accuracy.

    R4 = (VUndervolt - 1.25V) * R5 / 1.25V

    R5 = 1.25V / IOvervolt R1 & R2

    IOvervolt R1 & R2 = 250μA

