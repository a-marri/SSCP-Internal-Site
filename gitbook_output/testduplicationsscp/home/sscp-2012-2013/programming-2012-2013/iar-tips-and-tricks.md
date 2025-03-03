# SSCP - IAR Tips and Tricks

# IAR Tips and Tricks

To make a copy of an existing project:

- copy all project files to new folder. 

- remove workspace files from new folder (*.eww and ./settings/*.wsdt, NOT *.ewp.wsdt) 

- from IAR, create a new workspace (by exiting out of your current one), click project->add existing project, select the *.ewp file in the new project folder. 

- Save workspace in new project folder. 

If your code will not start when you power cycle:

Make sure you have no calls to printf in your code.  Calls to printf that go to IAR's terminal I/O (when you haven't written your own putchar) cannot run outside of debug mode.

If your variables aren't showing up in watch:

The compiler is probably optimizing them out. Go to project options -> C/C++compiler -> Optimizations -> Turn optimizations off.

Packing structs:

IAR uses a different keyword for struct packing than GCC.

[ keyword](http://netstorage.iar.com/SuppDB/Public/SUPPORT/005609/Example%205.pdf)

[If you don't know what struct packing is, don't worry about this.]

If your printfs aren't showing up:

Make sure you have \n at the end of the line.  It won't flush it out otherwise.

