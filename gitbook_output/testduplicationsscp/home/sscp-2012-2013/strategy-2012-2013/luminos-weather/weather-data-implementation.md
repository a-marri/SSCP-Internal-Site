# weather-data-implementation

## SSCP - Weather Data Implementation

## Weather Data Implementation

Current implementation plans:

1. Write a cron job that automatically fetches data from this site:

http://www.ncdc.noaa.gov/oa/wct/tutorials/?file=advanced-dataexporter

2. Figure out how to parse raw data.&#x20;

Use the WTC Batch Processing tool&#x20;

http://www.ncdc.noaa.gov/oa/wct/batch.php#Exporter

Use commands like: wct-3.6.6/wct-export NCEP-GFS-Global\_0p5deg\_best.ncd.nc testOutput.txt ASC wctBatchConfig.xml

3. send to db/matlab .mat file stored on aws.&#x20;

Info on calling matlab functinos through python:

https://code.google.com/p/danapeerlab/source/browse/trunk/freecell/depends/common/python/matlabcom.py?r=97

Source of Data:

http://www.ncdc.noaa.gov/oa/wct/data.php

[http://www.ncdc.noaa.gov/oa/wct/data.php](http://www.ncdc.noaa.gov/oa/wct/data.php)

Data Info page:

http://motherlode.ucar.edu:8080/thredds/catalog/grib/NCEP/GFS/Global\_0p5deg/catalog.html?dataset=grib/NCEP/GFS/Global\_0p5deg/best

Currently fetching:&#x20;

http://motherlode.ucar.edu:8080/thredds/ncss/grid/grib/NCEP/GFS/Global\_0p5deg/best/dataset.html

Longitude/Latitude of Route:

N: -10.336536

W: 128.144531

E: 141.481934

S: -39.232253
