# SSCP - Luminos Electrical Post-Analysis

# Luminos Electrical Post-Analysis

## Original Design Goals: 

[](#h.klexhe9pz67r)

##     Like much of the 2012-2013 design cycle, the overall design focus for Luminos’s electronics was reliability at all costs while (as in many cycles) doing as much custom as possible. To that end we purchased the most time-consuming and error-prone parts of the high-voltage bus (the MPPTs and the Motor Controllers) off the shelf and focused our efforts on the Battery Management System and low-voltage control/indication electronics. 

[](#h.o70yvvd1jv4k)

## What Worked:

[](#h.kl7zmqkmp1yq)

    Over the course of the race, we didn't have to spend any time on the side of the road on account of the electrical system, and no boards were damaged/needed replacement. When inspected every night, all connectors remained sturdily attached, the latches remained latched on the HVA280s, and the Phoenix connectors remained torqued. After re-tweaking of some calibration constants in Australia, the cruise control worked as intended, while the other control systems remained working as they were in the US without changes required. 

    

    It cannot be overstated how important this reliability is. Many teams at WSC either didn't complete the race or were significantly hindered by their electrical systems. To the best of my knowledge: Twente exploded a good deal of their electrical system due to an incomplete precharge, though this was at night so installing spares didn't directly effect their race time. A Michigan EE has told me that it is not uncommon for them to do similar things to their systems due to their continued use of a multi-switch breaker box for main power routing instead of a one-switch startup. UNSW blew their main pack fuse (presumed underspecced) under braking at Hidden Valley, with the resulting inductive ringing exploding both of their Tritiums and requiring extensive repair. Their main HV-LV DC DC also experienced issues that took out Hidden Valley practice time. While not strictly related, Minnesota experienced intermittent winding shorts in their custom motor, claiming the lives of several of their custom motor controllers along with (I believe) at least one Tritium. Michigan also had a massively shorted array (cells described as "completely black on the back") due to improper sealing and wiring, necessitating complicated and lengthy repairs in the days leading up to the race (and potentially during the race as well, though this is unconfirmed). Lastly, the US High School team (Mississippi Choctaw) arrived in Australia to find that their battery pack tabs had completely corroded during ocean shipment due to (at the very least) poor packaging, leaving them with no car to run. 

## What Didn't:

[](#h.plhv0t6ws0gb)

### Major Race-Influencing Issues:

[](#h.wi5jda9at3c)

    In rear-view vision scrutineering, the car was positioned directly facing an open door into the bright sun, and the camera system couldn't autobalance the dynamic range of light presented to the camera, and struggled to autofocus due to the large obstruction of the rear pillar of the bubble. Additionally, the camera was not mounted sufficiently strongly for the tastes of the WSC officials. The first two problems were solved by clever code hackery by Eric to hardcode some values, the last problem was solved with a layup of a flat plate of carbon to mount the license plate and camera. We had also mounted a secondary rear-view system, consisting of two pinhole cameras, two small LCDs, and a DC-DC from 24V to 12V, all purchased at Jaycar Electronics. This system took unknown but presumably terrible power, but was removed after the original system passed scrutineering.  

    This was only the first problem for the primary rear-view camera system, however. During normal operation, the telemetry box/rear view LCD would overheat and throw the CPU into a reboot loop, disabling all power save functionality and defaulting the backlight to full brightness. This ~10W of draw didn't exactly help matters thermally. Hence, rear-view was off for large sections of the race. By a pure stroke of luck, by the time we hit Alice Springs it had cooled off enough that it would at least work sometimes, and one of those times happened to be when it was inspected for operation at the Alice Springs control stop. Penalties for failing that second round of scrutineering are unknown by the author, but presumed painful. 

    Did I mention that the telemetry box/rear view system drew 10W? That was just the start. The electrical system as a whole drew an average of ~47.9W continuous for the entire race, costing approximately 52 extra minutes of race time (compared to zero quiescent), equivalent to 131 kg of extra mass. See the first link for a breakdown of where that power went (measured after the race). This problem was known to us before the race, though the effect it would have on the race time was only calculated later. However, by the time we started caring about that in any detail (instead of just focusing on making *something* work) it was too late to make any major changes.    

[ That was just the start.](http://i.imgur.com/cx9gk.gif)

[~47.9W continuous](/stanford.edu/testduplicationsscp/home/sscp-2012-2013/electrical-2012-2013/luminos-low-voltage-electrical-draw)

[ 52 extra minutes](/stanford.edu/testduplicationsscp/home/general-design-principles/design-metrics)

Max's analysis of BMS fail can be found here.

[ here](/stanford.edu/testduplicationsscp/home/sscp-2012-2013/electrical-2012-2013/electrical-systems/bms-7)

### Other Issues:

[](#h.3gvou362uk29)

    When the headlights and hazards (both turns signals) were turned on at the same time, the power draw would approach the maximum allowed by the Vicor, and the safety power-limiting protection of the BMS would disable the 24V electrical system, turning off the car. This was easily fixed by turning the car off and on again (this would in the process reset the lights to off, so this would not be a recurring cycle) but is still an slightly embarrassing fail.      

    The first rev of precharge detection circuitry on the MPPT interface board didn't work at all, leading to a slight explosion on the bottom third of the BMS board, a resistor losing 6 orders of magnitude of resistance, and a very sad Max. To combat this, a software lockout of 45 seconds (very conservatively estimated based on time constant of precharge resistor used + 6xMPPTs with 1200uF of cap per MPPT) was implemented. This successfully prevented any further explosions, but caused 45 seconds of dead time between when the car was turned on and when we would begin charging. Fortunately, to the best of my knowledge this penalty was only paid once at the start of each day (I don't remember having to reboot the car during the race, but if we did someone is free to correct me) at an approximate cost of 12.5 watt-hours per occasion (assuming 1000 watts * 45 seconds). 

