# SSCP - PCB Layout

# PCB Layout

Layout, which includes both placement of parts as well as routing, is a very critical aspect of creating a board. While you can't fix a broken schematic, you can make a completely feasible schematic an utter disaster. Here are some pointers to get you started on placing parts and routing traces.

### Steps:

[](#h.uwl19udnks7q)

1. Make sure the proper design rules are imported

[ design rules](/home/sscp-2012-2013/electrical-2012-2013/design-references/altium-design-rules)

2. Get the board outline from leads or mechanical

[ board outline](/home/sscp-2012-2013/electrical-2012-2013/design-references/creating-a-board-outline)

3. To make things simpler, you should add baseline dimensions to your board. 

4. Place parts

5. Make ground plane

6. Turn off ground net or route all grounds to make it easier

7. Route high speed signals/nets

8. Route power

9. Route everything else

10. Properly label silk screen

### Placement

[](#h.aep0i2hzp27s)

Keep parts close--unnecessary trace length can cause a lot of problems. With high frequencies you may get reflections and with power you can get voltage drops. Making sure traces are not too long will make your life easier on many levels. Placing bypass capacitors very close to the IC they are for is also critical.

Make sure you can assemble it and debug it -- Altium should tell you when parts and traces are physically too close, but you should keep in mind that you may need to get a soldering iron to the connection or connect it to a probe. It's also handy to keep things on one side of the board so that you only have to solder and re-flow one side.

Connectors -- Make sure connectors are accessible and are the proper distance from the edge of the board so that they can be plugged in.

Test points -- test points or probe points should be placed close to what they are measuring. When dealing with any high speed signals, the test or probe point should be inline (there should not be a branch on the net connecting the test point). This prevents reflections or accidental antennas. A test point is a single pin sticking out of the board that can be clipped to (used when you know you'll want to measure the net). A probe point is a small circle where the trace is exposed so that it can be probed or soldered to (used in tight spaces or where testing is unlikely but may be needed should something be wrong)

### Routing

[](#h.3aeoiiefe47b)

No 90 degree angles on traces -- a trace with a 90 degree bend can be a problem because it may physically peel off the board. It can also be a problem with very high frequencies that can make the bend and instead act like an antenna out into space.

Make power planes -- to keep your voltage drop down and make routing easier, you can make a plane to carry the power. This is almost always done for ground and should probably be done for the power rail if it is carrying substantial current. Make sure you do not splice your power plane with a trace or component.

Trace width -- traces that carry power should be larger than signal traces. This is a good calculator: http://www.desmith.net/NMdS/Electronics/TraceWidth.html.

[http://www.desmith.net/NMdS/Electronics/TraceWidth.html](http://www.desmith.net/NMdS/Electronics/TraceWidth.html)

Vias -- (electrical/mechanical holes in the board to carry signals) should not cover a pad of a part or be under a part. We do not use blind or buries vias. Minimum via size is limited by the manufacturer and there should be a file that, but you should make sure to increase via size when passing power through vias

### Silk Screen

[](#h.pi12jafm59z4)

Silk screen is the text that is used to label the board. Things you should label include:

The board - what is it? who made it?

Inputs and outputs!! - what voltage? where? What is it for?

Parts - What part is it? What value is the passive? Can someone else solder it just by looking at the board?

Critical nets where there is room

Revision Number

### Board Dimensions

[](#h.h9n1jebtmkkt)

You should add baseline dimensions to your board. To do this, make sure you have the utilities toolbar open (view -> toolbars -> utilities). In that toolbar, under the place dimensions setting, click the arrow and select "Place Baseline Dimension." Then simply click one edge of the board and drag to measure its distance.

