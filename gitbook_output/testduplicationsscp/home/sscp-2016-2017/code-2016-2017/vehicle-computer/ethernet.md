# SSCP - Ethernet

# Ethernet

Meeting notes:

We decided a while ago to ditch the old Catalog system and implement one based on ethernet.

The new system will take inspiration from the Catalog.

It should involve background broadcasting in the same spirit of the CAN subscribe method.

Every Board should have a large struct representing all of the variables tracks.

There should be a constants list in lib

We can use protobufs to serialize and send the data.

Make sure not to Don’t

 

 

 

P.S. Use ubiquity for hardware

END MEETING NOTES

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

Our base board extension has ethernet compatibility:

Base_Board_link

[Base_Board_link](http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-3rd-party-evaluation-tools/stm32f4dis-ext.html)

Heres the user manual:

Manual Link

[Manual Link](https://www.element14.com/community/docs/DOC-51124?ICID=knode-STM32F4-bboarduser)

Found example code for ethernet:

example code

[example code](https://www.element14.com/community/docs/DOC-54872?ICID=knode-STM32F4-bboardse)

(Also assumes we have other extension boards such as a screen, should comment those out)

