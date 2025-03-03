# SSCP - Cell Level Bypass Diodes

# Cell Level Bypass Diodes

Diode we're using: https://www.microsemi.com/existing-parts/parts/136636#docs-specs

How to use it: solder the side with the dot to the positive side of the cell. Make sure you put kapton tape (or some other insulating, high-temp tape) beneath where the wire/tab will touch the cell.

Sasha mentioned these at a design review: http://www.vishay.com/docs/49058/49058.pdf

[http://www.vishay.com/docs/49058/49058.pdf](http://www.vishay.com/docs/49058/49058.pdf)

When a single cell in a string is shaded, the entire string's power output is reduced. If the shaded cell can be bypasses, the rest of the cells can continue to function at full power, reducing the net loss.

Toby Sachs-Quintana, the 2012-2013 array lead, placed this high on his list of future improvements. In particular, it mitigates bubble shading. Toby proposed this diode (linked). This diode has low forward voltage drop and is low profile. We have proceeded with this diode until it makes sense to do an exhaustive part search and optimization.

[ this diode (linked)](http://www.digikey.com/product-detail/en/stmicroelectronics/STPS30L30DJF-TR/497-12867-1-ND/3043778)

Key question: What is the maximum performance benefit of cell level bypassing? (Use ShellPower)

Key question: Will putting extra stuff in the encapsulation degrade cell reliability? Particularly crack resistance.

As stated on the Gochermann call page (linked), he can bypass at the single cell level with 50 mV forward voltage diodes.

[Gochermann call page (linked)](/stanford.edu/testduplicationsscp/home/sscp-2016-2017/array-2016-2017/meetings-and-conversations/skype-call-with-oliver-gochermann)

SSCP has pursued the concept of putting flex PCB's with a bypass diode across the back of the cell and soldering to the tabs. This was prototyped by hand modifying/soldering the flat Alphawire used for the array. A mechanical test did not break the cell during the encapsulation process as evidenced by EL testing. An electrical test resulted in a direct short between the tabs during the encapsulation process.

## Thermal design:

[](#h.43ul13rhv8by)

Thermals will likely be the driving factor for integrated bypass diode design. Every diode must be capable of operating at maximum array current and maximum array temperature at the same time.

