# SSCP - Boxed CAN Power Supply 1

# Boxed CAN Power Supply 1

Project Owner: Max Praglin

Overview

Designers frequently want to test hardware without having to hunch over the whole vehicle for hours on end. Or they want to test hardware on the car but the battery pack is unavailable. The boxed CAN power supply's goal is to provide 24v to the CAN power bus from batteries so that the vehicle does not have to be tethered to do some basic testing. 

Specifications and Requirements

* Charge batteries from isolated mains supply, also protect batteries
* Indicator LEDs (power, battery status, CAN activity, target power)
* Output 24V @ 2A to target, can be turned off without turning off this box
* Monitor current consumption of target board
* Record and play back CAN messages
* Connect to a computer to send CAN messages

Charge batteries from isolated mains supply, also protect batteries

Indicator LEDs (power, battery status, CAN activity, target power)

Output 24V @ 2A to target, can be turned off without turning off this box

Monitor current consumption of target board

Record and play back CAN messages

Connect to a computer to send CAN messages

Current Design Implementation

Topology Overview

* When an AC adapter is plugged in, 24v conducts through FETS directly to the CAN Connector. The 24v input also charges the built-in battery pack.
* When there is no power applied on the input, a 36 Watt-hour battery pack (four Tenergy 18650 cells in series) powers a boost converter.
* A USB-to-Serial interface can be used to communicate with the MCU, which will allow interface between computer and CAN. A computer-side program will provide functionality such as message sending and logging.

When an AC adapter is plugged in, 24v conducts through FETS directly to the CAN Connector. The 24v input also charges the built-in battery pack.

When there is no power applied on the input, a 36 Watt-hour battery pack (four Tenergy 18650 cells in series) powers a boost converter.

A USB-to-Serial interface can be used to communicate with the MCU, which will allow interface between computer and CAN. A computer-side program will provide functionality such as message sending and logging.

How Do I Use It?

* Two switches are present on the board, labeled "Boost On/Off" and "Target On/Off""Target On/Off" connects the 24v supply to the target board. Use this for toggling power to the target board while keeping the power supply alive."Boost On/Off" provides power to the boost converter. Treat this as a system "Power Switch" when there is no AC adapter present. If there is an AC adapter present, simply unplug the adapter to turn off the board!
* "Target On/Off" connects the 24v supply to the target board. Use this for toggling power to the target board while keeping the power supply alive.
* "Boost On/Off" provides power to the boost converter. Treat this as a system "Power Switch" when there is no AC adapter present. If there is an AC adapter present, simply unplug the adapter to turn off the board!
* MCU functionality is TBD based on what the Code Team provides

Two switches are present on the board, labeled "Boost On/Off" and "Target On/Off"

* "Target On/Off" connects the 24v supply to the target board. Use this for toggling power to the target board while keeping the power supply alive.
* "Boost On/Off" provides power to the boost converter. Treat this as a system "Power Switch" when there is no AC adapter present. If there is an AC adapter present, simply unplug the adapter to turn off the board!

"Target On/Off" connects the 24v supply to the target board. Use this for toggling power to the target board while keeping the power supply alive.

"Boost On/Off" provides power to the boost converter. Treat this as a system "Power Switch" when there is no AC adapter present. If there is an AC adapter present, simply unplug the adapter to turn off the board!

MCU functionality is TBD based on what the Code Team provides

Components Overview

* A TDK-Lambda 120-24v power supply + C14 power inlet will provide 24v to either charge the batteries and/or power the onboard logic and target boardA pack will be constructed of four Tenergy Li-Ion 18650's in a battery holder - this will provide 16.4vThe LT3759 will be used in a boost configuration to provide 24v from the 16.4v of the batteryThe LTC4007 charging IC will charge the batteries and pass through 24v. It also indicates charge status via LEDs.
* A pack will be constructed of four Tenergy Li-Ion 18650's in a battery holder - this will provide 16.4v
* The LT3759 will be used in a boost configuration to provide 24v from the 16.4v of the battery
* The LTC4007 charging IC will charge the batteries and pass through 24v. It also indicates charge status via LEDs.
* A P-FET will be used to control the source of the 24v: by tying the gate to the voltage input of the charger chip, the boost converter will receive no power unless there is a logic low on the 24v line from the mains supply
* The first revision of the board will have minimal debugging support: LEDs, buttons, and a USB port (to provide serial communication) will be the interfaceThe processor will be a STM32F107_48LQFP unless there is a compelling reason to use a F4.
* The processor will be a STM32F107_48LQFP unless there is a compelling reason to use a F4.
* A FT232RL communicates to the MCU via serial.
* The board is designed to fit into a Polycase WC-24 box.

A TDK-Lambda 120-24v power supply + C14 power inlet will provide 24v to either charge the batteries and/or power the onboard logic and target board

