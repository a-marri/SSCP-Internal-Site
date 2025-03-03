# SSCP - Battery Management System

# Battery Management System

For details about the code of Arctan's Battery Management System, go here.

[ go here](/stanford.edu/testduplicationsscp/home/sscp-2014-2015/code-2014-2015/projects/bms-code)

Compiled suggestions for BMS improvements:

* Store SOC in battery-backed STM32F4 registersUse coin cell for turn-onPut test points on every single rail and every single signalInclude debugging indicatorsLeave option for Vicor or Max P. DC/DCUse LT6804 battery monitorInsulate high-current connections from one anotherUse right angle GT8E for internal connections if availableConsider EV200 contactor alternatives, including Gigavac Minitactor and Fujitsu FTR-J2Simplify balancing circuitryMeasure every battery module's temperature
* Store SOC in battery-backed STM32F4 registers
* Use coin cell for turn-on
* Put test points on every single rail and every single signal
* Include debugging indicators
* Leave option for Vicor or Max P. DC/DC
* Use LT6804 battery monitor
* Insulate high-current connections from one another
* Use right angle GT8E for internal connections if available
* Consider EV200 contactor alternatives, including Gigavac Minitactor and Fujitsu FTR-J2
* Simplify balancing circuitry
* Measure every battery module's temperature

* Store SOC in battery-backed STM32F4 registers
* Use coin cell for turn-on
* Put test points on every single rail and every single signal
* Include debugging indicators
* Leave option for Vicor or Max P. DC/DC
* Use LT6804 battery monitor
* Insulate high-current connections from one another
* Use right angle GT8E for internal connections if available
* Consider EV200 contactor alternatives, including Gigavac Minitactor and Fujitsu FTR-J2
* Simplify balancing circuitry
* Measure every battery module's temperature

Store SOC in battery-backed STM32F4 registers

Use coin cell for turn-on

Put test points on every single rail and every single signal

Include debugging indicators

Leave option for Vicor or Max P. DC/DC

Use LT6804 battery monitor

[LT6804 ](http://www.linear.com/product/LTC6804-1)

Insulate high-current connections from one another

Use right angle GT8E for internal connections if available

Consider EV200 contactor alternatives, including Gigavac Minitactor and Fujitsu FTR-J2

[Gigavac Minitactor](http://www.gigavac.com/pdf/ds/pp/p105.pdf)

[Fujitsu FTR-J2](http://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-j2.pdf)

Simplify balancing circuitry

Measure every battery module's temperature

* Use LT3638 for precharge
* Use LT3638 → ~48V → ~±6V to power relays and current sense circuitry
* Redesign current sense with LT partsShort array in safe stateUse isoSPI to modularize
* Short array in safe state
* Use isoSPI to modularize

Use LT3638 for precharge

[LT3638 ](http://www.linear.com/product/LTC3638)

Use LT3638 → ~48V → ~±6V to power relays and current sense circuitry

Redesign current sense with LT parts

* Short array in safe state
* Use isoSPI to modularize

Short array in safe state

Use isoSPI to modularize

Architecture Decisions

Distributed vs. Monolithic vs Modular

Distributed vs monolithic remains unchanged from BMS 7.

LT's introduction of a robust physical communications layer (isoSPI) made a BMS composed of two or more physical boards conceivable. In particular, it would allow manufacturing boards that need a lot of software development time first and debugging/respinning modules instead of the entire BMS.

I decided that for the number of BMS revisions expected (3) and the additional logical and physical interface complexity made a modular BMS unattractive. BMS 8 will be monolithic.

Engineering Decisions

Calculations and Low-level Circuit Explanation

Assumptions

Temperature: Maximum design temperature is at least 100 °C. Maximum temperature likely to encounter is 45 °C. See array cooling analysis for WSC 2013 pack data.

[ See array cooling analysis](/stanford.edu/testduplicationsscp/home/sscp-2014-2015/array-2014-2015/array-cooling)

Power Supplies

Power for the MCU arrives via the path: Pack->Vicor->24 to 5V buck converter

Power for the analog section of the current measurement arrives via the path: Pack->Vicor->24 to 5V buck converter> LT8300 +/-2.7V Converter

Power for the CAN transceiver, I2C transceiver, and buzzer arrives via the path: Pack->Vicor->24 to 5V buck converter

Altium Schematic Conventions

1. Use power ports often
2. Subsheet power ports are square. Subsheet signal ports are single or double arrow.
3. Prepend an "N" when naming voltage nets with a negative voltage. Specify the first decimal place after the "V". For example, N2V7, 24V0, 3V3.

Use power ports often

Subsheet power ports are square. Subsheet signal ports are single or double arrow.

Prepend an "N" when naming voltage nets with a negative voltage. Specify the first decimal place after the "V". For example, N2V7, 24V0, 3V3.

[](https://drive.google.com/folderview?id=1I77XTLn3ckEvVo9HjCs8SUwauwageVIt)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1I77XTLn3ckEvVo9HjCs8SUwauwageVIt#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1I77XTLn3ckEvVo9HjCs8SUwauwageVIt#list" frameborder="0"></iframe>

