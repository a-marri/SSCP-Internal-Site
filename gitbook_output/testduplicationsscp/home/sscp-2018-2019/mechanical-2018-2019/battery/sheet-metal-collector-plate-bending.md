# sheet-metal-collector-plate-bending

## SSCP - Sheet Metal (Collector Plate) Bending

## Sheet Metal (Collector Plate) Bending

This page details the methods used to determine the location/fabrication of a bend in sheet metal.  The examples are specific to the collector plates, but the methods can still be useful if you are working with sheet metal, want to make it 3d, and have no idea what you are doing.

The collector plates used were originally chemical etched by Italics.  In order to create the bend in them so that they would each have a tab to connect, we used a few trial and error methods.

1. Solidworks modeling: Any parts that are sheet metal and have a bend in them should be made in solidworks using the sheet metal tools. It is pertinent to begin making a part like this because if you make an L shaped part using extrusions, it is very difficult to convert it to sheet metal, you will probably need to start over.  When your model is done properly in sheet metal, you can unspress the “flat pattern” feature and select the outline to save a dxf of the flat pattern.  In order to determine the location of the bend line, create a drawing with the main (top) view of the part.  In drawing view options, change the configuration and/or view to “flat pattern”.  This will produce a drawing with the outline of the part and a dashed line where the bend line is. Use solidworks tutorials and help pages if you don’t know how to use sheet metal tools.

When using this method, it is critical to know the bend radius of your material and bend method.  Don’t just use the solidworks defaults, because they will give you poor results.  For us, we were using nickel and we tested the bend radius using the PRL’s sheet bender.  Basically we bent a test piece and used calipers/radius gauges to calculate the radius and then input this number into solidworks sheet metal bends.

2. PRL bender, guess and check: This method requires method 1 as a baseline for the initial bend line.  Using a reference edge, scribe or mark the bend line on the cp.  Bend 2 cp’s on this line to 90deg, in opposite directions according to the cad design.  Place the two cp’s next to each other how they would be connected in the modules.  Measure the distance between two distinct features across the two cp’s, i.e. measure from the closest ends of the center spot weld tabs.  Compare this with the theoretical distance from cad.  If they are off, adjust the distance from the bend line to the reference edge as necessary and repeat.
3. DIY bending jig at VAIL:  The PRL bender sucks for bending cp’s because it is extremely difficult to bend the tabs to 90deg consistently.  To make beautiful 90deg bends, get the following tools:

Vise

Sharp cornered block of steel

Another block of stock (sharpness irrelevant)

Small piece of sheet metal for use as a scrapper

Rubber mallet

Calipers

Fine tipped pencil/marker

Start by using method 1 as an initial guess at a bend line location.  Use calipers and marker to mark the line on 2 cp’s, both on separate sides so as to get a “left” and “right” cp. Place the blocks of stock in the vise with just enough room between them to fit the cp in.  Place the cp in with the large portion in between the stock and the tab sticking out.  The bend line should be aligned with the sharp bend edge, which ideally will be the closer edge to you; it is easier to bend towards yourself than away.  Clamp the plate in the vise and grab the scrapper piece.  Start at the base of the tab and use the scrapper to push the tab over the sharp edge and down onto the steel stock.  Run the scrapper over the now flat tab once or twice, then lay the scrapper flat over the tab.  Hit the scrapper a couple of times with the mallet to make sure everything is nice and flat.  Remove the cp and repeat for the second cp.

If there are 2 clamshells available, test how well the two cps align.  If the line needs to be edited, flatten the cp in the vise between the two pieces of stock and try again.  Once a good number is found, bend all of the cps with this bend line and setup.  Any changes to the material or setup will require “recalibration” of the bend line.  If you really wan to make a good note of the bend, go back into solidworks and adjust your bend line and radius so that the next time you print off the drawing, it has the correct bend line measurement.

Photos of method 3:

drive>subteams>battery>manufacturing>collector plates

https://drive.google.com/drive/u/0/mobile/folders/0AIwXL34J29MoUk9PVA/1fY8JmCJK2c9m3JLDXRDE08aa8IjriPAc/1EIlvELOmoRFJAT0QnlO0vBHKCLfF5Syq/1zrfkONDYRnKgTwgwu7iWnxadZZY1pXEF/1-9ppWtUt0DPYm-ftEYP9HLvf9ZWWciSj?sort=13\&direction=a

[https://drive.google.com/drive/u/0/mobile/folders/0AIwXL34J29MoUk9PVA/1fY8JmCJK2c9m3JLDXRDE08aa8IjriPAc/1EIlvELOmoRFJAT0QnlO0vBHKCLfF5Syq/1zrfkONDYRnKgTwgwu7iWnxadZZY1pXEF/1-9ppWtUt0DPYm-ftEYP9HLvf9ZWWciSj?sort=13\&direction=a](https://drive.google.com/drive/u/0/mobile/folders/0AIwXL34J29MoUk9PVA/1fY8JmCJK2c9m3JLDXRDE08aa8IjriPAc/1EIlvELOmoRFJAT0QnlO0vBHKCLfF5Syq/1zrfkONDYRnKgTwgwu7iWnxadZZY1pXEF/1-9ppWtUt0DPYm-ftEYP9HLvf9ZWWciSj?sort=13\&direction=a)
