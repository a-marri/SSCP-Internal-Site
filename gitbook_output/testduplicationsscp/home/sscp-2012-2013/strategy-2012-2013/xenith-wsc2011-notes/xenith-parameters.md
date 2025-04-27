# xenith-parameters

## SSCP - Xenith Parameters

## Xenith Parameters

Dan Posch

SSCP

Oct 2011

***

* Read the ideas.pdf for more information  \*

***

\====================

Array basics

\====================

Sunpower C60

***

STC: unencapsulated, 1000 Wm^-2 at 25C

Impp at STC: 5.92A

Vmpp at STC: 0.575V

Pmpp at STC: 3.40W

Thermal coef (power): -0.32% per deg C

Dimensions: 125 mm^2 cut from 160mm diameter wafer

Area: 0.0153125 m^2 each

Array

***

Layout: 26 panels of 3x5 cells each&#x20;

Num cells: 390

Area: 5.9719 m^2

Encapsulation loss: err, "0.00%"

Power at STC (ignoring curvature): 1326 W

Power at STC: approx 1300W

Power at 40C: approx 1235W

Power at 50C: approx 1195W

Power at 60C: approx 1155W

Measured (Darwin Oct. 15):

Raw max observed power: 860 W with 20/26 strings

Adjusted max power: 1130 W (whole array) @ 1030 W/m^2 irrad, \~97% tracker eff.

Adjusted for temp,irrad,and trackers: 1185W at STC from cells

Adjusted for temp,irrad: 1150W at STC absorbed by the pack &#x20;

Adjusted for temp,irrad,and sink: 1122W at STC absorbed by the pack &#x20;

Bottom line: 1150 W&#x20;

\====================

Batteries

\====================

Count: 455 (35S13P)

Model: NCR18650s

Datasheet Ah/cell: 3.1

Discharge curve

***

RAW WH - 4757.328125

0x8 - A0AA9445261A4B45 - 4.757 raw kWh

0xB - 686D0548252BB547 - 136629 raw couls

0xC - 96A89645716DC444 - 4.821 adjusted kWh

Measured Ah/cell: 2.91

Internal resistance

***

0.05 to 0.07 ohms depending on temp

0.05 to 0.12 ohms depending on temp below 20% SOC

Bottom line: 0.06 ohms

\====================

Sam\_MPPT

\====================

Devid 24, messageids 0-3 (corresponding to mppt)

Really simple. Each message is four 2-byte int vals:

* in voltage (1/100 volts)
* current (milliamps)
* out (batt) voltage (1/100 volts)
* temp (1/100 deg C)

Endian??

\====================

Timestamps

\====================

The telemetry database currently uses .NET-style timestamps: an 8-byte value representing 100-nanosecond units since 0001-01-01, in UTC, not counting leap seconds.

This differs from the usual Unix timestamps (either seconds or milliseconds, etc since 1970-01-01, not counting leap seconds).

Here's the .NET timestamp corresponding to 1970-01-01: 621355968000000000

To get Unix time, in seconds:

unix\_time = (net\_time - 621355968000000000) / 10000000.0

Caveats about timestamps:

* World Solar Challenge is run entirely in Darwin time (UTC + 9:30), even though South Australia has a different timezone since it will be on Daylight Savings Time (UTC + 10:30).
* Timezone offsets are not always whole hours. See above.
* There is no year 0. The number of years between 0001-01-01 and 1970-01-01 is 1969. The number of years between -0001-01-01 and 0001-01-01 is 1.&#x20;
* There are 477 leap days between 0001-01-01 and 1970-01-01.
