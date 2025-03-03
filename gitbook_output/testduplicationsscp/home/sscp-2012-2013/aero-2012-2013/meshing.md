# SSCP - Meshing

# Meshing

The most difficult part of doing a run of CFD is generating a quality mesh. 

## Guidelines from Danny 

[](#h.u87rbjw0tnpr)

### Domain Size

[](#h.6myk8urcz7js)

Front wall should be 3-4 car lengths away from the front of the car.

Rear wall should be around 5 car lengths away from the rear of the car.

Sides should each be about 3 car widths away from each side of the car. (For the asymmetrical car anyways) For this car, cut the car in half lengthwise and put a side boundary right at that half point, but the other side boundary should still be 3 car widths from the outside of the car side.

Ground should not be flush with the bottom of the fairings, but rather whatever distance the fairing bottoms would be from the ground.

Top can 2 car heights above perhaps, but that is the least important side of the boundary.

### Element Sizing Parameters

[](#h.x5ppnw3bvouf)

Mesh on the surface of the car should be about 1" thick for most gently sloping surfaces, and decrease to, at smallest, around .1" for highly curved parts of the car - the more highly curved, the smaller you want to go, until hitting .1". Grow about 10 prism layers from the car surface at an exponential rate of 1.2-1.3. First layer should be about .020" thick for a proper y+ value at the surface.

Fill with a tetrahedral fill mesh (called robust octree in ICEM, I don't know what they call it in Hypermesh), and far away from the car you can have 30" tetrahedral since computational accuracy is less necessary in the fluid flow far from the car. In hypermesh hopefully you can put those bigger and further away from the hex cubes on the car. Be sure to allow for small meshing around complex joins and areas, since the fluid flow is likely to be changed by those kinds of things.

If possible, aim for 7-8 million mesh elements

