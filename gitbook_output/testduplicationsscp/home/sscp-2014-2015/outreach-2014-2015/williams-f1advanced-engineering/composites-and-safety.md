# SSCP - Composites and Safety

# Composites and Safety

·         Design and Analysis

o   NX 7.5 CAD systemused to model all items

o   Sufacing, solid modelling, sheet metal, kinematics

o   Drawing definition via ply books or annotated views

o   All parts modelled with the correct materials and thickness – vital for mass tracking

o   Design Inputs:

§  Regulation – geometry, strength, stiffness, and safety

§  Aero – definition of all external surfaces and ducts (radiators, brake ducts)

§  Stress – sizing of components for strength, stiffness, and fatigue

§  Manufacturing – cost, lead times, processing (laminating, machining, fabricating, heat treatment, plating)

§  Logistics – ease of transport, fitting, maintenance, repair, modularity (upgrades)

o   Nastran used for FE analysis of both metallic and composite structures

o   Loads are driven by regulation and derived loads cases: aerodynamics, suspension, and inertial

o   Regulation

§  Static strength

·         Roll hoops have to withstand 120 kN

·         12.5 kN to 30 kN loads applied to survival cell

·         40 kN nose push off test

§  Stiffness

·         Many aerodynamic devices have deflection constraints to limit aero gains

·         Front wing, bodywork, floor, rear wing

§  Permissible materials

·         e.g. any metallic with a specific modulus > 40 GPa are banned

·         PAN (polyacrynonitrile) carbon fibers with tensile modulus < 550 GPa (this basically rules out pitch based fibers)

·         Density < 1.92 g/cm^3

·         No carbon nanotubes permitted

§  Impact strength

·         Nose (2 off), side, steering column, rear

§  Nose

·         Energy – 780 kg at 15 m/s = 87.8 kJ

·         Peak g for first 100 mm < 10 g

·         Peak permissible g increases linearly from 10 g at 100 mm to 20 g at 150 mm

·         Peak g over the first 60 kJ < 20 g

·         Average g over the first 150 mm > 2.5 g

·         Average g of trolley < 40 g

·         Peak g at dummy driver’s chest < 60 g for more than 3ms cumulative

·         No damage to the survival cell, fire extinguisher mounts, or seat belt mounts

§  Rear: fewer parameters

o   LS Dyna, Abaqus, and Nastran are our favored analysis tools

o   Derived load cases

§  Aerodynamic

·         Floor and wing loads (downforce, drag, yaw)

·         CFD important for providing pressure distribution

·         Proof, ultimate, and deflection limits defined by Design and Stress

§  Suspension

·         Bump, droop, steering, acceleration, braking, cornering, kerbing, and contract

·         Inputs into the monocoque are via front suspension mounts, and rear engine mounts (via gearbox, and rear suspension mounts)

§  Track data

·         Strain gauges, temperature/pressure sensors, pressure tapping

·         Materials

o   A very quick reminder of why we use composite materials

§  Rough comparison of fiber/woven/UD properties:

·         Strength: Fiber 100%: Woven 12%: UD 30%

·         Modulus: Fiber 100%: Woven 25%: UD 50%

o   Rough materials overview

§  Carbon prepregs

·         Standard modulus (woven)

·         Intermediate modulus (UD and woven)

·         High modulus (UD and woven)

§  Woven fabric styles

·         Plain

·         5 harness satin

·         2 x 2 twill

§  Woven aramid (Kevlar 49, etc)

§  Woven glass fabric (E or S2 types)

§  Resin types: epoxy, cynate ester, phenolic

§  Film adhesives

§  Pastes

§  Honeycombs: Aluminum hex, aluminum flex, Nomex hex

§  Foams: Rohacell 71, Rohacell 110, Zotec N50

·         Processing

o   Laminating

o   Curing – typically 1 hour at 135 degC

o   Trimming

o   Bonding

·         Paint

o   Paint shops are complimented on finish, rather than the minimal quantity of paint used

o   How important is paint finish from an aesthetic perspective?

o   Effect on aero performance?

o   Are parts weighed in/out of the paint shop?

o   Does the paint shop have any targets? Samples to use as a guide?

o   Are you lacquering over the paint?

o   Have you considered using vinyl wrap?

o   Do you paint all exposed surfaces? i.e. can you leave the underside of the body unpainted?

