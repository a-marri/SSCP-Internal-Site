# SSCP - Sunwhale 2014-2015 Suspension Design

# Sunwhale 2014-2015 Suspension Design

# KEY PARAMETERS

[](#h.hjjwi4nu2j0t)

Important numbers:

Wheelbase = 1842 mm

track width = 1400 mm

2015 WSC Race-Ready Corner Weights

![](../../../../../assets/image_8d6c514834.jpg)

# High-level design decisions

[](#h.njjqrq2anq51)

* Leading-arm vs. double wishboneAckerman steering vs. parallel steering
* Leading-arm vs. double wishbone
* Ackerman steering vs. parallel steering

* Leading-arm vs. double wishbone
* Ackerman steering vs. parallel steering

Leading-arm vs. double wishbone

Ackerman steering vs. parallel steering

## Leading-arm vs. double wishbone (From alumni design review)

[](#h.jx0vbethk5hx)

Leading-arm pros:

* No bump scrub (efficiency gains)Can be entirely packaged inside the fairing, leading to a thinner main airfoil
* No bump scrub (efficiency gains)
* Can be entirely packaged inside the fairing, leading to a thinner main airfoil

* No bump scrub (efficiency gains)
* Can be entirely packaged inside the fairing, leading to a thinner main airfoil

No bump scrub (efficiency gains)

Can be entirely packaged inside the fairing, leading to a thinner main airfoil

Leading-arm cons:

* Unfamiliar/complex designLongitudinal control arms must accommodate the wheel’s full range of steer travel
* Unfamiliar/complex design
* Longitudinal control arms must accommodate the wheel’s full range of steer travel

* Unfamiliar/complex design
* Longitudinal control arms must accommodate the wheel’s full range of steer travel

Unfamiliar/complex design

Longitudinal control arms must accommodate the wheel’s full range of steer travel

Double wishbone pros:

* Design is familiar to us from previous cyclesOffers more flexibility in placement of control arms/hardpoints
* Design is familiar to us from previous cycles
* Offers more flexibility in placement of control arms/hardpoints

* Design is familiar to us from previous cycles
* Offers more flexibility in placement of control arms/hardpoints

Design is familiar to us from previous cycles

Offers more flexibility in placement of control arms/hardpoints

Double wishbone cons:

* Bump scrub (can be minimized, but it will still be present)Wheel cambers during bump travelHaving both a kingpin and a caster angle will increase jacking forces
* Bump scrub (can be minimized, but it will still be present)
* Wheel cambers during bump travel
* Having both a kingpin and a caster angle will increase jacking forces

* Bump scrub (can be minimized, but it will still be present)
* Wheel cambers during bump travel
* Having both a kingpin and a caster angle will increase jacking forces

Bump scrub (can be minimized, but it will still be present)

Wheel cambers during bump travel

Having both a kingpin and a caster angle will increase jacking forces

# Alumni design review notes: 12/7/2014

[](#h.tisjlr5sa32t)

* An asymmetric aerobody design would lead to many stability concerns that would need to be resolved through careful suspension design. Some examples:Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.Luminos's suspension parameters ensured good stability/handling. They should be left the same for Sunwhale.Even though the control arms for a leading-arm geometry will not take up much width while allowing for the full range of the wheel's steer travel, they will still govern the width of the fairing. That is not good.
* An asymmetric aerobody design would lead to many stability concerns that would need to be resolved through careful suspension design. Some examples:Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.
* Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Luminos's suspension parameters ensured good stability/handling. They should be left the same for Sunwhale.
* Even though the control arms for a leading-arm geometry will not take up much width while allowing for the full range of the wheel's steer travel, they will still govern the width of the fairing. That is not good.

* An asymmetric aerobody design would lead to many stability concerns that would need to be resolved through careful suspension design. Some examples:Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.
* Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Luminos's suspension parameters ensured good stability/handling. They should be left the same for Sunwhale.
* Even though the control arms for a leading-arm geometry will not take up much width while allowing for the full range of the wheel's steer travel, they will still govern the width of the fairing. That is not good.

An asymmetric aerobody design would lead to many stability concerns that would need to be resolved through careful suspension design. Some examples:

* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.
* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.
* Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.

* Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.
* Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.

Increased lateral force on the driver-side tires when cornering, leading to faster tire wear.

Yaw moment around the CG when braking, unless brakes are carefully calibrated. Also, brakes may lock up on the lighter side of the car, due to less available friction.

Luminos's suspension parameters ensured good stability/handling. They should be left the same for Sunwhale.

Even though the control arms for a leading-arm geometry will not take up much width while allowing for the full range of the wheel's steer travel, they will still govern the width of the fairing. That is not good.

# Wheelbase Analysis

[](#h.ncb2ibjxhfyo)

Aravind, Max, and Caroline Abbott worked on an analysis of solar car wheelbases as an ME227 final project. Below is our summary to the team.

Hey Team,

Just thought you may be interested in seeing the results of a final project that Aravind, myself, and a friend worked on for ME227 (vehicle dynamics). 

We implemented a car model aimed at capturing the pitch and bounce dynamics of a solar car. The motivation is that we might be able to find parameters for a car (like its wheelbaseor suspension parameters) that minimize the angle of attack change as the car goes over the Stuart Highway. If you're wondering where/why this gets interesting, it's because the rear wheel sees a delayed version of what the front wheel sees!

Future work includes fully implementing Luminos' suspension geometry, so this is the modeled frequency response of a "solarcar type vehicle" going over a road with 1cm amplitude at 20m/s:

It turns out that all the data we can find on chip-sealed roads is at a much higher wavenumber than the frequencies at which a solar car's angle of attack change is most sensitive. Our takeaway is that given a road profile of the Stuart Highway on the order of meters, we could make informed decisions about how to build a car to be most efficient on the roads in Australia. It might be worth looking into mapping the road surface when we are next in Australia. Just some food for thought.

Thanks for reading, and hopefully you found this interesting!

# Exploratory leading-arm geometries:

[](#h.8cpaqnaqhkfz)

## Multi-link leading arm inspired by Xenith rear suspension

[](#h.xjjt60fiywu3)

![](../../../../../assets/image_f54efea140.png)

## Simple leading-arm geometry inspired by Nuna7

[](#h.zh0swzbcqzr8)

![](../../../../../assets/image_1984a2eb39.png)

![](../../../../../assets/image_db1813ec48.png)

## Leading-arm geometry with camber gain and kingpin angle

[](#h.let04fys0fku)

On Nathan Hall-Snyder's suggestion, I lowered the inboard hardpoint on the upper control arm. This causes the upper ball joint on the upright to move laterally in jounce/rebound, thus adding some camber gain to the bump travel. Camber gain is necessary for stability in cornering, because it maximizes the effective stiffness of the outer tire. This geometry also incorporates a kingpin angle, which reduces the scrub radius. The following parameters were used (these are identical to the parameters used in Luminos's suspension):

* Total camber change over full range of bump travel: 0.4 degreesCaster angle at maximum jounce: 5 degrees. This ensures that there is always enough mechanical trail to maintain the steering's self-centering behavior.Kingpin angle at 0 bump travel: 7.5 degrees.Scrub radius at 0 bump travel: 7 mm. This is small enough to prevent bump steer, but large enough to ensure that the car behaves properly in low-grip scenarios. (see http://www.sccaforums.com/forums/aft/6006)
* Total camber change over full range of bump travel: 0.4 degrees
* Caster angle at maximum jounce: 5 degrees. This ensures that there is always enough mechanical trail to maintain the steering's self-centering behavior.
* Kingpin angle at 0 bump travel: 7.5 degrees.
* Scrub radius at 0 bump travel: 7 mm. This is small enough to prevent bump steer, but large enough to ensure that the car behaves properly in low-grip scenarios. (see http://www.sccaforums.com/forums/aft/6006)

* Total camber change over full range of bump travel: 0.4 degrees
* Caster angle at maximum jounce: 5 degrees. This ensures that there is always enough mechanical trail to maintain the steering's self-centering behavior.
* Kingpin angle at 0 bump travel: 7.5 degrees.
* Scrub radius at 0 bump travel: 7 mm. This is small enough to prevent bump steer, but large enough to ensure that the car behaves properly in low-grip scenarios. (see http://www.sccaforums.com/forums/aft/6006)

Total camber change over full range of bump travel: 0.4 degrees

Caster angle at maximum jounce: 5 degrees. This ensures that there is always enough mechanical trail to maintain the steering's self-centering behavior.

Kingpin angle at 0 bump travel: 7.5 degrees.

Scrub radius at 0 bump travel: 7 mm. This is small enough to prevent bump steer, but large enough to ensure that the car behaves properly in low-grip scenarios. (see http://www.sccaforums.com/forums/aft/6006)

[ http://www.sccaforums.com/forums/aft/6006](http://www.sccaforums.com/forums/aft/6006)

![](../../../../../assets/image_cd383b78e4.png)

![](../../../../../assets/image_230c8c6456.png)

![](../../../../../assets/image_66f1e9e9c6.png)

# Exploratory double-wishbone design

[](#h.jd3l9th7heus)

This is a simple double-wishbone design that uses the same parameters as Luminos's suspension. The control arms are separated vertically by 10 cm, which will hopefully be small enough to fit them into a thin main airfoil.

![](../../../../../assets/image_818511b96c.png)

After discussing with Nathan Hall-Snyder, we agreed that having long A-arms separated by only 4 inches is not a good idea; previous solar cars with this suspension configuration have had problems with stability and buckling loads. This is an important consideration to keep in mind, going forward.

E-mails:

Hey Aravind,

I was looking through the PDM stuff, and I saw a suspension design with hardpoints suspiciously close to each other (4" in vertical) in addition to having the wheels far away from. I don't know if it's a work in progress or not - discard this if it is.

It just reminded me of an older design that was rather unstable, the Umicore Inspire.

Their car was extremely shaky/unstable on the road - they ended up getting blown off the road and into a tree. There wasn't much left of their car, but here's what happened to their suspension:

https://lh5.googleusercontent.com/-yTXx0V0hzjk/SzqN1RVJJ1I/AAAAAAAAGjU/vDDwkte1gS0/s800/IMG_0544.JPG

I would caution against adjacent hardpoints paired with long a-arms - cars I've seen in the past with these traits have not performed well.

The Tokai design is pretty reasonable, except for the driver's leg going through the suspension linkages. Their hardpoints are probably 5 or 6 inches apart and the a-arms are reasonably short, so the buckling forces are manageable. If properly designed it would be unlikely to fail.

The cautionary tale from Umicore is that with closely spaced, long a-arms the difficult-to-simulate buckling forces may cause problems. I wanted to make sure that you guys were aware of that challenge.

# Suspension fitting inside aerobody

[](#h.mqxcfw7rd2yk)

## Sunwhale_camber3_thick3

[](#h.mw6ha7mfvifh)

![](../../../../../assets/image_463e0a94d6.png)

![](../../../../../assets/image_b305b366ab.png)

![](../../../../../assets/image_f2421012b7.png)

![](../../../../../assets/image_f23f09a8a5.png)

Hey guys,

I tried fitting the double wishbone suspension in the catamaran that Darren sent me. Here's what I have so far. I shortened the control arms by ~3 inches (80 mm), and made the upright longer. It looks like the aerobody is about 5 inches thick at the front wheel wells, which means I couldn't place the control arms any farther apart than before. Even so, there's not enough room for the full jounce/rebound travel (see the attached pictures).

On the bright side, I was able to find a pretty good steering geometry for that wheelbase.

## Sunwhale_camber3_thick6

[](#h.647pyqlrm36t)

![](../../../../../assets/image_431e6bea86.png)

![](../../../../../assets/image_89191fb358.png)

![](../../../../../assets/image_16d64144dd.png)

![](../../../../../assets/image_9ed35c9bfd.png)

Hey guys,

I tried fitting the double-wishbone suspension in the sunwhale_camber3_thick6 models that Darren sent me. Here's how it looks inside the model with the 2.8m fairing. I was able to separate the control arms vertically by 5". The front suspension seems to fit ok, although I don't know if the thickness of the layup will cause problems later on. The rear suspension is a bit cramped; in rebound, the lower control arm is definitely constrained by the fillet on the fairing (see the pic -- the straight line is the A-arm, the curved line is the edge of the fillet). I could move it forward a bit, but the wheelbase is already a little too short in this configuration (~1.5m). Would it be possible to make the main foil about an inch thicker towards the rear?

Thanks,

-Aravind

# Suspension fit into Thickness 66 model

[](#h.qs7gpnpdqty)

This model, with slightly more fleshed-out suspension components, shows that the wheels do not have enough room to steer on the inboard side. Following this mishap, I have sent Anna a wheel envelope model that she can use to size the fairings.

![](../../../../../assets/image_73af8bd71a.png)

![](../../../../../assets/image_4af293cd39.png)

# Transition to multi-link suspension (repurposing Luminos geometry)

[](#h.sfuvxh49e9ir)

On Nathan Hall-Snyder's recommendation, I decided to switch to the Luminos style multi-link geometry because it would make it easier to steer a front-wheel-drive car, and do a better job of handling the loads on the lower ball joint. Although this would essentially involve re-using a design from Luminos, rather than exploring a new design, it is a tried and true solution that would give us more freedom in the mechanical design of the individual components. Making the transition to multi-link simply involved making a few edits to the original double-wishbone geometry sketch. The new geometry has the same control arm spacing as the original double-wishbone, and the same parameters (kingpin/caster angle, scrub radius, etc.) as Luminos.

![](../../../../../assets/image_020c647cf3.png)

![](../../../../../assets/image_d5723eca13.png)

# Sunwhale multilink v8: First practical suspension geometry simulated in Lotus Shark

[](#h.wrndy9z6enbt)

The first few iterations of the multi-link suspension geometry followed a worrying trend, which led to very short control arms spaced very close together vertically in order to fit the entire range of bump travel inside a thin main foil. This in turn led to very high simulated loads. Following some debate, it was decided that the main foil thickness would be increased to allow both control arms to extend into the main foil while still having enough room for jounce/rebound travel. Furthermore, to decrease loads on the suspension components, I increased the control arm vertical spacing and also made the control arms longer than in previous iterations.

Parameters:

* Vertical A-arm spacing: 5.5 inches (139.7 mm)Hardpoint-to-wheelhub lateral distance: 350 mm
* Vertical A-arm spacing: 5.5 inches (139.7 mm)
* Hardpoint-to-wheelhub lateral distance: 350 mm

* Vertical A-arm spacing: 5.5 inches (139.7 mm)
* Hardpoint-to-wheelhub lateral distance: 350 mm

Vertical A-arm spacing: 5.5 inches (139.7 mm)

Hardpoint-to-wheelhub lateral distance: 350 mm

![](../../../../../assets/image_7f4744a38f.png)

![](../../../../../assets/image_441b1ff636.png)

![](../../../../../assets/image_cfc09ab059.png)

## Lotus Shark results:

[](#h.swkev8ro9j45)

![](../../../../../assets/image_4404d6fae1.png)

See attached text file with results.

## Final suspension geometry characteristics:

[](#h.h3l29fhpru1l)

Ackerman % vs. rack travel (mm):

![](../../../../../assets/image_db6af07152.png)

Camber gain (deg) vs. bump travel (mm):

![](../../../../../assets/image_cd2544cb0d.png)

Bump scrub (mm) vs. bump travel (mm):

![](../../../../../assets/image_e9260a0047.png)

Bump steer (deg) vs. bump travel (mm): (geometry designed for 0 bump steer)

![](../../../../../assets/image_3d8ea98b78.png)

Shocks Specs from Kaz

![](../../../../../assets/image_9d43cba62d.png)

[](https://drive.google.com/folderview?id=1o-F1fyldMihv19CZFCO3NEX1JaX_JnV4)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1o-F1fyldMihv19CZFCO3NEX1JaX_JnV4#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1o-F1fyldMihv19CZFCO3NEX1JaX_JnV4#list" frameborder="0"></iframe>

