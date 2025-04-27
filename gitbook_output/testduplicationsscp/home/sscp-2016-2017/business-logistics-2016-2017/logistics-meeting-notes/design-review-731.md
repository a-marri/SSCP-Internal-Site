# design-review-731

## SSCP - Design Review 7/31

## Design Review 7/31

#### Embedded Content

Embedded content: [Embedded Content](design-review-731.md)

![](../../../../../assets/slides_32dp.png)

Hayden's Notes:

#### Embedded Content

Embedded content: [Embedded Content](design-review-731.md)

![](../../../../../assets/docs_32dp.png)

Kelsey's Notes:

* ArrayBacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatchGaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workabilityTopsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testingCurrent plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affectsTextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different texturesGochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* BacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatchGaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workabilityTopsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testingCurrent plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affectsTextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different texturesGochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* BacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatch
* Testing reflectance
* Golshan: have we characterized thermal performance of backsheets?
* Wesley: should test flatness/performance with an actual cell and in a larger size, not just individual
* NHS: the curling we have may not be fully indicative of mismatch
* GaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?
* Trade off number -- fairly simplistic -- is 27.3%
* GaAs degrades, harder to get
* Hardest part is procuring
* Nathan Golshan: can we do some mix of the two?
* Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?
* Want something that won't get dirty and need too much cooling
* Microstructures get destroyed by wiping, so if we went that way we couldn't do that anyway
* Electrostatically remove dust? Compressed air?
* Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workability
* Updated version of STR EVA (what we wanted to use last year)
* Testing a lot of potential encapsulants for performance and workability
* Topsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* 3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* Current plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Seeking advice: how best to compare all of these?
* Don't care about absolute -- just relative (solves the problem with the flash tester)
* Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cells
* We can compare to Gochermann but not Chuzel
* We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone
* We think Gochermann uses a stamp method (based on what it looks like)
* Rumors say that Chuzel uses the texture of SunPower cells
* Wesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?
* Should do a curvature test?
* Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Aero gains, voltage affects
* TextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different textures
* We've tried large scale, outside companies, or nanofab on campus
* Need to create and test a bunch of different textures
* Gochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)
* Need to be ready to make that call
* Bypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/useful
* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful
* Harry: did active bypass for Arctan at an array level -- kind of nice
* NHS: diodes can cause bubbling in the array (heating)
* Gist: not necessarily a bad idea, but require testing

Array

* BacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatchGaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workabilityTopsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testingCurrent plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affectsTextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different texturesGochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* BacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatch
* Testing reflectance
* Golshan: have we characterized thermal performance of backsheets?
* Wesley: should test flatness/performance with an actual cell and in a larger size, not just individual
* NHS: the curling we have may not be fully indicative of mismatch
* GaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?
* Trade off number -- fairly simplistic -- is 27.3%
* GaAs degrades, harder to get
* Hardest part is procuring
* Nathan Golshan: can we do some mix of the two?
* Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?
* Want something that won't get dirty and need too much cooling
* Microstructures get destroyed by wiping, so if we went that way we couldn't do that anyway
* Electrostatically remove dust? Compressed air?
* Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workability
* Updated version of STR EVA (what we wanted to use last year)
* Testing a lot of potential encapsulants for performance and workability
* Topsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* 3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* Current plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Seeking advice: how best to compare all of these?
* Don't care about absolute -- just relative (solves the problem with the flash tester)
* Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cells
* We can compare to Gochermann but not Chuzel
* We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone
* We think Gochermann uses a stamp method (based on what it looks like)
* Rumors say that Chuzel uses the texture of SunPower cells
* Wesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?
* Should do a curvature test?
* Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Aero gains, voltage affects
* TextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different textures
* We've tried large scale, outside companies, or nanofab on campus
* Need to create and test a bunch of different textures
* Gochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)
* Need to be ready to make that call
* Bypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/useful
* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful
* Harry: did active bypass for Arctan at an array level -- kind of nice
* NHS: diodes can cause bubbling in the array (heating)
* Gist: not necessarily a bad idea, but require testing
* BacksheetTesting reflectanceGolshan: have we characterized thermal performance of backsheets?Wesley: should test flatness/performance with an actual cell and in a larger size, not just individualNHS: the curling we have may not be fully indicative of mismatch
* Testing reflectance
* Golshan: have we characterized thermal performance of backsheets?
* Wesley: should test flatness/performance with an actual cell and in a larger size, not just individual
* NHS: the curling we have may not be fully indicative of mismatch
* GaAs vs SiTrade off number -- fairly simplistic -- is 27.3%GaAs degrades, harder to getHardest part is procuringNathan Golshan: can we do some mix of the two?
* Trade off number -- fairly simplistic -- is 27.3%
* GaAs degrades, harder to get
* Hardest part is procuring
* Nathan Golshan: can we do some mix of the two?
* Rule changes: cannot spray during control stopsWant something that won't get dirty and need too much coolingMicrostructures get destroyed by wiping, so if we went that way we couldn't do that anywayElectrostatically remove dust? Compressed air?
* Want something that won't get dirty and need too much cooling
* Microstructures get destroyed by wiping, so if we went that way we couldn't do that anyway
* Electrostatically remove dust? Compressed air?
* Encapsulant:Updated version of STR EVA (what we wanted to use last year)Testing a lot of potential encapsulants for performance and workability
* Updated version of STR EVA (what we wanted to use last year)
* Testing a lot of potential encapsulants for performance and workability
* Topsheet:3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* 3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing
* Current plan: test all of the permutationsSeeking advice: how best to compare all of these?Don't care about absolute -- just relative (solves the problem with the flash tester)Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cellsWesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Seeking advice: how best to compare all of these?
* Don't care about absolute -- just relative (solves the problem with the flash tester)
* Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cells
* We can compare to Gochermann but not Chuzel
* We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone
* We think Gochermann uses a stamp method (based on what it looks like)
* Rumors say that Chuzel uses the texture of SunPower cells
* Wesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?
* Should do a curvature test?
* Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Aero gains, voltage affects
* TextureWe've tried large scale, outside companies, or nanofab on campusNeed to create and test a bunch of different textures
* We've tried large scale, outside companies, or nanofab on campus
* Need to create and test a bunch of different textures
* Gochermann:Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)Need to be ready to make that callBypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)
* Need to be ready to make that call
* Bypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/useful
* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful
* Harry: did active bypass for Arctan at an array level -- kind of nice
* NHS: diodes can cause bubbling in the array (heating)
* Gist: not necessarily a bad idea, but require testing

Backsheet

* Testing reflectance
* Golshan: have we characterized thermal performance of backsheets?
* Wesley: should test flatness/performance with an actual cell and in a larger size, not just individual
* NHS: the curling we have may not be fully indicative of mismatch

Testing reflectance

Golshan: have we characterized thermal performance of backsheets?

Wesley: should test flatness/performance with an actual cell and in a larger size, not just individual

NHS: the curling we have may not be fully indicative of mismatch

GaAs vs Si

* Trade off number -- fairly simplistic -- is 27.3%
* GaAs degrades, harder to get
* Hardest part is procuring
* Nathan Golshan: can we do some mix of the two?

Trade off number -- fairly simplistic -- is 27.3%

GaAs degrades, harder to get

Hardest part is procuring

Nathan Golshan: can we do some mix of the two?

Rule changes: cannot spray during control stops

* Want something that won't get dirty and need too much cooling
* Microstructures get destroyed by wiping, so if we went that way we couldn't do that anyway
* Electrostatically remove dust? Compressed air?

Want something that won't get dirty and need too much cooling

Microstructures get destroyed by wiping, so if we went that way we couldn't do that anyway

Electrostatically remove dust? Compressed air?

Encapsulant:

* Updated version of STR EVA (what we wanted to use last year)
* Testing a lot of potential encapsulants for performance and workability

Updated version of STR EVA (what we wanted to use last year)

Testing a lot of potential encapsulants for performance and workability

Topsheet:

* 3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing

3M ribbed (unidirectional texture), very thin non-surface-treated FEP for texture testing

Current plan: test all of the permutations

* Seeking advice: how best to compare all of these?
* Don't care about absolute -- just relative (solves the problem with the flash tester)
* Darren: how does this compare to Chuzel and Gochermann?We can compare to Gochermann but not ChuzelWe know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly siliconeWe think Gochermann uses a stamp method (based on what it looks like)Rumors say that Chuzel uses the texture of SunPower cells
* We can compare to Gochermann but not Chuzel
* We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone
* We think Gochermann uses a stamp method (based on what it looks like)
* Rumors say that Chuzel uses the texture of SunPower cells
* Wesley: should think about bonding the array/manufacturability early and oftenShould do a curvature test?
* Should do a curvature test?
* Sasha: dicing -- consider system-level affectsAero gains, voltage affects
* Aero gains, voltage affects

