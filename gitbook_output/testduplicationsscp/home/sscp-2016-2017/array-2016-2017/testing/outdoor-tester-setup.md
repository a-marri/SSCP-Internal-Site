# outdoor-tester-setup

## SSCP - Outdoor Tester Setup

## Outdoor Tester Setup

Equations to calculate STC curve and power from a normal curve are attached in a document called "STC Calculation" courtesy of Oliver Gochermann.&#x20;

Notes on getting rid of that little bump in the Keithley curve:

in the 10A range, the maximum pulse width is 2.5 ms

With an NPLC of 0.01, the measure time is 1.05 ms.

&#x20;   If the pulse width is set too low, it will get ignored and the keithley will just output the minimum pulse width it can while getting accurate readings

Try querying V-source range

Notes on getting Agilent setup:

Scripts will be posted here soon, otherwise are on SVN under sundae\_array\_testing (or something like that? ask mchen18@stanford.edu)

If error message pops up, press "View" button to view them; use knob to scroll, then press view to confirm you want to look at error messages; then use knob to scroll through error messages. The list of them is on the Agilent 34970A page.&#x20;

For pyVisa, if your device is "agilent," then use agilent.write("stuff:stuff") to send commands, and agilent.query("stuff:stuff?") to query it; otherwise, your queries won't work!

Also note that the current script uses Python 2.7 syntax.&#x20;

Good Commands to know:

agilent.query("SYS:ERR?) clears one error off the FIFO queue for errors and reads it to you

&#x20;   after more than 10 errors stack up, you'll get a queue overflow error

agilent.write("ROUT:CLOSe (@\<channel\_list>") will close the relays on that channel list

&#x20;   naming syntax is 101:120 are the 20 channels on slot 1, 201:220 are for slot 2, etc.&#x20;

agilent.query("ROUT:CLOSe? (@\<channel\_list>)") queries if closed

&#x20;   returns 1 for success, 0 for not closed

agilent.query("ROUT:DONE?") queries if done with previous commands

&#x20;   returns 1 for success, 0 for failure

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1M8Lu4wO889YZOxSWxL6qCqlbGsE-iqab#list)
