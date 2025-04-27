# motor-design-review-2012\_09\_30

## SSCP - Motor Design Review 2012\_09\_30

## Motor Design Review 2012\_09\_30

#### Attendees

Jon Wagner, Matt, Paul Butterfield

Nathan Hall-Snyder, Forest, Greg, Matt Lambert, Sasha, Sam, Paul Karplus, Andre Ponec, Wesley, Wyles, Zach

#### Action Items

Magnetics

a.       Check out metglas as a material

b.      Look at ceramic magnets to reduce eddy current losses from surface conduction

c.       Do eddy current simulations if possible

d.   Make sure that the manufacturing process doesn't damage the laminations in any way

e.   Simulate and look at buried magnets

d.   Use a series winding

Case

a.       Consider the symmetry of the left/right motors/calipers

b.      Include consideration for identifying motor numbers

c.       Model heat output and cooling. Determine the efficiency loss due to heating

d.      Add cooling fins

e.       Add lead-ins for all components

f.        Put in a feature for removal of the stator

Rotor

a.       Set up a key system to key the rotor to the stator

b.      Re-do the shaft interface – use a flat interface and a bearing nut

Commutation

a.       Fix the keying between the tamagawa rotor to the shaft

b.      Consider using plastic washers on the resolver

c.       Use large washers for more threads in the aluminum

Connectors

a.       Seriously consider connectors

b.      Re-do the electrical scheme – NO PCBS

c.       Increase the amount of space for wiring

d.      Test the termination method of the 22 gauge wire

e.       Think about the termination method for the data connector – solder cups? Pigtail? Connector? Etc            &#x20;

Stator

a.       Examine tolerance stackup on the stator – stacking laminations is not easy. Test, come up with a method. Laser has tolerance, laser beam has tolerance, etc. Consider epoxy, cutting the epoxy, epoxying it to a piece of aluminum, CNCing the aluminum, etc. Consider various options

b.      Possibly implement a go-no-go gauge for the laminations, or maybe pot in shims

Bearings

a.       Add grease control to the roller bearing

b.      Re-examine the bearing shock loads, possibly re-size the inner bearing. Look at bearing life

d.      Get the fits for the bearings from SKF

