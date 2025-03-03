# SSCP - SVN - Installing SSCP Libraries (OLD)

# SVN - Installing SSCP Libraries (OLD)

***DEPRECATED***

1. Follow the tutorial for setting up SVN access to our repositories (Windows, Linux)

[Windows](/stanford.edu/testduplicationsscp/home/sscp-2020-2021/electrical-2020-2021/electrical-fundamentals/svn-using-tortoisesvn)

[ Linux](https://www.tutorialspoint.com/svn/index.htm)

2. Check out the sunkissed repository (repository URL can be found on the Windows SVN install page above)

3. Open Altium Designer

4. Click the gear in the upper right corner of the main Altium window (this opens Altium's main preferences windows)

5. In the preferences window that opens navigate to "Data Management"->"File-based Libraries".

6. Click "Install..." and then "Install from file..."

7. In the File Explorer window that opens, navigate to the folder where you checked-out the sunkissed repository.

8. Once inside the sunkissed repository, go to "electrical"->"libraries" and then select "sscp.DbLib". Note: If you cannot see sscp.DbLib, make sure you have "all files" selected in the bottom right dropdown.

9. Once you have selected "sscp.DbLib", click "Open". This will install our database library, which is a compilation of all of our libraries. If it was installed correctly, you should see sscp.DbLib listed.

10. That's it! You should now be able to select and place components from our libraries using the "Components" panel.

