# warp-motor-modifications

## SSCP - Warp Motor Modifications

## Warp Motor Modifications

Increasing Warp Core Max Speed

Feedback From Sam Lenius 9/16/2016

The warp core motors are not 'designed for 100V'. They simply have a speed constant that means that a 100V nominal pack leads to a maximum speed lower then you would like to cruise at.

Rewinding (I'd prefer the term 'remanufacturing') the motors is a time intensive process, and will only change their speed constants, without the benefit of higher efficiency. The motors require \~12-24hours of detailed hand labor each to wind, so I would not recommend it unless you are winding new more efficient stator cores to go with them (which I designed more then two years ago now). Additionally, all of the windings are epoxied in place. After the motors were wound and tested, NHS and I vacuum infused epoxy throughout the windings for reliability. Removing the windings that are on there now will require a lot of labor in cutting and chiseling them off, and has substantial risk of damaging the electrical steels.

The things that make these motors as efficient as they are are also what make them expensive. I got a few quotes for outside houses to wind them, but they were \~$5k-8k per motor for just stacking and winding.

If you want to make new motors, I can teach someone who's willing to learn how to wind motors. You can expect to pay \~$4k per stator for the steel (although I have a better relationship with protolam now, we might be able to get better pricing) and the materials to wind it cost under $100 per motor (plus invested suffering of the person who gets to wind it). I think we paid \~$2-3k per housing for machining as well, so make sure to factor that in.

Don't try to fix the speed limiting issue with a boost converter. Iowa State put a silly voltage converter on their car after not understanding motor speed constants at ASC. It's not an efficient way to solve the problem. Unfortunately Tritium doesn't support flux weakening, so that's not a great option.

We could program the speed constant another way as well, by changing the rotors. We initially made the motors with a lower flux rotor, and then decided we needed more torque, hence Black Edition rotors. If you can make a lighter and slipperier car, we could make new rotors that are a compromise between the black edition and the initial design rotors. This would increase the speed constant, while trading motor iron loss for copper loss (iron loss down, copper loss up) and trading lower torque for a higher top speed. This may or may not be a good trade, it would require some significant math and simulation to answer. New rotors cost $500-1000 each btw.

Pay attention to the Marand specs if you want to follow that route. Generally they are wound for higher voltage then you guys use, and make have other system efficiency considerations.

TLDR: Higher battery voltage or new motors recommended. New rotors are the cheap option if you don't want to change your battery voltage.&#x20;

-Sam

Other Potential Modifications

#### Create new housing

Relocate Hardpoints for suspension. &#x20;

Make motors robust for different loading conditions of Sundae suspension.

#### Suggested Changes (from Warpcore Documentation)

* Remove vanes from rotor carrier to reduce windage lossesBraze aluminum cover over vanesModify design for two-sided machining with no vanesModify cover to not interfere with brake calipersEasy cadUse a better material for the stator pad. Possibly put the stator pad underneath the stator or control tolerances to an extent that the aluminum provides the squishThe cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the statorFigure out how to stop the inner bearing outer race from spinning in place. Reminder: the black grease indicates that aluminum is being worn away from the shell.Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.Study, characterize, and eliminate playChange the bolt circle on the front ( make it actually a 7 bolt circle)Figure out a better way to remove the rotor assembly...3D print a rubber wire holder that guides and seals the connector area from the spinning motorEasily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?
* Remove vanes from rotor carrier to reduce windage lossesBraze aluminum cover over vanesModify design for two-sided machining with no vanes
* Braze aluminum cover over vanes
* Modify design for two-sided machining with no vanes
* Modify cover to not interfere with brake calipersEasy cad
* Easy cad
* Use a better material for the stator pad. Possibly put the stator pad underneath the stator or control tolerances to an extent that the aluminum provides the squishThe cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator
* The cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator
* Figure out how to stop the inner bearing outer race from spinning in place. Reminder: the black grease indicates that aluminum is being worn away from the shell.Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.
* Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.
* Study, characterize, and eliminate play
* Change the bolt circle on the front ( make it actually a 7 bolt circle)
* Figure out a better way to remove the rotor assembly...
* 3D print a rubber wire holder that guides and seals the connector area from the spinning motorEasily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?
* Easily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?
* Remove vanes from rotor carrier to reduce windage lossesBraze aluminum cover over vanesModify design for two-sided machining with no vanes
* Braze aluminum cover over vanes
* Modify design for two-sided machining with no vanes
* Modify cover to not interfere with brake calipersEasy cad
* Easy cad
* Use a better material for the stator pad. Possibly put the stator pad underneath the stator or control tolerances to an extent that the aluminum provides the squishThe cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator
* The cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator
* Figure out how to stop the inner bearing outer race from spinning in place. Reminder: the black grease indicates that aluminum is being worn away from the shell.Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.
* Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.
* Study, characterize, and eliminate play
* Change the bolt circle on the front ( make it actually a 7 bolt circle)
* Figure out a better way to remove the rotor assembly...
* 3D print a rubber wire holder that guides and seals the connector area from the spinning motorEasily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?
* Easily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?

Remove vanes from rotor carrier to reduce windage losses

* Braze aluminum cover over vanes
* Modify design for two-sided machining with no vanes

Braze aluminum cover over vanes

Modify design for two-sided machining with no vanes

Modify cover to not interfere with brake calipers

* Easy cad

Easy cad

Use a better material for the stator pad. Possibly put the stator pad underneath the stator or control tolerances to an extent that the aluminum provides the squish

* The cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator

The cork worked rather well - the tolerance of any given stator will probably not be close enough to use stator compression. If M19 steel is used, then we can use bolts directly on the stator

Figure out how to stop the inner bearing outer race from spinning in place. Reminder: the black grease indicates that aluminum is being worn away from the shell.

* Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.

Skf recommends the use of an o-ring on the outer bearing race to prevent it from rotating.

Study, characterize, and eliminate play

Change the bolt circle on the front ( make it actually a 7 bolt circle)

Figure out a better way to remove the rotor assembly...

3D print a rubber wire holder that guides and seals the connector area from the spinning motor

* Easily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?

Easily said, difficult to find 3d printable rubber that is strong enough. Maybe cast silicone?
