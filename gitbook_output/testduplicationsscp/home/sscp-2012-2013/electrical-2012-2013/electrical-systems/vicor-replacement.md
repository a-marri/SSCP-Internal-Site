# SSCP - Vicor Replacement

# Vicor Replacement

Work Log

Revision 1

Redesign TODOs

- Re-think FB circuit

- Resistors + fuses between VCC sources and control circuitry

2012-05-12

- Completely assembled. Tested it with 70V input.

- Feedback NPN began to smoke. Discovered the design created a large Vbe (approx. = Vin) - surprising that this eluded design review. Hacked feedback circuit to be a simple voltage divider.

- Replaced one busted npn (part of the Vin -> 15V circuit) and one potentially busted LT3837.

- Output voltage remains zero except a brief sustained rise during turnoff transient as the input cap drains. While on, Vfb is 3V (too high, should be 1.2V) and Vgate = 1V. During turnoff transient Vgate exhibits a square wave between 0 and 15V.

TODO: check feedback divider

2012-05-19

- Tested feedback divider - appears correct.

- Tied UVLO to VCC with a smaller resistor to account for the LT3837's current draw on that pin.

- Greg re-soldered the LT3837 and described my soldering as 'wretched' :(

- Appeared to be behaving strangely with a 70V input with the BK set at 100 Ohm - Vout rises asymptotically-ish to 24V over a period of about 150ms then falls abruptly to 0V, remaining off for 100ms.

- Tested it with a ~200 Ohm bank of power resistors. Output voltage appears correct.

- Tested it with Vin = 105V. The zener on the input darlington cascade exploded, blowing one pad off the board; the vias tying the pad to ground remain intact. Every piece of silicon on that ground was rendered inoperable.

- Re-soldered everything, appears to be working somewhat (~25V output with 500 Ohm load from the BK from a 17V input).

My hypothesis is as follows: a large voltage spike from the xformer's secondary that I'm using to power the control circuitry caused the linear regulator to fail short (very plausible considering leakage inductance and lack of protection), connecting the transformer's secondary directly to VCC, voltage spikes included (neither side of the linear regulator failed short to GND). The darlington subsequently failed, owing either to large reverse Vgs or to having so much current going through it through the xformer's secondary. This caused Vin to short through the first NPN, overcurrenting through the 15V zener.

TODO: test at incrementally higher voltages

2012-05-28

- At first the board exhibited very similar behaviour as at first (constant non-zero gate drive voltage even with sane other pin voltages). Reflowed the LT chip, and it worked.

- Tested it at 35VDC in.

- Output voltage is >50V at high resistance loads (5K), ~20V at lower resistance loads (50-200R). My hypothesis is when the chip detects a light load it goes into forced continuous conduction mode which could drive Vout too high. More datasheet reading required.

TODO: characterise Vout against Rload, work out what's up with the loop.

2012-06-08

- Tested it a little further and discovered a non-linear positive correlation between Vout and Vin.

- Examined feedback circuit. Discovered actual cause the npn failed last time - the design used a npn whereas the simulation and datasheet used a pnp. I am a tool.

- Confirmed suspicions using SPICE - when I modified the FB circuit the LT3837 freaked out and entered its default mode, which seemed to be a blind 90%-ish duty cycle (presumably just ton_min followed by toff_min, configured by various resistors). This explains why things broke at high voltages - Vout and consequently Vflyback went astronomical.

- Chose a MMBTA92-TPCT-ND PNP. I will need to yellow wire it in and re-design that part of the board.

TODO: wait until pnp arrives and yellow wire it on

[](https://drive.google.com/folderview?id=1pAcFnxtKe0Cv5Qc9PyE026DquU-eJ1G0)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1pAcFnxtKe0Cv5Qc9PyE026DquU-eJ1G0#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1pAcFnxtKe0Cv5Qc9PyE026DquU-eJ1G0#list" frameborder="0"></iframe>

