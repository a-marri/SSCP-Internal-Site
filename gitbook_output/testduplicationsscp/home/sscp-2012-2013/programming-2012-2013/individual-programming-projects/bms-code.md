# SSCP - BMS Code

# BMS Code

Attached files include logic settings files for debugging parts of the board and any datasheets I think are necessary.

Code for this project is currently in software-micro/bms_0.

11/25/2012

Have code to talk to all four ADCs after one START pulse.  Have not verified the validity of the data returned.

ADC code will be split into an ADS1246 driver in the drivers directory that includes struct and function definitions and AdcBms.c/h in the bms project with declarations for the ADCs used on BMS, usage of those ADCs, and usage of the data received from them.

[](https://drive.google.com/folderview?id=1XzmLuuxtMJxSFqRBMDz4jQi3ixziIAnF)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1XzmLuuxtMJxSFqRBMDz4jQi3ixziIAnF#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1XzmLuuxtMJxSFqRBMDz4jQi3ixziIAnF#list" frameborder="0"></iframe>