Seeking advice: how best to compare all of these?

Don't care about absolute -- just relative (solves the problem with the flash tester)

Darren: how does this compare to Chuzel and Gochermann?

* We can compare to Gochermann but not Chuzel
* We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone
* We think Gochermann uses a stamp method (based on what it looks like)
* Rumors say that Chuzel uses the texture of SunPower cells

We can compare to Gochermann but not Chuzel

We know that Chuzel uses Avery Denison retroreflective film, very thin, probably mostly silicone

We think Gochermann uses a stamp method (based on what it looks like)

Rumors say that Chuzel uses the texture of SunPower cells

Wesley: should think about bonding the array/manufacturability early and often

* Should do a curvature test?

Should do a curvature test?

Sasha: dicing -- consider system-level affects

* Aero gains, voltage affects

Aero gains, voltage affects

Texture

* We've tried large scale, outside companies, or nanofab on campus
* Need to create and test a bunch of different textures

We've tried large scale, outside companies, or nanofab on campus

Need to create and test a bunch of different textures

Gochermann:

* Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)
* Need to be ready to make that call
* Bypass diodes?Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/usefulHarry: did active bypass for Arctan at an array level -- kind of niceNHS: diodes can cause bubbling in the array (heating)Gist: not necessarily a bad idea, but require testing
* Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/useful
* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful
* Harry: did active bypass for Arctan at an array level -- kind of nice
* NHS: diodes can cause bubbling in the array (heating)
* Gist: not necessarily a bad idea, but require testing

Wesley: don't trust a vendor that says a few months will be fine for something custom (think 6 months)

Need to be ready to make that call

Bypass diodes?

* Sasha: less relevant than they used to be(SunPower is very careful to engineer around this)May gain benefit with module or string, but not cellXenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessaryLatency of active bypass means probably not necessary/useful
* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful
* Harry: did active bypass for Arctan at an array level -- kind of nice
* NHS: diodes can cause bubbling in the array (heating)
* Gist: not necessarily a bad idea, but require testing

Sasha: less relevant than they used to be

* (SunPower is very careful to engineer around this)
* May gain benefit with module or string, but not cell
* Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)Don't assume that it'll workLots of testing necessary
* Don't assume that it'll work
* Lots of testing necessary
* Latency of active bypass means probably not necessary/useful

(SunPower is very careful to engineer around this)

May gain benefit with module or string, but not cell

Xenith almost succeeded at this -- but coating was wrong (led to debonding between soldering and lamination)

* Don't assume that it'll work
* Lots of testing necessary

Don't assume that it'll work

Lots of testing necessary

Latency of active bypass means probably not necessary/useful

Harry: did active bypass for Arctan at an array level -- kind of nice

NHS: diodes can cause bubbling in the array (heating)

Gist: not necessarily a bad idea, but require testing

