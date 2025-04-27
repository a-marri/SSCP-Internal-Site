# SSCP - Installing SU2

# Installing SU2

This is a step-by-step tutorial for installing a fresh copy of SU2 on a Linux machine. This tutorial is written for someone who doesn't have a lot of experience poking around in the terminal, but ideally, since our meshes can only reasonably be run on a cluster with access to 100+ nodes, SU2 will only have to be installed once or twice per cycle by someone who knows what they're doing (maybe more than that if you use several cluster services.) Unless you have physical access to a server rack, you'll be doing this over ssh (so if you're a Windows user use your Linux partition, or Ubuntu for Windows which I honestly can't recommend enough for people new to Linux, or one of the toughbooks.) I'm going to assume that you know the most basic of terminal commands, how to use a text editor such as vim or emacs, how to copy files to a server using ftp, and that your machine has no sudo access and absolutely zero relevant software installed on it (on the off-chance you're trying to install this on either a fresh server, or a server where you can't access the programs for some reason, etc.) Please also take a moment to read through the SU2 github, the documentation seems sparse and overwhelming at first but is actually pretty good.

[ how to copy files to a server using ftp](/home/new-member-orientation/sftp-access)

[ SU2 github](https://github.com/su2code/SU2)

Let's get started.

Installing Python 2.7

SU2 uses Python 2, and this is a non-negotiable, if you try to run it with Python 3 you will get errors. One thing to watch out for in particular is that at the time of writing, Sabalcore's servers have by default the variable python pointing to Python 3, and the variable python2 pointing to Python 2.6 (where the standard is python points to 2 and python3 points to 3. Since all the SU2 .py files have a shebang line that references python, if you try to run SU2 without changing your $PYTHONPATH at all you'll run into trouble.) Additionally, if you're on a machine where you don't have sudo access, you probably want to install a python distribution anyway in your home directory because SU2 uses a lot of packages that may or may not be installed already on your server's copy of Python. Anaconda is a pretty good option and has all the packages you need, so that's what I'm going to recommend. You can download old versions of Anaconda here, make sure you grab Anaconda 2.3.0 because it comes with the correct version of Python (and get the version that matches your system architecture, assume _64 for 64 bits if you aren't sure if your machine is 64 or 32 bits, you can also check by typing uname -m, x86_64 is 64 bits and iXXX is 32 bits for Linux.) Copy the .sh file over to your server, and then execute it. If it refuses to execute, try chmod a+x filename then try again. Anaconda will ask you a couple questions, just answer yes to everything, and when it's done installing, answer yes again so that it automatically modifies your shell configs for you. After this is complete, you should be able to type which python in at any place under your home directory and see that the command python will refer you back to ~/anaconda/bin/python.

