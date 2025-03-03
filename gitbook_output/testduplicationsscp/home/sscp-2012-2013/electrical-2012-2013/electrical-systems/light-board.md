# SSCP - Light Board

# Light Board

Sunwhale Light Board Research Project:

One of the design considerations for this design cycle is to drive the lights from the HV battery rail directly instead of the the 24V BUS. This will allow the battery to 24V converter to not require as much power to be drawn from it.

Our two options are:

1. Use the existing LT3475-1 board to drive an external FET to control the LEDs. This would require some tricky isolation techniques

2. Use a forward converter (like the LT3799). The LT3799 is meant to take in wall AC voltage and convert the voltage to DC voltage for the lights, but we only need to take in DC voltage. We can exclude the Power Factor Correction and the AC to DC conversion features as well.

Currently developing the LT3799 option.

Base Specs

Vin Max =  27*4.2  = 113.4. Designing for 120V input max. 

Vin Min = 27*2.4    = 64.8. Designing for 60V input min.

Iout Typical = .35A.

Iout Max = .5A.

Vout Typical = 6*2.963V = 17.8V. Design for 18V output typical

Frequency of Operation

Page 4 of datasheet depicts oscillator maximum and minimum frequency vs temperature, and it looks like the hotter the chip gets the less restrictive the frequencies are. At 25C, the min frequency is 37kHz and the max frequency is 300kHz.

We need to ensure that this chip will always be operating within those bounds. By approximating that there is only magnetizing inductance, we can assume the following:

D = Vout * N/ (Vout * N + Vin)                     (see page 12)

Iout = .5 * (1-D) * N * Ipk,pri                        (see page 10, assuming triangular waveform)

Ton = L*Ipk,pri/Vin                                       (When Input is applied to primary of transformer)

Toff = L*Ipk,pri/(N*Vout)                              (When Output is applied to secondary of transformer)

f = 1/(Ton+Toff)                                            (Ensure the resulting frequency is in range)

Transformer Selection (Page 14 for predesigned transformers)

Model: 750813144 

Dimension: 16.5mm × 18mm × 18mm 

Primary Inductance: 600uH 

Turns Ratio (Primary, Secondary, Ancillary): 4:1:0.71 (Nps = 4.166)

Rpri: 2400 ohm

Rsec: 420 ohm

Target Application: 28V/.5A

N = 4

Picking Rsense (Page 12)

Rsense primarily determines the maximum output current. 

Rsense = 2*(1-D)N/(Iout,max * 42) *.95

.95 factor is for error tolerancing.

Voltage and Current Control (Page 11)

The important equation is to output the correct amount of current for the LEDs. 

We can set the output current by setting the voltage on the CTRL pins with a resistor divider. This divider can be set with the equation:

Iout = Ctrl*N/(42*Rsense)

R1 = R2 (2*N/(42*Iout*Rsense) - 1).

Winding Ratio

-Recommend keep duty cycle low.

-Keep Nps low

Switch Voltage Clamp Requirement

TVS diode necessary to protect the FET from leakage inductance. 

Put in series with flyback.

Reverse breakdown must be larger than (Vout + Vf)*N where Vout is output of flyback, Vf is secondary diode forward voltage, N is turns ratio.

MOSFET Selection

LT3799 has 1.9A gate driver. Standard MOSFETs are fine since chip can drive with 10V

Low Qg needed for max efficiency

Drain will be strained to Vout*Nps+Vin when off, but double check the voltage spike. 

http://www.digikey.com/product-detail/en/IPD50R3K0CE/IPD50R3K0CECT-ND/4214658

Secondary Diode Selection

The secondary diode stress = Vout + 2 • Vin/Nps

RC snubber in parallel can reduce the stress.

Calculations

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

The frequencies are within range.

Secondary Diode must handle = 18 + 2*120/4 = 78.0V

TVS diode must handle (assume Vf = .7) =  (18+.7)4 = 74.2V

MOSFET must handle 18 * 4 + 120 = 192V

Rsense = .2

Note About Power Factor Correction

Because we are using the battery as an input voltage source as opposed to an AC source that this product was engineered for, we don't need to use the power factor correction functionality.

Pin considerations:

Vin_sense - Feed the output of a voltage divider that takes in Vin and scales from 120 to 1.25V~1.5V.

Luminos Light Board Development:

Board should control all the driving lights (headlights, turn signals, break lights) on the car. It is responsible for receiving CAN messages on what needs to be done, and supplying to appropriate power to the lights. The lights on the car include 2 headlights, 2 front turn signals, 2 rear turn signals, and 2 rear brake lights.

CREE offers some excellent LEDs to use for all the lights. To compare LEDs, use their Product Characterization Tool.

