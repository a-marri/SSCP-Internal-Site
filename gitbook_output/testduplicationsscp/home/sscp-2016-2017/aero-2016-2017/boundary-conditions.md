# SSCP - Boundary Conditions

# Boundary Conditions

While CFD meshers (like Fluent and STAR-CCM+) can set the boundary conditions within the program, if you use Pointwise, you set the boundary conditions inside the mesh software before you export the file. Here is a log of the boundary conditions we use in different programs:

Sundae:

* STAR-CCM+car - wallground - wallwalls - symmetryinlet - inletoutlet - outlet
* STAR-CCM+car - wallground - wallwalls - symmetryinlet - inletoutlet - outlet
* car - wall
* ground - wall
* walls - symmetry
* inlet - inlet
* outlet - outlet

* STAR-CCM+car - wallground - wallwalls - symmetryinlet - inletoutlet - outlet
* car - wall
* ground - wall
* walls - symmetry
* inlet - inlet
* outlet - outlet

STAR-CCM+

* car - wall
* ground - wall
* walls - symmetry
* inlet - inlet
* outlet - outlet

car - wall

ground - wall

walls - symmetry

inlet - inlet

outlet - outlet

* Fluent (copied from Sunwhale cycle)car - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

Fluent (copied from Sunwhale cycle)

* car - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

car - wall

ground - wall

walls - symmetry

inlet - velocity inlet

outlet - outflow

Sunwhale/Arctan:

* SU2* --> Note that, for SU2, boundary conditions are set in the config file and not in Pointwise.car - wallground - euler wall (same as symmetry)walls - euler wall (same as symmetry)inletoutlet
* car - wall
* ground - euler wall (same as symmetry)
* walls - euler wall (same as symmetry)
* inlet
* outlet
* Fluentcar - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

SU2* --> Note that, for SU2, boundary conditions are set in the config file and not in Pointwise.

* car - wall
* ground - euler wall (same as symmetry)
* walls - euler wall (same as symmetry)
* inlet
* outlet

car - wall

ground - euler wall (same as symmetry)

walls - euler wall (same as symmetry)

inlet

outlet

Fluent

* car - wallground - wallwalls - symmetryinlet - velocity inletoutlet - outflow
* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

* car - wall
* ground - wall
* walls - symmetry
* inlet - velocity inlet
* outlet - outflow

car - wall

ground - wall

walls - symmetry

inlet - velocity inlet

outlet - outflow

* SU2 boundary conditions may need editing as I pulled these from memory and not by actually looking at the config file.

