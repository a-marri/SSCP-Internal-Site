# SSCP - Hardpoint Design

# Hardpoint Design

![](../../../../../assets/image_449ce19206.png)

We need to make sure our new hardpoints can take approximately twice the loads seen on the Luminos hardpoints. 

Loading Conditions

See attached doc and photo of hardpoint numbering.

Upper Hardpoint

upper front hardpoint (hardpoint 4)

-6328N FX

-8277 FY

-2610FZ

Loads were applied by taking the magnitude of this maximum force and drawing it along a unit direction vector. Loads were applied to the inside of the bolt holes, and the maximum load was divided by two to give a conservative estimate of the double-shear loading condition, even though the force wouldn't be split exactly in two given that the inner hole surfaces do not have the same area. This methodology is WRONG, and the bolt loading conditions should be used instead. 

Luminos hardpoints shown below with new loading. These still pass FEA as of Jan 17 2014. Hardpoint checked into PDM/Sunwhale Repository/Sunwhale Suspension/Sunwhale Upper Hardpoint A1. The hardpoint shown is the front upper hardpoint on the left side. 

HARDPOINT SIMULATION SHOWN ABOVE is WRONG. 

FEA Analysis with Load Direction Reversed

This simulation is RIGHT. 

Lower Hardpoint

lower front hardpoint (hardpoint 1)

14,080N FX longitudinal direction towards back of the car 

13,631N FY lateral outboard

3,630N   FZ upwards

Magnitude of force is 19,931N split in two because of the two inner bolt hole surfaces (bolt in double-shear). 

Luminos lower hardpoint shown below with new loading. These do not pass FEA, unmodified, as of Jan 17 2014. 

![](../../../../../assets/image_0a3180501f.png)

![](../../../../../assets/image_0de31b86ab.png)

Thickening the main folded body and centering the rodend cutout so that it still measures 0.60" but the thin hinge has greater thickness. 

![](../../../../../assets/image_ce06997cc2.png)

Rear end. The reddest sections of the FEA are the rear faces of the insert. I don't know why this is the case but the piece will not fail there. 

![](../../../../../assets/image_281d91105f.png)

With corrected loading orientation, the new FEA for the lower hardpoint looks like this. Minimum factor of safety is 1.7, and 1.6 at the minimum if I reduce the thickness of the part. 

![](../../../../../assets/image_06ba73d769.png)

Lower Hardpoint Sunwhale

New lower hardpoint design for Sunwhale accounts for tight tolerance below rodends. There are two versions of the loewr hardpoint, with the rodend hole placed in slightly different positions. See FEA images below and placement chart for Lower Hardpoints 1 and 2. 

![](../../../../../assets/image_27b0b96409.png)

![](../../../../../assets/image_00fa82bfac.png)

![](../../../../../assets/image_1bffbdffab.png)

FEA Analysis with Loading Reversed (Passes minimum 2.2 FOS, ignoring global contact condition red zones)

![](../../../../../assets/image_00405b8c42.png)

Lower Hardpoint Placement

![](../../../../../assets/image_2617df4077.jpg)

Hardpoints can be Found in PDM

Sunwhale Repository/Sunwhale Suspension/Sunwhale Suspension Hardpoints

 

[](https://drive.google.com/folderview?id=1FsfRWZbqTORuheoErAHm1YBUne3OqW5F)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1FsfRWZbqTORuheoErAHm1YBUne3OqW5F#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1FsfRWZbqTORuheoErAHm1YBUne3OqW5F#list" frameborder="0"></iframe>

