# slack-discussions

## SSCP - Slack Discussions

## Slack Discussions

mikechen \[3:46 PM] &#x20;

@gfiore btw, the calculations we performed today with pack voltage were based off the assumption that the mass of our GA cell is 48.5 g. That's going off of what WSC rated them to be last cycle. Datasheets, however, say the GA's "max mass" is 49.5 g.

\[3:47] &#x20;

Whether the cell is 48.5 g or 49.5 g will affect our optimal configurations and thus pack voltage (125 V isn't practical with a 49.5 g cell).

slackbot \[3:47 PM] &#x20;

optimal? so what optimization method are you using?

gfiore \[3:49 PM] &#x20;

@slackbot: :rage:

\[3:49] &#x20;

What would be a practical nominal voltage close to 125 with 49.5g cells?

\[3:49] &#x20;

@mikechen:

midoriabril \[4:32 PM] &#x20;

HAHA

mikechen \[4:41 PM] &#x20;

@gfiore There are several options: 115V at 5.29 kWh, 122.1 and 133V (both at 5.2 kWh), and lastly 148V at 5.24 kWh.

\[4:41] &#x20;

Our capacity takes a hit because our total usable cell count drops from 412 to 404.

gfiore \[4:42 PM] &#x20;

@mikechen What are the maximum voltages for each of those?

mikechen \[4:43 PM] &#x20;

@gfiore 115V = 86.8 min/130.2 max

\[4:44] &#x20;

122 V = 92.4 V min/138.6 V max

\[4:44] &#x20;

133.2 = 100.8 V min/138.6 V max

\[4:44] &#x20;

148 V = 112 V min/168 V max

gfiore \[4:45 PM] &#x20;

There are two 138.6 entries

\[4:46] &#x20;

Is the second one correct?

\[4:47] &#x20;

@mikechen Thanks for these numbers. When do you think we’ll know whether the cells are considered to be 48.5g or 49.5g?

kpregler \[4:48 PM] &#x20;

joined #mechanical-battery by invitation from @gfiore

mikechen \[4:48 PM] &#x20;

for 133.2V, max is 151 V

gfiore \[4:49 PM] &#x20;

Thanks.

mikechen \[4:49 PM] &#x20;

@kelseyjosund is working on getting confirmation from WSC. We might want to email someone directly, if possible. Since a lot of our pack design will depend on this.

gfiore \[4:50 PM] &#x20;

So, the issue is that the buck that greg is using has a max voltage of 140V.

mikechen \[4:52 PM] &#x20;

Is there anyway to use another buck rated for higher voltage? If the cell is 48.5 g, we would ideally do 125 V nom, giving a max V of 143

gfiore \[9:00 PM] &#x20;

That’s a question for @gbrandao

\[9:01] &#x20;

But we’re also looking into solving the problem by rewinding the motor rotors

\[9:01] &#x20;

I’m scheduling a call with NHS and Sam L. to try to understand exactly what the issue is and if it can be solved by rewinding.

\[9:01] &#x20;

And if it is affected by a lighter or more aerodynamic car

mikechen \[9:09 PM] &#x20;

@gfiore  okay and if we rewind, we won't change the pack voltage?

gfiore \[9:09 PM] &#x20;

That’s correct

mikechen \[9:11 PM] &#x20;

Okay, when are we making this decision by? We should ask if the motors can be dropped to below 100V because we could get less losses by doing so

gbrandao \[9:30 PM] &#x20;

We can go higher than 140V. The problem is that I will probably have to design the buck myself if we do, as there are no prepackaged solutions that go any higher than 140V.

mdrach \[9:40 PM] &#x20;

Thanks for reaching out to NHS and Sam, @gfiore .  Specifically, I hope we can discuss with them the math behind 1) voltage->top speed relationship and 2) torque->top speed tradeoff for the rotors.

\----- October 10th -----

mikechen \[12:26 AM] &#x20;

I've spoken to Max before about motor math and have done a bit of research myself. Basically, there is a constant that is associated with the motor windings. This constant, chosen for Luminos, is essentially 1 V (battery DC bus)/ (rads/s).

\[12:26] &#x20;

If you do some more math, 1 V/ (rads/s) translates to about 1 kph/V

\[12:28] &#x20;

