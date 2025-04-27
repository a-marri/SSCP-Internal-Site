# catamaran-fairing-distance-and-split

## SSCP - Catamaran Fairing Distance and Split

## Catamaran Fairing Distance and Split

These are based on the more successful Cambered Catamarans for body shape.

[Cambered Catamarans](../../../../../../stanford.edu/testduplicationsscp/home/sscp-2014-2015/aero-2014-2015/solidworks-flowsim-quick-simulations/cambered-catamarans/)

For each variation series, main foil shape is constant and different fairing configurations are varied.

45180 means that the car is 4.5meters long and 180cm wide.

camber 2 means it has the camber corresponding to coefficient of lift = .2 in Javafoil

thick3 means it has thickness of 3 (approx 3.6% for the Thickness t/c parameter in Javafoil)

These parameters integrated correspond to what the NACA name for the foil is, so NACA 64A-203 would be camber 2, thickness 3

The X component is drag, and Z component is lift (negative is downforce)

Drag value is highlighted in table.   &#x20;

Fairing Distance from Leading Edge

Directory: FairingPositionAug4

Sample name: Sunwhale-003-45180-camber5-thick3-front2&#x20;

front2 corresponds with fairing start 0.2m from leading edge

This series is uses the same main foil and fairings as Sunwhale-002-45180-camber5-thick3-shortfairing-16series

&#x20;   mainfoil = NACA64A-503

&#x20;   driver fairing = NACA 16-215

&#x20;   passenger fairing = NACA 16-211

Fairings are 3.38m long

Model: Sunwhale-003-45180-camber5-thick3-front2

Fairing Size on 2-Fairing Car

Directory: FairingSizeAug1

Sample name: Sunwhale-005-45180-camber3-thick6-fairing338

fairing338 corresponds to fairings of 3.38m length

This series is based on the main foil and fairings of Sunwhale-002-45180-camber5-thick3-shortfairing-16series, but with the following modifications:

&#x20;   \- thicker main foil (thickness 6) to reflect more realistic sizing in accommodating suspension etc.

&#x20;   \- non-cambered fairing foils

&#x20;   \- identical driver and passenger fairings

&#x20;   \- fairings are extruded 0.44m (instead of previously 0.54m)

&#x20;   mainfoil = NACA64A-306

&#x20;   driver fairing = NACA 16-011

&#x20;   passenger fairing = same as driver fairing

When changing length, fairings are placed a reasonable distance from the leading edge in order to maintain a sensible wheelbase. (e.g. 0.3m for a longer fairing, 0.5m for a shorter fairing) This results in a fairing relatively centered between the leading and trailing edges of the car.

When changing length, the foil is generally the same coordinates from Javafoil, but scaled up to length in excel--provided that the fairing does not become too wide or narrow.

Model: Sunwhale-005-45180-camber3-thick6-fairing28

&#x20;         Fairing size: 2.8m&#x20;

&#x20;       Distance from leading edge: 0.7m

![](../../../../../assets/image_71468f799f.png)

![](../../../../../assets/image_4fe99c279b.png)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

Model: Sunwhale-003-45180-camber5-thick3-front3

Model: Sunwhale-005-45180-camber3-thick6-fairing338

&#x20;  &#x20;

&#x20;         Fairing size: 3.38m&#x20;

&#x20;       Distance from leading edge: 0.5m

![](../../../../../assets/image_88835bf4ec.png)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

![](../../../../../assets/image_3c77ad5a6a.png)

&#x20;Force (N)

176.973

&#x20;Force x (N)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

&#x20;Force y (N)

0.394

&#x20;Force z (N)

&#x20;SA (m^2)

22.6072

Model: Sunwhale-003-45180-camber5-thick3-front4

44.773

-171.215

![](../../../../../assets/image_deb1e24f70.png)

Model: Sunwhale-005-45180-camber3-thick6-fairing38

&#x20;  &#x20;

&#x20;         Fairing size: 3.8m&#x20;

&#x20;       Distance from leading edge: 0.3m

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

![](../../../../../assets/image_66f8b1cb5f.png)

Model: Sunwhale-003-45180-camber5-thick3-front5

![](../../../../../assets/image_92c6dcfd4e.png)

&#x20;Force (N)

&#x20;Force x (N)

&#x20;Force y (N)

&#x20;Force z (N)

SA (m^2)

178.913

46.76

1.312

-172.69

23.2416

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

Fairing Size on 3-Fairing Car (split fairing)

Directory: SplitFairingAug5

Sample name: Sunwhale-004-45180-camber3-thick6-fairing338

fairing338 corresponds to fairings of 3.38m length

This series is based on the main foil and fairings of Sunwhale-002-45180-camber5-thick3-shortfairing-16series, but with the following modifications:

&#x20;   \- thicker main foil (thickness 6) to reflect more realistic sizing in accommodating suspension etc.

&#x20;   \- non-cambered fairing foils

&#x20;   \- same driver fairing as the corresponding 2-fairing car model for each given size

&#x20;   \- same front/rear fairings on the split fairing side

&#x20;   \- fairings are extruded 0.44m (instead of previously 0.54m)

&#x20;   mainfoil = NACA64A-306

&#x20;   driver fairing = NACA 16-011

&#x20;   split fairings = NACA 64A-020

When changing length, fairings are placed a reasonable distance from the leading edge in order to maintain a sensible wheelbase. (e.g. 0.3m for a longer fairing, 0.5m for a shorter fairing) This results in a fairing relatively centered between the leading and trailing edges of the car.

On the split fairing side, the front of the front fairing and rear of the rear fairing span the same length as the single fairing on the other side. The default for split fairing length is 1.5m.

Model: Sunwhale-003-45180-camber5-thick3-front6

![](../../../../../assets/image_8b98ec1681.png)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

Model: Sunwhale-003-45180-camber5-thick3-front7

Model: Sunwhale-004-45180-camber3-thick6-fairing28

&#x20;       Fairing size: 2.8m large, 1.2 small

&#x20;       Distance from leading edge: 0.7m

![](../../../../../assets/image_c59926925c.png)

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

![](../../../../../assets/image_b90ab55075.png)

Model: Sunwhale-003-45180-camber5-thick3-front8

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

![](../../../../../assets/image_90def61bab.png)

Model: Sunwhale-004-45180-camber3-thick6-fairing338

&#x20;  &#x20;

&#x20;         Fairing size: 3.38m large, 1.5m small

&#x20;       Distance from leading edge: 0.5m

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

![](../../../../../assets/image_eb852e9c4d.png)

![](../../../../../assets/image_a41ddba687.png)

&#x20;Force (N)

&#x20;Force x (N)

&#x20;Force y (N)

&#x20;Force z (N)

&#x20;SA (m^2)

22.3533

81.07

42.565

1.366

-68.983

#### Embedded Content

Embedded content: [Custom embed](catamaran-fairing-distance-and-split.md)

Model: Sunwhale-004-45180-camber3-thick6-fairing38

&#x20;  &#x20;

&#x20;         Fairing size: 3.8m large, 1.5m small

&#x20;       Distance from leading edge: 0.3m

![](../../../../../assets/image_49e6e550e1.png)

&#x20;Force (N)

61.054

&#x20;Force x (N)

&#x20;Force y (N)

&#x20;Force z (N)

&#x20;SA (m^2)

46.449

2.348

-39.555

22.6939
