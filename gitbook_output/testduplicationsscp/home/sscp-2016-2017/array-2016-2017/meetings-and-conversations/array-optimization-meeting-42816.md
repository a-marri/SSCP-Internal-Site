# SSCP - Array Optimization Meeting (4/28/16)

# Array Optimization Meeting (4/28/16)

Mismatch:

<Add picture>

* Minor Variations: cell binning
* Minor Variations: cell binning

1. Minor Variations: cell binning

Minor Variations: cell binning

* Affects current or voltage, alters IV curveSmall alterations do not affect max power point (on a PV curve, the max power point occurs when the slope is 0, so small alterations along this tangent don't affect much)Alex: Is there benefit to binning within bins? → Andrew: benefit would be small considering the cost of time and manpower; Power electronics not worth itAt what point does the size of the bin affect our IV curve? → find an IV modeler that allows us to input temperature and etc, generate curve, then sum up current at each voltage
* Affects current or voltage, alters IV curve
* Small alterations do not affect max power point (on a PV curve, the max power point occurs when the slope is 0, so small alterations along this tangent don't affect much)
* Alex: Is there benefit to binning within bins? → Andrew: benefit would be small considering the cost of time and manpower; Power electronics not worth it
* At what point does the size of the bin affect our IV curve? → find an IV modeler that allows us to input temperature and etc, generate curve, then sum up current at each voltage

* Affects current or voltage, alters IV curve
* Small alterations do not affect max power point (on a PV curve, the max power point occurs when the slope is 0, so small alterations along this tangent don't affect much)
* Alex: Is there benefit to binning within bins? → Andrew: benefit would be small considering the cost of time and manpower; Power electronics not worth it
* At what point does the size of the bin affect our IV curve? → find an IV modeler that allows us to input temperature and etc, generate curve, then sum up current at each voltage

Affects current or voltage, alters IV curve

Small alterations do not affect max power point (on a PV curve, the max power point occurs when the slope is 0, so small alterations along this tangent don't affect much)

Alex: Is there benefit to binning within bins? → Andrew: benefit would be small considering the cost of time and manpower; Power electronics not worth it

At what point does the size of the bin affect our IV curve? → find an IV modeler that allows us to input temperature and etc, generate curve, then sum up current at each voltage

* Orientation of Array
* Orientation of Array

1. Orientation of Array

Orientation of Array

* x
* x

* x

x

* Shading
* Shading

1. Shading

Shading

* Bypass diodes vs. cell modulesBrought up Arctan module diagram to look at bypass diode setup (between modules in blocks)If all mismatch losses come from hard shading, then per cell diodes would be ideal (tighter diode grid)Smart bypass diodes (ask Kate to explain)Some available in laminate (laminate in the diode during cell encapsulation)Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performanceJohn: Diffuse light effects when shade is present? (Logan’s simulation work); pyranometer always 100-200 W/m2 even in shadeBuck Converter: Voltage Step-Down ConverterPros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)Recommendations: look into using both bypass diodes and buck convertersQuestionable efficiency of running 5A through a buck converter…
* Bypass diodes vs. cell modules
* Brought up Arctan module diagram to look at bypass diode setup (between modules in blocks)
* If all mismatch losses come from hard shading, then per cell diodes would be ideal (tighter diode grid)
* Smart bypass diodes (ask Kate to explain)Some available in laminate (laminate in the diode during cell encapsulation)Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance
* Some available in laminate (laminate in the diode during cell encapsulation)
* Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance
* John: Diffuse light effects when shade is present? (Logan’s simulation work); pyranometer always 100-200 W/m2 even in shade
* Buck Converter: Voltage Step-Down ConverterPros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)Recommendations: look into using both bypass diodes and buck convertersQuestionable efficiency of running 5A through a buck converter…
* Pros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)
* Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Possible Fix Option: Bleed-Off Concept, only convert difference in power between cells
* Better Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Recommendations: look into using both bypass diodes and buck converters
* Questionable efficiency of running 5A through a buck converter…

* Bypass diodes vs. cell modules
* Brought up Arctan module diagram to look at bypass diode setup (between modules in blocks)
* If all mismatch losses come from hard shading, then per cell diodes would be ideal (tighter diode grid)
* Smart bypass diodes (ask Kate to explain)Some available in laminate (laminate in the diode during cell encapsulation)Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance
* Some available in laminate (laminate in the diode during cell encapsulation)
* Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance
* John: Diffuse light effects when shade is present? (Logan’s simulation work); pyranometer always 100-200 W/m2 even in shade
* Buck Converter: Voltage Step-Down ConverterPros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)Recommendations: look into using both bypass diodes and buck convertersQuestionable efficiency of running 5A through a buck converter…
* Pros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)
* Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Possible Fix Option: Bleed-Off Concept, only convert difference in power between cells
* Better Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Recommendations: look into using both bypass diodes and buck converters
* Questionable efficiency of running 5A through a buck converter…

