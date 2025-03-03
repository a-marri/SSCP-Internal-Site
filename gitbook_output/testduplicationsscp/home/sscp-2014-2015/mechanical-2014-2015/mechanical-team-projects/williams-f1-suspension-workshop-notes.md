# SSCP - Williams F1 suspension workshop notes

# Williams F1 suspension workshop notes

Presentations prepared for Williams are here and here.

[ here](https://docs.google.com/presentation/d/1g38TCaNLkXQ50zSOHnQ2s0-2o9ToZvHOVQHa3ExYJTQ/edit#slide=id.p16)

[ here](https://docs.google.com/presentation/d/1jYpDSUojwqGb9eo9A2fwFF2ssdu7JIXKLA3FpVbIvvs/edit)

These are Aravind's notes from the suspension design workshop offered to the team on December 15, 2014 by Phil Ingram, suspension engineer for Williams Advanced Engineering, and former suspension designer for Red Bull Racing and McLaren-Mercedes F1 teams.

# Formula 1 suspensions

[](#h.sujlqse9g1c5)

Important trade-offs: (I wasn't able to copy all of them down)

* Ride vs. Aero performance: The suspension needs to hold the car at the optimum ride height for aero performance, but also needs to provide some level of cushioning for the driver.Stability vs. response: The car needs to be agile and responsive to driver input, but also needs to handle in a stable manner.
* Ride vs. Aero performance: The suspension needs to hold the car at the optimum ride height for aero performance, but also needs to provide some level of cushioning for the driver.
* Stability vs. response: The car needs to be agile and responsive to driver input, but also needs to handle in a stable manner.

* Ride vs. Aero performance: The suspension needs to hold the car at the optimum ride height for aero performance, but also needs to provide some level of cushioning for the driver.
* Stability vs. response: The car needs to be agile and responsive to driver input, but also needs to handle in a stable manner.

Ride vs. Aero performance: The suspension needs to hold the car at the optimum ride height for aero performance, but also needs to provide some level of cushioning for the driver.

Stability vs. response: The car needs to be agile and responsive to driver input, but also needs to handle in a stable manner.

In a nutshell, F1 cars are terrible platforms for a suspension designer. The front suspension is surprisingly cramped, since the nose is generally placed as high as possible for aerodynamic reasons. So there is very little scope for hardpoint placement, and no suspension components can extend under the nose.

One really mind-blowing detail is that they use carbon-fiber flexures instead of ball joints at the inboard hardpoints. These are designed to take only longitudinal loads, while being compliant vertically.

## Front suspension details

[](#h.vo6gk8piaarj)

* 10-20 mm of bump travel; very restricted because the front wing needs to be kept at the correct ride height.Very bad suspension kinematics, due to aero constraints. This includes an outboard instantaneous center, and very high castor and kingpin angles (he didn't say how much). Scrub radius is also very high due to the width of the tires.Inerter ("spinning damper") used to improve ride quality.
* 10-20 mm of bump travel; very restricted because the front wing needs to be kept at the correct ride height.
* Very bad suspension kinematics, due to aero constraints. This includes an outboard instantaneous center, and very high castor and kingpin angles (he didn't say how much). Scrub radius is also very high due to the width of the tires.
* Inerter ("spinning damper") used to improve ride quality.

* 10-20 mm of bump travel; very restricted because the front wing needs to be kept at the correct ride height.
* Very bad suspension kinematics, due to aero constraints. This includes an outboard instantaneous center, and very high castor and kingpin angles (he didn't say how much). Scrub radius is also very high due to the width of the tires.
* Inerter ("spinning damper") used to improve ride quality.

10-20 mm of bump travel; very restricted because the front wing needs to be kept at the correct ride height.

Very bad suspension kinematics, due to aero constraints. This includes an outboard instantaneous center, and very high castor and kingpin angles (he didn't say how much). Scrub radius is also very high due to the width of the tires.

Inerter ("spinning damper") used to improve ride quality.

## Rear suspension details

[](#h.620nx7nx61di)

* 70-100 mm of bump travel; a lot more compliant than the front suspension.Spring rate roughly 400 N/mm; very high, but still a lot softer than the front suspension.High static ride height.Pullrod suspension components inside the gearbox; requires a lot of disassembly every time a component is switched out.20-30 degrees of camber gain.
* 70-100 mm of bump travel; a lot more compliant than the front suspension.
* Spring rate roughly 400 N/mm; very high, but still a lot softer than the front suspension.
* High static ride height.
* Pullrod suspension components inside the gearbox; requires a lot of disassembly every time a component is switched out.
* 20-30 degrees of camber gain.

* 70-100 mm of bump travel; a lot more compliant than the front suspension.
* Spring rate roughly 400 N/mm; very high, but still a lot softer than the front suspension.
* High static ride height.
* Pullrod suspension components inside the gearbox; requires a lot of disassembly every time a component is switched out.
* 20-30 degrees of camber gain.

70-100 mm of bump travel; a lot more compliant than the front suspension.

Spring rate roughly 400 N/mm; very high, but still a lot softer than the front suspension.

High static ride height.

Pullrod suspension components inside the gearbox; requires a lot of disassembly every time a component is switched out.

20-30 degrees of camber gain.

## Engineering tools and vehicle dynamics

[](#h.8u7rogpngnv6)

* ADAMS/SimpackFE integration
* ADAMS/Simpack
* FE integration

* ADAMS/Simpack
* FE integration

ADAMS/Simpack

FE integration

The car is simulated as being in static equilibrium at each point on the track. A lap is then simulated by "marching" the car around the track and calculating the static loads at each point. This is good for getting a rough idea of G-forces and lateral acceleration at each point.

Tires are characterized during winter testing, by mapping lateral G sensor readings to slip angles calculated via GPS sideslip measurements.

# Comments on solar-car suspension

[](#h.ayszeul2kbw3)

## Phil's list of solar car suspension requirements

[](#h.q3wauxqke97q)

(In a nutshell -- again, I wasn't able to copy all of them down)

* Low lateral scrubGood straight-line stability for crosswind performanceSmall frontal footprint, for good packaging inside fairings
* Low lateral scrub
* Good straight-line stability for crosswind performance
* Small frontal footprint, for good packaging inside fairings

* Low lateral scrub
* Good straight-line stability for crosswind performance
* Small frontal footprint, for good packaging inside fairings

Low lateral scrub

Good straight-line stability for crosswind performance

Small frontal footprint, for good packaging inside fairings

## Double-wishbone vs. Leading-arm

[](#h.a6dh85m7ahwj)

Both the double-wishbone and the leading-arm have very low lateral stiffness, which will make the car feel skittish in crosswinds. However, Phil admired Nuon's leading-arm design because it was obviously optimized for straight-line performance, plus it had 0 lateral scrub and a very low frontal profile. The double-wishbone geometry could potentially have a very high lateral scrub, exacerbated by the flexing of the rim and other suspension components. Furthermore, it has a large frontal profile and very high loads on the lower control arm.

The low lateral stiffness can be dealt with by adding enough castor and kingpin angle (which we have done). Another option is to make sure to mount the shock off the steering axis. Mounting the shock on the steering axis will eliminate jacking forces from the shock when turning, since there is no moment arm about the steering axis. However, having these jacking forces will make the steering feel "heavier" and more stable as a result.

Phil also commented that adding camber gain is a rather unnecessary feature on a solar car, since most of the race course is a straight line.

## Comments on our load simulation

[](#h.hrvcqee5wyg8)

A combined 4g bump, 2g brake and 1g corner simulation is way too extreme. For example, we will probably never see a 1g corner in the solar car. And most production cars experience only 3 g's of bump load when going over a pothole.

It would be a good idea to instrument Luminos to get an idea of shock loads and cornering loads, then use these more realistic loads in our Lotus Shark simulation. When doing FEA on the components, a factor of safety of ~1.4-1.5 is probably enough.

## Ideas for improving track performance

[](#h.2pg07ojc2s94)

Max brought up the fact that trying to pass cars on the first day of the race can be very detrimental to our strategy and can make us lose a lot of time. Qualifying on pole and then staying ahead of the pack would be ideal. So is there a way that we can improve our car's track performance, without losing straight-line performance for the race?

Phil said that in general, a negative camber angle would improve our stability in corners. One way to achieve this would be to design an upright in two pieces, that could be bolted together in any of several positions to change the camber angle of the wheel without changing the rest of the suspension geometry. For the race, we could move the lower piece inward by a few teeth to add negative camber; then we could put it back where it was for the race. Of course, for our suspension geometry where the lower control arm is above the wheel hub, there isn't much space for a partition; to keep the upright stiff, we would have to use some huge bolts (M12s?)

(Image soon to come)