* AeroSolidWorks -> Pointwise -> Tecplot (may switch to Fluent)Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirmNew rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb nowGeneral:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performanceAsking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the carGolshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or splitSuspensionDarren: trailing in the rear might be fineNHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inchesDarren: front should be A-armSame suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shouldersToe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = noneMotorsMarand = new motors that bolt into the wheel with no necessary constructionShould look into this -- could get away with one motor, need to buy more than oneTODO: contact Marand
* AeroSolidWorks -> Pointwise -> Tecplot (may switch to Fluent)Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirmNew rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb nowGeneral:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performanceAsking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the carGolshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or split
* SolidWorks -> Pointwise -> Tecplot (may switch to Fluent)
* Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* Want to back track from mesh and compare
* Anna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* New rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman
* Hayden researching smaller helmets
* Book: The Measurements of Man and Woman
* 2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Wesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycle
* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle
* Golshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...
* Nuon won't be following the rules 100%...
* Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?
* Should start looking for 50mm aluminum honeycomb now
* General:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* CP and CG farther apart -- bigger yaw
* Wesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues
* Golshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or not
* Crosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* At what point are the numbers not ok?
* Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)
* Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary
* Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* Adams/car softwarePublished for FSAE
* Published for FSAE
* Darren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* As a team, need to decide what the priorities are
* Luminos vs Arctan -- very different handling and performance
* Asking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the car
* Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)
* What is the surface area?
* Vortices can be optimized out of pretty much any design
* Straight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)
* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)
* Long = better in cross winds
* Pointy nose? Geometrically not possible in the past (array vs bounding box)
* Nuon does fancy stuff with the underside of the car
* Golshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or split
* Reasons to avoid are legitimate, but don't want to shoot ourselves in the foot
* Thinks asymmetrical has much more potential for optimization
* Look at Aurum, Nuna 8 -- lots of interesting ways to make this happen
* Side area is not a direct proxy for cross wind performance
* Asymmetrical fairings: skinny or split
* SuspensionDarren: trailing in the rear might be fineNHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inchesDarren: front should be A-armSame suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shouldersToe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = none
* Darren: trailing in the rear might be fine
* NHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inches
* Regardless not a ton longer -- 1-3 inches
* Darren: front should be A-arm
* Same suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shoulders
* Darren: could probably get away with a little less
* Wheel is  driving the array height
* NHS: put large fillets for the driver shoulders
* Toe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = none
* One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the opposite
* Luminos = small amount of toe, Arctan = none
* MotorsMarand = new motors that bolt into the wheel with no necessary constructionShould look into this -- could get away with one motor, need to buy more than oneTODO: contact Marand
* Marand = new motors that bolt into the wheel with no necessary construction
* Should look into this -- could get away with one motor, need to buy more than one
* TODO: contact Marand
* AeroSolidWorks -> Pointwise -> Tecplot (may switch to Fluent)Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirmNew rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb nowGeneral:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performanceAsking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the carGolshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or split
* SolidWorks -> Pointwise -> Tecplot (may switch to Fluent)
* Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* Want to back track from mesh and compare
* Anna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* New rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman
* Hayden researching smaller helmets
* Book: The Measurements of Man and Woman
* 2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Wesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycle
* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle
* Golshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...
* Nuon won't be following the rules 100%...
* Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?
* Should start looking for 50mm aluminum honeycomb now
* General:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* CP and CG farther apart -- bigger yaw
* Wesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues
* Golshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or not
* Crosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* At what point are the numbers not ok?
* Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)
* Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary
* Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* Adams/car softwarePublished for FSAE
* Published for FSAE
* Darren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* As a team, need to decide what the priorities are
* Luminos vs Arctan -- very different handling and performance
* Asking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the car
* Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)
* What is the surface area?
* Vortices can be optimized out of pretty much any design
* Straight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)
* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)
* Long = better in cross winds
* Pointy nose? Geometrically not possible in the past (array vs bounding box)
* Nuon does fancy stuff with the underside of the car
* Golshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or split
* Reasons to avoid are legitimate, but don't want to shoot ourselves in the foot
* Thinks asymmetrical has much more potential for optimization
* Look at Aurum, Nuna 8 -- lots of interesting ways to make this happen
* Side area is not a direct proxy for cross wind performance
* Asymmetrical fairings: skinny or split
* SuspensionDarren: trailing in the rear might be fineNHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inchesDarren: front should be A-armSame suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shouldersToe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = none
* Darren: trailing in the rear might be fine
* NHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inches
* Regardless not a ton longer -- 1-3 inches
* Darren: front should be A-arm
* Same suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shoulders
* Darren: could probably get away with a little less
* Wheel is  driving the array height
* NHS: put large fillets for the driver shoulders
* Toe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = none
* One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the opposite
* Luminos = small amount of toe, Arctan = none
* MotorsMarand = new motors that bolt into the wheel with no necessary constructionShould look into this -- could get away with one motor, need to buy more than oneTODO: contact Marand
* Marand = new motors that bolt into the wheel with no necessary construction
* Should look into this -- could get away with one motor, need to buy more than one
* TODO: contact Marand

Aero

