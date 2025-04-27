# leaving-advice-for-future-array-teams

## SSCP - Leaving Advice for Future Array Teams

## Leaving Advice for Future Array Teams

A Note To The Reader: Start Early!

The array is the most important part of the car and is a big ingredient in a team's success. Arguably, the WSC was won by Nuon's array. Unlike other systems in the car, work on the array can start on day 1 of the building cycle. If there was one, single, piece of advice that I could give to the array team lead is Start Early! Your rivals in this field, Hans Gocherman and Alan Chuzel are not as smart as you but they can make better arrays than you because they test a shit-ton of materials combinations and see what works.&#x20;

I cannot stress this point enough: Start Early! Get a bunch of material samples from different vendors and work closely with the vendors to find how long and how hot you should bake the module.&#x20;

-Toby Sachs-Quintana, PhD Candidate 2014, Array team lead 2011-2013

A Short Primer On Arrays&#x20;

A panel on the solar array consists of the following, listed from the bottom of the car going up.

1. Back sheet: This material has several purposes. 1. it electrically isolates the back of the solar cells from the car. The car's carbon fiber is electrically conductive. Make sure that somebody coats the car in fiberglass or some other dielectric as an added protection. 2. The backsheet is white and reflects some light that is not absorbed on the first pass of the solar cell. 3. The white color also helps the array cool.
2. Encapsulant: This should be EVA (ethylene vinyl acetate) EVA is used as the encapsulant by 99.999999% of all solar panels because it is reliable and has good transmission properties in the visible and the near-UV. If you are using a material other than EVA, you should have a VERY good reason. Make sure that the EVA you buy has a wide transmission window
3. Solar Cells: Lucky for you are on Stanford's solar team so you should be able to negotiate with SunPower for their top of the line solar cells. Your team should be the only one with these solar cells. We had bin K cells. No other team had them.
4. Encapsulant: EVA, again
5. Top Sheet: We used a flouropolymer from 3M for the top sheet, rumor has it that they don't make it anymore but DuPont sells solar top-sheets. Just google Dupont solar top sheet and you should get some good hits. I suspect that Chuzel and Gochermann use silicone and texture the silicone as their top sheet. I think that silicone has a better index match too.&#x20;

What Worked Well, and What Didn't

&#x20;  The Good

* Using EVA instead of TPU. Previous teams had used TPU because it has an index of refraction that is bettter matched to air than EVA. The downside of tpu is that it has poor transmission in the UV and SunPower cells do absorb some UV light. TPU is also one of the most hygroscopic polymers out there and you run the risk of shorting the array. Don't use TPU.
* Using Madico's white backsheet.&#x20;
* Working with a local module manufacturing company D2 Solar. They were very helpful and I recommend partnering with them next year. The key contacts there are Steve Coughlin and Mike Rowell

Using EVA instead of TPU. Previous teams had used TPU because it has an index of refraction that is bettter matched to air than EVA. The downside of tpu is that it has poor transmission in the UV and SunPower cells do absorb some UV light. TPU is also one of the most hygroscopic polymers out there and you run the risk of shorting the array. Don't use TPU.

Using Madico's white backsheet.&#x20;

Working with a local module manufacturing company D2 Solar. They were very helpful and I recommend partnering with them next year. The key contacts there are Steve Coughlin and Mike Rowell

&#x20;  The Bad

* Our top sheet.Our cells looked very blue compared to Gocherman and Chuzel meaning that they were not absorbing the blue light. If I had only started early I would have had more time to find a good top-sheet material. The 3M also highly reflective.
* We didn't have time to develop a good way to test our modules. The easy way to do this is to ask the electrical team to make a circuit that can do current-voltage sweeps. Then do an IV sweep of the solar module and record what the solar  radiation was at that time by visiting weather.stanford.edu
* More bypass diodes! It was really sad to see how much power we would lose as the bubble shaded parts of our array. If you have time after you are satisfied with the top-sheet, try to find a way to integrate more bypass diodes into the module. This bypass diode is a good start. http://www.digikey.com/product-detail/en/STPS30L30DJF-TR/497-12867-2-ND/3043802
* The dimensions on the CAD for some of the tabs in Solidworks are wrong. Someone needs to reconfirm all of the dimensions of the tabs before you use old tab layouts. The spacing between the fingers that solder to the cell on some of the tabs were off.

