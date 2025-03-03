# SSCP - Cell Binning 2017

# Cell Binning 2017

Binning 4/14/17 (John's birthday!)

Data is attached as Binning Data v1.xlsx and Binning 4_14_17 IV Curves.zip -- note that the I_sc changed notably on the 47th cell. When we binned, we split this into two datasets based on the I_sc change (so one was cells 1-46 and the other was 47-100), found the difference between the average values, and then used that to correct the second set. This worked fairly well, but we still saw the I_sc fall a little bit at the end of the second set. 

The final bins were: 

Ultra high: I_sc at 6.195 A and above

Race: 6.18-6.195 is race

Secondary: 6.16 - 6.18

Trash: below 6.16

The idea behind the ultra high bin (lol) was that the angle of the cells is actually pretty significant; even a one or two degree difference can result in a 1% difference in current. Since all of our strings have cells on the edge of the car (where they will be a bit curved), we figured that those cells will likely be the limiting cells. So, we're better off having better cells there since it's the worst cell (current-wise) that determines when you start current limiting. 

The qualitative splits between bins was that Ultra and Trash were fairly small; race was the largest by far; and secondary was a pretty good size as well (but smaller than race). 

In the future, the current plan is to designate 10 reference cells and retest them next time. From that, we'll get an average value. We will record the bin edges by % difference from the average value, and then bin based on that (so that we get relatively constant bins). The flash tester is not going to be accurate enough to give us good absolute values, but it can definitely do good reference values. 

[](https://drive.google.com/folderview?id=1q6Ci-2ivaZ76F4g-u-EdwDmYeTiaTpq4)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1q6Ci-2ivaZ76F4g-u-EdwDmYeTiaTpq4#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1q6Ci-2ivaZ76F4g-u-EdwDmYeTiaTpq4#list" frameborder="0"></iframe>

