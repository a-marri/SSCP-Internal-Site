# SSCP - Solar car suspension design guide with lessons learned [WIP]

# Solar car suspension design guide with lessons learned [WIP]

# Before you begin...

[](#h.cfpeh1ljg08)

Designing a suspension for a solar car is a fun and absorbing project. It is also one of the most important projects during each race cycle. Having control over the suspension design also means that you will affect, to a certain extent, the design of every single mechanical subsystem on the car (chassis, brakes, steering, roll cage, etc.).

However, it is also a challenging project. A poorly-designed suspension could cause you to waste precious hours on the side of the road, repairing or replacing components. An excessively compliant suspension, or one with too much bump scrub, will completely squander the precious watts that the electrical team spends so much time trying to save. And if you're careless with the design of your suspension geometry, your car will be dynamically unstable, with dire consequences.

Luckily, suspension design is not an obscure science. There are many proven designs to take inspiration from, and plenty of documentation to support them. This page will attempt to provide some tips and guidelines particular to suspension design for solar cars, but you'll learn a lot more (and have a higher chance of success) by finding these resources and using them. I'll try to point out a few that were especially useful to me over the course of the Arctan suspension design process. Furthermore, I'll include snippets of e-mail and g-chat conversations with alumni whose advice proved invaluable.

Another word of advice: START EARLY. "Early", in this case, means at least 2 months before the rules for the next race are released (which is usually in early June). Get together with the previous cycle's suspension designer, discuss what went well and what didn't, and what changes they would make to the suspension if they could. Read this page, and do as much research as you can on vehicle dynamics and suspension geometries. If possible, take ME227 (Chris Gerdes's vehicle dynamics class) to get a better understanding of weight transfer effects that are directly tied to suspension design. Since the suspension needs to fit inside the car's aerobody, you will be working closely with the aero team from the very beginning of the design cycle. If you've done your homework beforehand, you won't hold up the aero team when things start getting busy.

# Geometry

[](#h.c9u70362mvht)

The goal of a suspension is to give each wheel on the car exactly 1 degree of freedom. This degree of freedom is the up/down motion that you see when a car goes over a bump. The exact nature of this motion is controlled by the suspension geometry, and will have a noticeable impact on how the car "feels" to the driver (i.e. the vehicle dynamics).

The main element of the suspension geometry is the steering axis. The steering axis is an imaginary axis around which the wheel, along with all components rigidly connected to it (e.g. upright, spindle), pivots when steering. The steering axis is rigidly connected to the main rotational axis of the wheel (Fig. 1). Most suspension geometries are designed to specify the position and orientation of the steering axis at each point in the wheel's bump travel. The steering axis is usually defined by two ball joints, but this isn't always the case.

For a broad overview of suspension geometries used on road cars, you can read Carroll Smith's "Tune to Win" or Gillespie's "Fundamentals of Vehicle Dynamics". I'm going to focus on the geometries that are most relevant to solar cars.

## Suspension parameters

[](#h.bu63ibsdaee6)

To understand the advantages and disadvantages of a suspension geometry form factor, you'll first need to know how you want the wheel and steering axis to move. However, unless you're really good at visualizing things in 3D, you're going to have a hard time specifying the desired motion of the steering axis in 3D space. Fortunately, the motion can be broken down into several 2D parameters that can be defined at ride height (0 bump travel), and at both extremes of travel. Over the past couple of cycles, the team has arrived at a set of values for these parameters that seem to work well and achieve good compromises between vehicle dynamics and efficiency.

### Kingpin and caster angle

[](#h.31splpyszi6d)

The kingpin angle is the angle formed by the steering axis with a vertical line when viewed from the front of the car (Fig. __). The caster angle is the angle formed by the steering axis with a vertical line when viewed from the side of the car (Fig. __).

Kingpin angle is a necessary evil in a suspension geometry. While it allows you to keep a small scrub radius, it creates a "jacking force" by causing the tire to pivot around a non-vertical axis. The kingpin angle used on Luminos and Arctan was +7.5 degrees.

Caster angle also creates a jacking effect, by its very nature; however, it is much more of a necessity than kingpin angle. The caster angle is vital to the "self-centering" feel of the steering. Fig. __ attempts to show the effect known as mechanical trail. A positive caster angle places the intersection of the steering axis with the ground ahead of the tire contact patch. As a result, the lateral forces at the contact patch in a turn will create a moment around the steering axis, pushing the wheel back towards its centered orientation. Mechanical trail works alongside pneumatic trail (a side-effect of tire elasticity and the geometry of the contact patch) to provide steering feedback to the driver. A negative caster angle, meanwhile, has the opposite effect: in a turn, it will try to push the wheels towards full lock. The caster angle on Luminos and Arctan was +5 degrees.

Depending on suspension geometry, both kingpin and caster angle will change slightly with bump travel. When designing your suspension geometry, look at the extremes of bump travel and make sure that both kingpin and caster angle stay within acceptable limits. The last thing you want is for your caster angle to go negative while the car rolls in a turn, causing it to feel squirrelly all of a sudden.

### Bump scrub

[](#h.dxyvs75ifj8i)

Bump scrub is defined as the lateral movement of the tire contact patch over the range of bump travel. It can also be thought of as the change in effective track width of the car.

Bump scrub is 100% bad for solar cars. When the contact patch scrubs across the ground, it dissipates energy through friction (power loss = friction force * scrubbing velocity) and thus makes the car less efficient. The easiest way to remove or minimize bump scrub is to add camber gain, as explained below.

### Camber gain

[](#h.ch3mao7cbk9j)

For our purposes, we will define camber gain (Fig. __) as the change in camber angle of the wheel with respect to the chassis, over the range of upward travel from ride height (note that this does not include downward / droop travel). Camber gain is necessary in order to keep the wheel vertical (0 camber) with respect to the ground plane when the car rolls (Fig. __). Both Luminos and Arctan have approximately 0.6 degrees of camber gain.

In a solar car, camber gain also becomes a necessity if you choose a suspension geometry with some bump scrub. You will need to play around with the camber gain until the lateral movement of the tire contact patch cancels out the lateral movement of the wheel hub as closely as possible (Fig. __).

### Scrub radius

[](#h.pr5i92rbil9y)

The scrub radius (Fig. __) is the lateral distance between the point where the steering axis intersects the ground and the center of the tire contact patch. You can think of it as the lateral counterpart to mechanical trail. Luminos and Arctan had a scrub radius of 7 mm.

Like mechanical trail, scrub radius results in a moment arm around the steering axis. This time, the forces in play are longitudinal (e.g. braking, acceleration). As shown in Fig. __, when the scrub radius is positive, a braking force applied at the center of the tire contact patch will try to steer the wheel outward. Because of this effect, a large scrub radius is undesirable. Ways to reduce scrub radius include adding a positive kingpin angle, which will move the steering axis's intersection point with the ground further outboard.

However, a positive scrub radius is also necessary in certain situations. Consider the case where you are driving over a section of tarmac or concrete that is partially covered in sand. If your left front wheel loses grip on the sand, but the right front doesn't, then the tire with more grip is capable of reacting larger forces at the contact patch. Now let's assume the driver feels the loss of grip, and instinctively hits the brakes. Both tires will be subjected to longitudinal forces, but the right-front tire will feel higher forces than the left-front, since it has more grip. As a result, a moment will be created around the steering axis which will cause the right-front wheel to turn outwards, thus steering the car to the right -- away from the sand-covered area of the road!

Formula 1 cars suffer from enormous scrub radius, due to their wide tires. For an extreme case of the situation described above, read this article.

[ this](http://www.formula1.com/content/fom-website/en/latest/headlines/2015/2/mclaren--wind-to-blame-for-alonso-accident.html)

"(Alonso's) car ran wide at the entry to Turn 3 - which is a fast uphill right-hander - allowing it to run onto the Astroturf that lines the outside of the track," read McLaren’s statement. "A consequent loss of traction caused a degree of instability, spitting it back towards the inside of the circuit, where it regained traction and struck the wall side-on.

### Wait, what about roll centers?

[](#h.jeu0kp9a38il)

If you read either Gillespie's "Fundamentals of Vehicle Dynamics" or Carroll Smith's "Tune to Win", you'll notice that they describe suspension geometries almost exclusively in terms of tweaking the location of the roll center. This is indeed an important consideration in cars that go around corners at high speeds, experiencing very high lateral forces that could create pronounced jacking effects. These cars also usually have low CGs, so designers can get something out of playing with roll center location.

Unless you decide to go with a very unconventional solar car design, your car will have a high CG. Trying to make small changes to the geometry to get the roll center exactly where you want it will be a time-consuming and ultimately fruitless process. The easiest way to deal with this is to place the roll center on the ground; for Luminos and Arctan, we simply made the wishbones parallel at ride height. This way, you will eliminate jacking forces. You will still see a lot of lateral weight transfer in corners, and depending on your choice of springs, your car may still roll like a ship in a storm. But one of your jobs as a race crew will be to make sure that your car is never being driven "at the limit"; take corners at sane speeds, and you'll be just fine.

## Steering

[](#h.zcxro8xte6qr)

For the past few race cycles, the WSC's turning radius requirement has remained relatively unchanged. In the 2015 rules, it is phrased as follows:

"2.10.2 The Solar EV must be able to make a U-turn in either direction within a 16 m lane, kerb to kerb."

Note that this does not imply a turning radius of 8 m. It means the entire envelope of the car must not go outside a 16 m-wide lane when the car makes a U-turn at full lock. In front-wheel-steering cars, the turning radius is measured from the center of the rear axle (see diagrams below). Therefore, besides accounting for the extra width of the car, you'll also need to be aware that the front wheels will travel along a larger radius than the rear wheels.

Another thing you should keep in mind is that your car will never describe the turning radius that you design it for, due to slip angle effects. When making a U-turn at speed, your front wheels will have some non-zero slip angle. Unless you are able to measure the cornering stiffness of your tires, you will find it impossible to accurately model this phenomenon. One solution to this problem is to pad the turning radius of the outer-front wheel by a certain factor of safety For Arctan, I chose the outer front wheel's turning radius to be 7.6 m (5% less than half the kerb-to-kerb distance).

### Ackermann geometry

[](#h.w6r9bbqgql1q)

"Ackermann geometry" (Fig. __) is an over-arching term for a collection of steering geometries that will make the inner wheel describe a circle with a smaller radius than the one described by the outer wheel.

A car's steering geometry is usually described in terms of an Ackermann number or percentage. In a 100% Ackermann geometry (Fig. __), the circles described by all 4 wheels will be concentric (assuming no slip or other dynamic effects). In 0% Ackermann, also known as parallel steering, the two steerable wheels rotate through the same angle. Very few road-going cars have 100% Ackermann geometry, because suspension designers do try to account for slip. Both Luminos and Arctan were designed for 100% Ackermann, since we didn't have the ability to model slip.

### Finding required steering angles

[](#h.ijvp9mynt8yd)

Once you know your car's wheelbase and track width, you can calculate the required steering angle for each front wheel. An easy way to do this is to use the SolidWorks sketch shown in Fig. __ (you can find the SolidWorks file on PDM). Plug in the values, and read the angles off the sketch.

Chances are that you will need to find the required steering angles before the aerodynamic design of the car is finalized. The aero team will need these angles to figure out how wide to make the wheel fairings. This leads to an unavoidable problem: you will have no idea how far the aerobody extends ahead of the front wheels until your suspension geometry and aero design have been mostly locked in. Remember that the farther ahead it extends, the larger its turning envelope will be. As soon as the aero team starts to close in on a final design, use the steering-angle sketch to locate the outer front corner of the aerobody and figure out whether you'll still comply with the WSC regulations, as shown in Fig. __.

### Four-wheel steering?

[](#h.d13vu6tmjd00)

The pie-in-the-sky for all solar car teams. Meeting the turning-radius requirement with only front-wheel steering is directly at odds with your goal of making your car as slim as possible while managing to fit a suspension inside it. But steering all 4 wheels would make the turning radius not only accessible, but relatively easy to achieve.

Four-wheel steering (Fig. __) requires you to measure the turning radius from a point along the centerline of the car, between the front and rear axles. Its distance from the front axle depends on the angle through which you can steer the rear tires. If you have enough space for the rear tires to match the steering angle of the front tires, the point will be exactly halfway between the two axles (Fig. __). However, this will rarely be the case.

Designing a four-wheel steering geometry is simple, but implementing four-wheel steering is not. To make this system work, your car will need either:

* a second steering rack in the rear, orindividual steering actuators on each wheel
* a second steering rack in the rear, or
* individual steering actuators on each wheel

1. a second steering rack in the rear, or
2. individual steering actuators on each wheel

a second steering rack in the rear, or

individual steering actuators on each wheel

Either way, you will need to implement a steer-by-wire system to actuate the rear steering mechanism. Not only will you have added more hardware (i.e. weight) to the car, but you will have also increased its complexity, and hence the likelihood for something to fail at an inopportune moment.

### Bump steer

[](#h.gpsmaw4ytma1)

Bump steer (or roll steer) occurs when, due to geometry constraints, jounce or rebound travel causes the wheel to assume a certain steer angle, even if the steering rack is not actuated. When the tie-rod length or position is such that it is unable to accommodate the upward or downward travel of the unsprung mass, it will "push" or "pull" on the joint connecting it to the upright, causing the wheel to steer.

The most noticeable effect of bump/roll steer is "roll oversteer" or "roll understeer". When the car rolls while turning, the suspension on the inner side will rebound, while the outer suspension will jounce. If the steering geometry is symmetric with respect to the vehicle's centerline, jounce and rebound will have opposite bump-steer effects, meaning that the steer angles of both wheels will be either reduced (understeer) or increased (oversteer).

Fig. __ shows a front view of a double-wishbone suspension with non-parallel control arms. Let A and B be the upper and lower hardpoints. The instantaneous center of the linkage, C, is the intersection of the lines projected from the upper and lower control arms. Let D be a point on the upright, where we decide we want to attach the tie-rod. Where should the tie-rod's inner mounting point go? One commonly-used guideline for determining its position is the intersection of the lines AB and CD. This point on the chassis allows the projection of the tie-rod to be coincident with C for small jounce and rebound angles, while allowing D to follow the trajectories of A and B, orthogonal to the linkages at any point of travel. Note that this guideline is only presented for illustration purposes, and doesn't work for larger jounce and rebound angles. However, placing the tie-rod inboard mounts on the line joining the upper and lower hardpoints is a widely-accepted design practice, and most steering rack manufacturers (e.g. Woodward) assume that you are following this guideline.

Bump steer can only be fully eliminated through careful suspension geometry design, as described in a later section.

## Shock absorber geometry

[](#h.9t5qsiq5wns7)

When designing your suspension geometry, you should know the exact make and model of shock absorber that you will be using. Its stroke should be long enough to cover most, if not all, of the range of jounce/rebound travel. Furthermore, the shock absorber should be mounted as vertically as possible with respect to the chassis, so that you get the most out of the spring and damper forces. If the shock is mounted at a drastic angle from vertical, it may introduce too much lateral stiffness into the geometry, and make steering the car difficult (see next section). For Arctan, I defined a shock angle of __ from vertical at maximum jounce (Fig. __).

One important function of the shock absorber is to act as a bump stop, and prevent your upper ball joint from crashing through your car's topshell and prematurely ending your race. For this reason, you should define the shock mounting locations such that its fully compressed length corresponds to full jounce travel.

Always make sure the shocks you plan to use are actually available before you start designing. In fact, you may even wish to buy them in advance. Here's why: Luminos used Kaz/Penske 7800-series Double Adjustable shocks with a 75mm stroke, which allow the user to adjust the amount of damping force over a range of velocities. We initially planned on using the same shocks on Arctan, and the suspension geometry and shock mounting were designed around this model. However, we later received word from Kaz that they had discontinued the 75mm stroke version of the double-adjustable shock. Since the other double-adjustable option's 50mm stroke was too short for our purposes, Kaz suggested we switch to their Quarter-Midget shocks. These had a similar stroke (70mm), but very different compressed and extended lengths which caused significant changes in the position of the lower mounting point for the shock. Since they came with similar damping settings and spring options, the change didn't affect us too much, but we were caught off-guard at a late stage in the design cycle -- never a good thing.

## Lateral Stiffness

[](#h.hmz7bcsokvhv)

One of your main goals as a suspension designer is to ensure that the car delivers the right amount of mechanical feedback to the driver, through the steering column, when maneuvering. If the car feels too "light" or easy to turn, the driver is more likely to lose control. Williams suspension engineer Phil Ingram gave us an excellent term for the car's ability to transmit steering feedback to the driver: Lateral stiffness.

By now, you hopefully understand that the "self-centering" effect that you feel when turning a steering wheel is due to various moments around the steering axis. These include mechanical and pneumatic trail, jacking forces, and the force exerted by the shock absorber (provided it is mounted a certain orthogonal distance away from the steering axis). You'll have to achieve the right balance to give the driver just the right amount of feedback. If the forces or moment arms are too big, the steering will feel "heavy" and the car will be very difficult to turn. If they are too small, the steering will feel "light" and the driver will need to put more effort into keeping the car going in a straight line. Either extreme is bad. The suspension parameters described above have worked well in the past to introduce the right amount of mechanical/pneumatic trail.

## Geometry types and variants

[](#h.57hmp0xccu3w)

Most solar cars use either a leading/trailing arm or a double-wishbone geometry. These can have several variants, but they generally operate on the same principle.

### Leading/trailing arm

[](#h.3pl7i92xjjfm)

The basic trailing-arm geometry (Fig. __) is probably one of the simplest you'll come across, and is usually used on the rear wheels, since they don't need to be steered. It consists of a single rigid link that constrains the wheel in 5 degrees of freedom. If the trailing-arm geometry is flipped around, it becomes a "leading-arm". Trailing-arms are generally found on motorcycles and small off-road vehicles such as dune buggies or ATVs. Twente's 2013 WSC entry had a trailing-arm rear suspension (Fig. __). You'll be hard-pressed to find a leading-arm geometry on any production vehicle, and for good reason. However, Nuna7 (Nuon's 2013 WSC entry) had a leading-arm front suspension (Fig. __), as did several cars in WSC 2015 (e.g. Michigan, Tokai, Megalux).

Leading and trailing arms have two major advantages, both important for solar cars. The first is zero bump scrub. Since leading and trailing arms constrain the wheel's midplane to a single plane, there is effectively no change in track width over the entire range of the wheel's bump travel.

However, in order to eliminate bump scrub we sacrifice another important aspect of the wheel's motion: camber gain. In a pure leading or trailing arm suspension, you will notice that as the car rolls when turning, the wheels camber in the opposite direction to the turn, thus reducing the car's overall cornering capability. Some camber gain can be added to the geometry through smart design (for example, see Fig. __); however, this naturally adds some bump scrub as well.

The other advantage of leading and trailing arms is that they have a very small lateral footprint. If you look at the suspension from the front of the car, most of it will be in the same plane as the wheel. For a solar car, this means the geometry can be more easily packaged in a narrow fairing, resulting in significant aerodynamic gains from a thin main foil.

However, this advantage also comes with a caveat. As you can see from the picture of Nuna7's front suspension, a leading-arm geometry becomes considerably more complex once you add steering into the mix. The control arms need to be designed to give both wheels enough space to sweep through the required steer angle. More often than not, this will require you to design a very wide control arm and thus negate the benefits of a narrow suspension.

### Double wishbone

[](#h.iqhaorc6j6qt)

The double wishbone geometry is one of the most popular suspension geometries in road-going cars; you will often find it on the rear wheels of the average family sedan. Open-wheel racers, such as Formula 1 cars, use this geometry on all four wheels. It consists of two rigid links, often referred to as "A-arms" or "wishbones". Each A-arm removes 2 degrees of freedom from the motion of the steering axis. The 5th degree of freedom is removed using an additional toe-link or tie-rod, which sets the steer angle of the wheel.

Double wishbones inherently have bump scrub, since both the upper and lower ball joints that define the steering axis describe an arc when their motion is viewed from the front of the car. However, it is possible to fix this with camber gain. When the wheel moves up or down, the suspension geometry will cause the wheel hub to move inboard or outboard from the car's centerline. But if you can dial in just enough camber gain to keep the contact patch stationary, you will have little to no bump scrub.

The biggest disadvantage of the double-wishbone geometry in a solar car is its lateral footprint. The two wishbones must necessarily extend into the main foil of the aerobody. Consequently, the main foil will have to be thicker to accommodate them. Having very short wishbones, or wishbones that are spaced very closely together, is a bad idea. Suspension members (i.e. control arms) must react all the non-vertical forces and moments exerted on the steering axis by the road. When modeling the suspension in a static loading condition, you will find that putting any two ball joints within 4-5 inches of one another -- whether they're on the same short control arm, or on two different closely-spaced control arms -- will substantially increase the forces going through them, in order to react the moments created at the tire contact patch. This will make mechanical design and FEA difficult later on. Although the initial aero iterations of Arctan had a very thin main foil, we were forced to thicken it in order to give the A-arms more vertical room.

Luminos / Arctan multi-link suspension

Luminos and Arctan both used a variation on the double-wishbone suspension, where the lower A-arm was split into two separate control arms. This geometry was dubbed a "multi-link" suspension, although it's actually not as complex or innovative as other multi-link suspensions (e.g. the Tesla Model S rear suspension, or the Koenigsegg One:1 rear suspension). It is identical to the Model S front suspension.

[ Tesla Model S rear suspension](http://www.edmunds.com/car-reviews/track-tests/2012-tesla-model-s-signature-performance-suspension-walkaround.html)

[ Koenigsegg One:1 rear suspension](https://www.youtube.com/watch?v=bbgjRBT4ltM)

The custom motor which was first used in the 2013 cycle was the main motivator for this design decision. The motor housing is attached to the upright with a pre-defined bolt pattern, which you must design into the upright as well (more on this later). As a result, you won't be given much freedom in how you position the motor inside the wheel-well. Furthermore, the tire midplane (or the center of the contact patch, if you will) is exactly 100.8811 mm (almost 4 inches) away from the motor-upright mounting face (see Fig. __). This creates a significant challenge when trying to reduce the scrub radius, and tends to increase the envelope through which the wheel sweeps when steering.

By splitting the lower A-arm into two separate links, you have created a 4-bar linkage in place of a rigid A-arm, where the upright is the coupler link. As shown in Fig. __, the instantaneous center (IC) of this new 4-bar linkage becomes a "virtual" lower ball-joint, and the steering axis is now defined by this instantaneous center and the upper ball-joint. By changing the position and orientation of the two lower arms, you can control the location of the IC, and thus the position and orientation of the steering axis. You can now specify a suitably small scrub radius. Furthermore, you will have reduced the steering envelope of the upright/motor/wheel assembly.

## Developing a 3D model

[](#h.hc7gykxx88fc)

Once you've decided on a suspension geometry and values for each parameter, you will need to create a 3D geometry model in CAD. SolidWorks's 3D sketch feature, while difficult to get used to, is perfect for this purpose. 2D diagrams of projected views of the geometry can also be useful, to a certain extent. However, they cannot accurately model combined bump/steer positions, which are vital for verifying that the full sweep of suspension travel positions fits inside the wheel well. Therefore, the best way to define parameters like kingpin and caster angle, which are defined in terms of a 2D projection, is to create the projection yourself inside the 3D sketch.

### Chassis and hardpoint positions

[](#h.gqo95qo5sscg)

### Upright

[](#h.5zdrhsuqt8yv)

### Control arms

[](#h.zhazkzsyg02l)

### Neutral, jounce and rebound positions

[](#h.awnyxu7b0wme)

### Creating 2D projections inside a 3D sketch

[](#h.fbgitfhl88vw)

### Steering geometry

[](#h.6jypxov5qdtd)

## Simulation and loading conditions

[](#h.fvwhyilpt8up)

Once you have a fully defined geometry, you will need to determine the worst-case loads that each component of the suspension could experience in a racing situation. A widely-used standard for determining worst-case loads is the 4g-2g-1g loading condition. This scenario (Fig. __) puts three loads at the tire contact patch: 4g in bump (vertical), 2g in braking (longitudinal), and 1g in cornering (lateral), where "g" is equal to 0.7 times the weight of the car. While unlikely, this particular combination of loads could actually happen if, for example, the car runs wide in a turn and slams its outer front wheel into a kerb.

Once these loads are applied at the tire contact patch, you are left with a 3D statics problem. With the suspension in its full bump position, solve for the forces acting at each bolted connection by balancing forces and moments. We use the full bump position because theoretically, the worst-case loads will occur when the shock absorber is fully compressed, thus turning it into a rigid link. Any position below full bump wouldn't make sense for a static loading scenario, since the suspension would still be able to travel upwards under a 4g bump load.

The MATLAB script attached to this page is one I wrote to solve the static loading condition for the Arctan/Luminos multi-link geometry. I modeled the lower control arms and tie-rod as 2-force members, and the upper control arm as a truss (each "leg" of the upper control arm is a 2-force member, and the loads at the upper ball joint are the resultant of the loads in the two legs). The script first calculates the full-bump position of the suspension geometry using rotation matrices, and stores the position of each point in 3D space. It then solves 6 equations for 6 unknowns; the equations balance forces and moments on the upright. Moments are taken around the upper ball joint for simplicity, although they could also be taken around the tire contact patch or either of the lower ball joints. The results of this script are identical to those calculated using SHARK, a commercial suspension modeling program from Lotus.

A note on worst-case loads:

While the 4g-2g-1g combined loading case is one that is commonly used in the automotive industry, it will not necessarily give you worst-case loads for all suspension members. Depending on the suspension geometry, a pure 4g bump or 2g braking force may sometimes result in a higher load on a particular joint than the one calculated using the combined scenario. For example, [Fill in example case]. Therefore, you should always run several different combinations of loading conditions and account for the true worst-case loads in the mechanical design of the components.

## Interfacing with Aero

[](#h.y0yq5xd9sbqs)

# Mechanical design

[](#h.90skgys30geu)

## FEA essentials

[](#h.h8ni5cmums9g)

## Upright

[](#h.ay36iwa6kwbz)

## Control arms

[](#h.omc028ysg1hq)

## Choosing shocks

[](#h.lxbbp0n8m10v)

## All about fasteners

[](#h.oshj0d2as3k2)

The basics of Mechanics of Materials (ME80) apply to fasteners as well as any other material you use. Although we normally assume that nuts and bolts are orders of magnitude stronger than the materials they hold together, it is very common in automotive and aerospace applications for fasteners to be subjected to high loads, resulting in stripped threads, sheared bolts or worse.

The best resource I found for fastener design during the Arctan cycle was the NASA Fastener Application Guide (attached to this page), which Michael Hall-Snyder was kind enough to forward to us. Read it from beginning to end, and you should have all the information you need to figure out fastener types and torque specs for every bolt in the suspension. Since most of the basic information you need is presented in the NASA guide in a very readable format, I'll just leave some details here on how fastener design worked out on Luminos and Arctan.

* As a rule, we used Grade 8.8 steel bolts for all suspension-related applications, and calculated bolt torques accordingly. However, Luminos and Arctan used Grade 12.9 steel bolts to attach the motor to the upright. There is nothing intrinsically wrong with using Grade 12.9 -- it is stronger, after all; however, one must be aware that the stronger a material, the more brittle it becomes. Grade 12.9 steel is especially vulnerable to hydrogen embrittlement. Therefore, if you decide to continue the trend and use Grade 12.9 bolts to mount your motors and hubs to the upright, make sure they are zinc-plated. Zinc-plate (or zinc-flake) coating is an automotive-grade coating that is supposed to prevent hydrogen "bubbles" from getting trapped inside the steel. There's also nothing wrong with using Grade 8.8 bolts, as long as you arrive at the correct torque spec for them.When designing the upright, be sure to give some thought to the design of the upper ball joint. Luminos and Arctan suspension designers both took a significant risk by loading the upper ball joint bolt in single shear; however, it was a calculated risk and we chose a fat enough bolt (3/8"-24) to withstand the expected loads. Do the necessary analysis on your suspension geometry to determine whether this design is still viable. If it isn't, you should consider switching to a bolt in double shear (the standard on production vehicles). It'll make your upright more likely to smack into your topshell, but that can be avoided with more smart aero design.In case it isn't obvious: ALWAYS use the minor diameter of the bolt as a conservative approximation of the bolt diameter when calculating tensile or shear factors of safety.A nut factor of 0.2 works just fine for this application. Most online torque calculators (e.g. Futek) also use 0.2 by default unless the user inputs a different nut factor.When calculating torque specifications for the ball joints, which were loaded in both tension and shear, I used the most conservative interaction curve to calculate the allowable tensile FOS of the bolt. Read the NASA fastener guide for more details.Apply non-permanent threadlocker (blue Loctite) to all bolts going into aluminum threads or non-locking helicoils. Apply anti-seize to all bolts going into locking helicoils (read: Click-Bond inserts and hardpoints), so that they don't gall together when torqued. Do not apply any chemical to bolts that go into lock nuts.
* As a rule, we used Grade 8.8 steel bolts for all suspension-related applications, and calculated bolt torques accordingly. However, Luminos and Arctan used Grade 12.9 steel bolts to attach the motor to the upright. There is nothing intrinsically wrong with using Grade 12.9 -- it is stronger, after all; however, one must be aware that the stronger a material, the more brittle it becomes. Grade 12.9 steel is especially vulnerable to hydrogen embrittlement. Therefore, if you decide to continue the trend and use Grade 12.9 bolts to mount your motors and hubs to the upright, make sure they are zinc-plated. Zinc-plate (or zinc-flake) coating is an automotive-grade coating that is supposed to prevent hydrogen "bubbles" from getting trapped inside the steel. There's also nothing wrong with using Grade 8.8 bolts, as long as you arrive at the correct torque spec for them.
* When designing the upright, be sure to give some thought to the design of the upper ball joint. Luminos and Arctan suspension designers both took a significant risk by loading the upper ball joint bolt in single shear; however, it was a calculated risk and we chose a fat enough bolt (3/8"-24) to withstand the expected loads. Do the necessary analysis on your suspension geometry to determine whether this design is still viable. If it isn't, you should consider switching to a bolt in double shear (the standard on production vehicles). It'll make your upright more likely to smack into your topshell, but that can be avoided with more smart aero design.
* In case it isn't obvious: ALWAYS use the minor diameter of the bolt as a conservative approximation of the bolt diameter when calculating tensile or shear factors of safety.
* A nut factor of 0.2 works just fine for this application. Most online torque calculators (e.g. Futek) also use 0.2 by default unless the user inputs a different nut factor.
* When calculating torque specifications for the ball joints, which were loaded in both tension and shear, I used the most conservative interaction curve to calculate the allowable tensile FOS of the bolt. Read the NASA fastener guide for more details.
* Apply non-permanent threadlocker (blue Loctite) to all bolts going into aluminum threads or non-locking helicoils. Apply anti-seize to all bolts going into locking helicoils (read: Click-Bond inserts and hardpoints), so that they don't gall together when torqued. Do not apply any chemical to bolts that go into lock nuts.

* As a rule, we used Grade 8.8 steel bolts for all suspension-related applications, and calculated bolt torques accordingly. However, Luminos and Arctan used Grade 12.9 steel bolts to attach the motor to the upright. There is nothing intrinsically wrong with using Grade 12.9 -- it is stronger, after all; however, one must be aware that the stronger a material, the more brittle it becomes. Grade 12.9 steel is especially vulnerable to hydrogen embrittlement. Therefore, if you decide to continue the trend and use Grade 12.9 bolts to mount your motors and hubs to the upright, make sure they are zinc-plated. Zinc-plate (or zinc-flake) coating is an automotive-grade coating that is supposed to prevent hydrogen "bubbles" from getting trapped inside the steel. There's also nothing wrong with using Grade 8.8 bolts, as long as you arrive at the correct torque spec for them.
* When designing the upright, be sure to give some thought to the design of the upper ball joint. Luminos and Arctan suspension designers both took a significant risk by loading the upper ball joint bolt in single shear; however, it was a calculated risk and we chose a fat enough bolt (3/8"-24) to withstand the expected loads. Do the necessary analysis on your suspension geometry to determine whether this design is still viable. If it isn't, you should consider switching to a bolt in double shear (the standard on production vehicles). It'll make your upright more likely to smack into your topshell, but that can be avoided with more smart aero design.
* In case it isn't obvious: ALWAYS use the minor diameter of the bolt as a conservative approximation of the bolt diameter when calculating tensile or shear factors of safety.
* A nut factor of 0.2 works just fine for this application. Most online torque calculators (e.g. Futek) also use 0.2 by default unless the user inputs a different nut factor.
* When calculating torque specifications for the ball joints, which were loaded in both tension and shear, I used the most conservative interaction curve to calculate the allowable tensile FOS of the bolt. Read the NASA fastener guide for more details.
* Apply non-permanent threadlocker (blue Loctite) to all bolts going into aluminum threads or non-locking helicoils. Apply anti-seize to all bolts going into locking helicoils (read: Click-Bond inserts and hardpoints), so that they don't gall together when torqued. Do not apply any chemical to bolts that go into lock nuts.

As a rule, we used Grade 8.8 steel bolts for all suspension-related applications, and calculated bolt torques accordingly. However, Luminos and Arctan used Grade 12.9 steel bolts to attach the motor to the upright. There is nothing intrinsically wrong with using Grade 12.9 -- it is stronger, after all; however, one must be aware that the stronger a material, the more brittle it becomes. Grade 12.9 steel is especially vulnerable to hydrogen embrittlement. Therefore, if you decide to continue the trend and use Grade 12.9 bolts to mount your motors and hubs to the upright, make sure they are zinc-plated. Zinc-plate (or zinc-flake) coating is an automotive-grade coating that is supposed to prevent hydrogen "bubbles" from getting trapped inside the steel. There's also nothing wrong with using Grade 8.8 bolts, as long as you arrive at the correct torque spec for them.

When designing the upright, be sure to give some thought to the design of the upper ball joint. Luminos and Arctan suspension designers both took a significant risk by loading the upper ball joint bolt in single shear; however, it was a calculated risk and we chose a fat enough bolt (3/8"-24) to withstand the expected loads. Do the necessary analysis on your suspension geometry to determine whether this design is still viable. If it isn't, you should consider switching to a bolt in double shear (the standard on production vehicles). It'll make your upright more likely to smack into your topshell, but that can be avoided with more smart aero design.

In case it isn't obvious: ALWAYS use the minor diameter of the bolt as a conservative approximation of the bolt diameter when calculating tensile or shear factors of safety.

A nut factor of 0.2 works just fine for this application. Most online torque calculators (e.g. Futek) also use 0.2 by default unless the user inputs a different nut factor.

When calculating torque specifications for the ball joints, which were loaded in both tension and shear, I used the most conservative interaction curve to calculate the allowable tensile FOS of the bolt. Read the NASA fastener guide for more details.

Apply non-permanent threadlocker (blue Loctite) to all bolts going into aluminum threads or non-locking helicoils. Apply anti-seize to all bolts going into locking helicoils (read: Click-Bond inserts and hardpoints), so that they don't gall together when torqued. Do not apply any chemical to bolts that go into lock nuts.

# Choosing spring rates

[](#h.r6oa64lkw4z2)

# Preparing for Aerodyn

[](#h.mycb96dseyji)

## Peg legs and actuator locations

[](#h.garerybxulg1)

## Solid shocks vs. live suspension

[](#h.11rtvf9igvsp)

# Vehicle dynamics testing

[](#h.k5pn1m1o747)

