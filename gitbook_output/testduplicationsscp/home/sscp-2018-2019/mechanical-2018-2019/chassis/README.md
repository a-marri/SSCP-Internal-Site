# chassis

## SSCP - Chassis

## Chassis

Design subpage stuff below.

The Black Mamba chassis had a lot of major design flaws (and design process flaws). In list form, some of the major ones:

* the design focused more on packaging than anything else (over-reliance on "overbuild" and a magic materials factor)Not enough attention was paid to loadpaths from the suspension into the rest of the car (ideally opposing loads will be transferred through the chassis so that they meet)bad manufacturing practices from previous cars were carried forward, mostly in how teklam panels were usedThe build itself was rushed and the chassis wasn't as well bonded as it should have beenAccess to electronics and driver-critical systems was done well, but access to the back of suspension parts and critical bolts was done very poorlyThe structural analysis that was done was more of a hand-calcs style borrowed from previous years than a full-scale FEA. This was poor in that it made a lot of glaring assumptions and treated the car as a collection of independent walls instead of a homogenous whole, and probably won't fly in the future.
* the design focused more on packaging than anything else (over-reliance on "overbuild" and a magic materials factor)
* Not enough attention was paid to loadpaths from the suspension into the rest of the car (ideally opposing loads will be transferred through the chassis so that they meet)
* bad manufacturing practices from previous cars were carried forward, mostly in how teklam panels were used
* The build itself was rushed and the chassis wasn't as well bonded as it should have been
* Access to electronics and driver-critical systems was done well, but access to the back of suspension parts and critical bolts was done very poorly
* The structural analysis that was done was more of a hand-calcs style borrowed from previous years than a full-scale FEA. This was poor in that it made a lot of glaring assumptions and treated the car as a collection of independent walls instead of a homogenous whole, and probably won't fly in the future.
* the design focused more on packaging than anything else (over-reliance on "overbuild" and a magic materials factor)
* Not enough attention was paid to loadpaths from the suspension into the rest of the car (ideally opposing loads will be transferred through the chassis so that they meet)
* bad manufacturing practices from previous cars were carried forward, mostly in how teklam panels were used
* The build itself was rushed and the chassis wasn't as well bonded as it should have been
* Access to electronics and driver-critical systems was done well, but access to the back of suspension parts and critical bolts was done very poorly
* The structural analysis that was done was more of a hand-calcs style borrowed from previous years than a full-scale FEA. This was poor in that it made a lot of glaring assumptions and treated the car as a collection of independent walls instead of a homogenous whole, and probably won't fly in the future.

the design focused more on packaging than anything else (over-reliance on "overbuild" and a magic materials factor)

Not enough attention was paid to loadpaths from the suspension into the rest of the car (ideally opposing loads will be transferred through the chassis so that they meet)

bad manufacturing practices from previous cars were carried forward, mostly in how teklam panels were used

The build itself was rushed and the chassis wasn't as well bonded as it should have been

Access to electronics and driver-critical systems was done well, but access to the back of suspension parts and critical bolts was done very poorly

The structural analysis that was done was more of a hand-calcs style borrowed from previous years than a full-scale FEA. This was poor in that it made a lot of glaring assumptions and treated the car as a collection of independent walls instead of a homogenous whole, and probably won't fly in the future.

Expounding on lessons learned below:

Teklam (and other) sandwich panels

* Sandwich panels are meant to take loads that are in-plane with the panel itself, so that the face skin of the panel can transfer the load across the whole thing. They are not meant to take loads in bending or push-pull loads into or out of the face of the panel. They also aren't meant to be cantilevered or cut into small, badly-supported pieces.When used properly, sandwich panels are a great way to add stiffness to a structure and to transfer loads across large areas, but to do so they have to be loaded in the right direction and well supported on as many sides as possible. The panels cannot transfer load through the core - this is very important. All the load transfer happens through the face skins. This is why glue fillets are sketchy - the amount of surface area put into the bond is very small and glue alone is less reliable than carbon. It's much much better to bond panels using a wet layup fillet or a right-angle piece of carbon bonded on.Extensive cutouts are probably not worth much in terms of weight savings, especially in a well designed (i.e. simple) chassis. Unless you're western sydney chasing down that last 1/8th of a pound or whateverthe interlocking-joint design from mamba is nice for locating parts but bad for load transfer. If the panels were solid and could transfer loads through their center, then it would be good, but they aren't - better to leave the face skins uncut when possible and get nice big bond surfaces from one to the other
* Sandwich panels are meant to take loads that are in-plane with the panel itself, so that the face skin of the panel can transfer the load across the whole thing. They are not meant to take loads in bending or push-pull loads into or out of the face of the panel. They also aren't meant to be cantilevered or cut into small, badly-supported pieces.
* When used properly, sandwich panels are a great way to add stiffness to a structure and to transfer loads across large areas, but to do so they have to be loaded in the right direction and well supported on as many sides as possible.&#x20;
* The panels cannot transfer load through the core - this is very important. All the load transfer happens through the face skins. This is why glue fillets are sketchy - the amount of surface area put into the bond is very small and glue alone is less reliable than carbon. It's much much better to bond panels using a wet layup fillet or a right-angle piece of carbon bonded on.
* Extensive cutouts are probably not worth much in terms of weight savings, especially in a well designed (i.e. simple) chassis. Unless you're western sydney chasing down that last 1/8th of a pound or whatever
* the interlocking-joint design from mamba is nice for locating parts but bad for load transfer. If the panels were solid and could transfer loads through their center, then it would be good, but they aren't - better to leave the face skins uncut when possible and get nice big bond surfaces from one to the other
* Sandwich panels are meant to take loads that are in-plane with the panel itself, so that the face skin of the panel can transfer the load across the whole thing. They are not meant to take loads in bending or push-pull loads into or out of the face of the panel. They also aren't meant to be cantilevered or cut into small, badly-supported pieces.
* When used properly, sandwich panels are a great way to add stiffness to a structure and to transfer loads across large areas, but to do so they have to be loaded in the right direction and well supported on as many sides as possible.&#x20;
* The panels cannot transfer load through the core - this is very important. All the load transfer happens through the face skins. This is why glue fillets are sketchy - the amount of surface area put into the bond is very small and glue alone is less reliable than carbon. It's much much better to bond panels using a wet layup fillet or a right-angle piece of carbon bonded on.
* Extensive cutouts are probably not worth much in terms of weight savings, especially in a well designed (i.e. simple) chassis. Unless you're western sydney chasing down that last 1/8th of a pound or whatever
* the interlocking-joint design from mamba is nice for locating parts but bad for load transfer. If the panels were solid and could transfer loads through their center, then it would be good, but they aren't - better to leave the face skins uncut when possible and get nice big bond surfaces from one to the other

