# SSCP - Xenith Aero Analysis Part 1

# Xenith Aero Analysis Part 1

I just completed a suite of aero analyses on the car. I thought I would summarize all of it as my final bit of work. Be prepared though, this is a long e-mail with a lot of information: you don't have to read if you don't want to. 

All simulations are run at 24.59 m/s (55 mph, 88.5 kph). All simulations also have a "rolling road" ground surface included. Keep in mind that every simulation is on a perfect car body with no seams or imperfections. Also, all of the simulations on Xenith include skirts that go all the way to the ground. I know that is not completely realistic, but I needed to make some simplifications to keep my sanity. There is a discussion of the skirts in the attached powerpoint presentation.

The summary to take away from all of this is that all of the simulations I did indicate that our car should be competitive with Nuna. We know that in a very controlled wind tunnel without their tires rotating, Nuna had about 31N of drag. Obviously, in the real world they would be a bit higher than that due to inherently higher turbulent intensity in the on-rushing air on the open road. They also had rotating tires on the open road. 

It seems that the negative angle of attack should not have hurt us as much as my hand calculations initially indicated. I plugged the Schwalbe tire friction data that we had into a spreadsheet along with the aero simulation results and got the following predictions: 

1350 W at 55mph and zero angle of attack on the car

1366 W at 55mph and -0.8 deg. angle of attack on the car.

We were much, much higher than this during the race, so I don't know where all the power is going. I included a few powerpoint slides on how the skirts should work. I know a few of you expressed concern about dragging air along with the car, but the same happens if you aren't running skirts, and the slides explain why. That said, the skirts are not fully understood, so it would be nice to get a proper set into a wind tunnel to see how they actually perform.

Basically I see the team having three options going forward:

1. Test the current car in a wind tunnel and do some more research to figure out where the power losses are going. Use this knowledge to tweak the current car and aerobody. New molds would be required for Michelin tires and to fix any items found during the wind tunnel testing, but it would largely look the same as the current car. This option requires limited involvement from somebody on the team that knows aerodynamics in case you can't find someone suitably trained to work for the team.

2. Test the current car in a wind tunnel and figure out where the power losses are going. Take this knowledge so that the same mistakes are not repeated, and then design a completely new aerobody. The new car would be thicker to allow for more suspension travel (assuming that is still considered a problem after the wind tunnel testing) and would also get rid of the high pressure region in front of the driver fairing that the current car has.

3. Test the current car in a wind tunnel to learn lessons and design a completely new car that is thicker and uses active boundary layer control with fans. This would involve several wind-tunnel trips for the next car and probably some heavy involvement from not just a Master's student, but some professors who really know what they are doing.

I think it is important to get the current car into a wind tunnel so that you can learn lessons from it. It should be an instructive experience. Without it, I am afraid that the team will go forward blindly. Obviously the options get harder as you go down the list. That said, I think that the only way to really go for the win in the next race is option 3. Nuna, Tokai, and Michigan have all perfected their cars over several cycles and many wind-tunnel test sessions. Options 1 and 2 could lead to victory, but everything from production to the race would have to go perfectly to have a chance. It's really up to the team what your priorities are. Do you want to win, or do you want to continue as more of a research and learning tool with less stress and effort put forth? I can tell you, and I think that most alumni will also tell you that you must choose one or the other, you absolutely cannot have it both ways. It takes a completely different state of mind to go after victory. All of a sudden the current team's focus of 95% design and production of cool things with 5% testing has to change to 70/30 or even 60/40% design/testing. The design for victory has to be simpler in some areas and more developed in others, and the execution during manufacture and during the race has to be done with military-like precision.

That said, here are the aero simulation numbers:

Nuna 6 Laminar Simulation

The numbers from the Nuna 6 simulation I ran while in Australia. This was a laminar simulation only, so the drag numbers are going to be drastically underestimated. That said, it will offer a comparison to our car for the same type of simulation. In the Nuna simulation I put in some wheels below the car, but did not set them rotating.

Pressure Drag: 14.28N

Viscous Drag: 2.3N

Total Drag: 16.59N

Lift: 30N