* SolidWorks -> Pointwise -> Tecplot (may switch to Fluent)
* Plan is to do a lot more automatic deformation stuffWant to back track from mesh and compareAnna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* Want to back track from mesh and compare
* Anna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm
* New rules:Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman
* Hayden researching smaller helmets
* Book: The Measurements of Man and Woman
* 2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Wesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycle
* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle
* Golshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...
* Nuon won't be following the rules 100%...
* Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?
* Should start looking for 50mm aluminum honeycomb now
* General:Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issuesGolshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or notCrosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)Adams/car softwarePublished for FSAEDarren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* CP and CG farther apart -- bigger yaw
* Wesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues
* Golshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or not
* Crosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* At what point are the numbers not ok?
* Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)
* Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary
* Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* Adams/car softwarePublished for FSAE
* Published for FSAE
* Darren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* As a team, need to decide what the priorities are
* Luminos vs Arctan -- very different handling and performance
* Asking for advice: how can we make the lines look better (no vortices)?Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)Nuon does fancy stuff with the underside of the car
* Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)
* What is the surface area?
* Vortices can be optimized out of pretty much any design
* Straight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)
* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)
* Long = better in cross winds
* Pointy nose? Geometrically not possible in the past (array vs bounding box)
* Nuon does fancy stuff with the underside of the car
* Golshan: should do more asymmetricalReasons to avoid are legitimate, but don't want to shoot ourselves in the footThinks asymmetrical has much more potential for optimizationLook at Aurum, Nuna 8 -- lots of interesting ways to make this happenSide area is not a direct proxy for cross wind performanceAsymmetrical fairings: skinny or split
* Reasons to avoid are legitimate, but don't want to shoot ourselves in the foot
* Thinks asymmetrical has much more potential for optimization
* Look at Aurum, Nuna 8 -- lots of interesting ways to make this happen
* Side area is not a direct proxy for cross wind performance
* Asymmetrical fairings: skinny or split

SolidWorks -> Pointwise -> Tecplot (may switch to Fluent)

Plan is to do a lot more automatic deformation stuff

* Want to back track from mesh and compare
* Anna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm

Want to back track from mesh and compare

Anna O and Max P thought this didn't work last time; Darren thinks it worked -- should confirm

New rules:

* Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessaryHayden researching smaller helmetsBook: The Measurements of Man and Woman
* Hayden researching smaller helmets
* Book: The Measurements of Man and Woman
* 2" on either side of the driverWesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycleGolshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?Should start looking for 50mm aluminum honeycomb now
* Wesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycle
* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle
* Golshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...
* Nuon won't be following the rules 100%...
* Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?
* Should start looking for 50mm aluminum honeycomb now

Occupant's helmet 50mm from the bubble--probably a bigger bubble will be necessary

* Hayden researching smaller helmets
* Book: The Measurements of Man and Woman

Hayden researching smaller helmets

Book: The Measurements of Man and Woman

2" on either side of the driver

* Wesley: have we chosen a driver yet?Should probably at least find potential peopleLast cycle drivers didn't show up until later in the cycle
* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle
* Golshan: unless we're being ridiculous, we can probably find a way to make things fixNuon won't be following the rules 100%...
* Nuon won't be following the rules 100%...
* Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?
* Should start looking for 50mm aluminum honeycomb now

Wesley: have we chosen a driver yet?

* Should probably at least find potential people
* Last cycle drivers didn't show up until later in the cycle

Should probably at least find potential people

Last cycle drivers didn't show up until later in the cycle

Golshan: unless we're being ridiculous, we can probably find a way to make things fix

* Nuon won't be following the rules 100%...

Nuon won't be following the rules 100%...

Could we use aluminum honeycomb as part of the energy absorbing material? Can we integrate the foam into the layup?

Should start looking for 50mm aluminum honeycomb now

General:

* Longer noseCP and CG farther apart -- bigger yawWesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* CP and CG farther apart -- bigger yaw
* Wesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues
* Golshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or not
* Crosswinds/yawAt what point are the numbers not ok?Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessaryAiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* At what point are the numbers not ok?
* Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)
* Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary
* Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)
* Adams/car softwarePublished for FSAE
* Published for FSAE
* Darren:As a team, need to decide what the priorities areLuminos vs Arctan -- very different handling and performance
* As a team, need to decide what the priorities are
* Luminos vs Arctan -- very different handling and performance

Longer nose

* CP and CG farther apart -- bigger yaw
* Wesley: Does a longer wheelbase help?Rachel: focus on ratio of wheelbase/track widthIdea is smaller fairings = less side wind issues
* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues

CP and CG farther apart -- bigger yaw

Wesley: Does a longer wheelbase help?

* Rachel: focus on ratio of wheelbase/track width
* Idea is smaller fairings = less side wind issues

Rachel: focus on ratio of wheelbase/track width

Idea is smaller fairings = less side wind issues

Golshan: do we have a comparison of Arctan's driver fairing width to what would be required here? Could affect whether we'd do a catamaran or not

Crosswinds/yaw

* At what point are the numbers not ok?
* Should we care about tire data?Darren: whyGolshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)
* Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary
* Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)

