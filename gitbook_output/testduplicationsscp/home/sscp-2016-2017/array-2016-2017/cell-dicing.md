# SSCP - Cell Dicing

# Cell Dicing

Manufacturing: How did we dice?

We used a company called A-Laser to dice our cells. Our contacts there were Joe Azevedo and Fuad Barakat (Joe Azevedo <jazevedo@fctassembly.com> and Fuad Barakat <fuad.barakat@a-laser.com>). Joe is the salesperson and Fuad was the engineer; I would recommend reaching out to Joe and cc'ing Fuad if you want to contact them. The best method to use for cell dicing is to scribe with a laser (I think A-Laser said they used a UV laser) and then mechanically break the cells by hand. The idea is the you create a line on which the cells will break by using the laser to cut most of the way through the silicon, but not into the metal -- if you cut into the metal, you'll lower the shunt resistance of the cell and that's a bad time because it lowers your efficiency. This is stressful (understatement), but gets you the best performance that we tested. To be fair, we only tested this and cutting all the way through at once, but we've heard a lot of solar companies do it this way, so as of December 2017 I would suggest sticking with it unless the team has new information from somewhere.

It's worth mentioning that doing this by hand is actually the best way to avoid cracks; I tried doing it on a table and it was even more stressful. If this is your first time trying it I would highly suggest starting with a round of cheap cells you don't care about to give yourself experience in the method. Some tips: be very patient and just work the smaller part of the cell that you're cutting off back and forth until it breaks off. Only bend it backward (like toward the back of the cell) because if you bend it forward then the silicon will grate on itself. Honestly, this is a lot easier in person so if you're ever doing this without someone who's done it before just ask alumni to come help (John Stayner, Alex Lubkin, Eric So, Abby Taussig, Gillian Micale, and Jonah Sargent all have some level of experience with this).

It's also worth mentioning that you cut from the FRONT of the cell, not the back! So, cut into the blue side. This is tough because you're trying to align the cut to landmarks on the back of the cell, but you're cutting from the front.

As of Dec. 5, 2017, I added the files we sent to A-Laser to use for dicing. There are two files: they're both .dxf format (which is a good format for sending things because it's not proprietary and most programs can import files that are .dxf), which is a 2D format. One has the lines on the back of the E60 cell drawn out in painstaking detail by Jonah. Basically, what you want to do is have the laser cut on the lines of silicon that are on the back of the cell. These are the blue lines (non-white); the white lines are the metal on the back of the cell that we solder onto to get the current to complete our circuit.

Because of the rules, we were constrained to 4 sq. meters of silicon. To meet this rule and have 25 diced cells on the car, we had to dice each cell to 82.81 mm. This wasn't optimal. If we had been able to go a bit farther, we would have been able to intersect the silicon of the three lines that end right near the solder pads on both sides of the cell, which makes them easier to break after you scribe them with the laser. On the attached file, the upper side of the cell is the one where the cutting line is lined up, and the bottom one is where it isn't. If you zoom in, it's a fairly noticeable difference. Anyway, if you line those up you'll make it easier to break once you get to that portion.

Dicing Performance: Is it worth it?

This will the the main question for whether you want to dice or not. It came down to multiple reasons for us: the fact that we got an extra 2/3 cell and that we raised the voltage of the string (which raises the efficiency of the MPPT when it converts your string voltage to the battery voltage) were the two big ones. For future cars, you may be able to make them smaller as well, but I would highly suggest having two full models of your car (one with dicing and one without) before you make any decisions like that, since it'll be heavily based on aero and our team has found in the past that the gains wouldn't be worth it.

For us, it looks like we lost 0.2% absolute efficiency by dicing. Our bin Me1 cells (average 24.1% efficiency roughly) came out with an average of 23.9% efficiency. The difference is because the shunt resistance of the cell gets lowered, not because of any losses in I_sc or V_oc. We theorize based on info from SunPower people like Kat Han that the lowered R_sh is because the edges of the cell are no longer passivated -- some people have suggested that we could re-passivate the edges, but that would be a whole project on its own and would be difficult for an undergrad team like us to do unless someone steps up and focuses solely on that.

I'm attaching two spreadsheets: one from the original dicing experiment when we decided if it was worth it, and one that has the binning data for most of our diced cells (not sure where the rest of it is, but I'm searching as of 12/5/17). As always with SunPower cell information, do not release it to other people because we are under an NDA!

You'll notice if you look at Dicing Losses.xlsx that the losses for that one were actually higher than we got in the final round -- I'm not sure if that's because of the difference between C60 and E60 cells (maybe E60 have better technology that makes them less susceptible) or if we just did a better job on the cells we used on the car.

[](https://drive.google.com/folderview?id=1kMZwZMZOwpW49ezxjUtDOkZ6HiolbBet)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1kMZwZMZOwpW49ezxjUtDOkZ6HiolbBet#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1kMZwZMZOwpW49ezxjUtDOkZ6HiolbBet#list" frameborder="0"></iframe>

