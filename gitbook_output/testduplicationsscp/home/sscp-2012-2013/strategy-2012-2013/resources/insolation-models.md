# SSCP - Insolation Models

# Insolation Models

See resources on insolation modeling in files attached at bottom.

While I have not personally parsed any material in "Solar Radiation and PV Theory," it may give additional insight on modeling principles and generating pretty graphs (where "pretty" == "knowledge-delivering").

## WSC Data Fit meets Wikipedia Model

[](#h.iepxdfhu1uka)

Assume 1300 W at Solar Noon.

See "Parameters" maxPower and "Sim" line 27 PowerProduction in Strategy09.xlsb attached at bottom.

(.xlsb found at strategy > race > wsc2009)

"Sim" line 26 ArrayPowerProportion calls to line 18 SunInclinationSine formula for geometric calculation.

## CEE176B Model (calc_insolation_1.m)

[](#h.2savk07cetfw)

MATLAB function found under strategy > Lumex > helpers

Model derived from Insolation Calculator.xls, attached below and found under strategy > theory.

A compilation of notes from Gil Masters' course CEE176B is found as PVs and Insolation Slides.

>  help calc_insolation_1

for examples on how to use this function

## Gavin .go model

[](#h.am7yywrpe48w)

energySolar float64 = avgArrayPower * 1000 / speed

Where

avgArrayPower = radiation * cellEfficiency * arraySize * curvatureFactor / dayLength

cellEfficiency, arraySize, curvatureFactor = 0.32, 3, 0.95

radiation = 6060 * 3600

See SOC Models

[SOC Models](/stanford.edu/testduplicationsscp/home/sscp-2012-2013/strategy-2012-2013/luminos-soc-modeling)

## Read CSV File

[](#h.aboui5y6sua7)

power_produced.m found under strategy > Lumex > helpers

Edit to take in pre-processed insolation data, and return array power based on efficiency and m^2.

[](https://drive.google.com/folderview?id=1RFYaH5EI5iUggZyHkTBCzAJ5DkksAnji)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1RFYaH5EI5iUggZyHkTBCzAJ5DkksAnji#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1RFYaH5EI5iUggZyHkTBCzAJ5DkksAnji#list" frameborder="0"></iframe>