Here's a page Prags directed me to re:motor physics: http://lancet.mit.edu/motors/motors3.html

\[12:29] &#x20;

We probably have the rotational speed vs. torque curve for our motors on the internal site, but theres essentially a graph somewhere that looks like this generic one:

mikechen \[12:29 AM] &#x20;

uploaded an image: motor math&#x20;

Add Comment

mikechen \[12:31 AM] &#x20;

Prags added in the yellow line, it's meant to represent the hard current cutoff we've built into our system so we don't fuck any electronics up at low speeds + high torque

loganherrera \[1:08 AM] &#x20;

What is this concern about a dc dc converter max voltage?

mikechen \[10:00 AM] &#x20;

@loganherrera: we're concerned that having our pack's max voltage above 140 would mean we'd need to design a custom buck converter @gbrandao

loganherrera \[11:39 AM] &#x20;

What is a "custom buck converter"?

mikechen \[2:07 PM] &#x20;

@gbrandao

gbrandao \[2:28 PM] &#x20;

As in LT (nor any other company as far as I could tell) doesn't have anything that goes above 140V for my power requirements (3A). As such, as I see it, going above that threshold would mean leaving the wonderful world of LT's prepackaged solutions and designing more significant parts of the buck myself. Any suggestions you have would be greatly appreciated

mdrach \[3:26 PM] &#x20;

@mikechen thanks for the info.  Do you have a link to the speed vs torque graph for our motors on the internal site?  From Sam and NHS (I may reach out to Prags too) we need to get the actual values of these torque constants so we can do math to determine top speed.

loganherrera \[4:28 PM] &#x20;

This is very near rectified mains voltage. Making power supplies at this voltagr level is a solved problem. I don't know that a buck, specifically, is commercially available at this voltage and power level

\[4:29] &#x20;

This would be a good candidate for buying a power supply brick I think

\[4:29] &#x20;

And then worry about highly  optimizing later

mdrach \[10:03 PM] &#x20;

Gawan and I spoke with Sam today and have an idea of the math we need to do to make this decision.  We can talk more on Wednesday.

gfiore \[11:22 PM] &#x20;

@mikechen @gbrandao @loganherrera&#x20;

While there still is some related math to be done, I think it is likely that we won't need to bring the max pack voltage above 140V.

\----- October 11th -----

mikechen \[12:32 AM] &#x20;

Ian is coming Thursday at 7, btw guys

\----- October 12th -----

mikechen \[2:26 PM] &#x20;

Jk, @channel he's coming at 9 today. Come by if you've got any questions about the pack. I'll be going over the voltage change with him, asking about designing the modules, welding, nail Test stuff, the form factor of the box itself, and etc

\----- October 16th -----

tpunnoose \[2:22 PM] &#x20;

joined #mechanical-battery. Also, @jmgiron joined.

\----- October 17th -----

mikechen \[12:39 AM] &#x20;

@gfiore @gbrandao just wanted to post this here so I don't forget: I need to get the MPPT efficiency data from Sam Lenius because the battery spreadsheet is based off the Luminos mppt's

gfiore \[8:41 AM] &#x20;

MPPT efficiency page with old data: https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2012-2013/electrical/individual-projects/critical-systems/sam

Sam says that the new MPPTs have similar efficiency:  "For first order analysis, the efficiency is the same. For second order, they're 1% more efficient above 2:1 boost ratio."

\[8:41] &#x20;

From Max

mdrach \[6:16 PM] &#x20;

Also, here's the Tritium equation so you can double check also

\[6:16] &#x20;

Here's the Tritium efficiency equation you can check against what Max has on the spreadsheet (two photos on the page) https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2012-2013/electrical/individual-projects/critical-systems/battery-pack-1/battery-pack#TOC-Minimizing-Power-Converter-Losses

\----- October 18th -----

mikechen \[12:10 AM] &#x20;

@gfiore The current equation being used is (1-0.006)\*boost\_ratio

\[12:10] &#x20;

to calculate efficiency

\[12:11] &#x20;

I dont think it's necessary to edit the sheet to denote that 1% gain above 2:1 boost ratios, but correct me if I'm wrong

mikechen \[12:26 AM] &#x20;

