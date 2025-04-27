# array-passthrough-integration

## SSCP - Array Passthrough Integration

## Array Passthrough Integration

190625 Peer Review / Design Review by Cori

This was an inpromptu and informal peer review of how the array module tabs will be passed through the topshell to be wired to the rest of the ee system. It was very helpful and it's been good to make sure everyone is aware of the process and on the same page. I do recognize however that this could have happened quite a bit earlier -- didn't need to wait to get physical modules in hand, could've made the mockup a lot earlier...!

* Reviewers: Sarah Woodard, Maggie Ford, Temidayo Dairo, Maisam Pyarali, Ricardo IglesiasGoal: Wanted to get a final sanity check on the process; any considerations I'm missing? Do all the connections sound okay from the EE stance?
* Reviewers: Sarah Woodard, Maggie Ford, Temidayo Dairo, Maisam Pyarali, Ricardo Iglesias
* Goal: Wanted to get a final sanity check on the process; any considerations I'm missing? Do all the connections sound okay from the EE stance?
* Reviewers: Sarah Woodard, Maggie Ford, Temidayo Dairo, Maisam Pyarali, Ricardo Iglesias
* Goal: Wanted to get a final sanity check on the process; any considerations I'm missing? Do all the connections sound okay from the EE stance?

Reviewers: Sarah Woodard, Maggie Ford, Temidayo Dairo, Maisam Pyarali, Ricardo Iglesias

Goal: Wanted to get a final sanity check on the process; any considerations I'm missing? Do all the connections sound okay from the EE stance?

* Verdict: Approved

Verdict: Approved

Context: Alta array modules are design with a bus bar containing 3x blocking diodes on the long edge of the module (in-plane with the module). Historically, the array tabs on our Silicon based arrays come through the back of the module and fold down immediately. These GaAs tabs come out of the side of the module -- our aerobody design is tight and smol and doesn't fit the additional 5mm needed per module to fit the bus bars in plane. So we asked Alta to give us modules without the bus bar soldered on, and then SSCP would be responsible for assembling the bus bars and soldering it on "below deck". (Retroactively I think Alta meant below the carbon fiber, but we're going with below the module but above the carbon fiber.)

* Do we need the bus bars? Can't we just take the (potentially negligible) performance losses due to occasional shading? No -- the bypass diodes on the bus bar prevent "hot spots," i.e. if part of the module is shaded, weird current loading cases might occur that could result in a hot spot that burns through the array. So the bus bars with bypass diodes are necessary from a safety perspective as well as performance.
* Do we need the bus bars? Can't we just take the (potentially negligible) performance losses due to occasional shading? No -- the bypass diodes on the bus bar prevent "hot spots," i.e. if part of the module is shaded, weird current loading cases might occur that could result in a hot spot that burns through the array. So the bus bars with bypass diodes are necessary from a safety perspective as well as performance.
* Do we need the bus bars? Can't we just take the (potentially negligible) performance losses due to occasional shading? No -- the bypass diodes on the bus bar prevent "hot spots," i.e. if part of the module is shaded, weird current loading cases might occur that could result in a hot spot that burns through the array. So the bus bars with bypass diodes are necessary from a safety perspective as well as performance.

Do we need the bus bars? Can't we just take the (potentially negligible) performance losses due to occasional shading? No -- the bypass diodes on the bus bar prevent "hot spots," i.e. if part of the module is shaded, weird current loading cases might occur that could result in a hot spot that burns through the array. So the bus bars with bypass diodes are necessary from a safety perspective as well as performance.

Proposed Methodology

(1) Assemble a bus bar

&#x20;   CHECK  all diode connections w/ multimeter before & after soldering

&#x20;            Also CHECK entire bus bar resistance after soldering (catch if anything is wildly out of spec)

&#x20;           << nominal values >>

&#x20;           note: resistance is lower immediately after soldering (due to higher temp of wire/diode) OR during hotter parts of the day

&#x20;   Kapton the perpendicular I tab parts -- 1/2" Kapton, one layer per side

&#x20;           Keep the tails really long, to thread through passthroughs

&#x20;   Kapton the entire bus bar -- 1/2" Kapton, one layer per side

&#x20;           Use two people to do this? One gently holding tape, the other lightly rolling over it to avoid weird creasing? --> practice this on a spare wire (thinner width)

&#x20;           Dog-ear the very ends? So you can solder to the tabs, then re-sandwich the tape over the solder joint

&#x20;   Solder the 4x module tabs to the bus bar -- CHECK  polarity of bus bar!

&#x20;           At what length out?

&#x20;   Kapton the 4x module tabs after soldering to bus bar  -- 1/2" Kapton, one layer per side

(2) Fold tabs following the below directions

&#x20;   Align module (tab-side) edge with edge of table (tabs hanging out over edge of table)

&#x20;   With square tweezers (?), carefully fold each tab one at a time about \~2mm out from the edge of the cells (assuming we want a 2mm lam border)