[power supply](http://search.digikey.com/us/en/products/LS75-24/285-1827-ND/1918838)

[C14 power inlet](http://search.digikey.com/us/en/products/703W-00%2F07/Q335-ND/1164206)

* A pack will be constructed of four Tenergy Li-Ion 18650's in a battery holder - this will provide 16.4v
* The LT3759 will be used in a boost configuration to provide 24v from the 16.4v of the battery
* The LTC4007 charging IC will charge the batteries and pass through 24v. It also indicates charge status via LEDs.

A pack will be constructed of four Tenergy Li-Ion 18650's in a battery holder - this will provide 16.4v

[Tenergy Li-Ion 18650's](http://www.all-battery.com/4pcsTenergyLi-Ion18650Cylindrical3.7V2200mAhRechargeableBatteriesWithTabs.aspx)

[battery holder](http://search.digikey.com/us/en/products/BK-18650-PC8/BK-18650-PC8-ND/2330515)

The LT3759 will be used in a boost configuration to provide 24v from the 16.4v of the battery

[LT3759](http://www.linear.com/product/LT3759)

The LTC4007 charging IC will charge the batteries and pass through 24v. It also indicates charge status via LEDs.

[LTC4007](http://www.linear.com/product/LTC4007)

A P-FET will be used to control the source of the 24v: by tying the gate to the voltage input of the charger chip, the boost converter will receive no power unless there is a logic low on the 24v line from the mains supply

The first revision of the board will have minimal debugging support: LEDs, buttons, and a USB port (to provide serial communication) will be the interface

* The processor will be a STM32F107_48LQFP unless there is a compelling reason to use a F4.

The processor will be a STM32F107_48LQFP unless there is a compelling reason to use a F4.

A FT232RL communicates to the MCU via serial.

[ FT232RL](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf)

The board is designed to fit into a Polycase WC-24 box.

Design Decision Log

Components Considered But Not Used

* Spare 18650's and a MAX1924 protection chipUsing Tenergy cells will make the project simpler: each battery is protected with internal circuitryLT3436 boost converterAlthough the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759LCD interfaceNot pursued on this revision: this revision is expected to provide minimal functionality and work quickly.
* Spare 18650's and a MAX1924 protection chipUsing Tenergy cells will make the project simpler: each battery is protected with internal circuitry
* Using Tenergy cells will make the project simpler: each battery is protected with internal circuitry
* LT3436 boost converterAlthough the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759
* Although the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759
* LCD interfaceNot pursued on this revision: this revision is expected to provide minimal functionality and work quickly.
* Not pursued on this revision: this revision is expected to provide minimal functionality and work quickly.

* Spare 18650's and a MAX1924 protection chipUsing Tenergy cells will make the project simpler: each battery is protected with internal circuitry
* Using Tenergy cells will make the project simpler: each battery is protected with internal circuitry
* LT3436 boost converterAlthough the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759
* Although the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759
* LCD interfaceNot pursued on this revision: this revision is expected to provide minimal functionality and work quickly.
* Not pursued on this revision: this revision is expected to provide minimal functionality and work quickly.

Spare 18650's and a MAX1924 protection chip

[MAX1924](http://www.maxim-ic.com/datasheet/index.mvp/id/3417)

* Using Tenergy cells will make the project simpler: each battery is protected with internal circuitry

Using Tenergy cells will make the project simpler: each battery is protected with internal circuitry

LT3436 boost converter

[LT3436](http://www.linear.com/product/LT3436)

* Although the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759

Although the LT3436 boost requires fewer components, it is rated to a lower input voltage and leaves less of a margin than the LT3759

[LT3759](http://www.linear.com/product/LT3759)

LCD interface

* Not pursued on this revision: this revision is expected to provide minimal functionality and work quickly.

Not pursued on this revision: this revision is expected to provide minimal functionality and work quickly.

Notes

* A linear regulator for 24-3.3v was chosen because the 3.3v rail only powers a MCU.A FT232RL was chosen because USB to STM32 directly has not yet been implementedSimply using the SHDN or EN pin on the boost converter will not workPower can flow through the boost inductor out of the circuit!See annotations in below schematic for notes on specific parts.
* A linear regulator for 24-3.3v was chosen because the 3.3v rail only powers a MCU.
* A FT232RL was chosen because USB to STM32 directly has not yet been implemented
* Simply using the SHDN or EN pin on the boost converter will not workPower can flow through the boost inductor out of the circuit!
* Power can flow through the boost inductor out of the circuit!
* See annotations in below schematic for notes on specific parts.

* A linear regulator for 24-3.3v was chosen because the 3.3v rail only powers a MCU.
* A FT232RL was chosen because USB to STM32 directly has not yet been implemented
* Simply using the SHDN or EN pin on the boost converter will not workPower can flow through the boost inductor out of the circuit!
* Power can flow through the boost inductor out of the circuit!
* See annotations in below schematic for notes on specific parts.

A linear regulator for 24-3.3v was chosen because the 3.3v rail only powers a MCU.

A FT232RL was chosen because USB to STM32 directly has not yet been implemented

Simply using the SHDN or EN pin on the boost converter will not work

* Power can flow through the boost inductor out of the circuit!

Power can flow through the boost inductor out of the circuit!

See annotations in below schematic for notes on specific parts.

[](https://drive.google.com/folderview?id=1LvxbT85vbRF6MTqKHPISn402acfV_qfg)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1LvxbT85vbRF6MTqKHPISn402acfV_qfg#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1LvxbT85vbRF6MTqKHPISn402acfV_qfg#list" frameborder="0"></iframe>

