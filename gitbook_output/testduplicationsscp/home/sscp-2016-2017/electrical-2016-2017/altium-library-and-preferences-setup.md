# SSCP - Altium Library and Preferences Setup

# Altium Library and Preferences Setup

Note: Altium recently released a 64 bit version, whereas this set of instructions was written when only the 32 bit version

was available. Depending on the version you download (32 bit or 64 bit) and the version of Microsoft office you are using, you may need to take some additional steps in order for some of our libraries to function properly.

Read here for more information:Using DbLibs with 32-bit or 64-bit Altium

[Using DbLibs with 32-bit or 64-bit Altium](http://www.altium.com/documentation/18.0/display/ADES/Using+Database+Libraries+with+32-bit+and+64-bit+Altium+Design+Software+on+the+same+Computer)

Download this Office plugin: Microsoft Office Plugin

[Microsoft Office Plugin](http://www.microsoft.com/download/en/confirmation.aspx?id=23734)

Follow these instructions to set up some basic Altium preferences and our libraries:

* open altiumDXP->preferences->system->view->check open internet links in external web browser, middle click to close document tab if you wantsystem->default locations, change document path to C:\sundae\electrical\projects, change library path to C:\sundae\electrical\librariesdata management->installed librariesmake sure “library path relative to” and make sure same as in (c)Remove all existing librariesAdd all files from schlib and pcblib (make sure viewing “all files”)go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)don’t worry about intlib right nowdata management->templates: set location to C:\sundae\electrical\templates\deutsch_templatedata management->suppliers: only check Mouser, DigiKeypcb editor->defaults->double click component-> designator font: select true type, arial, bold, change height to 40 milthen hit ok
* open altium
* DXP->preferences->system->view->check open internet links in external web browser, middle click to close document tab if you want
* system->default locations, change document path to C:\sundae\electrical\projects, change library path to C:\sundae\electrical\libraries
* data management->installed librariesmake sure “library path relative to” and make sure same as in (c)Remove all existing librariesAdd all files from schlib and pcblib (make sure viewing “all files”)go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)don’t worry about intlib right now
* make sure “library path relative to” and make sure same as in (c)
* Remove all existing libraries
* Add all files from schlib and pcblib (make sure viewing “all files”)
* go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)
* don’t worry about intlib right now
* data management->templates: set location to C:\sundae\electrical\templates\deutsch_template
* data management->suppliers: only check Mouser, DigiKey
* pcb editor->defaults->double click component-> designator font: select true type, arial, bold, change height to 40 mil
* then hit ok

1. open altium
2. DXP->preferences->system->view->check open internet links in external web browser, middle click to close document tab if you want
3. system->default locations, change document path to C:\sundae\electrical\projects, change library path to C:\sundae\electrical\libraries
4. data management->installed librariesmake sure “library path relative to” and make sure same as in (c)Remove all existing librariesAdd all files from schlib and pcblib (make sure viewing “all files”)go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)don’t worry about intlib right now
5. make sure “library path relative to” and make sure same as in (c)
6. Remove all existing libraries
7. Add all files from schlib and pcblib (make sure viewing “all files”)
8. go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)
9. don’t worry about intlib right now
10. data management->templates: set location to C:\sundae\electrical\templates\deutsch_template
11. data management->suppliers: only check Mouser, DigiKey
12. pcb editor->defaults->double click component-> designator font: select true type, arial, bold, change height to 40 mil
13. then hit ok

open altium

DXP->preferences->system->view->check open internet links in external web browser, middle click to close document tab if you want

system->default locations, change document path to C:\sundae\electrical\projects, change library path to C:\sundae\electrical\libraries

data management->installed libraries

1. make sure “library path relative to” and make sure same as in (c)
2. Remove all existing libraries
3. Add all files from schlib and pcblib (make sure viewing “all files”)
4. go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)
5. don’t worry about intlib right now

make sure “library path relative to” and make sure same as in (c)

Remove all existing libraries

Add all files from schlib and pcblib (make sure viewing “all files”)

go to dblib and add resistor and sscp libraries (“altium database library” NOT excel files)

don’t worry about intlib right now

data management->templates: set location to C:\sundae\electrical\templates\deutsch_template

data management->suppliers: only check Mouser, DigiKey

pcb editor->defaults->double click component-> designator font: select true type, arial, bold, change height to 40 mil

then hit ok

Finally, to edit which fields appear in the component search for the dblib (capacitor_auto and resistor) libraries:

1. Activate the "Libraries" workspace panel by selecting View->Workspace Panels->System->Libraries

2. If the libraries window does not immediately pop up, select the Libraries panel by clicking on the tab on the right hand side of the schematic editing window.

3. Right click on one of the columns in the row under the grey "drag a column header here to group that by column" and click on "Select Columns"

4. Pick which columns you would like to see (usually Value (Human Readable), Package, Voltage/Power)