Sandwich panels are meant to take loads that are in-plane with the panel itself, so that the face skin of the panel can transfer the load across the whole thing. They are not meant to take loads in bending or push-pull loads into or out of the face of the panel. They also aren't meant to be cantilevered or cut into small, badly-supported pieces.

When used properly, sandwich panels are a great way to add stiffness to a structure and to transfer loads across large areas, but to do so they have to be loaded in the right direction and well supported on as many sides as possible.&#x20;

The panels cannot transfer load through the core - this is very important. All the load transfer happens through the face skins. This is why glue fillets are sketchy - the amount of surface area put into the bond is very small and glue alone is less reliable than carbon. It's much much better to bond panels using a wet layup fillet or a right-angle piece of carbon bonded on.

Extensive cutouts are probably not worth much in terms of weight savings, especially in a well designed (i.e. simple) chassis. Unless you're western sydney chasing down that last 1/8th of a pound or whatever

the interlocking-joint design from mamba is nice for locating parts but bad for load transfer. If the panels were solid and could transfer loads through their center, then it would be good, but they aren't - better to leave the face skins uncut when possible and get nice big bond surfaces from one to the other

Tub chassis

* Most of the really good teams use a hybrid chassis style (some layup structures, some panels for load transfer). Eindhoven for example used layup around most of their driver protection structure but used panels to complete the load transfer between front and rear suspension and to build a casing around their battery compartment. (pics on drive somewhere)Jamie suggests aluminum core for a tub chassis.
* Most of the really good teams use a hybrid chassis style (some layup structures, some panels for load transfer). Eindhoven for example used layup around most of their driver protection structure but used panels to complete the load transfer between front and rear suspension and to build a casing around their battery compartment. (pics on drive somewhere)
* Jamie suggests aluminum core for a tub chassis.
* Most of the really good teams use a hybrid chassis style (some layup structures, some panels for load transfer). Eindhoven for example used layup around most of their driver protection structure but used panels to complete the load transfer between front and rear suspension and to build a casing around their battery compartment. (pics on drive somewhere)
* Jamie suggests aluminum core for a tub chassis.

Most of the really good teams use a hybrid chassis style (some layup structures, some panels for load transfer). Eindhoven for example used layup around most of their driver protection structure but used panels to complete the load transfer between front and rear suspension and to build a casing around their battery compartment. (pics on drive somewhere)

Jamie suggests aluminum core for a tub chassis.

Bolt-on Parts

* Blind inserts (not through-hole) are kinda sus. Try to encourage your MEs not to design critical load parts such that they would need to bolt into the aerobody or anything you won't be able to access both sides of.Also, loading threads in shear is bad. Loading teklam in pull is bad. The chassis designer is going to be responsible for catching a lot of the weird load-case shit that happens when the whole car is interacting as a system so learn to watch out for these things.If using sandwich panel inserts, the long side or the threaded side goes on the opposite side of the panel as the part
* Blind inserts (not through-hole) are kinda sus. Try to encourage your MEs not to design critical load parts such that they would need to bolt into the aerobody or anything you won't be able to access both sides of.
* Also, loading threads in shear is bad. Loading teklam in pull is bad. The chassis designer is going to be responsible for catching a lot of the weird load-case shit that happens when the whole car is interacting as a system so learn to watch out for these things.
* If using sandwich panel inserts, the long side or the threaded side goes on the opposite side of the panel as the part
* Blind inserts (not through-hole) are kinda sus. Try to encourage your MEs not to design critical load parts such that they would need to bolt into the aerobody or anything you won't be able to access both sides of.
* Also, loading threads in shear is bad. Loading teklam in pull is bad. The chassis designer is going to be responsible for catching a lot of the weird load-case shit that happens when the whole car is interacting as a system so learn to watch out for these things.
* If using sandwich panel inserts, the long side or the threaded side goes on the opposite side of the panel as the part

Blind inserts (not through-hole) are kinda sus. Try to encourage your MEs not to design critical load parts such that they would need to bolt into the aerobody or anything you won't be able to access both sides of.

Also, loading threads in shear is bad. Loading teklam in pull is bad. The chassis designer is going to be responsible for catching a lot of the weird load-case shit that happens when the whole car is interacting as a system so learn to watch out for these things.

If using sandwich panel inserts, the long side or the threaded side goes on the opposite side of the panel as the part