I just checked, our calculations should be all correct. The tritium eqs havent change, I dont think. The only change, if we want to calculate any, would be the efficiency increase w/ the new MPPTs

\[12:27] &#x20;

I think max just thought of the wrong order of magnitude when he spoke with us sunday. 40W is the expected total loss

mikechen \[12:50 AM] &#x20;

@gbrandao @gfiore Are we completely ruling out 125V? A huge concern that max raised was that 31 cells in series (to achieve 114V) would make greg's life very annoying since its a prime number

loganherrera \[9:34 AM] &#x20;

Why is a prime number so painful?

gfiore \[9:57 AM] &#x20;

Max said something about splitting up the modules for voltage monitoring (I think) and the issue was having different number of cells attached to different monitors. @mikechen does that sound right?

mikechen \[11:38 AM] &#x20;

Yeah apparently the voltage sense component senses either 2-3 cells

loganherrera \[12:23 PM] &#x20;

what does voltage sense component mean? @gbrandao

mikechen \[11:56 PM] &#x20;

@gbrandao ^^^

\----- October 19th -----

gbrandao \[7:48 PM] &#x20;

Hey, sorry about the delay

gbrandao \[8:02 PM] &#x20;

a prime number of cells is doable, just pretty annoying. The reason for this is that having a number of cells that is evenly divisible by 2 or 3 means that we can hook up 2 or 3 chips and communicate with them in exactly the same way. Having different numbers of cells hooked up to each chip, while doable, means that each chip must have a different schematic and handling in code

\----- October 20th -----

kelseyjosund \[10:38 AM] &#x20;

I asked again on the WSC forum, trying to get a straight answer out of them. They censored documentation —> d&#x6F;_**entation, again —> a**_&#x6E;, and honored —> \*\*nored

\[10:38] &#x20;

Their censorship is just ridiculous

gbrandao \[10:42 AM] &#x20;

wowww that is amazing

mikechen \[3:13 PM] &#x20;

@gfiore @gbrandao when do we want to fully confirm the battery pack voltage? 31 aka 115 V would make it annoying for greg. 34 series aka 125 V would be fine, but would mean that our contactor needs to be changed to handle 148 V max

\[3:14] &#x20;

I'm going to design for 31 in series rn, but i want to know for sure which one we're going to stick with

gfiore \[4:47 PM] &#x20;

Here's my take. Doing 125V instead of 115V will cost us less than a minute in race time. If it's the type of implementation issue that will give @gbrandao a headache and make it unnecessarily complex, then go with 125V nominal. I'd be very surprised if the race came down to 1 minute.

kelseyjosund \[4:59 PM] &#x20;

And if it did come down to one minute, there are tons of other places we could look to explain a difference that small, so it’s not like we’d blame it on any one particular decision

\----- October 21st -----

mikechen \[2:13 PM] &#x20;

Okay, the way I understand it, @gbrandao please correct me if I'm wrote, the biggest downside to 125V nominal is that the max voltage will be 148ish at the top of the pack, which we dont maintain for long. The issue with 148V is that our contactors are rated for 140V max. Is this as simple as a hardware switch or are there more downstream issues we might also need to consider?

gbrandao \[2:24 PM] &#x20;

No. the contactors are just fine. Its the power converters that start to get annoying. it should be fine no matter what, but I'm trying to finalize my first rev within the next week and would like to have a solid answer on voltage by then, as moving to that voltage will require me to completely redesign parts of my power circuitry

gfiore \[9:02 PM] &#x20;

@gbrandao: minor correction. The max voltage for 125V nominal would be 142.8V. I don't know if that changes anything.

\[9:03] &#x20;

@gbrandao: what will be more work for you? Having 31 modules or having a max voltage > 140V?

\----- October 23rd -----

gbrandao \[5:02 PM] &#x20;

31 modules would be better.

mikechen \[5:44 PM] &#x20;

uploaded and commented on a file&#x20;

Previous Panasonic Requirements

133KB

PDF

&#x20;Click to view

1 Comment

found this on the internal site, seems like the guidelines from last cycle. not confirmed

tpunnoose \[8:08 PM] &#x20;

assuming it doesn't change, the 5mm/sec penetration speed rules out the nail gun idea

mikechen \[9:47 PM] &#x20;

