# SSCP - Toby's thoughts on the new module

# Toby's thoughts on the new module

tobys@stanford.edu, toby.sachs.quintana@gmail.com

July 9 2012: Met with Greg and Wesley and talked about the new module

Greg: The next module should be light, waterproof, it should clean itself. There are right now, 3 types of encapsulants, the first one is EVA which is essentially hot glue, another one is TPU. TPU is easier to work with because the flow temperature and the curing temperature are not as close as they are for EVA. Xenith shorted due to water getting behind the cells. Index of reflection matching is a good idea, the index for silicon is 3.9. TPU and EVA are not stiff.

Wesley: Me, Greg and Paul made the last array. On Apogee, the substrate was plastic but on Xenith, the substrate was glass. It was a special thin glass from Corning. It was nice because the glass didn't get dirty, whereas Apogees cells got dirty. Xenith's cells were cleaned just by the air flowing over the array. Less layers is better, less reflection 

Ways of improving the module

1. Using a super low viscocity sealant. According to Wesley, they used vaseline and it was a total mess on Xenith

2. Do we really need a textured surface on the plastic that is between the solar cell and air? This sounds lossy to me.

3. Using white paint to reflect light back into the cell (or a fancy metal/transparent insulator)

4. Finding a bitching glass that will reflect IR

Stuff that would be cool to calculate

1. Is a textured top plastic really better? Ray optics simulation could help with this 

2. Is it worth it to have an IR filter on top, what kind of loss would we get in reflection versus temperature in cooling?

July 16, 2012:

NHS: top layer of the top shell should be insulating it's called "surface master" the back should not be kapton (correction - the back of the panel can be kapton....the back of each panel should be completely insulated regardless of topshell material)

Paul: Lockheed uses Kevlar, Kapton is brittle it can be poked through,

Action Items for this week:

Paul: Will talk to Ultra Tape about a nice alternative to Kapton, Will talk to Brisbane Materials regarding their ARC and why it works

Erin: Talking to Saint Gobain regarding their solar encapsulation materials

Toby: Talking to Kuka regarding their encapsulation, will begin  

July 23, 2012

Action items for this week:

Toby: Talk to D2 regarding having them encapsulate for us, stay on KUKA solar

Erin: Trying to get samples from Saint Gobain; also will be working on finding how hot HIT cells have to get to equal the efficiency of SunPower solar cells

July 28, 2012

Wesley has asked me to do due diligence on KUKA to see what the hell they could possibly want an NDA for:

sites I've covered:

http://www.kuka-systems.com/en/branches/solar/photovoltaik/ a site w general overview dc

[http://www.kuka-systems.com/en/branches/solar/photovoltaik/](http://www.kuka-systems.com/en/branches/solar/photovoltaik/)

http://www.kuka-systems.com/en/branches/solar/photovoltaik/P_KUKA_Modul_Linie.htm

[http://www.kuka-systems.com/en/branches/solar/photovoltaik/P_KUKA_Modul_Linie.htm](http://www.kuka-systems.com/en/branches/solar/photovoltaik/P_KUKA_Modul_Linie.htm)

In their module line, they say that they are able to automatic electroluminescence testing, cool

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/)

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/roboLoad/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/roboLoad/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/roboLoad/)

Does glass unload and foil layup?

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/acs_600/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/acs_600/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/acs_600/)

The soldering system that they do is infrared, maybe it's sensitive IP?

http://www.kuka-

[http://www.kuka-](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/string_tmp/)

systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/string_tmp/

[systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/string_tmp/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/string_tmp/)

The Strin test measure and place "The vision system calculates an offset for the robot and allows the string to be accurately positioned on the solar module. Defective strings are rejected to a repair buffer or shuttle" The TMPsystem can detect cracks with its cameras. It also has a system to test electro luminescence

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_x/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_x/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_x/)

This doesn't look very useful, the cross ties are for soldering multiple PV strings

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_bond/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_bond/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_bond/)

They have some sort of edge sealant?

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sheet/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sheet/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sheet/)

This is the robot that they use for doing layup of EVA sheets, I believe they use silicone as an encapsulant

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_trim/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_trim/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_trim/)