[ here](https://repo.continuum.io/archive/)

Installing OpenMPI

This step may not be necessary, but I'm including it for completeness. If this is your first time trying to install SU2, you may want to skip this step and use the mpicc and mpicxx executables located in the ~/anaconda/bin folder you just created. If you tried to compile SU2 and got an error along the lines of "your c++ compiler can't create executables", stop right there and return to this line. You may also find yourself needing to build OpenMPI if you're trying to set up on a machine that uses slurm or some other scheduler instead of pbs for job scheduling, and the MPI distribution on your server didn't happen to be configured for slurm. At any rate, if you're reading this it's because you want to know how to install OpenMPI, so grab the latest version and learn about build flags from here, drop the .tar.gz onto your Linux server and get going. After you've unzipped the folder (tar -xvf filename), navigate into the folder you just created and type ./configure. If you need OpenMPI to be installed in a folder other than the folder you're currently in, type ./configure --prefix=/some/other/path/you/already/created. After that finishes running, type make all install. Now it's time to check which mpicc and see if it matches the file folder path you just created, if not, go to Modifying your Shell and add a path variable such that the OpenMPI bin has preference over other files. If you're following this tutorial word-for-word and installed OpenMPI because you couldn't get the compilers Anaconda built to work, make sure you delete mpicc, mpicxx && mpirun from anaconda/bin so that the shell doesn't try to use them instead of your newly build OpenMPI compilers.

[ here](https://www.open-mpi.org/software/ompi/v3.1/)

Installing SU2

First, you need to pick and download a version of SU2 from the github releases page. As of right now, we only have working config files for SU2 version 4, (both Arctan and Sundae used some version of SU2 v4, config files are on ftp) and the final version of SU2v4 is 4.3.0, (4.2 has memory leak issues) so that's a pretty good bet. After downloading the relevant files, copy them over to your server.

[ github releases page](https://github.com/su2code/SU2/releases)

Next, you need to know the location of your MPI compilers for C++ and C. If you followed the instructions above, your MPI compilers are called mpicxx and mpicc respectively, and they're located in the /bin folder of whatever folder tree you created to install openmpi. You can find out if your server has a version of mpicc/mpicxx already installed by, again, typing which mpicc and then seeing what folder structure gets outputted to your shell. Your server may have a different, non-OpenMPI set of MPI compilers installed, such as Intel's mpiicc or MPICH's version, which is also, iirc, called mpicc. It is ABSOLUTELY CRUCIAL that your output for which compiler matches the path you input in your SU2 commands, because if a different path or a different version of mpi runs when you call SU2, instead of running 10 separate instances in parallel on 10 different nodes when you submit a job, you'll run 10 instances of the same program in serial on one node, and your SU2.out file will look like it's having a seizure. The full command for configuring SU2 correctly (for parallel and with the python wrapper enabled) on any given machine is ./configure --prefix=/path/you/want/for/SU2 --enable-mpi --with-cc=/full/path/from/root/not/home/to/mpicc --with-cxx=/full/path/from/root/not/home/to/mpicxx CXXFLAGS='-O3' --enable-PY_WRAPPER, but there's nothing I hate more than typing that out, so I recommend creating an alias for it in your shell so you can type something shorter (see Modifying your Shell).

Create an interactive job (qsub -I -V -l nodes=1:ppn=X, where X is the number of cores you want but you definitely don't need more than 4 and no you can't fold those flags together), navigate to your SU2 home directory, then type in your config command (the one on the Sabalcore clusters is config_SU2) and if you get an error about the compilers, stop and return to the Installing OpenMPI section. Once you are able to configure without errors, you can type make -j X all install or just make all install and then wait for a long long time (15-40 minutes) while SU2 compiles itself. Once it's complete, you'll need to add SU2_HOME and SU2_RUN to your path variables, SU2 will tell you the literal lines to add so it's almost foolproof, please see Modifying your Shell.

Modifying your Shell

Don't do this unless you really really know what you're doing, it's easy to break the shell and then make your machine completely inaccessible. If you suspect you've done your shell in and miraculously haven't logged out of all your terminals yet (or you still have an open sftp via Filezilla), find a way to copy a working .bashrc or whatever your shell config is called into your home directory and don't log out of that terminal until you confirm that you can log in and out and use basic programs like vim/ssh correctly on a different terminal window.

After making changes to your shell, none of them will be active on your current terminal (because the .bashrc or other config file is only read out on login), you'll need to logout and log back in (but if you're new to this, again, for safety, maybe just open a new terminal tab/window and log in to the server there to ensure that you can still do so.) If you are 100% sure that you haven't fucked the shell then there are commands you can use instead of full logout/login but honestly, if you can't figure out how to use google to find out what they are then you aren't ready to use them.

Bash

All bash settings can be changed from .bashrc.

Adding an Alias

Add a line to the bottom of .bashrc (located in ~) that says alias command="./executable -flags -more-flags SOME_INPUT /some/other/input/idk" to create a command called command that executes executable -flags -more-flags SOME_INPUT /some/other/input/idk when typed into your shell. You can use this for any command that is long and annoying to type/something you use a lot/whatever.

Setting an Environment Variable

You can create a new variable by adding export VARIABLE="value" to .bashrc. For instance, you might add export SU2_HOME="/d/05/sscpat02/SU2/SU2-4.3.0".

Modifying the Path Variable

In Linux, your $PATH environment variable determines where the shell searches for executable programs. You can create a new variable (which you could use to search for executables, for instance) following the instructions above. For instance, I created $MPI_RUN=/d/03/sscpat01/openmpi/bin. You can then add the variable to your path using something like export PATH=$MPI_RUN:$PATH. It's crucial that you include $PATH in any export PATH lines you add to your .bashrc, and the order variables are listed in is the order that bash checks for an executable. So if you have two copies of mpicc on your machine, one in $PATH and one in $MPI_PATH, if you list $MPI_PATH first you'll run $MPI_PATH/mpicc when you call mpicc, and if you list $PATH first you'll run $PATH/mpicc first.

TCSH

TCSH has multiple files that control the shell settings.

Adding an Alias

Navigate to ~ and open .tschrc.alias. Add the line alias command './executable -flags input' to the file.

Setting an Environment Variable

Navigate to ~ and open .tschrc.set. Add setenv VARNAME /whatever/the/variable/is to a new line in the bottom of the file.

These are the only shell instructions I'm including for now, because you'll almost certainly be on a machine running bash. TCSH is included because it's the shell for the login node for FarmShare (when you log into rice.stanford.edu), I may include more later in the cycle but for pretty much all shells the steps are very similar, just google "changing path for xxx", "adding an alias for xxx", etc where xxx is your shell. If you're unsure what your shell is, I always check by going to my home folder (cd ~), typing ls -la to see hidden files, (prefixed with a "." so they don't appear every time you're looking through your other files) and then reading through the hidden files to see what shell options are available/enabled. I only do this because sometimes there will be one shell on the login node and a different shell for the nodes in the cluster you submit jobs to, and you'll be able to see if this is the case by using the above method, but if you're only concerned about your current shell you can just type echo $SHELL.

Now that you've installed, check out running SU2!

