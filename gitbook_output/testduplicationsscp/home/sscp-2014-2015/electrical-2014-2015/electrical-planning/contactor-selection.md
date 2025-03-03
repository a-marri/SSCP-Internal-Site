# SSCP - Contactor Selection

# Contactor Selection

I chose to evaluate two contactors to start with, the EV200 from Tyco/Kilovac (our choice for many years past), the EV100, also from Tyco/Kilovac, and the Minitactor P105 from Gigavac. Datasheets for each are attached to this page.

## Assumed Conditions:

[](#h.a8g09euyehm3)

Worst-case current draw from the battery pack is 4000W @ lowest battery voltage (27* 2.5V) = 59.26A

Probable best-case (in terms of power creation) but worst-case in terms of contactor power dissipation from the array is ~2500W @ (27*2.5V) = 37.04A 

## EV200:

[](#h.1xrm1mc147i3)

Holding Current: 0.07A @ 24V, 0.03A @ 48V 

Continuous Carry Current rating slightly harder to factor, but smallest number I see is 325A, well above our usage case.

Max Contact Resistance (@200A listed): 0.4mR

Weight: 430g

LxWxH: 3.17” x 2.58” x 2.85”

 

## EV100:

[](#h.drjilrv9znmz)

Holding Current: 0.15A @ 24VDC (with built-in economizer)

Continuous Current Rating: 100A.

Max Contact Resistance: 0.5mR

Weight: 130g

LxWxH: 2.12" x 1.56" x 1.78"

## Minitactor P105:

[](#h.qcwzcmdb7bh8)

Holding current: 0.085A @ 24V, 0.045A @ 48V

Current Carry Rating graph on page 1 of datasheet shows time limit of 300 seconds (5 minutes) at the worst-case current draw for battery pack. The 37A is less than the 50A rated value, and as such is solidly in the huge lifespan range.  

Contact Resistance (@50A listed): 2mR.

Weight: 100g

LxWxH: 3.1” x 1.19” x 1.81”

## Conclusion:

[](#h.pnxm6q207dqv)

Inside the battery pack the EV200 must be used as it is the only one of the two that can support continuous draw of our worst-case scenario. For the MPPT box the minitactor or EV100 may be used if the size and mounting requirements of the EV200 are unacceptable, however, the EV200 is still preferred due to its lower coil power and lower contact resistance. 

[](https://drive.google.com/folderview?id=189mSGCdBDS7qfiy7-Siljv7Qkr8BI3vm)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=189mSGCdBDS7qfiy7-Siljv7Qkr8BI3vm#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=189mSGCdBDS7qfiy7-Siljv7Qkr8BI3vm#list" frameborder="0"></iframe>

