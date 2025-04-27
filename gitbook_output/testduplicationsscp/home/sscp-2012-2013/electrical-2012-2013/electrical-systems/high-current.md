# high-current

## SSCP - High Current

## High Current

The high current module differs from the low and medium current POL Power Supplies in that it isn't routed with voltage protection and current sense modules.This is done for two reasons: 1 - The large capacitors and inductors required for the high current module don't easily fit on a 24-pin DIP package. 2 - Where an inaccurate estimation of a low or medium current application could require a swapping out of the power module, most applications that need high current could never run on a low or medium current module, meaning that a high current modules don't require the swapability that the low and medium current modules do.

#### Layout Notes

The high current module still interfaces with a low or medium current module for protections and current sensing purposes and provides a slot for the 24-pin DIP package to plug in so that they don't have to be routed again.

The schematic for the high power module features a port for a feedback resistor, the upper resistor in the feedback voltage divider is set to 316K and the lower can be set by the user in order to set the output voltage. For a 3.3V output, a 102K (<1%) is used for the lower feedback resistor. On the PCB layout for the High Current Test Assembly, this feedback resistor is marked as FB whereas the feedback resistor for the low/medium power buck on the 24-pin DIP is marked as LOW/MED FB.

The protection module on the 24-pin DIP package needs to have its current sense resistor set appropriately.

#### Component Selection Notes

The high power module uses the LT3690 buck converter (which comes in a 26-pin QFN package) for the voltage step down chosen for its resilience to change in inputs, high maximum output current, low ripple output, and programmable output voltage.

Switching Frequency: 600 kHz

&#x20;   Chosen based on typical VIN and desired VOUT. (See datasheet for formula.)

Output Inductor: 3.30μH, <.03Ω DCR,

&#x20;   Chosen based on VOUT and switching frequency. (See datasheet for formula.)

Output Capacitor: 100μF

&#x20;   Chosen based on VOUT and switching frequency. (See datasheet for formula.)

Boost Capacitor: .68μF

&#x20;   Chosen based on VOUT and switching frequency. (See datasheet for formula.)

Soft-Start Capacitor: 10nF

&#x20;   Chosen based on boost capacitor and desired ramp time. (See datasheet for formula.)

Input Ratings

Input Operating Voltage Limits: 3.9V - 36V

Optimal Operating Voltages: 4.16V - 27.39V (For optimal output ripple. Depends on voltages and switching frequency. See datasheet for formula.)

Input Transient Tolerance: 60V  (Should never occur, since the protection circuitry should block these.)

Output Ratings

Output Voltage: 3.3V

Output Max Current: 4A (Should be limited by protection circuitry entering overcurrent mode.)

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1J951KX0Y1pNam54JSzLWqN9lZQc_Eafz#list)