At what point are the numbers not ok?

Should we care about tire data?

* Darren: why
* Golshan/Rachel: existing simulations require thisWe can run Arctan and compare (have to)
* We can run Arctan and compare (have to)

Darren: why

Golshan/Rachel: existing simulations require this

* We can run Arctan and compare (have to)

We can run Arctan and compare (have to)

Gerdes pointed out that there's some nonintuitive counter steer behavior that's necessary

Aiming for similar or better ratio of drag to sidewinds as Arctan had (Golshan: seems reasonable)

Adams/car software

* Published for FSAE

Published for FSAE

Darren:

* As a team, need to decide what the priorities are
* Luminos vs Arctan -- very different handling and performance

As a team, need to decide what the priorities are

Luminos vs Arctan -- very different handling and performance

Asking for advice: how can we make the lines look better (no vortices)?

* Architectural stuff may be more useful nowWhat is the surface area?Vortices can be optimized out of pretty much any designStraight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)Long = better in cross windsPointy nose? Geometrically not possible in the past (array vs bounding box)
* What is the surface area?
* Vortices can be optimized out of pretty much any design
* Straight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)
* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)
* Long = better in cross winds
* Pointy nose? Geometrically not possible in the past (array vs bounding box)
* Nuon does fancy stuff with the underside of the car

Architectural stuff may be more useful now

* What is the surface area?
* Vortices can be optimized out of pretty much any design
* Straight lines are badPurpose of an airfoil is a prolonged drop in air pressure(One inflection point, with varying gradients)
* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)
* Long = better in cross winds
* Pointy nose? Geometrically not possible in the past (array vs bounding box)

What is the surface area?

Vortices can be optimized out of pretty much any design

Straight lines are bad

* Purpose of an airfoil is a prolonged drop in air pressure
* (One inflection point, with varying gradients)

Purpose of an airfoil is a prolonged drop in air pressure

(One inflection point, with varying gradients)

Long = better in cross winds

Pointy nose? Geometrically not possible in the past (array vs bounding box)

Nuon does fancy stuff with the underside of the car

Golshan: should do more asymmetrical

* Reasons to avoid are legitimate, but don't want to shoot ourselves in the foot
* Thinks asymmetrical has much more potential for optimization
* Look at Aurum, Nuna 8 -- lots of interesting ways to make this happen
* Side area is not a direct proxy for cross wind performance
* Asymmetrical fairings: skinny or split

Reasons to avoid are legitimate, but don't want to shoot ourselves in the foot

Thinks asymmetrical has much more potential for optimization

Look at Aurum, Nuna 8 -- lots of interesting ways to make this happen

Side area is not a direct proxy for cross wind performance

Asymmetrical fairings: skinny or split

Suspension

* Darren: trailing in the rear might be fine
* NHS: there are hacky ways to avoid the lengthening effects (may not be advised)Regardless not a ton longer -- 1-3 inches
* Regardless not a ton longer -- 1-3 inches
* Darren: front should be A-arm
* Same suspension travel as ArctanDarren: could probably get away with a little lessWheel is  driving the array heightNHS: put large fillets for the driver shoulders
* Darren: could probably get away with a little less
* Wheel is  driving the array height
* NHS: put large fillets for the driver shoulders
* Toe or not?One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the oppositeLuminos = small amount of toe, Arctan = none
* One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the opposite
* Luminos = small amount of toe, Arctan = none

Darren: trailing in the rear might be fine

NHS: there are hacky ways to avoid the lengthening effects (may not be advised)

* Regardless not a ton longer -- 1-3 inches

Regardless not a ton longer -- 1-3 inches

Darren: front should be A-arm

Same suspension travel as Arctan

* Darren: could probably get away with a little less
* Wheel is  driving the array height
* NHS: put large fillets for the driver shoulders

Darren: could probably get away with a little less

Wheel is  driving the array height

NHS: put large fillets for the driver shoulders

Toe or not?

* One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the opposite
* Luminos = small amount of toe, Arctan = none

One paper says toe is worse than scrubbing the tires when driving, Rachel's boss says the opposite

Luminos = small amount of toe, Arctan = none

Motors

* Marand = new motors that bolt into the wheel with no necessary construction
* Should look into this -- could get away with one motor, need to buy more than one
* TODO: contact Marand

Marand = new motors that bolt into the wheel with no necessary construction

Should look into this -- could get away with one motor, need to buy more than one

TODO: contact Marand
