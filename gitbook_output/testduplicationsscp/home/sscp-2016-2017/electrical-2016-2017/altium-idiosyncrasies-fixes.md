# altium-idiosyncrasies-fixes

## SSCP - Altium Idiosyncrasies & Fixes

## Altium Idiosyncrasies & Fixes

### All of the libraries disappear

Problem: I had libraries installed, but they wouldn't appear under the library tab or when I went to place a part.&#x20;

Solution: Use the uninstaller to wipe all of the preferences, _do not_ import your preferences, and manually set them again.&#x20;

### None of the dblibs will open

Problem: My dblibs will appear empty or will not open.

Solution: Altium uses Microsoft access engine 2007, as included in Microsoft Office 2007. No kidding. Since most people don't have Microsoft Office 2007, you should install the system driver to enable data connectivity, e.g. your dblibs working. In past cycles, when Altium was 32-bit, you only needed the 32-bit AccessDatabaseEngine to get the dblibs working, but since Altium has now (finally) upgraded to being 64-bit, you now need both engines operating in tandem, but Microsoft will try to prevent you from doing this. Please follow the steps outlined below so that you can continue using our resistor libraries :^)

Step 1. Go to this link, click the "download" option, then select both AccessDatabaseEngine.exe (32-bit) and AccessDatabaseEngine\_X86.exe (64-bit) for download. If you've had Altium up and working on your machine since before Sunrise cycle, only download the 64-bit version and skip to step 3.

[this link](https://www.microsoft.com/en-us/download/details.aspx?id=13255)

Step 2. After both have completed downloading, install the 32-bit version _first_ by double-clicking on the executable.

Step 3. After the 32-bit version is installed, the 64-bit will throw an error if you try to run it, so open a Windows command prompt window (search bar, cmd.exe) and then type the full path to your 64-bit executable followed by the flag /passive switch to override this error (i.e. "C:\Users\<username>\Downloads\AccessDatabaseEngine\_X64.exe /passive"

Step 4. Roll your eyes at Altium. This step is crucial.

Step 5. Go to your registry editor (search bar, regedit.exe) and navigate to the Microsoft Office 14 folder ("HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Office\14.0\Common\FilesPaths".) If you see an entry there labeled mso.dll, delete it. Otherwise, do nothing.