A robot that they have to trim excess sheet material the trim can be hot or cold

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_tape/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_tape/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_tape/)

a robot that can cut tape

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_frame/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_frame/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_frame/)

a robot that does framing

http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sun_sim/

[http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sun_sim/](http://www.kuka-systems.com/en/products/standard_products_photovoltaic/pv_module_assembly/robo_sun_sim/)

This is pretty cool, they have a large, xenon lamp sun simulator. Xenon's are nice because their lamp spectrum closely matches the solar spectrum

http://www.prnewswire.com/news-releases/globalwatt-inc-chooses-kuka-systems-local-michigan-supplier-for-the-advanced-liquid-encapsulant-line-in-saginaw-mi-93415914.html

[http://www.prnewswire.com/news-releases/globalwatt-inc-chooses-kuka-systems-local-michigan-supplier-for-the-advanced-liquid-encapsulant-line-in-saginaw-mi-93415914.html](http://www.prnewswire.com/news-releases/globalwatt-inc-chooses-kuka-systems-local-michigan-supplier-for-the-advanced-liquid-encapsulant-line-in-saginaw-mi-93415914.html)

KUKA is being used by a company called GlobalWatt Inc to use a liquid encapsulation which I assume is silicone they are slated to open a 250MW production facility in November 2010

http://www.ipvea.org/index.php?id=146&tx_ttnews%5Btt_news%5D=3706&tx_ttnews%5BbackPid%5D=160&cHash=457ed49287

[http://www.ipvea.org/index.php?id=146&tx_ttnews%5Btt_news%5D=3706&tx_ttnews%5BbackPid%5D=160&cHash=457ed49287](http://www.ipvea.org/index.php?id=146&tx_ttnews%5Btt_news%5D=3706&tx_ttnews%5BbackPid%5D=160&cHash=457ed49287)

The liquid encapsulant that they are using is called PV-6100 which is sold by Dow Corning. The silicone is also slated to be more transparent than EVA. PV-6100 has a shorter cure time than EVA as well. 

http://www.globalwatt.com/index.html

[http://www.globalwatt.com/index.html](http://www.globalwatt.com/index.html)

The cells that these guys make using their advance manufactering process i.e. KUKA robots, have pretty low efficiency, module efficiency at 15.3% Their website kind of sucks.

http://www.greentechmedia.com/articles/read/GlobalWatt-Evicted-From-Its-Empty-Solar-Factory/

[http://www.greentechmedia.com/articles/read/GlobalWatt-Evicted-From-Its-Empty-Solar-Factory/](http://www.greentechmedia.com/articles/read/GlobalWatt-Evicted-From-Its-Empty-Solar-Factory/)

GlobalSolar kind of sucks, here's their swan song.

KUKA solar also installed machines at Evergreen solar's plant in Deven's massacucetts 

KUKA solar installed stuff for "Canada's largest solar manufacterer. Whoever that is. 

Solarwatt in dresden also bought KUKA's stuff to make a 150 MW facility

Sunday, August 4, 2012

Erin calculates that the module would have to read 100C before sunpower cells degrade to the point that they are equal in efficiency to SunPower cells. 

Nathan Golshan says that the next car will have to be a polymer in place of glass because the next body is going to be super curvey

Sam D'Amico says that the reason that Gochermann has better performance over a broader angle of incidence is because their polymer is textured. Sam says that it would be best to use a textured polymer sheet like the one that 3M makes..

Monday, August 6, 2012

Greg got on our case for not calling people. We assigned tasks

Erin: Will call Saint Gobain RE: textured barrier film, EVA, EVA & Backsheet two-ply, try to get samples

Erin: Will contact Stevens Urethane

Paul: WIll contact Brisbane materials, 

Paul: 3M about their front sheet

Toby: Will contact Dupont re:backsheets

Monday, August 20, 2012

Sam thinks he knows how Gochermann gets his solar texture. Essentially the way to duplicate it would be to etch 100 um features into a copper plate. Then you would put the plate in the breather bag and flow the TPU on top of it. To remove the copper plate from the epoxy, you would just etch it away.

