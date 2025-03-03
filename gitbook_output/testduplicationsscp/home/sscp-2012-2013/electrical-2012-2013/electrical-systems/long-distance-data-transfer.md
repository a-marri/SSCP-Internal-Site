# SSCP - Long Distance Data Transfer

# Long Distance Data Transfer

Requirements:

This project would be to convey data over long range distances during the race. It should be able to clearly send signals at a distance great than 5 miles without line of site and will be used mainly for conveying critical information needed for strategy such as the solar insulation down the road. It should be able to run off the 12V that most car cigarette lighters put out and be able to convey data to a laptop/wireless network so that telemetry can receive the data.

Information we currently want to send: location, solar insulation, time, short messages.

Proposed Solutions:

Sending Data: This board would interface with ham radio and send/receive the appropriate data protocol.

 -Using a ham radio: This might work to send data over long distances of up to 25 miles, but it would require the users to have a licence. It would also not work for getting data from a distance further than that 25 miles and we may want to send data or communicate with individuals in scout over a longer distance. (idea credit: Sasha)

-Using Satellite communication: Satellite communication would work over a wide range of distances but has two main disadvantages. 1. you have to pay per message sent. When sending data, this cost could really add up. 2. There has been a lot of talk about them not being reliable enough. Iridium has apparently improved, but this is to be seen how good it is.

-Other alternatives: Some other kind of HF or VHF communication.

-Possibly just having solar base stations set up near towns with cell reception that will send us data when we have cell network reception. This could give us data over a long period of time so that we know what the data. (idea cred: Sasha)

Measuring Solar Insulation: A simple photo diode could be used to measure the sun's intensity and software can account for the non-linear curve and maybe even shift over temperature. A far more accurate way would be to take our own panel and just measure the short circuit current or trace the curve.

Knowing Position and time: A GPS receiver could work great.

Connecting to telemetry: Maybe using a USB to someone's laptop or wirelessly.

Companies doing interesting things with APRS:

http://www.argentdata.com/

[http://www.argentdata.com/](http://www.argentdata.com/)

http://www.byonics.com/

[http://www.byonics.com/](http://www.byonics.com/)

Links for HAM radio:

http://hflink.com/interface/

http://www.ke4nyv.com/aprs.htm

http://www.coffeepower.net/ham/pin_ham.htm#packet

http://www.tcmaker.org/wiki/doku.php?id=hamradio:aprs

[http://www.tcmaker.org/wiki/doku.php?id=hamradio:aprs](http://www.tcmaker.org/wiki/doku.php?id=hamradio:aprs)

http://forums.qrz.com/archive/index.php/t-328036.html

[http://forums.qrz.com/archive/index.php/t-328036.html](http://forums.qrz.com/archive/index.php/t-328036.html)

http://cazsys.com/APRS/APRS%20Hardware%20Options.pdf

[http://cazsys.com/APRS/APRS%20Hardware%20Options.pdf](http://cazsys.com/APRS/APRS%20Hardware%20Options.pdf)

http://garydion.com/projects/whereavr/

[http://garydion.com/projects/whereavr/](http://garydion.com/projects/whereavr/)

http://www.rev0proto.com/wiki/index.php/Rev0Trac

[http://www.rev0proto.com/wiki/index.php/Rev0Trac](http://www.rev0proto.com/wiki/index.php/Rev0Trac)