Can't tell if that's a max or a min, but yeah, I'd assume so too. I'm going to try to get a clear set of guidelines from Paul, our Panasonic rep, this week

\----- October 24th -----

mikechen \[4:15 PM] &#x20;

@gbrandao @gfiore Confirming that the pack voltage will be 115 V nominal, meaning 31 modules in series, 13 in parallel. Our min voltage will be 86.8V and our max is now 130.2V. We'll have 403 total cells for a capacity of 5.29 kWh

gfiore \[4:21 PM] &#x20;

@mikechen:  Hold up. I'm looking back the battery calculations sheet and the minimum bus voltages on the first page (calculations) don't match with the minimum bus voltages on the cell utilization page. What's up with that?

mikechen \[4:22 PM] &#x20;

The cell utilization sheet should be the most accurate because that's where they're copied over from. I'll check it out later after class

gfiore \[4:23 PM] &#x20;

Ok. Because the minimum voltage is what we care about for speed limiting, so let's be very sure of that number before we proceed.

tinali \[8:16 PM] &#x20;

joined #mechanical-battery

\----- October 25th -----

gfiore \[10:49 AM] &#x20;

@mikechen: any update?

mikechen \[11:41 AM] &#x20;

check now they should be matched up

gfiore \[4:37 PM] &#x20;

Based on the older numbers I thought that the min voltage for 115 nom would be 92V. It’s actually 86.8V. That means we would be limited to   roughly 86.8 \* 0.92 = \~80 kph at minimum voltage. Can you send me the V vs. SOC chart? Depending on voltage at around 5% SOC, the 115V nominal could be problematic.

\[4:37] &#x20;

@mikechen forgot to tag you

mikechen \[4:41 PM] &#x20;

Don't have that data yet. We need to characterize the cells to have an inhouse table for SOC, V, and temperature

\[4:41] &#x20;

@gfiore

gfiore \[4:41 PM] &#x20;

@mikechen but can you send me the ones from last year so I can at least get a rough estimate?

mikechen \[4:44 PM] &#x20;

kk hold on, in class rn

\[4:45] &#x20;

I'll send you the folder of matlab files and raw data, just run the model.m file and it'll generate the SOC triscatteredinterpolant

\[4:46] &#x20;

SOC is a function of current, voltage, and temperature, so it's a bit tricky to say voltage at around 5% SOC

\----- October 26th -----

mikechen \[7:56 PM] &#x20;

@tpunnoose Hey could you figure out how we should collect multichannel temperature probe data? We're going to need to record the temperature at multiple locations. If we need to buy any equipment (like a temperature specific data collector or whatever), we should move on that now. I'm guessing we probably have everything we need minus the temperature probes

tpunnoose \[8:59 PM] &#x20;

Yeah I can look into it

\----- October 27th -----

mikechen \[7:21 PM] &#x20;

pretty interesting read on the samples of intercellular material we're receiving soon

\[7:21] &#x20;

http://www.nrel.gov/transportation/energystorage/pdfs/42544.pdf

\----- October 28th -----

loganherrera \[2:15 AM] &#x20;

What interests you?

mikechen \[12:39 PM] &#x20;

NREL's testing paradigm and the results

\[12:39] &#x20;

and that this was developed in 2007

mikechen \[12:52 PM] &#x20;

@tpunnoose just shipped the part for 3D printing, arriving next wednesday

tpunnoose \[1:15 PM] &#x20;

Dope you got two of them right

mikechen \[2:48 PM] &#x20;

Yeah

\----- October 31st -----

mikechen \[10:59 AM] &#x20;

I'm going to go ahead and tell Panasonic that we're doing 13p31s this cycle

\[10:59] &#x20;

and are going to stack modules vertically

\[10:59] &#x20;

unless anyone objects to that @channel

kelseyjosund \[11:07 AM] &#x20;

Sounds good to me

gfiore \[12:12 PM] &#x20;

:thumbsup:

kelseyjosund \[7:42 PM] &#x20;

New response from WSC:

\[7:42] &#x20;

Teams are required to submit detailed specifications of the cells they will be using. These specifications must include the nominal m\*\*\* of the cells, and must be endorsed by the manufacturer.

In the previous event, several teams based their design on preliminary or brief specifications that did not match detailed specifications and were not endorsed by the manufacturer. Hence the warning in the regulations:

