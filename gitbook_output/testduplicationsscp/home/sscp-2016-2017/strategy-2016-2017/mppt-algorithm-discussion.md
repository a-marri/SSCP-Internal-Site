# SSCP - MPPT Algorithm Discussion

# MPPT Algorithm Discussion

loganherrera [11:29 AM]  

@gfiore how much total energy was consumed while the array was turned off during the 2015 race?

[11:30]  

this is a proxy for my actual question of:

[11:31]  

if the array had stayed on, but had limited output power to exactly what the car was drawing at high SoC, how much more energy is extracted from the cells

[11:33]  

the MG Solar (Dutch Manufacturer) MPPT + BMS system Nuon + Twente use does this, and I would like to know how much it matters

gfiore [2:58 PM]  

@loganherrera:  I'll look into this, but we had telemetry connectivity issues the first day, so I may not have the data to work with.

[2:58]  

Also, we don't explicitly track when the array is on or off, so I may just have to guess at segments, even though they could be shadow, etc.

loganherrera [3:29 PM]  

don't we have the commands sent from BMS to MPPT to turn them off?

[3:30]  

hrmm ok

[3:30]  

what about the end of last day?

kelseyjosund [4:27 PM]  

We don’t have those commands parsed, although they may have been sent

[4:27]  

I’d have to look at the code running on the IMU at that time, which is actually an open question right now

[4:27]  

But if we had connectivity issues we wouldn’t have had that anyway

loganherrera [4:38 PM]  

MPPT current is parsed and would be 0

[4:38]  

that's a solid indicator

kelseyjosund [8:20 PM]  

Ok, we can look through logs for that

[8:20]  

Not sure about end of last day — I don’t recall connectivity issues

loganherrera [10:43 PM]  

I'm hypothesizing that the surplus power generated during city driving on the last day is a proxy for the first day

[10:44]  

I also recall first day connectivity issues happening after leaving city proper

[10:44]  

My point is to ask what the data actually shows for first day

----- Today November 6th, 2016 -----

gfiore [1:08 PM]  

@loganherrera:  The data shows 3Wh of power could have been saved by going directly from array to motors. That's equivalent to 2.7 seconds of race time. Aka, not useful.

I told Kelsey this before, but I'm calling BS on that company's claim that their BMS algorithm's array power diverting actually saved Nuon/Twente any power.