Bypass diodes vs. cell modules

Brought up Arctan module diagram to look at bypass diode setup (between modules in blocks)

If all mismatch losses come from hard shading, then per cell diodes would be ideal (tighter diode grid)

Smart bypass diodes (ask Kate to explain)

* Some available in laminate (laminate in the diode during cell encapsulation)
* Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance

Some available in laminate (laminate in the diode during cell encapsulation)

Is there enough space between cell corners to insert diode (Gochermann) → more bypass diodes = better shading performance

[Gochermann](/home/sscp-2016-2017/array-2016-2017/meetings-and-conversations/skype-call-with-oliver-gochermann)

John: Diffuse light effects when shade is present? (Logan’s simulation work); pyranometer always 100-200 W/m2 even in shade

Buck Converter: Voltage Step-Down Converter

* Pros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)
* Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small returnPossible Fix Option: Bleed-Off Concept, only convert difference in power between cellsBetter Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Possible Fix Option: Bleed-Off Concept, only convert difference in power between cells
* Better Fix Option: only insert buck converters around bubble (area that may be affected by shading)
* Recommendations: look into using both bypass diodes and buck converters
* Questionable efficiency of running 5A through a buck converter…

Pros: reduces voltage but increases current of underperforming cell to match other cells; higher voltage in, lower voltage out (chop higher V by pulse-width modulation; duty cycle and filter)

Cons: may affect MPPT of entire string, now all the power travels through components such as FETS and inductors which causes losses and heat generation (which could decrease efficiency and power) → big investment in complexity with potentially small return

* Possible Fix Option: Bleed-Off Concept, only convert difference in power between cells
* Better Fix Option: only insert buck converters around bubble (area that may be affected by shading)

Possible Fix Option: Bleed-Off Concept, only convert difference in power between cells

Better Fix Option: only insert buck converters around bubble (area that may be affected by shading)

Recommendations: look into using both bypass diodes and buck converters

Questionable efficiency of running 5A through a buck converter…

Other:

Andrew/Darren: How reliable are your modeling methods?

Smart-Bypass Diode Producers: TI (used by Darren/Andrew), Micro-Semi

* TI has a 3mmx5mm bypass-diode (good size for potentially inserting in diamond shaped spaces between cell corners) http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593
* TI has a 3mmx5mm bypass-diode (good size for potentially inserting in diamond shaped spaces between cell corners) 
* http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593

* TI has a 3mmx5mm bypass-diode (good size for potentially inserting in diamond shaped spaces between cell corners) 
* http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593

TI has a 3mmx5mm bypass-diode (good size for potentially inserting in diamond shaped spaces between cell corners) 

http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593

[http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593](http://www.digikey.com/product-detail/en/texas-instruments/LM74670QDGKTQ1/296-43209-2-ND/5764593)

Stay in touch via email!

