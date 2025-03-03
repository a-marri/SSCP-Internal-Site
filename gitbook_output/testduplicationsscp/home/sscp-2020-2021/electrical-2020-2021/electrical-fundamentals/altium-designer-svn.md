# SSCP - Altium Designer - SVN

# Altium Designer - SVN

Introduction

Subversion (SVN) offers both centralized storage and revision control for multiple users. It's an effective way to pursue engineering projects with multiple contributors. 

It allows us to see who made changes and when. For plaintext files it can also summarize the differences between versions of files as well as merge conflicted versions. 

In the past, we have used SVN for software, electronics, and mechanical systems. As of the 2020-2021 cycle, only the electrical team still uses SVN.

Gaining access

To gain access to the SVN repository, you'll need to ask any server administrator to add you to the list of approved SVN users. Right now that's Simon Acker (email) and Maisam Pyarali (email). 

[email](mailto:simonack@stanford.edu)

[email](mailto:maisam@stanford.edu)

Once you have been given access to the SVN repository, you will be able to login via Stanford's SUnet system using the same username and password as the one you use for Axess.

Using the SVN Repository

The idea behind a Version Control System (VCS) like SVN is to enable multiple people to independently modify a set of files, in this case Altium schematics and PCBs, in a simple, streamlined way.

To utilize the SVN repository, you will need to consider the system you are using. On Windows, the easiest way is to use TortoiseSVN. On Linux systems you should consult the documentation for your distribution to install the official 'subversion' package.

[ TortoiseSVN](http://tortoisesvn.net)

Note: Altium Designer has SVN software built into it. You are welcome to utilize it (see more here). As a team, we utilize TortoiseSVN because it offers better integration with File Explorer and easier library management. Even if you use TortoiseSVN or another program, you may notice that Altium's internal SVN notices when you are working with files checked-out from an SVN repository. For example, Altium may recognize that you have checked-out and then altered a file by putting a red circle next to it in the Project panel. This is fine. You are welcome to ignore Altium's internal SVN system.

[ here](/stanford.edu/testduplicationsscp/home/sscp-2020-2021/electrical-2020-2021/electrical-fundamentals/svn-using-altiums-internal-svn-tools)

Guides:

How to use TortoiseSVN (Recommended)

[How to use TortoiseSVN (Recommended)](/stanford.edu/testduplicationsscp/home/sscp-2020-2021/electrical-2020-2021/electrical-fundamentals/svn-using-tortoisesvn)

How to use Altium's Internal SVN Tools

[How to use Altium's Internal SVN Tools](/stanford.edu/testduplicationsscp/home/sscp-2020-2021/electrical-2020-2021/electrical-fundamentals/svn-using-altiums-internal-svn-tools)

How to use subversion (linux)

[How to use subversion (linux)](https://www.tutorialspoint.com/svn/index.htm)

Before working with SVN, make sure you look at SVN Protocol/Etiquette!!

[SVN Protocol/Etiquette](/stanford.edu/testduplicationsscp/home/sscp-2020-2021/electrical-2020-2021/electrical-fundamentals/svn-best-practices)

