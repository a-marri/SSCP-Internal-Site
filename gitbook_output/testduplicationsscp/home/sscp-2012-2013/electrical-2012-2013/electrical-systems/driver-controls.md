# SSCP - Driver Controls

# Driver Controls

Driver Controls is responsible for taking in driver inputs and sending out the appropriate CAN signals.

Buttons: Appropriately detecting button presses can be difficult in a harsh EMI environment. For this reason we use BJT's to sense current rather than voltage from the signal lines coming form the physical buttons.

Pedals: How much the pedals depress must be accurately measured and the CAN messages sent out to the tritium. These are the next pedal encoders.

[ These](http://media.digikey.com/pdf/Data%20Sheets/Honeywell%20Sensing%20&%20Control%20PDFs/RTY_Hall_Effect_Rotary_Position_Sensors_.pdf)

Possible improvements: Making the button circuit more robust (no problems with the Xenith implementation but it was not as fault tolerant as it should have been)

On the next car, there will be a separate button board. This button board will have the buttons for the driver as well as a display. Example display can be seen here and here. The separate board for buttons is primarily to reduce any problems with noise from the buttons. It has the added bonus of reduced lines for connecting to buttons and running a display for the driver. In addition it allows for the driver controls to be simpler.

[ here](https://www.sparkfun.com/products/9395)

[ here](https://www.sparkfun.com/products/709)

[](https://drive.google.com/folderview?id=1g85pWVCWX4p2bPSxyiflg5QGdRXNGRWt)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1g85pWVCWX4p2bPSxyiflg5QGdRXNGRWt#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1g85pWVCWX4p2bPSxyiflg5QGdRXNGRWt#list" frameborder="0"></iframe>

