# SSCP - Fluent Simulations

# Fluent Simulations

Useful: 2012-2013 Fluent Page

[ 2012-2013 Fluent Page](/home/sscp-2012-2013/aero-2012-2013/fluent-set-up-and-usage)

Licensing

We have some number of HPC licenses available to us through Stanford Research. Our campus-wide Ansys contact is Arin Rouse, Arin.rouse@ansys.com.

You may need to be on the VPN for this to work. 

Server: cadlic0.stanford.edu

Ports: All defaults (1055 for Ansys) 

If this doesn't work, try license3.stanford.edu with the ports specified here. If that link doesn't work, check the PDF attached to this page.

[here](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/ANSYS)

## Ports

[](#h.cigfpfuiglp5)

Getting Ansys licencing to work through a firewall can be confusing. The usual problem is that only two of the three ports get opened through a firewall. The third port is not obvious based on the user only being required to set two port numbers in their environment as above. Further, by default this third port is not locked to a specific port number.

There are three TCP port numbers to consider.

* FlexLM lmgrd. This needs to run on port 1055 to be consistent with the Ansys manual. This port number corresponds to ANSYSLMD_LICENSE_FILE.Ansys Licensing Interconnect daemon, ansysli_server. This needs to run on port 2325 to be consistent with the Ansys manual. This port number corresponds to ANSYSLI_SERVERS.Ansys FlexLM vendor daemon ansyslmd. This can run on any available port. Ansys tools do not talk to this directly, but FlexLM tools require it. FlexLM tools get the port number by querying lmgrd.
* FlexLM lmgrd. This needs to run on port 1055 to be consistent with the Ansys manual. This port number corresponds to ANSYSLMD_LICENSE_FILE.
* Ansys Licensing Interconnect daemon, ansysli_server. This needs to run on port 2325 to be consistent with the Ansys manual. This port number corresponds to ANSYSLI_SERVERS.
* Ansys FlexLM vendor daemon ansyslmd. This can run on any available port. Ansys tools do not talk to this directly, but FlexLM tools require it. FlexLM tools get the port number by querying lmgrd.

* FlexLM lmgrd. This needs to run on port 1055 to be consistent with the Ansys manual. This port number corresponds to ANSYSLMD_LICENSE_FILE.
* Ansys Licensing Interconnect daemon, ansysli_server. This needs to run on port 2325 to be consistent with the Ansys manual. This port number corresponds to ANSYSLI_SERVERS.
* Ansys FlexLM vendor daemon ansyslmd. This can run on any available port. Ansys tools do not talk to this directly, but FlexLM tools require it. FlexLM tools get the port number by querying lmgrd.

FlexLM lmgrd. This needs to run on port 1055 to be consistent with the Ansys manual. This port number corresponds to ANSYSLMD_LICENSE_FILE.

Ansys Licensing Interconnect daemon, ansysli_server. This needs to run on port 2325 to be consistent with the Ansys manual. This port number corresponds to ANSYSLI_SERVERS.

Ansys FlexLM vendor daemon ansyslmd. This can run on any available port. Ansys tools do not talk to this directly, but FlexLM tools require it. FlexLM tools get the port number by querying lmgrd.

## Configuring the Ansys Licensing Interconnect Daemon

[](#h.bvs8h7toxnzc)

Just stick to the default port of 2325.

8/10/14: <Max> I've had quite a bit of trouble converging Pointwise meshes in Fluent - it appears that maximum cell skewness is causing convergence problems. A workaround for this is given in this post. It makes simulations slow, but they don't blow up - will post update if fixed mesh fixes problems.

[ this](http://www.cfd-online.com/Forums/fluent/44367-what-under-relaxation-factor.html#post140717)

"The [Ansys] campus licenses include ICEM CFD Meshing"

---------- Forwarded message ----------

From: Arin Rouse <arin.rouse@ansys.com>

[arin.rouse@ansys.com](mailto:arin.rouse@ansys.com)

Date: Mon, Nov 18, 2013 at 11:30 AM

Subject: Re: [solarcore]: ANSYS Assessment of Computing Needs

To: Guillermo Gomez <ggomez2@stanford.edu>

[ggomez2@stanford.edu](mailto:ggomez2@stanford.edu)

Hi Guillermo,

Thanks for forwarding this thread. I wanted to address a few of the topics mentioned. The campus licenses include ICEM CFD Meshing.

Make sure you have your members register for an ANSYS account providing access to tutorials, videos, etc... 

This can be done here:

Go to:   https://support.ansys.com/portal/site/AnsysCustomerPortal/student/template.REGISTER

[https://support.ansys.com/portal/site/AnsysCustomerPortal/student/template.REGISTER](https://support.ansys.com/portal/site/AnsysCustomerPortal/student/template.REGISTER)

Fill out the registration information - please be sure to use your student email address

you'll need some information about the school's account

Account number - 670021

Name of School - Stanford University

****************************

Professor Name - Sheri Sheppard

A great second source is the SimCafe through Cornell University. This site has great modules from basic to pretty advanced.

https://confluence.cornell.edu/display/SIMULATION/Home

[https://confluence.cornell.edu/display/SIMULATION/Home](https://confluence.cornell.edu/display/SIMULATION/Home)

Here's the full text of our license file from our license server:

# Server Hostname, flexlm hostid, and port (port shouldn't change)

##############################################################################

SERVER license3.Stanford.EDU 005056854406 27035

[license3.Stanford.EDU](http://license3.stanford.edu/)

############################################################################## 

# Vendor License Binary

############################################################################## 

VENDOR ansyslmd /usr/local/bin

##############################################################################

# Licensed Products

##############################################################################

# Products licensed in this file:

# 1. ANSYS Academic Research (25 Tasks): 10 task(s) Lease expiring 14-Sep-2014 Customer # 670021

INCREMENT aa_mcad ansyslmd 9999.9999 14-sep-2014 250 85A8C486BC8B \

    VENDOR_STRING=customer:00670021 SUPERSEDE ISSUER=SIEBEL \

    ISSUED=12-sep-2013 START=12-sep-2013 SIGN2="0074 8947 372C \

    DDA2 D9AC 5117 B264 9B00 CAFB 4532 1EE9 8604 A188 8CB1 DE28"

INCREMENT aa_r ansyslmd 9999.9999 14-sep-2014 250 CE187DCF4018 \

    VENDOR_STRING=customer:00670021 SUPERSEDE ISSUER=SIEBEL \

    ISSUED=12-sep-2013 START=12-sep-2013 SIGN2="00C9 EE57 B8C4 \

    A0DB 1476 5475 3DBC 0C00 0C6F CBEA 10B3 0B09 DD6E 0ECE 90AB"

I don't think it's valid for anything other than the host license3.stanford.edu

[license3.stanford.edu](http://license3.stanford.edu/)

Guillermo, you can try to point your software to license3.stanford.edu port 27035

[license3.stanford.edu](http://license3.stanford.edu/)

This is the only thing we have for ANSYS, and all the ANSYS software installed in FarmShare just points to this license server.

https://www.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/ANSYS

[https://www.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/ANSYS](https://www.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/ANSYS)

[](https://drive.google.com/folderview?id=1xafjLlHQKCFIxCdjJiMtlqFhhVq8RKaK)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1xafjLlHQKCFIxCdjJiMtlqFhhVq8RKaK#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1xafjLlHQKCFIxCdjJiMtlqFhhVq8RKaK#list" frameborder="0"></iframe>