"Specifications from third party suppliers or found on the internet might not match t\*\*se endorsed by manufacturers."

To ensure that you are compliant with the regulations, you must obtain detailed specifications of the cells you will be using and have these endorsed by the manufacturer.

\----- November 1st -----

mikechen \[4:08 PM] &#x20;

@kelseyjosund looks good. I think we can say that we're in the clear, given the email paul sent a week or so ago. What do you think?

kelseyjosund \[5:35 PM] &#x20;

Yeah, I agree

\[5:35] &#x20;

It sounds like they just want to be sure that we’re getting our data sheets from a manufacturer, not from some random place on the internet

\----- November 4th -----

mikechen \[12:48 AM] &#x20;

@hayden8hall, if I'm really limited by the pack's vertical height, can i turn it so that the long end isn't going in perpendicular to the longitudinal axis of the car? like have it go longer into the empty space in the fairing behind it?

\[12:48] &#x20;

im wasting a lot of space having the pack have a square footprint

hayden8hall \[12:48 AM] &#x20;

joined #mechanical-battery by invitation from @mikechen

mikechen \[12:49 AM] &#x20;

I don't need extra space vertically if i can flatten it it's XY base out in

\[12:49] &#x20;

one direction

mikechen \[1:19 AM] &#x20;

@gbrandao what's your BMS height? I'm going to give it a bounding box of 7" x 7" and 3" tall

loganherrera \[2:14 AM] &#x20;

BMS 8.2 tallest component is nominally 1.375in above top plane of PCB

mikechen \[10:50 AM] &#x20;

How about the contact IRS?

\[10:50] &#x20;

I have a separate compartment for the boards because of the way the cells are vertically stacked

loganherrera \[11:28 AM] &#x20;

contactors are taller and are going to be different this time I think

\[11:28] &#x20;

@gbrandao

kpregler \[11:59 AM] &#x20;

@mikechen: maybe you talked about the bms dimensions with Greg already but 7"x7" sounds smaller than last cycle to me

loganherrera \[11:59 AM] &#x20;

nope

\[12:00] &#x20;

BMS 8.2.2 has a bounding box of almost exactly 7x7

kpregler \[12:00 PM] &#x20;

Oh ok good :thumbsup:

mikechen \[12:00 PM] &#x20;

I saw the cad of arc tans and it was 6 by 7 or something like that and was an L

\[12:00] &#x20;

Yep

loganherrera \[12:00 PM] &#x20;

Still needs clearance for real wires to connect, etc

\[12:00] &#x20;

but that's the size

kpregler \[12:03 PM] &#x20;

Wrt contactors the minitactor option is 1.321" tall

\[12:03] &#x20;

Otherwise I think we're going with the same as last year

\[12:04] &#x20;

http://www.gigavac.com/sites/default/files/catalog/spec\_sheet/p125.pdf

mikechen \[12:50 PM] &#x20;

Where can I get the min/ideal bend radii I need to allow the wires we're going to use?

\[12:50] &#x20;

I'm going to be conservative for now and leave as much extra space as possible

loganherrera \[12:50 PM] &#x20;

rule of thumb minimum bend radius is 4x wire diameter

\[12:51] &#x20;

but Greg is going to have a bad time if he can't get his fingers in

gbrandao \[1:10 PM] &#x20;

7X7 should hopefully be enough, though that will likely make the next BMS design even more space constrained than the last as all the contactors, and fuses now have to fit into that space as well.

\[1:11] &#x20;

is 7X7X3 the board space or the total compartment space?

loganherrera \[1:21 PM] &#x20;

are all of the contactors and fuses board mounted now?

gbrandao \[1:22 PM] &#x20;

right now, yes

mikechen \[2:15 PM] &#x20;

Total@board space there is more space in the compartment

\[2:15] &#x20;

It's a 9.5x13.65x3.5 compartment

gbrandao \[2:16 PM] &#x20;

what will the rest of the space be used for?

mikechen \[3:34 PM] &#x20;

routing wiring and whatever else is needed

\[3:35] &#x20;

and connectors to the outside

\[3:35] &#x20;

and from the module compartment into the bms compartment

gbrandao \[3:54 PM] &#x20;

Alright, so I have some room to play with then
