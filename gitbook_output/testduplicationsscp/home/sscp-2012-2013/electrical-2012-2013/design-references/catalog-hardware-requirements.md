# catalog-hardware-requirements

## SSCP - Catalog Hardware Requirements

## Catalog  Hardware Requirements

### Microprocessor RAM Requirement

To support telemetry's catalog of parameters a great deal of RAM is required beyond the amount normally used for the execution of code. At a minimum the catalog imposes a 12byte overhead on every variable entered into the catalog. This is 12 bytes does not include the memory required to hold the name string of each variable.

### Board Serial Number Requirement

In order to support board serial number in hardware two pins need to be designated as serial number pins. Each pin will have options for both a pull up and pull down resistor. By changing the stuffing options and size of the resistor the software can extract 4 bits of information by the two pins.&#x20;

### Hardware Revision Requirement

Two pins are required to support the hardware revision number with stuffing options exactly like the ones described above.&#x20;
