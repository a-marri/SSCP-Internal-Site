# SSCP - Writing to flash memory

# Writing to flash memory

Writing to flash memory is possible through ‘eeprom emulation’. ST offers sample code for eeprom emulation

-info sheet: https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDo0M2YzNDVkY2VmYjUwZjRj

[ https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDo0M2YzNDVkY2VmYjUwZjRj](https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDo0M2YzNDVkY2VmYjUwZjRj)

-sample code download:

https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDoyZmM3ODM1NjQ5NGRmMA

[https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDoyZmM3ODM1NjQ5NGRmMA](https://docs.google.com/a/stanford.edu/viewer?a=v&pid=sites&srcid=c3RhbmZvcmRzb2xhcmNhci5jb218c3NjcHxneDoyZmM3ODM1NjQ5NGRmMA)

Note that, although the eeprom.h and eeprom.c were built on this sample code, the implementation has been changed significantly. I found the sample code to fail to deliver the amount of read/writes it offered (since it relied on reading the header addresses on every write, effectively limiting us to 10k writes/reads) and not to suit our needs because it operated on arrays.

Our custom system includes a task writeToFlash() function that provides a structure for how to write with eeprom. However it is the same as simply using the exported functions EEWriteVariable() and EEReadVariable() elsewhere in code.

While the sectors can theoretically hold near 10,000 distinct variables, I recommend staying below that. Every 20,000 reads the system will call a transfer function that will need at most (numberOfVariables*20,000) operations.

In depth:

At a high level eeprom.h/c writes to sectors in memory, their addresses can be found in page 61 of

http://cdn.sparkfun.com/datasheets/Dev/dotNET/DM00031020RM.pdf

[http://cdn.sparkfun.com/datasheets/Dev/dotNET/DM00031020RM.pdf](http://cdn.sparkfun.com/datasheets/Dev/dotNET/DM00031020RM.pdf)

They are defined in eeprom.h and their size is calculated from this. The system benefits from the use of these sectors because it calls FLASH_EraseSector() which can delete large blocks of data much faster than if we were to try to do so word by word. In order to prevent our program heap, stack etc. from growing into these sectors I have overwritten the shared linker file with a local one, which limits the Rom to right before our first sector.

Writing and reading: The basic principle is the same as in the sample code and is illustrated in page 11 of the info sheet. It basically stores a half word of data and uses another half word to indicate a ‘virtual address’ to identify it. This virtual address is supplied by the user. When the user ‘re-writes’ a variable (aka when he/she calls EEWriteVariable with a virtAddress parameter that has already been used) instead of looking for that address in our sector, it simply writes the new variable & virtAddress in the first empty space available. When EEReadVariable() is called it searches for the address starting from the first empty slot and traverses backwards until it finds it.

The reason for this instead of simply writing and reading on the physical memory address every time is that flash memory has a limited number of re-writes (at least 10,000 according to the MCU’s data sheet). This may seem like a lot, but consider logging a variable every second and you end up getting less than 3 hours of use before it is corrupted.

But what about when the sector fills up? We could go back and start writing from the beginning but then we risk losing data that may not have been updated since then. Instead we have two sectors of identical sizes. When one fills up, the data is transferred to the other.

Transfering: Each sector has a header, which is a halfword containing either

0x0000: page available for write,

0xEEEE: page available for write during transfer if 0x0000 is full or

0xFFFF for page empty.

EEPageTransfer() reads backwards from the available of sector to looking for the highest virtaddress. It searches for its latest copy in the same way EEReadVariable does. Then it searches for data with that max virtAddress-1 and so on and so forth until it gets to 0. Notice that this unfortunately suffers in that if, for example, a user simply only stored one variable with the virtAddress of 100 we would need to traverse the sector this 100 times until the program is allowed to exit. Because of this EEPageTransfer is our slowest operation and a lot of care is taken to fix transfers that did not finish (because of power loss etc) in EE_Init()

EE_Init: the mechanics of this are pretty straight forward from code. It tries to restart transfer when it finds it halfway. If it needs to choose between possibly corrupt data and a complete erase, it will opt for a complete erase.

[](https://drive.google.com/folderview?id=1oHT-wZSaJRgywDrPOIaBj6BBUrVe-qS1)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1oHT-wZSaJRgywDrPOIaBj6BBUrVe-qS1#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1oHT-wZSaJRgywDrPOIaBj6BBUrVe-qS1#list" frameborder="0"></iframe>

