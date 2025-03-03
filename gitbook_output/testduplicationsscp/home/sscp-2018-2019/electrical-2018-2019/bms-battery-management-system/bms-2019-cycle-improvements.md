# SSCP - BMS 2019 Cycle Improvements

# BMS 2019 Cycle Improvements

* Current Sense: We previously used the MCP3903 which requires 5.5V, 3.3V and 2.5V inputs. Past measurements were not particularly accurate, as noise from the motor controller lines affected the reliability of our reference voltage. Additionally, the chips themselves required frequent calibration. LDOs have been used to smooth the 5.5 V and 2.5 V lines. Future current sense designs should look into other chip options and involve more characterization and smoothing of the voltage references.
* Car-Side Buck: The buck can provide about 5A safely, but our LEDs drew almost 8A which forced us to decrease the sense resistor used to limit current draw. However, this did not explain why our LEDs pulled so much current (note from Kate--we upped the brightness on the LED's after I told Greg to expect no more than 5A) and, should the lights be left on for long periods of time, could result is strange BMS behavior. Future designs should implement controllers for the LEDs to limit current draw.
* Re-Design of Car-Side Power Architecture: Instead of the aforementioned buck, consider using an isolated converter. Currently, when you turn off the high side contactors a voltage spike could potentially harm the buck. An isolated converter would prevent this and also decrease the ability for damage should there be a short between High-Voltage (HV) and Low-Voltage (LV) on the car-side.
* Buzzer: The current buzzer isn't loud enough.

Current Sense: We previously used the MCP3903 which requires 5.5V, 3.3V and 2.5V inputs. Past measurements were not particularly accurate, as noise from the motor controller lines affected the reliability of our reference voltage. Additionally, the chips themselves required frequent calibration. LDOs have been used to smooth the 5.5 V and 2.5 V lines. Future current sense designs should look into other chip options and involve more characterization and smoothing of the voltage references.

Car-Side Buck: The buck can provide about 5A safely, but our LEDs drew almost 8A which forced us to decrease the sense resistor used to limit current draw. However, this did not explain why our LEDs pulled so much current (note from Kate--we upped the brightness on the LED's after I told Greg to expect no more than 5A) and, should the lights be left on for long periods of time, could result is strange BMS behavior. Future designs should implement controllers for the LEDs to limit current draw.

Re-Design of Car-Side Power Architecture: Instead of the aforementioned buck, consider using an isolated converter. Currently, when you turn off the high side contactors a voltage spike could potentially harm the buck. An isolated converter would prevent this and also decrease the ability for damage should there be a short between High-Voltage (HV) and Low-Voltage (LV) on the car-side.

Buzzer: The current buzzer isn't loud enough.

