# SSCP - Testing

# Testing

11/3 Derek's Meeting with Spectrolab Saul Vargas (Technical Head Illumination and Sensor Products)

Spectrolab makes solar stuff for space-based applications. Thus, they use germanium-based cells, so the guy wasn't sure if their simulators would be appropriate for us. They should be though if they adjust the wavelength output a little (since some infrared and UV get weeded out upon entering the atmosphere). Their machines can cost over $500,000 so they can't really get us. However, Saul is really, really excited about helping us out, and he said he'll look into letting us use their facilities to test cells. Obviously not as ideal as having the machine in-house, but a good back up plan!

11/2 Derek's Meeting with Eternal Sun representatives, Pepijin Veling (sales engineer) and Willem Zwetsloot (engineer, was major participant on Nuon team)

I asked about solar simulators in general as well as their product. What follows is the chronological progression of our conversation, which jumped around at times. Their machine can go from 400 to 1300 W/m^2, which is perfect since the Australian sun shines around 1250 W/m^2 AM 1.5. Their big hook is that they use a floodlight lamp that allows your solar cells to lie flat and still get uniform illumination. Thus the distance from the lamp can be much smaller, from 10 ft in other machines to just 10 cm in theirs. In terms of the machine's dimensions, since our biggest modules are around 75cm by 50cm, we would need to make enough room in VAIL for a 1 meter tall, 1 meter wide, 1 meter length device. The only input it needs is a high power outlet (no vacuum, gas tank, etc.). They make custom size simulators, so we need to figure out the minimum testable area that we require. The three big things to look out for in a solar simulator are uniformity (theirs is less than 1.5% deviance and supposedly one of the best in the industry), stability (over short and long term), and spectrum. Flash testers (on the order of 100 ms) are old school technology that are good for 80% of tech for IV curves, but not good for OLED, CIGS, etc. that need longer exposure. So for our silicon panels we can use the flash tester, but we'd be missing out on having continuous sunlight for max point trackers, temperature effects, etc. (Random discussion: I asked about binning and they said all we need is a four point probe system. They sell one but there should be tons on campus.) In terms of lifetime/maintenance of the machine, the lamp has two parts. The first part has a lifetime of 1800 hours and costs 27 euros to replace. The second part has a lifetime of 9000 hours and costs 93 euros to replace. Overall, the solar simulator will cost around $100,000 euros. (Random: Let's look into Sol Excel.) Obviously that's a ton but there are a few ways we can lower costs for SSCP. 1) If we help Nuon get good solar cells (they've had difficulty getting sponsored by Sun Power.) 2) Look into bare minimum area to lower costs. 3) Get money from other departments and promise that they'll be able to use the machine for labs and stuff. Final random thing that Willem gave advice on: We need an IV tracing system, which we do, but we don't need Eternal Sun's super expensive one. When I mentioned that we have our own, homemade one (I think), he said that we need to look out for a few things to make sure our data is good. Using an oscilloscope, we need to make sure that the load algorithm doesn't pulsate, but is a straight line. We also need to see if the V and I are sampled at the exact same time. Any Keithley instrument should work. 

So things that need to be done: Figure out minimum area, see if we can help Nuon, talk to professors about getting help with funding. We don't need Eternal Sun, however, if Sinton Instruments works out.

Action Items:

Get SourceMeter (John)

    Frank from Keithley scheduled for tour 4:00 PM tomorrow -- unit will arrive 2-3 weeks! 

Contact D2Solar (John)

    Emailed morning of 10/20, no response yet

Ask Kat if we can use labs for encapsulation (John)

Solar simulator (Sinton Instruments, Eternal Sun, Spectrolab, Abet Technologies, OAI, Oriel, Newport, Sciencetech)

[](https://drive.google.com/folderview?id=1vyxll2gvhMMch_xpZrHlUyXmCos_501Y)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1vyxll2gvhMMch_xpZrHlUyXmCos_501Y#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1vyxll2gvhMMch_xpZrHlUyXmCos_501Y#list" frameborder="0"></iframe>

