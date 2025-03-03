# SSCP - Sunbad CFD Setup

# Sunbad CFD Setup

I've been primarily using the .step files.  No need for x_t.  At the moment, the Army clusters are down because of coolant issues, so I am only able to mesh for the time being.  Once they are fixed (monday or tuesday, earliest) I'll be able to run simulations of the Naca67 body (already meshed) and the Naca 63 bodies.

For the splits, we only need them at trailing edges of the main aerobody and the wheel fairings.  You can look at the attached image1 for a visual idea of the splits and image2 for explanations of why.  Splitting the geometry at the trailing edge allows me to mesh the areas where the geometry is thinnest in the best possible way.

As for the results, the primary reason for all of the drag in the x direction is the increase in wetted area and the change in shape.  Because your aerobodies are not as flat as past cars, it is only natural that the flow will react much differently than before.  Moreover, if you inspect the morelliV3 shape, you will notice that the negative angle of attack of the leading edge of the aerobody can account for much of the negative lift in the z-direction.  3-D flows are less predictable than 2-D flows, so you should understand that the numbers cannot get better without refinement of any single aerobody shape.  Even after speaking with Professor Alonso and Professor Beiker about understanding 3D effects, the best answer he could give us was to run the numbers through CFD and make adjustments from those results.  Since a final shape has not been selected, it is only natural that we are getting these premature results.  We will only be able to start hitting ballpark numbers when we start modifying the shapes and not simply testing different shape types.  If you want to inspect the streamlines and pressure regions in more detail, I have already uploaded my .exo files in the FTP server that can be visualized in Paraview.

When Danny did the CFD analyses, he was able to focus on a 2D airfoil and then combine those slices to achieve a 3d shape meaning that the 3D flow effects had less impact on the overall solution compared to this year's car.  Even then, he had to iterate about 5 times to reach an aerobody with zero-lift,  Because of the change in design requirements, we cannot simply base our design off of a 2D airfoil, but must instead test more with CFD.  The results will come, but I imagine that they will take longer than Danny's process because of the change in design requirements.

If you are unhappy with the speed with which the results are being processed, you should realize that currently, I am the only one who has been meshing, processing, and post processing the results for the designs so far.  It's a lot of work, and it's something I've had to juggle while also working on simulations for the U.S. Navy and Army.  If you want suggestions for design modifications you should talk to Sean since he has taken the most fluid classes amongst Solar Car members.

Below are numbers and programs/codes that I have been using for all of the simulations

Codes & Programs::::::::::

Meshing Software: Ansys ICEM CFD

CFD Code: AERO-F

I realize that you guy's might be skeptical of these results since the code is not a consumer code, but you should know that the professor who oversees this code and its continued developments is a consultant for Ansys' products.  Below are links to articles regarding its usage.  It's a highly robust code that even the military has confidence in.

- http://www.dodsbir.net/sitis/archives_display_topic.asp?Bookmark=42081

