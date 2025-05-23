# strength-analysis

## SSCP - Strength Analysis

## Strength Analysis

### From Vivian Lee, Alum From Equinox/Apogee

* Attached pdf explains aerobody FEA analysis in Ansys.Link to page explaining composite stress-strain math: http://www.mech.utah.edu/\~rusmeeha/labNotes/composites.htmlBelow is an email from Vivian:
* Attached pdf explains aerobody FEA analysis in Ansys.
* Link to page explaining composite stress-strain math: http://www.mech.utah.edu/\~rusmeeha/labNotes/composites.html
* Below is an email from Vivian:
* Attached pdf explains aerobody FEA analysis in Ansys.
* Link to page explaining composite stress-strain math: http://www.mech.utah.edu/\~rusmeeha/labNotes/composites.html
* Below is an email from Vivian:

Attached pdf explains aerobody FEA analysis in Ansys.

Link to page explaining composite stress-strain math: http://www.mech.utah.edu/\~rusmeeha/labNotes/composites.html

[http://www.mech.utah.edu/\~rusmeeha/labNotes/composites.html](http://www.mech.utah.edu/~rusmeeha/labNotes/composites.html)

Below is an email from Vivian:

This was back in ANSYS V10/12 days so there might be something newer now. We did more extensive analysis at Boeing, but probably not needed for solar car. Instructions attached. Let me know if you have questions.

In terms of the math behind it, you're really just using a numerical solver in FEA to solve Hooke's Law (F=kx) and Stress (Sigma = Modulus\*epsilon). It just looks complicated because it's now a 6x6 matrix where not everything is zero. For metals (isotropic), most of it zeros out.

&#x20;

Essentially, you will build a surface model of the structural members of the car (the chassis panels, the bottom shell between the panels, and the panel between the two shocks) and combine it with the solid rollcage model.  You can define a laminate stacking sequence on the surfaces to define the properties of the composites. Then you can apply point loads through the suspension hardpoints to simulate the loading conditions.  For a crash, you can apply the required loads directly to the rollcage or the chassis panels.  We can't simulate the crush zone outside the panels with this method, but as long as it works on the chassis you can say that energy will only be taken out by the extra body crush.  If the analysis shows that it wouldn't survive with the load applied directly to the chassis, then you can either do some handwaving to say the crush zone would take care of it, or we would have to increase the fidelity of the model.&#x20;

&#x20;

One more thing...you will need to know the material properties of the composite fabric and core for this to work.  You can get them from your carbon suppliers, or estimate them based on common carbon values.

&#x20;

The values you will need are below.  E is elastic (Young's) modulus, nu is Poisson's ratio, and G is the shear modulus.  x is the primary fiber direction, y is perpendicular to the fibers in the plane of the ply, and z is perpendicular to the plane of the ply.  For core, z is perpendicular to the plane, and x and y are in the plane (technically there is a difference between the two in-plane directions of the core, but not much, and you aren't going to get any planar stiffness from your core anyway)

&#x20;

Carbon weave:

* E\_x = E\_y (since this is a woven fabric, the two primary fiber directions will have the same properties)
* E\_z (not as important, can be assumed to be \~0.01\*E\_x)
* nu\_xy
* nu\_xz = nu\_yz (again, not as important, can be assumed zero)
* G\_xy
* G\_xz = G\_yz (again, can be assumed to be \~0.01\*G\_xy)

&#x20;

Carbon uni:

* E\_x
* E\_y = E\_z (more important for uni, you should look this up)
* nu\_xy = nu\_xz
* nu\_yz (can be assumed to be zero)
* G\_xy = G\_xz
* G\_yz (can be assumed to be \~0.01\*G\_xy)

&#x20;

Core

* E\_z
* E\_x = E\_y (can be assumed to be \~0.001\*E\_z)
* G\_xy
* G\_yz = G\_xz (can be assumed to be \~0.001\*G\_xy)

&#x20;

&#x20;

You would also ideally need failure criteria (maximum stress on fibers, maximum interlaminar shear for the prepreg and for the bond to the core, and maximum compressive stress on the core), but those are harder to come by.  Ask around and see if you can find them.  Prof. Springer or Prof. Chang in the Aero/Astro department might have some good common carbon fiber laminate properties that you could use.&#x20;

Sounds like you have access to some datasheets already though.

### From Williams F1

Attached spreadsheet can be used to estimate composite material strength.

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1uB7m7ILYl_2KYKJoaTTcd6RxtB3ZFgj5#list)