Xenith Laminar Simulation

This is the Laminar simulation on Xenith. This should offer a comparison to Nuna's car. Xenith appears to have a bit less drag. Turbulent transitions are not taken into account in these kinds of simulations, but I would think that Xenith would actually be better than Nuna in regards to turbulent transition. I designed the car for that, we he had a much smoother array surface than they did, thanks to the glass and everyone's attention to seam details on this car.

Pressure Drag: 7.4N

Viscous Drag: 5.43N

Total Drag: 12.8N

Lift: 26.28N

Xenith Turbulent Simulation (k-omega model)

This model is fairly well established in the aero world for both 2D and 3D simulations. It assumes that all flow has some turbulence to it, but the turbulent intensity can vary. Therefore, there is no laminar flow and no "transition" but you can have very low turbulent intensity flow which would lead to relatively low skin friction. I would still expect this model to have slightly higher skin friction than a proper laminar-to-turbulent transition model.

Pressure Drag: 7.72N

Viscous Drag: 23.16N

Total Drag: 30.88N

Lift: 52.51N

Xenith Transition Simulation (Transition SST)

This model attempts to predict the transition from laminar to turbulent flow. Ideally this would provide the most accurate simulation. Problem is, I don't know much about it, nor was I able to get it to work properly. There are a lot of parameters for turbulent intensity and intermittency that I was not able to get right nor was I able to find help on it online. I also am not sure if this model is meant for 3D flow or if it's really just for 2D simulations. In any case, the results showed that the flow transitioned to fully turbulent about 20 inches in front of the car, which clearly is wrong. However, some useful information can be gleaned, namely that the k-omega turbulent simulation above is probably pretty accurate. Both the k-omega fully turbulent simulation and the Transition SST model (which turned out to be fully turbulent) are pretty close.

Pressure Drag: 9.43N

Viscous Drag: 26.2N

Total Drag: 35.62N

Lift: 57.7N

Xenith Turbulent Simulation with negative angle of attack (-0.8 deg. angle of attack, k-omega model)

This simulation attempted to replicate the angle of attack that we ran in Australia. -0.8 deg is what we measured in the pits just before the race started. I was quite surprised that it produced almost no difference in drag. Apparently changing the angle of attack on the car doesn't have a huge effect on lift. Some well established simple equations for airfoils predict that an angle of attack change like this should have a massive effect on lift and hence on drag as well. Those equations were predicting an increase in drag of over 20N and an increase in downforce of 30+ lbs. Apparently the high pressure region underneath the car caused by the interaction between the wheel and driver fairing and the main foil produce most of the lift, and it does not vary much with angle of attack.

Pressure Drag: 8.7N

Viscous Drag: 23.1N

Total Drag: 31.8N

Lift: -39.6N

Xenith Transition Simulation with negative angle of attack (Transition SST model, -0.8 deg. angle of attack)

Again, I wasn't able to get this transition simulation to work properly and it was predicting fully turbulent flow 30 in. in front of the car. I thought I would include the results for completeness anyways.

Pressure Drag: 10.26N

Viscous Drag: 26.11N

Total Drag: 36.5N

Lift: -46N

Xenith Sidewind Laminar Simulation (5 deg. cross wind, 24.59 m/s forward speed)

Pressure Drag: 6.328N

Viscous Drag: 5.794N

Total Drag: 12.12N

Lift: 37.87N

Xenith Sidewind Turbulent Simulation (k-omega turbulence model, 5 deg. cross wind, 24.59 m/s forward speed)

Pressure Drag: 6.59N

Viscous Drag: 23.6N

Total Drag: 30.2N

Lift: 66.25N

Sorry that was so long-winded.

It was interesting working on this car. Fun, stressful, and infuriating all at the same time. I learned a lot.

Thanks,

-- 

Danny Koelker

[](https://drive.google.com/folderview?id=1LnXci-cMJyGjP64LD3kTq6I-Darv8dBB)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1LnXci-cMJyGjP64LD3kTq6I-Darv8dBB#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1LnXci-cMJyGjP64LD3kTq6I-Darv8dBB#list" frameborder="0"></iframe>