e.       Determine how to remove bearings (add holes, flanges, etc

Sealing

a.       Test the labyrinth seal

b.      Try to fit in an o-ring seal

#### Meeting Notes

•       The current options all have disadvantages. CSIRO is difficult to package, NGM has low efficiency, Mitsuba is expensive.&#x20;

◦       CSIRO: It is a package, so you have to design a shell yourself. Aurora carries eight backup motors. Our 2011 team had no backups. They are 13k or 25k.

•       Existing motors are designed to function as a single motor for the entire car so they have high torque specs.&#x20;

•       We could design with one motor but we would be concerned about cornering, unbalanced unsprung mass,&#x20;

•       Q: Matt L: who has done two wheel drive: A: Bochum

•       Q: Matt. How are you measuring efficiency.&#x20;

•       Our design spec: We want our motor to match CSIRO design specs for torque and speed.

•       Sasha:

◦       is doing analysis to find the topography of the WSC course and&#x20;

◦       First draft: 25N-M peak torque should work for us

◦       (insert histogram of Sasha's histogram of torque specs)

▪       For every 5k on the race course, Sasha calculates a required torque to maintain forward motion on a 260kg car.

▪       Graph goes above 25N-M, but Sasha says this is calculation error

•       Q Paul:&#x20;

•       Q John we also want to consider car speed in our analysis. So do a three degree histogram of Torque, speed, and frequency  (like Sam L. had from Minnesota).

•       Sam's Radial Flux motor from Minnesota:&#x20;

◦       had high torque and high power

◦       Uses the same nickel alloy that we plan to use.

◦       but it had problems:

▪       flux in the core was too high

▪       so it had high core losses

•       Design Goals

◦       98% at 1041 RPM

◦       25Nm per motor max load torque

◦       Small diameter iron core

◦       160mm diameter

•       Material Selection

◦       Stator/Rotor Iron

▪       Carpenter 49-49% nickel

▪       Q: John: 6x lower hysteresis losses

◦       Magnets

▪       Sm2Co17

▪       less expensive

▪       resistant to damage: low temp coefficient. high curie temp.

▪       more brittle to Neodymium

▪       $160 per Kg

▪       Q Paul: $250 per Kg for Neodymium

◦       Carpenter 49 requires special annealing cycle.&#x20;

▪       Pure hydrogen atmosphere at 2k Celsius

▪       Changes permeability by a factor of 10

▪       They did this at Minnesota

▪       You can't drop the stator. You can ruin the annealing with a large shock.

▪       John: you can also destroy the annealing with press fitting.&#x20;

▪       Q John: Did you look at other alloys e.g. Cobalt Iron: A: Sam: not extensively. We need low core loss at high load

▪       Q Paul: Have you tried. A; NHS no. A: Andre: we have some in the shop. Metglass: an amorphous metallic.

◦       We chose 24 pole 28 magnets

▪       with trapezoidal BEMF pattern

▪       Q: why don't you use ceramics for the dyno:&#x20;

▪       Sm2Co17 is better with heat

◦       Winding patterns:

▪       RMxprt and Mxwell for design and FEA

▪       MATLAB for final analysis

◦       Q: what is peak flux

▪       .8 or .9 tesla

◦       This is an inside rotor motor:&#x20;

▪       for packaging reasons.&#x20;

▪       outside rotor is challenging due to challenge of sealing the motor

◦       Q: highest rpm

▪       1100 RPM

◦       Second animation

▪       1.6 tesla (saturation)

◦       Air gap

▪       120mm diameter

◦       at saturation it is still able to produce torque, it is just less efficiency

▪       there are few hills

•       Efficiency map

◦       flat ground, aero load&#x20;

◦       the upward sloping lines are with upward sloping grades in the road

◦       assumed 25% mechanical load in addition to aero load

◦       Largest incline is +2.5%

•       Q: do we have adequate acceleration for acceleration

◦       no: we are doing straight lines for most of the day. Should only have two start-stops during the race.

◦       Also, on the track most teams use CSIRO motors, which rapidly derate during peak torque and high temp. We will have better cooling than the CSIRO.

•       Q: weight.&#x20;

◦       9kg

•       Q: does software consider eddy current loss.

◦       A: Sam. it can, but we are not including it due to computational requirements to run the simulation

◦       includes eddy current losses within the steel, but not in the bulk materials outside of the steel.

◦       Action Item: Do one simulation to see how eddy currents hurt us.&#x20;

◦       John: difficult to believe that&#x20;

•       Q: Laminations are well insulated to each other, but you may have shorting at the edge.

◦       A; sam: you cannot coat, but we will have rounded edges

▪       cannot coat before annealing due to high temp coating.

▪       Minnesota used a powder coated epoxy after the stack. Thinner than nomex.

•       Sam getting B-H curves

◦       John: we would want to run at 100 or 400 hz, not 60hz

◦       Results: off by a factor of 4.

◦       The C5 coating probably destroyed the magnetic characteristics

◦       Sam used results to adjust his FEA dyno in maxwel.&#x20;

•       NHS Solidworks:&#x20;

◦       Discussion on tires: we want to use Michelins. They are supposed to be available for fitment in December

◦       CRR of 1.5x steel wheel on a steel rail

◦       Rim: 18in. tire radius 22in

◦       For those doing math. the outder .558m

◦       stator slip fit, not press fit in

◦       brake rotor on each wheel.

▪       braking for emergency and race rule compliance

◦       a cover for dust.

◦       Motor would be a unit that we can dyno and send to Australia.

▪       no one on the team should have to open the motor box

▪       motor is tall to bolt to the suspension upright

▪       Q: how much current through phase lines. 4-5amps nominal  35amps max.&#x20;

▪       Q: Don't forget about contact resistance. consider ring terminal blocks might be better.

▪       Q: is motor controller external. yes.&#x20;

▪       Q: symmertry: the left side will be a mirror image. brake rotors are directional.

▪       Q: will we need external inductors: Sam: no.&#x20;

▪       CSIRO requires three external inductors

▪       Q: How far away will motor controller be.

▪       it should be close. <5ft.

▪       Q: can motor controller go in the upright.&#x20;

▪       a lot of vibration and limited space.&#x20;

▪       no

◦       Components:&#x20;

▪       wheel nut. conical press fit on the wheel nut. The ducati race nut.

▪       brake rotor: hayes brake rotor

▪       6 shear pins transfer torque. high grade steel 2.5 FOS. press fit.

▪       front face plate

▪       bearing

▪       clip to hold bearing

▪       carrier to hold rotor

▪       tamagawa resolver

▪       roller bearing

▪       cover, caliper, etc.&#x20;

•       Switching away form hall sensors. Only have 6 points of reference. our motor controller is not smart enough. Looking at BEMF works ok, but a resolver allows you to know exact position.&#x20;

◦       Tamagawa has 98% of resolver market

◦       allows us to start on hills

•       Q; Paul trapezoidal stator. We can use sine wave. windings pack even better. NHS built cad around the largest possible&#x20;

•       Q: John see plot of flux around air gap.

•       The resolver rotor comes with the rotor, so you don't have to recalibriate the motor.

•       Q: every motor will have a different alignment. We will have to recalibrate the motor controller. We can store 15 profiles in the motor controller. We have to.&#x20;

•       WE could key the rotor to the stator. DO it.&#x20;

•       tamagawa rotoro is keyed to the shaft.

◦       Q: John says use a small end milll key shape. What we have not is not machinable.&#x20;

◦       Q: why is the part lobed.&#x20;

◦       Q: Angular ?? Goal is within 1 thou. 1 degree electrical&#x20;

•       resolver is held in place with four bolts. Bolts will force the resolver against it's keyed position.

◦       It shouldn't matter if bolts scratch the resolver.&#x20;

◦       Use a plastic washer under the bolt. We don't really know if scratching will be a problem.&#x20;

◦       Paul did not use M3 button heads, because John hates them.&#x20;

◦       M3 torx will be OK

◦       Use a big washer

•       Connector

◦       Tyco connector for automotive use

▪       question about sourcing and electrical.&#x20;

▪       Q: Why not connect directly to wire terminals.&#x20;

▪       people will not use good connectors for high powered.&#x20;

▪       use our own connectors or use&#x20;

▪       We would have to make a lot of extra crimps.&#x20;

▪       If we don't need to have a connector, then don't use them.&#x20;

▪       Why do we have lugs.&#x20;

▪       so we can remove the stator without cutting wires

▪       Q: how to get from magnet wire to lugs.

▪       we currently use a PCB. the PCB stays with the stator. ring terminals stay with .

▪       John says no to a PCB.&#x20;

▪       Q: can we get more space for ourselves

▪       take magnet wire and use royal fusing or brazing. PCB and solder is a bad idea.&#x20;

▪       Don't use that many wires. strip with propane, sand, solder the lug if you are confident in crimp.&#x20;

▪       Minnnesota;&#x20;

▪       use Minnesota's design.

▪       the ring terminal will creep and shift over time.&#x20;

▪       2 strands of 22 gauge wire per phase.

▪       that seems way too small.&#x20;

▪       John would guess 8 strands of 28.&#x20;

▪       terminating two 22 gauge wires is difficult to crimp.&#x20;

▪       They make special magnet wire crimps that we could use.&#x20;

▪       Insulstrip: we could use it

▪       it is super nasty and smells bad

▪       you have to have the heat capacity to keep the molten slot liquid

▪       Do prototyping for crimping.&#x20;

▪       data out. 6 for resolver and 2 for termsitor

▪       solder cup.&#x20;

▪       we should add strain relief afterwards

▪       move the zip tie closer to the connector.

▪       make sure the wire length on the resolver will fit.&#x20;

▪       Could we use a PCB after the data connector?&#x20;

▪       we want the resolver to be removable

▪       matt says eliminate PCBs everywhere unless you are potting them.&#x20;

▪       Q; can you strain relief a phoenix connector.?

▪       no, you could pot the back of the connector

▪       Q; is there cooling.&#x20;

▪       no. only case cooling.&#x20;

▪       we will use thermal silicon grease to conduct heat

▪       There is minimal air flow, but the wheel is a fan.&#x20;

▪       Q: Do we have an idea of steady state temp

▪       no

▪       we are also taking hot air from the pavement road surface.

▪       CSIRO was at 65 c. steady state. and it was cold weather during the race

▪       Q: loss in efficiency due to temperature.&#x20;

▪       will be efficiency losses.

▪       Q: can we put fins on&#x20;

▪       no reason not to.&#x20;

▪       use circumferential fins.&#x20;

▪       difficult to machine.&#x20;

▪       we could use a key cutter.&#x20;

▪       or use a slitting saw.

▪       Have we considered buried magnets:

▪       no.&#x20;

▪       less losses on the rotor if we do

▪       losses reduced due to flat??

▪       There are huge mechanical advantages

▪       we could commit to a thinner air gap.

▪       surface magnets have to deal with a lot of centripetal force. 80g

▪       use a good glue.&#x20;

▪       using henkel glue.

▪       magnets would have a slip fit.&#x20;

▪       toyota motor uses it

▪       motor would be heavier. magnets will short, so you need&#x20;

▪       assembly is way easier.

▪       Sam planned to have features in the rotor to key the magnets.&#x20;

▪       will have little teeth

▪       we would need rounded outside of the magnets

▪       Insight hybrid uses this

◦       Assembly method:&#x20;

▪       laminations laser cut

▪       stator cut: powder coated and epoxy?

▪       rotor: epoxied laminations

▪       windings might change

▪       assembles in the z-direction.&#x20;

▪       John thinks that alignment will be difficult.

▪       we may want to fit this on the mill.&#x20;

▪       laser cut laminations have +/- 2 thou. ID jig must be at least .004 smaller.&#x20;

▪       we would be better off comolding an epoxy feature on the outside.&#x20;

▪       build up a bunch of power coat and turn it on a lathe.&#x20;

▪       the current design prevents this due to the keying feature.&#x20;

▪       The best way to do our current orientation si to build the stator, measure it and then build aluminum.&#x20;

▪       using a CMM could fool us.&#x20;

▪       We could order 3x the need that we need and then sort the laminations.

Jon: consider ring terminals or test main connector after cycles and test all of them.&#x20;

Jon: Considery adding a male key to the rotor to prevent recalibration of the motor controller for each swap

Jon: tomagawa feature is not machinable and sucks

Jon: Add plastic washer to clamp of resolver to prevent grinding the resolver

Jon: "Dude no M3 button heads" use button head torq

Jon: "Glands guys dont get too fancy here" "If you dont have to have one dont have it"

Jon: "PCB no no no no no"

Jon" "You would be way better off braising magnet wire to a lug" "PCB and solder in a motor.... dont do it"

Jon: "Two strands of 22 seems way too small" "People dont wind motor with 22awg wire"

Jon" "Terminating two 22awg wire is sucky"

Jon" Consider using inulstrip (super nasty) need lots of heat capacity for it use it

Jon: Prototype crimping methods.&#x20;

Jon: "add strain relief rfeaure close to M12 connector"

Sasha: "Put a pcb on the back of the M12 connector"

"Dont add pcbs or connectors in high vibe enviornments"

Make thermal model&#x20;

Jon: I would not see why you would not put curcumferntial slitting saw to do fins

Paul: "Have you considered burried magnet rotors "a lot fewer losses on the rotor"&#x20;

Jon: "Huge mechanical advantages to doing that"

Paul: "laser weld then anneal"

Jon: "laser 2thou on the line 4 thou on the diameter tolerence stackup is fucking you"

"Consider turning down on lather but done punch though power coating"

Jon: Get stators measured. "You will get fooled just telling you"

"Go no go gague on laminations"

Jon: "plan for clearence makes it harder to get concentric"

Jon: "very doable but pay attention to tolerence stackup"

"Add in shims on the sides"

Insert stator in lathe

Insert stator in Aluminum tube and machine that

inject heat sinking compound into the gap.&#x20;

Jon: "I am not sure you can field service this motor"

Jon: "use linear bearing which is much stiffer"

Jon: Two bushings and some threads which ride on the OD of the acme thread

Jon: "the grease coming out is a huge problem"&#x20;

Paul: The grese is just going to fly out"&#x20;

Paul B. "Capture the gree

"Combo shield that captures the bearing to hold the greese in&#x20;

Jon: "felt seal"

Jon" inside smaller bearing might see shock load"

Jon: "for lifetime use 1/10 of dynamic rating"

Jon: "Breaking rotor applies moment on bearing stack during breaking"

Jon: "rating of bearing changes based on the lubrication"

Jon: "bearings do see axial load"

jon: "Get SKF to tell you the fits"

Jon: "press fit expands inner race and presses on the balls"

Jon: "Drill holes to get bearing out"

PK: amount of material for big bearing not enough along with the circip

Jon: "This is not good. Taper has to be cut on a lathe"

Jon: "surface finish really important on a taper"

PK: "make make the bolt piece a seperate piece"

Mate it to the same shaft to taper 100 times to get good surface finish

Jon: "you might be better off using a flat face and bolts to transfer the torque"

Jon: "use a bearing nut"

Jon: "Use face friction instead bring the taper out to a flat"

Jon: "You are going to hate your life making that taper and you dont need it"

Jon: "you should assume you will have a different calibration for each motor"

Jon: Put holes to press stator out that you cover with screws

PK\&Jon: "Lead ins on everything expesially the big part"

Paul B: "Not going to be much of an issue for bearings curents. If you cna use ceramic bearings use them"

Sam L: "Consider keying feature so that brake rotor cannot be installed wrong"

Jon: consider o-ring

Paul B: "Consider only using series winding"

&#x20;