[http://www.dodsbir.net/sitis/archives_display_topic.asp?Bookmark=42081](http://www.dodsbir.net/sitis/archives_display_topic.asp?Bookmark=42081)

- http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA503531

[http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA503531](http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA503531)

- http://me.stanford.edu/research/centers/ahpcrc/Project1-3feature.html

[http://me.stanford.edu/research/centers/ahpcrc/Project1-3feature.html](http://me.stanford.edu/research/centers/ahpcrc/Project1-3feature.html)

Post-Processing: Paraview & Gnuplot - Used by Sandia Nat'l Labs and the Army Research Lab to name a few

- http://www.paraview.org

[http://www.paraview.org](http://www.paraview.org/)

- http://www.gnuplot.info

[http://www.gnuplot.info](http://www.gnuplot.info/)

I am currently outputting pressure and velocity for each case.  I will be outputting vorticity as well for the upcoming tests.  Newer results will also be visualized without the symmetry condition so you can see the full car.

Simulation Metrics::::::::::

All simulations thus far have been made with the assumption that there are no exterior walls.  Boundary conditions of the fluid are simply inlet and outlet.  Ground effects are taken into account with a stick condition in place.  Mesh models have been created with symmetry.  The flow is viscous, compressible, and turbulent.

Air: density = 1.205 kg/m^3 • kinematic viscosity = 15.11e-6 m^2/s • freestream velocity = 24.5872

MorelliV3:

Aerobody Characteristic Length = 4.504697415 m

[4.504697415](tel:4.504697415)

Aerobody Reynolds = 7330105.645

Aerobody Boundary Layer Thickness = 0.0706066004 m

Front Wheel Fairing Characteristic Length = 1.387 m

Front Wheel Fairing Reynolds = 2257081

Front Wheel Fairing Boundary Layer Thickness = 0.0275166115 m

Back Wheel Fairing Characteristic Length = 1.019615394 m

Back Wheel Fairing Reynolds = 1659132.205 

Back Wheel Fairing Boundary Layer Thickness = 0.0215110648 m

Meshing Method: Octree -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Prism -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Cut Prisms into Tetras -> Final Smoothing

Mesh Type: Tetrahedral

Mesh Size: ~ 4 MIllion Nodes (This is nearly as big as Danny's final CFD runs and it is only the initial stage)

Mesh at the Boundary Layer consists of 12 layers

For Boundary Layer Thickness, I have been utilizing Schlichting's formula: delta =  0.37*characteristic length * Re^-0.2

Cfl: Implicit

Run in parallel over 256 processors

TeardropV2:

Aerobody Characteristic Length = 4.57301545 m

Aerobody Reynolds = 7441273.691

Aerobody Boundary Layer Thickness = 0.0714619622

Front Wheel Fairing Characteristic Length = 1.298028587 m

Front Wheel Fairing Reynolds = 2112169.985

Front Wheel Fairing Boundary Layer Thickness = 0.026093973 m

Back Wheel Fairing Characteristic Length = 1.022887553 m

Back Wheel Fairing Reynolds = 1664456.707

Back Wheel Fairing Boundary Layer Thickness = 0.0215662739 m 

Meshing Method: Octree -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Prism -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Cut Prisms into Tetras -> Final Smoothing

Mesh Type: Tetrahedral

Mesh Size: ~ 4 MIllion Nodes (This is nearly as big as Danny's final CFD runs and it is only the initial stage)

Mesh at the Boundary Layer consists of 12 layers

For Boundary Layer Thickness, I have been utilizing Schlichting's formula: delta =  0.37*characteristic length * Re^-0.2

Cfl: Implicit

Run in parallel over 256 processors

Naca67:

Aerobody Characteristic Length = 4.462176 m

Aerobody Reynolds = 7260914.212

Aerobody Boundary Layer Thickness =  0.0700729109 m

Front Wheel Fairing Characteristic Length = 1.0001883 m

Front Wheel Fairing Reynolds = 1627520.17

Front Wheel Fairing Boundary Layer Thickness = 0.0211825489 

Back Wheel Fairing Characteristic Length = 0.999417 m

Back Wheel Fairing Reynolds = 1626265.1

Back Wheel Fairing Boundary Layer Thickness = 0.0211694799 m

Meshing Method: Octree -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Prism -> Regular Smoothing -> Laplace Smoothing -> Regular Smoothing -> Cut Prisms into Tetras -> Final Smoothing

Mesh Type: Tetrahedral

Mesh Size: ~ 5.4 MIllion Nodes (This is nearly as big as Danny's final CFD runs and it is only the initial stage)

Mesh at the Boundary Layer consists of 12 layers

For Boundary Layer Thickness, I have been utilizing Schlichting's formula: delta =  0.37*characteristic length * Re^ -0.2

Cfl: Implicit

Run in parallel over 256 processors

I'm no longer on campus, you can reach me by e-mail.

 

--