[ Product Characterization Tool](http://pct.cree.com/dt/index.html)

Protecting the LEDs from overvoltage or over current is essential, especially if the lights are embedded. In line fuses on the board with a constant current IC is ideal on the board, along with TVS diodes. However, it is best to also have protection on the board itself because the wires can be shocked or connected incorrectly. Here are some nice fuses that could be a potential solution. PCT's and TVS diodes might be a good ideal for the LED board itself.

[ Here](http://www.littelfuse.com/products/led-protectors.aspx)

Power Constraints.

All the lights should be kept at a low power. The max power for the entire electrical system is 60 Watts (due to the replacement vicor), and one should assume the system will draw 10 Watts with no lights on, so that's less than 50 Watts for ALL the lights. The more power you put into the lights, the more power the needs to be dissipated. The typical way to dissipate large amounts of power from the LEDs is to distribute the heat to the back of the board through numerous vias and attache a heat sink to the back. 

Here's some preliminary power values for the lights:

Headlights:    6 White XT-E's.      926 lumens at 6.222 watts total. 0.35A and 2.963V each LED.       2 headlights, 12.444 watts.

Front Turn:     6 Amber XP-E's.    285 lumens at 4.374 watts total. 0.35A and 2.073V each LED.       2 turn lights, 8.748 watts.

Brake:           6 Red XP-E's         363 lumens at 4.356 watts total. 0.35A and 2.073V each LED.       2 brake light, 8.712 watts.

Front Turn:     6 Amber XP-E's.    285 lumens at 4.374 watts total. 0.35A and 2.073 each LED.         2 turn lights, 8.748 watts.

38.7 total watts so far. The amount of lumens emitted is a bit small, so they can be increased. Tail Lights are excluded.

Note: Can Red-Orange lights be used instead? 

These are more efficient than red lights (can operate 435.6 Lumens at 4.356 watts at .35A. ~100 more lumens than red lights at the same power draw).

LED Driver Chip Selection:

In regards to the driver, the LT3475-1 will be selected. It is a dual-step down dc/dc converter that outputs constant current. The nice about this driver is that it can drive two strings at once, and outputs up to 1.5A. It allows PWMing to control brightness of the lights.

Sizing Components and Design Considerations:

Input Voltage: The driver will be protected from over/undervoltage with the help of a power module, which outputs around 24V. Decoupling capacitors rated at that voltage will be placed.

Switching Frequency: We want a slow enough frequency to not have significant switching and efficiency losses, but fast enough to prevent voltage over/undershoots and have faster transient response. 

This board operates the light board at 1.8MHz. The resistor to select this frequency has been set to 4.7kOhm (the table on page 8 of the datasheet helps the selection)

Inductor: Equation for picking the inductor is (Vout+Vf)(1.2MHz/f). If f=1.8Mhz, Vout=12, Vf (voltage of catch diode)~.4V.

10uH rated at around 5A is good. 

Catch Diode: Has to be switching really fast and can handle the voltage (24V) and current (4.5A) that is being boosted. Schottky Diode Selected was rated at those values.

Current Output: A voltage divider that goes into VAdj that uses VRef as the high voltage is used to set the output current. Tying VRef directly to VAdj will cause the driver to operate 1.5A. The current design is for .35mA, so a voltage divider that uses 33k and 10k will give the correct output current.

SHDN: Chip shutdown when shdn is pulled low, so this pin is connected to the mc with pull-up resistors. 

PWM: These pins are connected to mc as well. 

Fuse: Since we're using LEDs that operate at around .35A and 12V, an appropriate fuse is needed as protection, so one rated at 32V and .5A is placed.

For LT3475-1 applications with higher output voltages, an additional Zener diode may be necessary (Figure 5d) to maintain pin voltage 

below the absolute maximum. (Sasha notes that it is not ncessary for our purposes)

Future Considerations:

-Try to put as many control pins on the same channel of the mc.

-Separate the light board into two, so that there are two chips per board as opposed to the current four per board.

-Make the chip smaller (currently 5in by 5in. derp)

Board Bring-Up, Rev 1.1.0

Major changes for this revision: 

3 driver chips per board for 6 output channels.

Massive reduction in driver section area by means of using 4-layer boards and physically smaller inductors from coilcraft.

[ inductors from coilcraft](http://www.coilcraft.com/xal50xx.cfm)

New form factor to match the standard box design including Deutsch and Phoenix connectors. 

Some notes: 

LEDs are being driven!

The LT chips' orientation could be marked more clearly.

PWM3L and PWM3R are currently attached to STM32F4 pins PC4 and PC5, which are not PWM enabled. Luckily, pins PB0 and PB1 (directly next door) are PWM enabled, and it's an easy fix. 

Lower PWM duty cycles (<50%) result in a fairly tremendous whining racket. However, this appears it will drop off tremendously when it'll be sealed in the box. 

