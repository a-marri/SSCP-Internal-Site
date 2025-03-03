# SSCP - Board design guidelines

# Board design guidelines

### Introduction

[](#h.ksbkrwrvtqoj)

Boards have a long lead time, cost a lot, and are a pain to rework, so it's worthwhile to be as diligent as possible to ensure their correctness and maximize their value before sending them out for production. Following these bullets will not guarantee that your board is flawless, but are instead intended as a minimum baseline to try and reduce flaws.

### Pre-design

[](#h.ya9cpttcogpm)

Understand the required functionality

* Electrical constraintsExpected input interfacesRequired outputsPower budgetIsolation requirementsEMI environmentSelf-check and self-monitoring requirementsReliability and robustness requirementsMechanical constraintsComponent clearancesBoard shape (get a CAD file)ConnectorsEnclosureWater resistanceManufacturability (ie, assembly motion leading to interference)DocumentationCreate a project page for this board, or a subpage for a revisionSummarize the requirements
* Electrical constraintsExpected input interfacesRequired outputsPower budgetIsolation requirementsEMI environmentSelf-check and self-monitoring requirementsReliability and robustness requirements
* Expected input interfaces
* Required outputs
* Power budget
* Isolation requirements
* EMI environment
* Self-check and self-monitoring requirements
* Reliability and robustness requirements
* Mechanical constraintsComponent clearancesBoard shape (get a CAD file)ConnectorsEnclosureWater resistanceManufacturability (ie, assembly motion leading to interference)
* Component clearances
* Board shape (get a CAD file)
* Connectors
* Enclosure
* Water resistance
* Manufacturability (ie, assembly motion leading to interference)
* DocumentationCreate a project page for this board, or a subpage for a revisionSummarize the requirements
* Create a project page for this board, or a subpage for a revision
* Summarize the requirements

* Electrical constraintsExpected input interfacesRequired outputsPower budgetIsolation requirementsEMI environmentSelf-check and self-monitoring requirementsReliability and robustness requirements
* Expected input interfaces
* Required outputs
* Power budget
* Isolation requirements
* EMI environment
* Self-check and self-monitoring requirements
* Reliability and robustness requirements
* Mechanical constraintsComponent clearancesBoard shape (get a CAD file)ConnectorsEnclosureWater resistanceManufacturability (ie, assembly motion leading to interference)
* Component clearances
* Board shape (get a CAD file)
* Connectors
* Enclosure
* Water resistance
* Manufacturability (ie, assembly motion leading to interference)
* DocumentationCreate a project page for this board, or a subpage for a revisionSummarize the requirements
* Create a project page for this board, or a subpage for a revision
* Summarize the requirements

Electrical constraints

* Expected input interfaces
* Required outputs
* Power budget
* Isolation requirements
* EMI environment
* Self-check and self-monitoring requirements
* Reliability and robustness requirements

Expected input interfaces

Required outputs

Power budget

Isolation requirements

EMI environment

Self-check and self-monitoring requirements

Reliability and robustness requirements

Mechanical constraints

* Component clearances
* Board shape (get a CAD file)
* Connectors
* Enclosure
* Water resistance
* Manufacturability (ie, assembly motion leading to interference)

Component clearances

Board shape (get a CAD file)

Connectors

Enclosure

Water resistance

Manufacturability (ie, assembly motion leading to interference)

Documentation

* Create a project page for this board, or a subpage for a revision
* Summarize the requirements

Create a project page for this board, or a subpage for a revision

Summarize the requirements

### Architecture

[](#h.pvrkj5c8lb7i)

Design a block diagram to meet the electrical functionality requirements

* Software expectationsOrdering of digital bus pins Analog inputs, sampling rates, filteringExpected error rates and mitigation strategiesMajor component selectionUse pre-designed blocks wherever reasonable.Use processors that have been used before wherever reasonable.Try to re-use ICs from other designs to minimize inventory diversity.SimulationUse LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.DocumentationModify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.Upload simulations so that others can see what you were thinkingArchitecture reviewsSoftware person will check to make sure they can write software for your board.Fellow hardware person will check for structural failures in the design and check over your simulations.Alumnus will check both and provide wisdom from days past.
* Software expectationsOrdering of digital bus pins Analog inputs, sampling rates, filteringExpected error rates and mitigation strategies
* Ordering of digital bus pins 
* Analog inputs, sampling rates, filtering
* Expected error rates and mitigation strategies
* Major component selectionUse pre-designed blocks wherever reasonable.Use processors that have been used before wherever reasonable.Try to re-use ICs from other designs to minimize inventory diversity.
* Use pre-designed blocks wherever reasonable.
* Use processors that have been used before wherever reasonable.
* Try to re-use ICs from other designs to minimize inventory diversity.
* SimulationUse LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.
* Use LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.
* Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.
* DocumentationModify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.Upload simulations so that others can see what you were thinking
* Modify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.
* Upload simulations so that others can see what you were thinking
* Architecture reviewsSoftware person will check to make sure they can write software for your board.Fellow hardware person will check for structural failures in the design and check over your simulations.Alumnus will check both and provide wisdom from days past.
* Software person will check to make sure they can write software for your board.
* Fellow hardware person will check for structural failures in the design and check over your simulations.
* Alumnus will check both and provide wisdom from days past.

* Software expectationsOrdering of digital bus pins Analog inputs, sampling rates, filteringExpected error rates and mitigation strategies
* Ordering of digital bus pins 
* Analog inputs, sampling rates, filtering
* Expected error rates and mitigation strategies
* Major component selectionUse pre-designed blocks wherever reasonable.Use processors that have been used before wherever reasonable.Try to re-use ICs from other designs to minimize inventory diversity.
* Use pre-designed blocks wherever reasonable.
* Use processors that have been used before wherever reasonable.
* Try to re-use ICs from other designs to minimize inventory diversity.
* SimulationUse LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.
* Use LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.
* Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.
* DocumentationModify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.Upload simulations so that others can see what you were thinking
* Modify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.
* Upload simulations so that others can see what you were thinking
* Architecture reviewsSoftware person will check to make sure they can write software for your board.Fellow hardware person will check for structural failures in the design and check over your simulations.Alumnus will check both and provide wisdom from days past.
* Software person will check to make sure they can write software for your board.
* Fellow hardware person will check for structural failures in the design and check over your simulations.
* Alumnus will check both and provide wisdom from days past.

Software expectations

* Ordering of digital bus pins 
* Analog inputs, sampling rates, filtering
* Expected error rates and mitigation strategies

Ordering of digital bus pins 

Analog inputs, sampling rates, filtering

Expected error rates and mitigation strategies

Major component selection

* Use pre-designed blocks wherever reasonable.
* Use processors that have been used before wherever reasonable.
* Try to re-use ICs from other designs to minimize inventory diversity.

Use pre-designed blocks wherever reasonable.

Use processors that have been used before wherever reasonable.

Try to re-use ICs from other designs to minimize inventory diversity.

Simulation

* Use LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.
* Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.

Use LTspice to simulate functional blocks. Not all circuits can be easily simulated, but power management circuits, filtering, analog stages, and many other cases are easy to simulate and doing so helps foster design insight and improves design communicability.

[ LTspice](http://www.linear.com/designtools/software/)

Abuse your circuits in LTspice. Apply noise, voltage spikes, draw too much current, etc. Make sure that it behaves as you would expect. Check the power dissipation in your components (alt-click) and make sure that there are no surprises.

Documentation

* Modify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.
* Upload simulations so that others can see what you were thinking

Modify the project page with your component selection proposals. Look to other projects pages for exampls of what this should look like.

Upload simulations so that others can see what you were thinking

Architecture reviews

* Software person will check to make sure they can write software for your board.
* Fellow hardware person will check for structural failures in the design and check over your simulations.
* Alumnus will check both and provide wisdom from days past.

Software person will check to make sure they can write software for your board.

Fellow hardware person will check for structural failures in the design and check over your simulations.

Alumnus will check both and provide wisdom from days past.

### Schematic

[](#h.24diq3xvallt)

This is the real legwork of design. Generally you will be recreating abstract circuit blocks with concrete components in order to realize a practical design. There are a lot of schematic best practices

* Ensure that the components are purchasable from existing inventory.Ensure that the components are uniquely identifiable. Don't just place a resistor and change its value. Place the resistor that you want from the library. This helps generate a purchasable bill of materials (BOM).Make sure that test points for signals and clip points for power rails are clearly labeled.Documentation (modify the project page)Put up a block diagram and a written description of the board's requirements and how you've satisfied them.Upload a PDF of the schematic so that users without the electrical toolchain can view it.Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.Produce a BOM and take it with you to the reviewRepeatedly review with software, EE, and alumnus, using the review page in the documentation to keep track of issues until there are no more corrections.
* Ensure that the components are purchasable from existing inventory.
* Ensure that the components are uniquely identifiable. Don't just place a resistor and change its value. Place the resistor that you want from the library. This helps generate a purchasable bill of materials (BOM).
* Make sure that test points for signals and clip points for power rails are clearly labeled.
* Documentation (modify the project page)Put up a block diagram and a written description of the board's requirements and how you've satisfied them.Upload a PDF of the schematic so that users without the electrical toolchain can view it.Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.
* Put up a block diagram and a written description of the board's requirements and how you've satisfied them.
* Upload a PDF of the schematic so that users without the electrical toolchain can view it.
* Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.
* Produce a BOM and take it with you to the review
* Repeatedly review with software, EE, and alumnus, using the review page in the documentation to keep track of issues until there are no more corrections.

* Ensure that the components are purchasable from existing inventory.
* Ensure that the components are uniquely identifiable. Don't just place a resistor and change its value. Place the resistor that you want from the library. This helps generate a purchasable bill of materials (BOM).
* Make sure that test points for signals and clip points for power rails are clearly labeled.
* Documentation (modify the project page)Put up a block diagram and a written description of the board's requirements and how you've satisfied them.Upload a PDF of the schematic so that users without the electrical toolchain can view it.Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.
* Put up a block diagram and a written description of the board's requirements and how you've satisfied them.
* Upload a PDF of the schematic so that users without the electrical toolchain can view it.
* Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.
* Produce a BOM and take it with you to the review
* Repeatedly review with software, EE, and alumnus, using the review page in the documentation to keep track of issues until there are no more corrections.

Ensure that the components are purchasable from existing inventory.

Ensure that the components are uniquely identifiable. Don't just place a resistor and change its value. Place the resistor that you want from the library. This helps generate a purchasable bill of materials (BOM).

Make sure that test points for signals and clip points for power rails are clearly labeled.

Documentation (modify the project page)

* Put up a block diagram and a written description of the board's requirements and how you've satisfied them.
* Upload a PDF of the schematic so that users without the electrical toolchain can view it.
* Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.

Put up a block diagram and a written description of the board's requirements and how you've satisfied them.

Upload a PDF of the schematic so that users without the electrical toolchain can view it.

Link to a revisions page to keep track of proposed and implemented schematic review items. Google docs are good for this as they allow simultaneous editing.

Produce a BOM and take it with you to the review

Repeatedly review with software, EE, and alumnus, using the review page in the documentation to keep track of issues until there are no more corrections.

### Layout

[](#h.o2ut28tlqvhx)

Once you have a design that you like, it's time to turn it in to a physical reality. There are a lot of guidelines, rules of thumb, and best-practices that are beyond the scope of a "what do I do next?" style of checklist. For a basic step procedure, see PCB layout.

[ PCB layout](/stanford.edu/testduplicationsscp/home/sscp-2012-2013/electrical-2012-2013/design-references/pcb-layout)

* Import the board shape from the mechanical CAD file. Print it out from a Gerber and make sure it looks like it has been scaled correctly and fits in the box that you've chosen.Group components by functional block to make it easier to do the layoutComponent placementStart placing components within functional blocks.Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.Nudge components around until they mesh nicely with the board shape and minimize routingRoutingDefine your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.Route the ratlines to connect components. Add vias to planes.Check to make sure that the design rules for your board house of choice have been satisfied. Most board houses will also check your Gerbers for compliance, but doing the check locally first eliminates most problems before they happen.Self-documentationMove component silkscreens so that they are near to the referenced component and legible.Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreenDocumentationAdd an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.ReviewME will tell you if the layout will have clearance or interference problemsEE will tell you if you're asking for EMI or solderability problems
* Import the board shape from the mechanical CAD file. Print it out from a Gerber and make sure it looks like it has been scaled correctly and fits in the box that you've chosen.
* Group components by functional block to make it easier to do the layout
* Component placementStart placing components within functional blocks.Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.Nudge components around until they mesh nicely with the board shape and minimize routing
* Start placing components within functional blocks.
* Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.
* Nudge components around until they mesh nicely with the board shape and minimize routing
* RoutingDefine your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.Route the ratlines to connect components. Add vias to planes.
* Define your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.
* Route the ratlines to connect components. Add vias to planes.
* Check to make sure that the design rules for your board house of choice have been satisfied. Most board houses will also check your Gerbers for compliance, but doing the check locally first eliminates most problems before they happen.
* Self-documentationMove component silkscreens so that they are near to the referenced component and legible.Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen
* Move component silkscreens so that they are near to the referenced component and legible.
* Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen
* DocumentationAdd an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.
* Add an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.
* ReviewME will tell you if the layout will have clearance or interference problemsEE will tell you if you're asking for EMI or solderability problems
* ME will tell you if the layout will have clearance or interference problems
* EE will tell you if you're asking for EMI or solderability problems

* Import the board shape from the mechanical CAD file. Print it out from a Gerber and make sure it looks like it has been scaled correctly and fits in the box that you've chosen.
* Group components by functional block to make it easier to do the layout
* Component placementStart placing components within functional blocks.Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.Nudge components around until they mesh nicely with the board shape and minimize routing
* Start placing components within functional blocks.
* Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.
* Nudge components around until they mesh nicely with the board shape and minimize routing
* RoutingDefine your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.Route the ratlines to connect components. Add vias to planes.
* Define your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.
* Route the ratlines to connect components. Add vias to planes.
* Check to make sure that the design rules for your board house of choice have been satisfied. Most board houses will also check your Gerbers for compliance, but doing the check locally first eliminates most problems before they happen.
* Self-documentationMove component silkscreens so that they are near to the referenced component and legible.Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen
* Move component silkscreens so that they are near to the referenced component and legible.
* Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen
* DocumentationAdd an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.
* Add an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.
* ReviewME will tell you if the layout will have clearance or interference problemsEE will tell you if you're asking for EMI or solderability problems
* ME will tell you if the layout will have clearance or interference problems
* EE will tell you if you're asking for EMI or solderability problems

Import the board shape from the mechanical CAD file. Print it out from a Gerber and make sure it looks like it has been scaled correctly and fits in the box that you've chosen.

Group components by functional block to make it easier to do the layout

Component placement

* Start placing components within functional blocks.
* Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.
* Nudge components around until they mesh nicely with the board shape and minimize routing

Start placing components within functional blocks.

Move functional blocks to their homes on the board, taking care to knit them together is a sensible way that reduces routing length and keeps blocks apart which might interfere with one another.

Nudge components around until they mesh nicely with the board shape and minimize routing

Routing

* Define your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.
* Route the ratlines to connect components. Add vias to planes.

Define your power and ground planes. Consider turning off the visibility of ratlines in those nets to reduce visual congestion while you do the rest of your design. Don't forget to leave some room for vias to connect pads on these nets to the planes.

Route the ratlines to connect components. Add vias to planes.

Check to make sure that the design rules for your board house of choice have been satisfied. Most board houses will also check your Gerbers for compliance, but doing the check locally first eliminates most problems before they happen.

Self-documentation

* Move component silkscreens so that they are near to the referenced component and legible.
* Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen

Move component silkscreens so that they are near to the referenced component and legible.

Add board revision, pin function, voltage limit, test point, and other labeling to the silkscreen

Documentation

* Add an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.

Add an annotated screenshot of the board, defining the functional blocks to the project page. This assists others when they need to debug failed hardware or when they are assisting you with board bringup.

Review

* ME will tell you if the layout will have clearance or interference problems
* EE will tell you if you're asking for EMI or solderability problems

ME will tell you if the layout will have clearance or interference problems

EE will tell you if you're asking for EMI or solderability problems

### Fabrication

[](#h.2byod8y4dtl0)

* Generate your Gerbers and verify them in a third party viewer (ie, ViewMate)Send them to the board house for design-for-manufacturability (DFM)Get a financial person to pay to get the boards made. They will check to make sure that you're done all of these steps and will enforce a day "waiting period" to make sure no nagging issues change your design.Send out a Digikey order where the customer reference includes your name and the project. When the parts come in, place them in a dedicated box for your project. This makes it easy to find things that are for your board and cuts down dramatically on part hunting.
* Generate your Gerbers and verify them in a third party viewer (ie, ViewMate)
* Send them to the board house for design-for-manufacturability (DFM)
* Get a financial person to pay to get the boards made. They will check to make sure that you're done all of these steps and will enforce a day "waiting period" to make sure no nagging issues change your design.
* Send out a Digikey order where the customer reference includes your name and the project. When the parts come in, place them in a dedicated box for your project. This makes it easy to find things that are for your board and cuts down dramatically on part hunting.

* Generate your Gerbers and verify them in a third party viewer (ie, ViewMate)
* Send them to the board house for design-for-manufacturability (DFM)
* Get a financial person to pay to get the boards made. They will check to make sure that you're done all of these steps and will enforce a day "waiting period" to make sure no nagging issues change your design.
* Send out a Digikey order where the customer reference includes your name and the project. When the parts come in, place them in a dedicated box for your project. This makes it easy to find things that are for your board and cuts down dramatically on part hunting.

Generate your Gerbers and verify them in a third party viewer (ie, ViewMate)

[ ViewMate](http://www.pentalogix.com/viewmate.php)

Send them to the board house for design-for-manufacturability (DFM)

Get a financial person to pay to get the boards made. They will check to make sure that you're done all of these steps and will enforce a day "waiting period" to make sure no nagging issues change your design.

Send out a Digikey order where the customer reference includes your name and the project. When the parts come in, place them in a dedicated box for your project. This makes it easy to find things that are for your board and cuts down dramatically on part hunting.

### Ways to make debugging easier

[](#h.q7ffrctqjay0)

* Accessible test points on all rails and all signal lines (CAN, I2C, SPI, etc.)If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.Board can be powered in more than one way.  At the very least:CAN (Phoenix cable from battery pack)Testpoints/clips to supply 28V and groundTestpoints/clips to supply logic voltage and groundIdeally also make it possible to power the board over USB.
* Accessible test points on all rails and all signal lines (CAN, I2C, SPI, etc.)If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.
* If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.
* Board can be powered in more than one way.  At the very least:CAN (Phoenix cable from battery pack)Testpoints/clips to supply 28V and groundTestpoints/clips to supply logic voltage and ground
* CAN (Phoenix cable from battery pack)
* Testpoints/clips to supply 28V and ground
* Testpoints/clips to supply logic voltage and ground
* Ideally also make it possible to power the board over USB.

* Accessible test points on all rails and all signal lines (CAN, I2C, SPI, etc.)If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.
* If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.
* Board can be powered in more than one way.  At the very least:CAN (Phoenix cable from battery pack)Testpoints/clips to supply 28V and groundTestpoints/clips to supply logic voltage and ground
* CAN (Phoenix cable from battery pack)
* Testpoints/clips to supply 28V and ground
* Testpoints/clips to supply logic voltage and ground
* Ideally also make it possible to power the board over USB.

Accessible test points on all rails and all signal lines (CAN, I2C, SPI, etc.)

* If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.

If you have an obscene number of signal lines, consider breaking it out to a header of some sort.  The LeCroy can deal with that.

Board can be powered in more than one way.  At the very least:

* CAN (Phoenix cable from battery pack)
* Testpoints/clips to supply 28V and ground
* Testpoints/clips to supply logic voltage and ground

CAN (Phoenix cable from battery pack)

Testpoints/clips to supply 28V and ground

Testpoints/clips to supply logic voltage and ground

Ideally also make it possible to power the board over USB.

