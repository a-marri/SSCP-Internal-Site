# design-review-with-danny-2012\_08\_27

## SSCP - Design Review with Danny 2012\_08\_27

## Design Review with Danny 2012\_08\_27

Notes from Wesley: Unfortunately, I came in at the tail end of the talk...

Notes from Danny

used NACA 63 or 62 for the rear

USed NACA 0025 foil on the front

A 66 foil is too pointed in the front to see out of

teams do not try to have a long laminar flow bubble

Danny says have thickest point line up with where the driver is positioned

He designed for as much laminar flow as possible

Can

1.5 for opening and 3.5 for closing was Sam's ratio for chord ratios when designing air foils. (i.e. take thickest point on car. The distance between nose and thickest point is 1.5xHeight. The distance between thickest point and the tail is 3.5xHeight.

Danny designed for 10 degrees in crosswinds, but that was a mistake. You should design for 5-7 degree cross winds.&#x20;

You have to think about what the critical number (point when the fairing stalls) will be. As angle of attack increases on the fairings you will get more thrust. When the fairing stalls you a lot of drag.&#x20;

C2 curvature continuity only matters when you are doing airfoils.&#x20;

Bondo can make things C2 curves even if they are only tangent when you start.&#x20;

NHS says that C2 curves vs a simple fillet will be very different

Danny likes Morelli because it is flatter.&#x20;

Danny things that TsAGI\_Modified is too rounded. It will make it difficult to define junction at the wheel fairing since you will have air moving laterally.&#x20;

There is a reason why race cars are very chunky. You can manage air flow a lot easier on a chunky shape. A svelte shape makes it difficult to deal with complexities.&#x20;

Take CDF slices along different planes of the airfoil to look at airfoil.

Danny has said that turbulence from a spinning wheel won't make a huge difference. With Fluent we could easily insert a spinning cylinder. What can we do with the Army Stuff.&#x20;

Danny is unconvinced that we need to blend the fairings as much as we have on the blended body shape.&#x20;

Danny said that we should be able to bring the bottom of the fairing up to the main airfoil

Danny is unsold on the Michigan style air foil, but he doesn't necessarily understand why Michigan uses their type of fairing.

With a more rectangular fairing it is easier to make adjustments to air flow.&#x20;

Pressure distribution on the foil should have nice gradation lines, there shouldn't be sharp changes in pressure distribution. you don't want pressure distribution to&#x20;

Danny doesn't know about particle based CFD tools.&#x20;

Danny thinks we should chop down the mesh size of our iterations. We don't need more than 3 million elements.&#x20;

We should do high resolution before we send out for molds, but not now.&#x20;

If we can choose two models we can use the tunnel to choose one and then spend the rest of the time perfecting that model.&#x20;

It is REALLY IMPORTANT to iterate to zero lift before you get into the tunnel. The data that we have is meaningless right now because we have so much induced drag.&#x20;

Danny said we shouldn't be tweaking the shape of the airfoil with this little time. We should just do things like change angle of attack to get to zero lift.&#x20;

2-3in fillet is big enough to eliminate flow issues at junctions.&#x20;

Danny says to still do two cars in the wind tunnel&#x20;

Talking about F1 cars simulations>start with turbulent flow.&#x20;

Reminder> Danny was pushing out the aerobody this time next week