Our top sheet.Our cells looked very blue compared to Gocherman and Chuzel meaning that they were not absorbing the blue light. If I had only started early I would have had more time to find a good top-sheet material. The 3M also highly reflective.

We didn't have time to develop a good way to test our modules. The easy way to do this is to ask the electrical team to make a circuit that can do current-voltage sweeps. Then do an IV sweep of the solar module and record what the solar  radiation was at that time by visiting weather.stanford.edu

More bypass diodes! It was really sad to see how much power we would lose as the bubble shaded parts of our array. If you have time after you are satisfied with the top-sheet, try to find a way to integrate more bypass diodes into the module. This bypass diode is a good start. http://www.digikey.com/product-detail/en/STPS30L30DJF-TR/497-12867-2-ND/3043802

The dimensions on the CAD for some of the tabs in Solidworks are wrong. Someone needs to reconfirm all of the dimensions of the tabs before you use old tab layouts. The spacing between the fingers that solder to the cell on some of the tabs were off.

Key Concepts That You Need To Understand.

* Transmission Windows Our SunPower solar cells absorb in the UV and it is important that the encapsulant and the top sheet have good transmission in that range. The quantum efficiency (efficiency as a function of wavelength) for our cells can be found in a pdf file attached here https://sites.google.com/a/stanfordsolarcar.com/sscp/home/array/sunpower-cells
* Index Matching By having the index of refraction of the top-sheet be directly in the middle of the index of refraction for air and the index of refraction of the enecapsulant, you will be in good shape. Check out this website for more details http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/freseq.html A good exercise is to write a MATLAB program to plug in different values of n and see what the reflection is&#x20;
* EVA crosslinks! When you cure EVA, it will cross link which will cause massive shrinkage in the EVA. If you cool too fast from curing, the EVA will rapidly shrink, pull the top sheet with it, and create wrinkles. A key insight that we had to create beautiful, wrinkle-free modules, is to let the solar modules slow-cool under vacuum overnight

Transmission Windows Our SunPower solar cells absorb in the UV and it is important that the encapsulant and the top sheet have good transmission in that range. The quantum efficiency (efficiency as a function of wavelength) for our cells can be found in a pdf file attached here https://sites.google.com/a/stanfordsolarcar.com/sscp/home/array/sunpower-cells

[https://sites.google.com/a/stanfordsolarcar.com/sscp/home/array/sunpower-cells](../../../../../../stanford.edu/testduplicationsscp/home/sscp-2012-2013/array-2012-2013/sunpower-cells/)

Index Matching By having the index of refraction of the top-sheet be directly in the middle of the index of refraction for air and the index of refraction of the enecapsulant, you will be in good shape. Check out this website for more details http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/freseq.html A good exercise is to write a MATLAB program to plug in different values of n and see what the reflection is&#x20;

[http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/freseq.html](http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/freseq.html)

EVA crosslinks! When you cure EVA, it will cross link which will cause massive shrinkage in the EVA. If you cool too fast from curing, the EVA will rapidly shrink, pull the top sheet with it, and create wrinkles. A key insight that we had to create beautiful, wrinkle-free modules, is to let the solar modules slow-cool under vacuum overnight

A Commend on Texturing

You might notice that Chuzel and Gocherman's cells are textured. I chose not to make a big push to texture our cells for a couple of reasons. 1. Texturing in 2 dimensions can make the solar cells very dirty and hard to clean and will decrease the current gains that you might get from capturing more light at a grazing incidence. Cleaning the array is key during the race. 2. I believe that spending the time on figuring out how to put in more bypass diodes is more important. If you can figure out how to integrate more than 1 diode per module, that will be HUGE.&#x20;

Race Day Notes

Only used DI water to clean the cells. Anything else will leave white streaks. Check out the first-hand account on my blog. http://tobysachsquintana.wordpress.com/ Also, keep watering the cells. The cooling effect from the evaporating water really helps improve the voltage and you keep the car clean which helps out with the current.&#x20;
