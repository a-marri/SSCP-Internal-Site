# SSCP - Factors of Safety

# Factors of Safety

## Factor of Safety

[](#h.2a5ewax10c3f)

Factor of safety is the multiple beyond the minimum needed to fulfill the load, typically defined to be based on the yield strength.

Helpful guidelines on FOS can be found on EngineeringToolbox.com: https://www.engineeringtoolbox.com/factors-safety-fos-d_1624.html

[https://www.engineeringtoolbox.com/factors-safety-fos-d_1624.html](https://www.engineeringtoolbox.com/factors-safety-fos-d_1624.html)

## Historical Factors of Safety

[](#h.ohhjxwp0tjgi)

See mechanical reports for each car for more details

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

*Mamba's roll cage was designed to be 1, but once we updated the loading condition and the weight of the car used in the analysis, it turned out to be less than 1.

Comments from a long email thread:

So much history is embedded in the numbers that we have chosen for loading conditions and factor of safety - I'll do my best to offer a history combined with my understanding of the function of factor of safety.

Why Factor of Safety?

First, factor of safety is a controversial idea. Every industry specifies their own definition of factor of safety, and textbooks disagree about the way to calculate. In the case of solar cars, we typically talk about the yield factor of safety (since we would prefer that mechanical components, with the exception of the roll cage) do not yield (deform plastically) under normal operation). A roll cage factor of safety typically uses the ultimate strength with the full weight of the car (weight * gravity), since the roll cage only has to work once and must take the entire weight of the car.

The objective of the factor of safety is to allow for corrosion, material defects, assembly errors, wear, errors in analysis, and still allow the part to perform throughout its life. There are so many ways that the strength of a part can be reduced. Here are a few SSCP-specific examples where part strength would have been reduced by poor engineering:

- The surface finish for the highly-stressed fillet in the titanium Luminos motors is critical but uncontrolled. Processing of the titanium may have caused minor chlorine embrittlement (we don't know all of the materials used by Gonsels when he machined the spindles).

- The fatigue life of all pre-Luminos parts was reduced due to aluminum anodizing. We learned about this from the Sunswift team at WSC 2011.

- A difficult-to-drill hole reduced a critical wall thickness on the Xenith upright. A similar difficult-to-machine thin wall ate into the factor of safety on the first-rev Xenith motor.

- Powder coating reduced the strength of the Luminos wheels by a small amount (5-10%?) due to the change in temper.

- Machining of a number of suspension components to get rid of collisions, including a steering arm on Xenith, a brake mount on Apogee and a large hunk of an upright on Xenith in order to fit different tires :( . 

I define factor of safety as a fudge factor that is actually a measurement of an engineer's confidence in his or her understanding of the design, manufacturing, and use case for an engineering project.

If that statement concerns you, then I encourage you do do more research on the history of factor of safety. Even in some of the most carefully analyzed and maintained structures ever built (such as those used for human-rated spaceflight), the use of some design and test over-specification is universal.

What factor of safety has SSCP historically used?

When I started designing mechanical parts for Xenith, I sought to standardize the factor of safety so that more team members could work on parts in parallel. In order to choose a value, I looked over previous documentation for factors of safety used. I had heard that a factor of safety of 6 was used for the Equinox roll bar. A factor of safety of 3 was used for the Apogee roll bar. Parts of Apogee varied between 1.3 and 4. I consulted with Danny, who mentioned the factors that Lockheed used for satellite design (1.1 for non-human-rated spaceflight). Based on the spectrum of factors of safety, and our desire to reduce the weight of Xenith versus Apogee, I arbitrarily decided that FOS 2 would be an appropriate target for Xenith. That decision has been rewarded by a healthy history of no structural mechanical failures* since Xenith.

*with the exception of one bolt on the Xenith suspension, for which a shear analysis was incorrectly substituted for a bending analysis.

History of SSCP Loading Conditions

Equinox Loading Conditions:

Equinox's rollcage was designed with a FOS >1, from a combined 3G load at 30, 60, and 90 degrees on the rollcage, which can be considered as an effective FOS of 6 or 9, depending on how you look at it, but I didn't actually check for FOS for a 1G loading case, so it's hard to tell). This was decided out of an abundance of caution, and the applicable experience from previous teams designing space frame chassis. The suspension was designed with similar constraints as Apogee, except with higher margins: 3G bump, 2g brake, 1g corner (John Shen has the mechanical report, email him if you want it, can't figure out how to upload on here). This was done based on advice from previous teams and erred on the side of being conservative and safe, as this was Stanford's first monocoque car, and the weight penalty was fairly low on the team's priorities at the time (racing with a 8m2 GaAs array). The interesting thing about Equinox is that the roll cage was validated in a 80kph rollover accident.

Apogee's Loading Conditions

Apogee (see mechanical report) loading conditions used were based on American Solar Challenge Regulations at the time, which required a minimum of (1g brake, 2g bump, 1 g corner. Teams entering ASC are still required to demonstrate that they have done analysis to meet these specifications. The mechanical report is supposed to include analysis as to the calculation for "g". Apogee used (car weight)/3, under the assumption that weight was evenly divided between wheels. The team at the time, given the "minimum" specification as well as the known more rough road in Australia (cattle grates), increased the bump load to 3g. The brake load was also increased from 1g to 2g for an important reason: the rod end used in bending on the top a-arm of Equinox repeatedly popped out and snapped due to braking and motor torques. The team must have decided that the 1g load was not appropriate because failures were seen in testing.

I would ask Adem for the history of the 1g brake, 2g bump, 1g corner. I suspect it comes from the excellent analysis done by GM employees for Sunraycer. Either Adem or Sam L has a printed copy of the technical manual.

It's important to note that Apogee had one structural failure on the race - one of the hardpoints fatigued on a line created by a machining error. This set a number of us on edge (we had no idea what fatigue was).

Xenith Loading Conditions

Xenith was designed similarly, with the 3-2-1 loading condition and "g" = weight*g/3. When we set out building Xenith, I asked Fred Ford (a friend of Danny's who did structural analysis at Lockheed) to help out with the suspension analysis. Looking back through the matlab code (originally written by Ryan McCullough of Equinox/Apogee), he adapted defined g = ((220kg + 80kg) * 9.81)/3 = 980N. The heavy weight was the result of expecting a much thicker and heavier array cover glass. The suspension was designed to that specification with a minimum FOS of 2. The analysis for all components (with the exception of the roll cage) was done in Solidworks. The exception to the rule was the rear motor, where a 4*"g" bump load was used. This number came from the CSIRO motor thesis of Rabih Al Zaher of the 2009 Nuon team, which indicated that the motor should be simulated to 4G.

[ CSIRO motor thesis of Rabih Al Zaher of the 2009 Nuon team](http://repository.tudelft.nl/assets/uuid:029674d0-3844-4b92-be6d-90bdcc4b9dad/Thesis_Rabih_Al_Zaher.pdf)

Luminos Loading Conditions

The loading conditions for Luminos were complicated by the arrival of Sam L, who shared what UMNSVP had historically used. As the car was four wheels, we were originally planning on using a 4g-2g-1g loading scenario where g = weight*gravity/4, but discussions between Greg, me and Sam L found some issues with this plan:

- Weight distribution: Luminos was intended to be front heavy (a maximum of 60% front, 40% rear, similar to a Toyota Camry or VW Passat). Therefore, simply assuming that the car's weight was evenly divided seemed dubious. Therefore, we needed the worst case to be the weight on the front wheels divided in two. However...

- Weight transfer under braking:  In the worst case braking scenario (practically -9.81m/s^2), a significant amount of weight is transferred to the front wheels. From Carrol Smith's Tune to Win, page 32, the weight transfer in any axis is given as (weight transfer) = (acceleration * weight * cg height) / (wheelbase). 

[ Carrol Smith's Tune to Win](http://users.telenet.be/AudiR8/Carroll%20Smith%20-%20Tune%20to%20win%20OCR.pdf)

- Weight transfer under cornering: We assumed that the weight transfer during cornering to be similar to braking, with a maximum acceleration of 9.81m/s^2.

When we ran the numbers for what we expected of Luminos at the time for a combined loading scenario of one of the front wheels, we came up with the factor of .7 as the maximum amount of the car's weight that can be transferred to a single wheel in the absolute worst case. That forms the basis of the 1G corner, 2G brake, and 4G bump (G = W *g*.7) that Sam L and I used while designing the motors and (I believe) the basis for the loading conditions for SHARK and subsequent suspension design. All critical suspension components (motor/spindles, upright), were simulated to these specifications in ANSYS after initial checking in Solidworks. The roll cage analysis was done separately - see the google site for details.

...And there were no mechanical failures on Luminos, despite some spinning-out antics that I heard about!

Therefore...

Since the design is now in your hands, you're free do choose whatever factor of safety and analysis techniques you like. However, I've heard a number of people on the current team attribute the success of teams like Nuon to the presence of alumni to assist in knowledge transfer. I would argue that the selection of factor of safety and loading conditions are one of the most important pieces of knowledge that could possibly be transferred between teams.

[ you're free do choose whatever factor of safety and analysis techniques you like](https://i.imgur.com/3eggNaX.gif)

[ presence of alumni](https://i.imgur.com/CU2GUR8.gifv)

</wall of text>

I encourage other alumni to correct me if I missed details or have some details wrong - thanks in advance!

Cheers,

NHS

In fact, I have already located the numbers, and they do indeed originate way back with the 19[87] GM Sunraycer.  That car was designed for the following load cases:

4G bump

1G corner

1G braking

2G twist

These are the values that Minnesota has historically used as far back into the deep mists of time as my archives reach.  Minnesota has only ever had one major structural failure - During the 4th day of ASC 2003, west along Route 66 (many, many potholes), Borealis II's chassis failed at the point where the rear shock mount attached (1, 2, 3) and had to be fixed with the application of MOAR METAL (1, 2).  By the way, this failure is a good object lesson on how NOT to load composite panels.

[1](https://www.flickr.com/photos/umnsvp/3471042842/in/set-72157617166555853)

[2](https://www.flickr.com/photos/umnsvp/3470227705/in/set-72157617166555853)

[3](https://www.flickr.com/photos/umnsvp/3471043016/in/set-72157617166555853)

[1](https://www.flickr.com/photos/umnsvp/3470227545/in/set-72157617166555853)

[2](https://www.flickr.com/photos/umnsvp/3470227555/in/set-72157617166555853)

-Above from Adem

* I agree strongly second the notion that FOS * Loading COnditions should be related to the confidence in design manufacture and simulation qualityWe use 3-2-1 loading conditions w/ weight measured weight transfer numbers @ workshit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than thisWe violated our FOS spec on a few parts on LuminosTarget was 2FOS sometimes went down to the ~1.3 rangeonly violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hubMost top European teams use less conservative numbers than we doNo real difference in SW and Ansys results for simple FEAeasier to get higher mesh quality in Ansys which does impact resultsI only used Ansys when I had to solidworks is faster
* I agree strongly second the notion that FOS * Loading COnditions should be related to the confidence in design manufacture and simulation quality
* We use 3-2-1 loading conditions w/ weight measured weight transfer numbers @ workshit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than this
* shit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than this
* get screwed by material properties being out of spec for example
* we now run incoming quality tests to failure on all batches of all parts
* your loading conditions + FOS should be more conservative than this
* We violated our FOS spec on a few parts on LuminosTarget was 2FOS sometimes went down to the ~1.3 rangeonly violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hub
* Target was 2FOS sometimes went down to the ~1.3 range
* only violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hub
* part examples roll cage (only has to survive one load cycle) spindles, and rear hub
* Most top European teams use less conservative numbers than we do
* No real difference in SW and Ansys results for simple FEAeasier to get higher mesh quality in Ansys which does impact resultsI only used Ansys when I had to solidworks is faster
* easier to get higher mesh quality in Ansys which does impact results
* I only used Ansys when I had to solidworks is faster
* solidworks is faster

* I agree strongly second the notion that FOS * Loading COnditions should be related to the confidence in design manufacture and simulation quality
* We use 3-2-1 loading conditions w/ weight measured weight transfer numbers @ workshit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than this
* shit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than this
* get screwed by material properties being out of spec for example
* we now run incoming quality tests to failure on all batches of all parts
* your loading conditions + FOS should be more conservative than this
* We violated our FOS spec on a few parts on LuminosTarget was 2FOS sometimes went down to the ~1.3 rangeonly violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hub
* Target was 2FOS sometimes went down to the ~1.3 range
* only violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hub
* part examples roll cage (only has to survive one load cycle) spindles, and rear hub
* Most top European teams use less conservative numbers than we do
* No real difference in SW and Ansys results for simple FEAeasier to get higher mesh quality in Ansys which does impact resultsI only used Ansys when I had to solidworks is faster
* easier to get higher mesh quality in Ansys which does impact results
* I only used Ansys when I had to solidworks is faster
* solidworks is faster

I agree strongly second the notion that FOS * Loading COnditions should be related to the confidence in design manufacture and simulation quality

We use 3-2-1 loading conditions w/ weight measured weight transfer numbers @ work

* shit fails more often than I am used toget screwed by material properties being out of spec for examplewe now run incoming quality tests to failure on all batches of all partsyour loading conditions + FOS should be more conservative than this
* get screwed by material properties being out of spec for example
* we now run incoming quality tests to failure on all batches of all parts
* your loading conditions + FOS should be more conservative than this

shit fails more often than I am used to

* get screwed by material properties being out of spec for example
* we now run incoming quality tests to failure on all batches of all parts
* your loading conditions + FOS should be more conservative than this

get screwed by material properties being out of spec for example

we now run incoming quality tests to failure on all batches of all parts

your loading conditions + FOS should be more conservative than this

We violated our FOS spec on a few parts on Luminos

* Target was 2FOS sometimes went down to the ~1.3 range
* only violated when heavily constrained by designpart examples roll cage (only has to survive one load cycle) spindles, and rear hub
* part examples roll cage (only has to survive one load cycle) spindles, and rear hub

Target was 2FOS sometimes went down to the ~1.3 range

only violated when heavily constrained by design

* part examples roll cage (only has to survive one load cycle) spindles, and rear hub

part examples roll cage (only has to survive one load cycle) spindles, and rear hub

Most top European teams use less conservative numbers than we do

No real difference in SW and Ansys results for simple FEA

* easier to get higher mesh quality in Ansys which does impact results
* I only used Ansys when I had to solidworks is faster
* solidworks is faster

easier to get higher mesh quality in Ansys which does impact results

I only used Ansys when I had to 

* solidworks is faster

solidworks is faster

It really does not change the weight much between 2x changes in loading conditions and FOS in parts that are not the wheels and motors so dont get too caught up on chasing grams. That said my feeling was always that we could get away with less conservative loading conditions. 

-Above from Greg