&#x20;   Carefully flip module and check/improve fold

(3) Apply VHB to module backside -- CHECK no gaps in VHB! (no water ingress!)

&#x20;   Use 1/2" width tape on borders (should be totally flush with lam border, not inset into the module)

&#x20;       At the +/- tabs, the VHB will just go over the Kapton wrapped tabs.

&#x20;   Apply 1" width tape to center rib of module (between columns 2 and 4 on the module)

&#x20;   Should we apply VHB right next to bus bar to keep it all down?

(4) Ready to adhere!

&#x20;   So the bus bar goes on first, then VHB (?), then peel off backing and VERY GENTLY roll module down onto topshell. --> should practice this roll method with a burner module (last cycle they did the whole slowly pull backing off of VHB as the module was laid down, but I think that was because the Si module is so brittle that you cant just roll the mod down, it would crack)

&#x20;

<>

Key Design Reasoning and Concerns:

The borders are really tight on the array to fit on the aerobody -- about 2mm max per module edge of lamination, which means the tab fold has to happen immediately. Talked about shingling tabs from one module under that of the neighboring module, but this won't always work. I.e. if you have 4 modules across the short width of the car, you can shingle the first three mods but then the fourth edge mod has no where to shingle the tabs. If you flip the mod and try to reverse shingle the tabs back to the previous module, you'd have two sets of tabs right on top of each other. So basically folding will always be needed on some of the modules -- therefore it seemed like better design practice to standardize the implementation method and fold all module tabs.

My main concerns were:

&#x20;   (1) Since the +/- bars and tabs are right on the ends of the module, the VHB border of the module has to go over these tabs. This means the module won't actually be adhered to the carbon in those areas -- however the VHB is wider than the tape and should make some contact with the carbon. Second barrier layer is the array sealant in between modules, which should fill any gaps in the VHB seal.

&#x20;   (2) Will the array sealant cover the Kapton folded wires? --> I'm still not sure on this. The VHB is only 0.64mm and the array stack is 0.3mm, so a Kapton-wrapped folded wire is non-negligible thickness. Realistically I think we're going to end up with a very thing layer of sealant over those folded wire areas -- I think I will keep an eye on all the module borders, and if we see Silicon degrading away, we can either re-seal that area, or put smol tape over it....not the most elegant solution, but I do not think flying rocks or dust will severely put those Kapton areas at risk if they become exposed.

&#x20;   (3) Handling. I didn't actually bring this one up, but flipping the modules and folding the bus bars and applying the VHB will all exert some force on the cells. A bit concerened about that. I think our cells are WAY more survivable than the Si due to their small/thin nature (not prone to easy cracking or etc) -- but obviously something to be aware of. Should use extreme care with all parts of this process.

Design Feedback:

* Will the folded wires in Kapton break over time?I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.
* I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.
* I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.
* Similarly, should we spotweld?No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.Did not seem like significant value added to spot-weld.
* No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.Did not seem like significant value added to spot-weld.
* No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.
* Did not seem like significant value added to spot-weld.

Will the folded wires in Kapton break over time?

* I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.
* I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.
* I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.

I stressed a pc back and forth vigoursly for a few minutes and the wire DID break. But we will not see repeated bending in lifetime -- likely lots of vibrational stress due to driving, but I do not think vibrational forces can cause that Kapton-wrapped wire to break.

Similarly, should we spotweld?

* No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.Did not seem like significant value added to spot-weld.
* No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.
* Did not seem like significant value added to spot-weld.
* No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.
* Did not seem like significant value added to spot-weld.

No joint connections will be bent. Solder connections happen around diodes and between bus bar and tabs, but all of those joints will be held in a flat plane.

Did not seem like significant value added to spot-weld.

* What will the order of operations be? What quality checks will you have? Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).
* What will the order of operations be? What quality checks will you have? Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).
* Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.
* I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).
* What will the order of operations be? What quality checks will you have? Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).
* Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.
* I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).

What will the order of operations be? What quality checks will you have?&#x20;

* Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.
* I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).

Good questions. I have not written an SOP yet but will do so and ask for a peer review again. Key takeaway is to triple-check bus bar polarity before soldering to module.

I will also walk through this process with whoever I do the installation with (someone detail-oriented?) Side note that in this implementation scheme, there is no required order that the modules go down (no overlap between modules).

* Will all electrical connections happen on the "dry" side, i.e. on the bottom side of the topshell?Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.
* Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.
* Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.

Will all electrical connections happen on the "dry" side, i.e. on the bottom side of the topshell?

* Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.
* Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.
* Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.

Theoretically, modules connected in series in a lengthwise orientation could have their tabs wired directly to one another to form one giant bus bar....but again, in best design practice, let's standardize and have all tabs drop through (other than in tail) and connections happen on the backside of the topshell. NOTE that we need to sort out the array PCBs.

