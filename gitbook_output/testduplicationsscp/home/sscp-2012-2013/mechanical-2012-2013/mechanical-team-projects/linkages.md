# linkages

## SSCP - Linkages

## Linkages

### Surface Prep

&#x20;   Ideal: Phosphoric Acid Anodize

&#x20;       ANODIZE PER AMS-A-8625

&#x20;       TYPE I, CLASS 1 (recommended by tye). No further preparation required after this.

&#x20;   Exploring: Theoretical 3M Coating

&#x20;       3M AC-130 Spray/film

&#x20;   Less Ideal:

&#x20;       West Aluminum Etch: http://www.pbsboatstore.com/860-aluminum-etch-kit.htm

### Fitment Check

![](../../../../../assets/image_c41f6b52af.png)

### FEA

#### Mesh

Mesh element size is about 1.1mm with a mesh control applied to the inner ace to make it a smaller .55mm.&#x20;

![](../../../../../assets/image_dd0f56dfa2.png)

#### FEA Setup

![](../../../../../assets/image_478b9268ba.png)

Load

The purple line shows the applied maximum of 6800N of force which was found from the suspension load .txt file that was simulated by shark.&#x20;

Bearing Contact Set

The inner and outer race of the bearing were joined with a rigid connection in this analysis.&#x20;

Bearing Linkage Interface

The bearing linkage interface was simulated as a bearing connection. It is not sufficent to fix the inside surface of the bearing as in tension the lower part will pull away as can be seen in the deformed result

#### Results

Factor of Safety&#x20;

![](../../../../../assets/image_08072611c6.png)

From the the image you can see that all areas of factor of safety below about 2.5 are due to mesh issues and therefore the factor of safety of this part is at least 2.5.

#### Stress & Deformed Result

![](../../../../../assets/image_d05853c08b.png)

The deformed result shows that the bearing contact set worked as we would like.&#x20;

#### Design Insight

![](../../../../../assets/image_e60de98fdb.png)

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1BVPJGqjzPIA0qNHCI3pzD_91-CCAQe2-#list)
