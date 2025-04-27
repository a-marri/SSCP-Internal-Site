# resources

## SSCP - Resources

## Resources

CAN Catalog descriptions

badpec,0x1,0x70,uint32\_t, "Bad messages fram LTC6803 battery monitoring chips"

goodpec,0x1,0x71,uint32\_t, "Good same from LTC6803 battery monitoring chips"

goodpec,0x1,0x72,uint32\_t, "Total? messages from LTC6803 battery monitoring chips"

bstate,0x1,0x31,uint32\_t enum, "battery state (under voltage, below nominal minimum (pack trips), nominal, above array max (no charging is allowed), overcharged)"

soc,0x1,0x32,float, "State of charge from 0.0 to 1.0"

hghst\_v,0x1,0x35,float, "Highest cell voltage"

lwst\_v,0x1,0x36,float, "Lowest Cell voltage"

cell\_v,0x1,0x37,float, "Array of 27 cell voltages"

lwst\_c,0x1,0x38,uint32\_t, "Index of the lowest cell (0-indexed)"

hghst\_c,0x1,0x39,uint32\_t, "Index of thte highest cell (0-indexed)"

time,0x1,0x20,uint32\_t, "Time since BMS booted"

cstate,0x1,0x40,uint32\_t enum, "Car state (startup, waitForPrechargeDone, PostCzonkaDelay, RunningNominally, HardFault, OvervoltageFault, RecoveringDelay, RecoveringDecision) (look at bms\_1/inc/global.h for the actual enum definition)"

chrge\_en,0x1,0x41,bool, "Charging enabled--array and regen"

disch\_en,0x1,0x42,bool, "Discharging (throttle) enabled"

cznka\_en,0x1,0x43,bool, "Czonka enabled"

prchg\_en,0x1,0x44,bool, "Precharge enabled"

24bus\_en,0x1,0x45,bool, "24 volt bus enabled"

ntc1,0x1,0x46,float, "Thermistor 1"

ntc2,0x1,0x47,float, "Thermistor 2"

adc\_bat,0x1,0x48,float, "F4 ADC measurement of total battery voltage"

adc\_hv,0x1,0x49,float, "F4 ADC measurement of voltage on the hv bus"

avg\_curr,0x1,0x4A,float, "Current that BMS is drawing, averaged over a \~1s window.  Measured by the LTC4151"

min\_curr,0x1,0x4B,float, "See above, but minimum current over that window"

max\_curr,0x1,0x4C,float, "See above, but maximum current over that window"

err\_flgs,0x1,0x60,bool, "BMS error flags, not yet used"

vcr\_curr,0x1,0x50,float, "Vicor shunt current"

arr\_curr,0x1,0x51,float, "Array shunt current"

bcurr,0x1,0x52,float, "Battery shunt current"

mc\_curr,0x1,0x53,float, "Motor controller shunt current"

amphours,0x1,0x54,float, "Amp-hours (possibly currently amp-seconds or amp-millesconds"

Time,0x3,0x20,uint64\_t, "Front lightboard time since boot in ms"

lights brightness,0x3,0xEE,uint32\_t, "Packed lights data. Every 3 bits signify a light brightness value for a particular light, up to 10 lights total"

Braking,0x4,0x22,bool, "1 = Braking, 0 = Not Braking"

DriveMode, 0x4,0x23,uint32\_t, "Driver control's drive mode (0=forward;1=reverse;2=cruise)"

EnableThrottle,0x4,0x20,bool, "BMS telling driver controls to enable throttle"

EnableRegen,0x4,0x21,bool, "BMS telling driver controls to enable regen"

AvgSpeed,0x4,0x30,float, "Driver control's average of two Tritium velocities (m/s)"

AvgRPM,0x4,0x31,float, "Driver control's averge of two Tritium rpms"

AvgOdometer,0x4,0x32,float, "Same as above, but for odometer (meters)"

MotorTemp0,0x4,0x33,float, "Left Tritium motor temp (C)"

MotorTemp1,0x4,0x34,float, "Right Tritium motor temp (C)"

TritHeatSinkTemp0,0x4,0x39,float, "(C)"

TritHeatSinkTemp1,0x4,0x3A,float, "(C)"

TritiumAlive0,0x4,0x35,bool, "Driver controls has communication with left Tritium"

TritiumAlive1,0x4,0x36,bool, "Driver controls has communication with right Tritium"

TritiumCurrent0,0x4,0x37,float, "Amps"

TritiumCurrent1,0x4,0x38,float, "Amps"

TritiumErrorFlags0,0x4,0x3B,uint16\_t, "Tritium errors, refer to Tritium User Manual"

TritiumErrorFlags1,0x4,0x3C,uint16\_t, "Tritium errors, refer to Tritium User Manual"

TritiumLimitFlags0,0x4,0x3D,uint16\_t, "Tritium limit flags (what is limiting velocity), refer to Tritium User Manual"

TritiumLimitFlags1,0x4,0x3F,uint16\_t, "Tritium limit flags (what is limiting velocity), refer to Tritium User Manual"

DCTime,0x4,0x51,uint64\_t, "Driver controls time since boot (ms)"

ButtonState,0x4,0x50,uint32\_t, "Bitfield for steering wheel buttons"

CruiseKP,0x4,0x40,float, "Cruise control constant for P term"

CruiseKI,0x4,0x41,float, "Cruise control constant for I term"

CruiseSpeed,0x4,0x42,float, "Cruise control set-point speed"

speed\_mps,0x2,0x30,float, "Driver controls to button board announce speed"

cruise\_mps,0x2,0x31,float, "Driver controls to button board announce cruise set-point speed"

drive\_mode,0x2,0x32,uint32\_t, "DC to BB announce drive mode"

soc,0x2,0x33,float, "DC to BB state of charge \[0,1]"

current\_1,0x2,0x34,float, "DC to BB left Tritium current"

current\_2,0x2,0x35,float, "DC to BB right Tritium current"

motor\_temp\_1,0x2,0x37,float

motor\_temp\_2,0x2,0x38,float

tritium\_temp\_1,0x2,0x39,float

tritium\_temp\_2,0x2,0x3A,float

ledState,0x2,0x36,uint32\_t, "Driver controls to BB bitfield turning on LEDs on steering wheel"

bbtime,0x2,0x40,uint64\_t, "Button board time since boot (ms)"

Array-Voltage,0x6,0x10,float, "One MPPT's array voltage."

Array-Current,0x6,0x11,float, "One MPPT's current voltage."

Battery-Voltage,0x6,0x12,float, "One MPPT's output voltage to battery"

Temperature,0x6,0x13,float, "One MPPT's temperature (C)"

CATHASH,0x7,0x1,uint32\_t

VERSION,0x7,0x0,uint32\_t

VARIDS,0x7,0x2,uint8\_t

BOARDNAME,0x7,0x3,char

FWHASH,0x7,0xD,uint32\_t

HWREV,0x7,0xE,uint32\_t

SERIAL,0x7,0xF,uint32\_t

SYSTIME,0x7,0x10,uint64\_t

REBOOTFLAG,0x7,0x11,bool

gps unix time,0x7,0x20,int64\_t

gps latitude,0x7,0x21,float

gps longitude,0x7,0x22,float

gps speed,0x7,0x26,float

gps altitude,0x7,0x27,float

gps bearing,0x7,0x28,float

barometer temperature,0x7,0x23,float

barometer pressure,0x7,0x24,float

barometer altitude,0x7,0x25,float