Next Steps:

* Order the Kapton and tweezers and exacto knife and cutting board?
* Write out an SOPCan decouple the bus bar assembly step (prior to bus bar attach)Vet the SOP (walk through it with people and try it with mockups)
* Can decouple the bus bar assembly step (prior to bus bar attach)Vet the SOP (walk through it with people and try it with mockups)
* Can decouple the bus bar assembly step (prior to bus bar attach)
* Vet the SOP (walk through it with people and try it with mockups)

Order the Kapton and tweezers and exacto knife and cutting board?

Write out an SOP

* Can decouple the bus bar assembly step (prior to bus bar attach)Vet the SOP (walk through it with people and try it with mockups)
* Can decouple the bus bar assembly step (prior to bus bar attach)
* Vet the SOP (walk through it with people and try it with mockups)
* Can decouple the bus bar assembly step (prior to bus bar attach)
* Vet the SOP (walk through it with people and try it with mockups)

Can decouple the bus bar assembly step (prior to bus bar attach)

Vet the SOP (walk through it with people and try it with mockups)

* Make sure array PCBs get sorted
* Make sure array PCBs get sorted
* Make sure array PCBs get sorted

Make sure array PCBs get sorted

* Go ahead and start re-assembling bus barsHave someone quality check all solder jointsHave someone check all diode res values and polaritiesFigure out the Kapton methodThen, kapton bus bars and dog ear
* Have someone quality check all solder jointsHave someone check all diode res values and polaritiesFigure out the Kapton methodThen, kapton bus bars and dog ear
* Have someone quality check all solder joints
* Have someone check all diode res values and polarities
* Figure out the Kapton method
* Then, kapton bus bars and dog ear
* After IV testing mods for eff, figure out what laminate border is needed on which moduleTrim module borders (very carefully!)THEN solder bus bar attachTHEN kaptonTHEN VHB module backside
* Trim module borders (very carefully!)THEN solder bus bar attachTHEN kaptonTHEN VHB module backside
* Trim module borders (very carefully!)
* THEN solder bus bar attach
* THEN kapton
* THEN VHB module backside

Go ahead and start re-assembling bus bars

* Have someone quality check all solder jointsHave someone check all diode res values and polaritiesFigure out the Kapton methodThen, kapton bus bars and dog ear
* Have someone quality check all solder joints
* Have someone check all diode res values and polarities
* Figure out the Kapton method
* Then, kapton bus bars and dog ear
* Have someone quality check all solder joints
* Have someone check all diode res values and polarities
* Figure out the Kapton method
* Then, kapton bus bars and dog ear

Have someone quality check all solder joints

Have someone check all diode res values and polarities

Figure out the Kapton method

Then, kapton bus bars and dog ear

After IV testing mods for eff, figure out what laminate border is needed on which module

* Trim module borders (very carefully!)THEN solder bus bar attachTHEN kaptonTHEN VHB module backside
* Trim module borders (very carefully!)
* THEN solder bus bar attach
* THEN kapton
* THEN VHB module backside
* Trim module borders (very carefully!)
* THEN solder bus bar attach
* THEN kapton
* THEN VHB module backside

Trim module borders (very carefully!)

THEN solder bus bar attach

THEN kapton

THEN VHB module backside

* Go ahead and start marking up passthrough holes on topshellConfirm PCB qty need with EEConfirm edges of array that can be bondoed -- build a tape retainer wall??Cut all passthroughsPot, cut, etcIMPLEMENTbe ready to seal immediately (try out syringe method)
* Go ahead and start marking up passthrough holes on topshellConfirm PCB qty need with EEConfirm edges of array that can be bondoed -- build a tape retainer wall??
* Confirm PCB qty need with EE
* Confirm edges of array that can be bondoed -- build a tape retainer wall??
* Cut all passthroughsPot, cut, etc
* Pot, cut, etc
* IMPLEMENTbe ready to seal immediately (try out syringe method)
* be ready to seal immediately (try out syringe method)
* Go ahead and start marking up passthrough holes on topshellConfirm PCB qty need with EEConfirm edges of array that can be bondoed -- build a tape retainer wall??
* Confirm PCB qty need with EE
* Confirm edges of array that can be bondoed -- build a tape retainer wall??
* Cut all passthroughsPot, cut, etc
* Pot, cut, etc
* IMPLEMENTbe ready to seal immediately (try out syringe method)
* be ready to seal immediately (try out syringe method)

Go ahead and start marking up passthrough holes on topshell

* Confirm PCB qty need with EE
* Confirm edges of array that can be bondoed -- build a tape retainer wall??

Confirm PCB qty need with EE

Confirm edges of array that can be bondoed -- build a tape retainer wall??

Cut all passthroughs

* Pot, cut, etc

Pot, cut, etc

IMPLEMENT

* be ready to seal immediately (try out syringe method)

be ready to seal immediately (try out syringe method)
