# SSCP - Realtime Weather Forecast

# Realtime Weather Forecast

NOAA

A list of publicly available weather data

http://www.ncdc.noaa.gov/oa/wct/data.php

Here are the steps for downloading realtime forecast data.

1. Fetch global realtime weather forecasts here
2. Download the NOAA Weather and Climate Toolkit here
3. Load the data in the Toolkit (aah... pretty...)

Fetch global realtime weather forecasts here

[ here](http://motherlode.ucar.edu:8080/thredds/ncss/grid/fmrc/NCEP/GFS/Global_0p5deg/NCEP-GFS-Global_0p5deg_best.ncd/dataset.html)

Download the NOAA Weather and Climate Toolkit here

[ here](http://www.ncdc.noaa.gov/oa/wct/install.php)

Load the data in the Toolkit (aah... pretty...)

_______________________________________________

Batch Processing .nc files 

http://www.ncdc.noaa.gov/oa/wct/batch.php

Exports to ArcInfo ASCII Grid Format (http://en.wikipedia.org/wiki/Esri_grid)

Sample command: (note, <output> must have the correct file type, otherwise you get a StringIndexOutOfBoundsException...)

wct-3.6.6/wct-export NCEP-GFS-Global_0p5deg_best.ncd.nc testOutput2.asc asc wctBatchConfig.xml

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WEATHERZONE

1. Access to Weatherzone Business for all weather data (excluding solar input and detailed cloud)

2. Access to the FTP for solar insolation and detailed cloud (total %, low/medium and high)

3. See attached "Stanford Weather Map" for the geographic zones within Australia.

I have already set you up with access to Weatherzone Business. Access the Opticast tab and scroll down, here you can setup your own csv downloads - click update and save the URL for regular scheduled updates. Note that the system updates every single hour so a fetch every 30 mins should suffice (for the race great if you have 3G/Sat internet connection? - But not crucial as the forecasts have lead times to 14 days if you need- note: 7 for solar). I can go into much more detail on Opticast once you have been playing with it - ie its strengths and weaknesses. 

Here are the login details for 1.Weatherzone Business:

URL: http://pro.weatherzone.com.au

[http://pro.weatherzone.com.au](http://pro.weatherzone.com.au/)

User: pochuan@stanford.edu

[pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Pass: stanfordwx

Also,

Username: stanfordsolar

Password: i676euW0

FTP Host: ftp.theweather.com.au

[ftp.theweather.com.au](http://ftp.theweather.com.au/)

HTTP URL: http://clients.theweather.com.au/stanfordsolar/data

[http://clients.theweather.com.au/stanfordsolar/data](http://clients.theweather.com.au/stanfordsolar/data)

[](https://drive.google.com/folderview?id=1mhEPP5-Qw6Xndsg5EZ6Z3C1dc3jL1NoH)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1mhEPP5-Qw6Xndsg5EZ6Z3C1dc3jL1NoH#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1mhEPP5-Qw6Xndsg5EZ6Z3C1dc3jL1NoH#list" frameborder="0"></iframe>

