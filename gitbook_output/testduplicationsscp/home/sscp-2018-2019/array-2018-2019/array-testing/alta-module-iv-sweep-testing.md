# SSCP - Alta Module IV Sweep Testing

# Alta Module IV Sweep Testing

Date: 190626

Test Timeframe: ~12:00-14:30

Solar Noon: 13:11:26 (https://www.esrl.noaa.gov/gmd/grad/solcalc/)

[https://www.esrl.noaa.gov/gmd/grad/solcalc/](https://www.esrl.noaa.gov/gmd/grad/solcalc/)

Goal:

(1) make sure all IV curves look nominal (any damage when shipping from Alta to VAIL / due diligence quality check)

(2) based on calculated efficiency of the modules (or maybe fill factor) strategically determine where more/less efficient modules should go

Test Methodology:

* 15ft out from VAIL pillarIV Sweep from 0-28V in 0.1V steps, 1.25A complianceRerun if the line is wiggly or has peaks (random clouds)Denote solar irradiance from Extech solar metertolerance is +/- 10Wmeter was held at constant position, angle up like the module but NOT angled normal to sunDouble check cathode (+) is connected to the tab that runs BEHIND the cells, and the anode (-) is attached to the tab that runs in FRONT of the cells (see picture)Cori renamed the python data files and executed the python test script, Peter coordinated removing and replacing/attaching modules to the leadsAll modules were taped down to their cardboard spacers (parchment paper and foam packing removed) to keep the modules from blowing away
* 15ft out from VAIL pillar
* IV Sweep from 0-28V in 0.1V steps, 1.25A compliance
* Rerun if the line is wiggly or has peaks (random clouds)
* Denote solar irradiance from Extech solar metertolerance is +/- 10Wmeter was held at constant position, angle up like the module but NOT angled normal to sun
* tolerance is +/- 10W
* meter was held at constant position, angle up like the module but NOT angled normal to sun
* Double check cathode (+) is connected to the tab that runs BEHIND the cells, and the anode (-) is attached to the tab that runs in FRONT of the cells (see picture)
* Cori renamed the python data files and executed the python test script, Peter coordinated removing and replacing/attaching modules to the leads
* All modules were taped down to their cardboard spacers (parchment paper and foam packing removed) to keep the modules from blowing away

* 15ft out from VAIL pillar
* IV Sweep from 0-28V in 0.1V steps, 1.25A compliance
* Rerun if the line is wiggly or has peaks (random clouds)
* Denote solar irradiance from Extech solar metertolerance is +/- 10Wmeter was held at constant position, angle up like the module but NOT angled normal to sun
* tolerance is +/- 10W
* meter was held at constant position, angle up like the module but NOT angled normal to sun
* Double check cathode (+) is connected to the tab that runs BEHIND the cells, and the anode (-) is attached to the tab that runs in FRONT of the cells (see picture)
* Cori renamed the python data files and executed the python test script, Peter coordinated removing and replacing/attaching modules to the leads
* All modules were taped down to their cardboard spacers (parchment paper and foam packing removed) to keep the modules from blowing away

15ft out from VAIL pillar

IV Sweep from 0-28V in 0.1V steps, 1.25A compliance

Rerun if the line is wiggly or has peaks (random clouds)

Denote solar irradiance from Extech solar meter

* tolerance is +/- 10W
* meter was held at constant position, angle up like the module but NOT angled normal to sun

tolerance is +/- 10W

meter was held at constant position, angle up like the module but NOT angled normal to sun

Double check cathode (+) is connected to the tab that runs BEHIND the cells, and the anode (-) is attached to the tab that runs in FRONT of the cells (see picture)

Cori renamed the python data files and executed the python test script, Peter coordinated removing and replacing/attaching modules to the leads

All modules were taped down to their cardboard spacers (parchment paper and foam packing removed) to keep the modules from blowing away

Data Location:

https://drive.google.com/drive/folders/1g03nv3b2TtPRAsVoc0qjQ3bj4pLkSPME

[https://drive.google.com/drive/folders/1g03nv3b2TtPRAsVoc0qjQ3bj4pLkSPME](https://drive.google.com/drive/folders/1g03nv3b2TtPRAsVoc0qjQ3bj4pLkSPME)

Results:

https://docs.google.com/spreadsheets/d/16EKfi4TtOe4e2quNev4XE_Fa_WkO9zqS3Gi7EQRvXSs/edit#gid=0

[https://docs.google.com/spreadsheets/d/16EKfi4TtOe4e2quNev4XE_Fa_WkO9zqS3Gi7EQRvXSs/edit#gid=0](https://docs.google.com/spreadsheets/d/16EKfi4TtOe4e2quNev4XE_Fa_WkO9zqS3Gi7EQRvXSs/edit#gid=0)

Binned by FF rather than eff because I think the FF is more reliable than the eff values (solar meter variance?)

Binning because MPPT is current limited by the worst module.

* Binned in order of best to worst:D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* Binned in order of best to worst:D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun

* Binned in order of best to worst:D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun

Binned in order of best to worst:

* D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun
* tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun

D8 --> D7 --> C6 --> C5 or B4 --> A2 --> B3 --> A1

* tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun

tail is most normal to sun, B3 gets shading first and is split around bubble, A1 is curviest and least normal to sun

References

Module Area

* 24x1 --> 0.02077 m^2 -- 415.4mm x 50mm24x2 --> 0.041748 m^2 -- 415.4mm x 100.5mm
* 24x2 --> 0.041748 m^2 -- 415.4mm x 100.5mm
* 24x3 --> 0.06273 m^2 -- 415.4mm x 151.0 mm24x4 --> 0.0837 m^2  -- 415.4mm x 201.5mm
* 24x4 --> 0.0837 m^2  -- 415.4mm x 201.5mm

24x1 --> 0.02077 m^2 -- 415.4mm x 50mm

* 24x2 --> 0.041748 m^2 -- 415.4mm x 100.5mm

24x2 --> 0.041748 m^2 -- 415.4mm x 100.5mm

24x3 --> 0.06273 m^2 -- 415.4mm x 151.0 mm

* 24x4 --> 0.0837 m^2  -- 415.4mm x 201.5mm

24x4 --> 0.0837 m^2  -- 415.4mm x 201.5mm

 These sizes are WITHOUT diodes (as they would be under the deck) and without a laminate border. This is just the size of the cells themselves. So you should build in a bit of a border on all sides when doing your calculations, likely about 1-2mm for each (so 2-4mm between modules).

 

* 24x4415.4mm x 201.5mm29x1500.9mm x 50mm24x1415.4mm x 50mm20x1347mm x 50mm12x1210.2mm x 50mm
* 24x4415.4mm x 201.5mm
* 415.4mm x 201.5mm
* 415.4mm x 201.5mm
* 29x1500.9mm x 50mm
* 500.9mm x 50mm
* 500.9mm x 50mm
* 24x1415.4mm x 50mm
* 415.4mm x 50mm
* 415.4mm x 50mm
* 20x1347mm x 50mm
* 347mm x 50mm
* 347mm x 50mm
* 12x1210.2mm x 50mm
* 210.2mm x 50mm
* 210.2mm x 50mm

* 24x4415.4mm x 201.5mm
* 415.4mm x 201.5mm
* 415.4mm x 201.5mm
* 29x1500.9mm x 50mm
* 500.9mm x 50mm
* 500.9mm x 50mm
* 24x1415.4mm x 50mm
* 415.4mm x 50mm
* 415.4mm x 50mm
* 20x1347mm x 50mm
* 347mm x 50mm
* 347mm x 50mm
* 12x1210.2mm x 50mm
* 210.2mm x 50mm
* 210.2mm x 50mm

24x4

* 415.4mm x 201.5mm
* 415.4mm x 201.5mm

* 415.4mm x 201.5mm

415.4mm x 201.5mm

29x1

* 500.9mm x 50mm
* 500.9mm x 50mm

* 500.9mm x 50mm

500.9mm x 50mm

24x1

* 415.4mm x 50mm
* 415.4mm x 50mm

* 415.4mm x 50mm

415.4mm x 50mm

20x1

* 347mm x 50mm
* 347mm x 50mm

* 347mm x 50mm

347mm x 50mm

12x1

* 210.2mm x 50mm
* 210.2mm x 50mm

* 210.2mm x 50mm

210.2mm x 50mm

