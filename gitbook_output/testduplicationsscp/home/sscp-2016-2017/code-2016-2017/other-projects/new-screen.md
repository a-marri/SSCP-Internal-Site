# new-screen

## SSCP - New Screen

## New Screen

Datasheet

http://www.newhavendisplay.com/specs/NHD-0216KZW-AG5.pdf

Investigate spi on board. Try to get board to board communication. Find a good library.

NOTES:

To use screen:

&#x20;   1\) follow initialization sequence for 8-bit mode (on data sheet; see "Screen\_Init()" in button\_board)

&#x20;   2\) send commands (check if busy before sending each command; see "Send\_Command(uint16\_t data)")

To send commands:

&#x20;   1\) follow instruction description for format (each instruction described using 10 bits on data sheet)

&#x20;   2\) pad the 10 bits from (1) above with six 0's (create 16 bits total)

&#x20;   3\) convert to hexadecimal and send command (see "Send\_Command(uint16\_t data)")

To create/display custom characters:

&#x20;   0\) optional: turn cursor off

&#x20;   1\) set CGRAM address (0x00 to 0x07 or 0x08?)

&#x20;   2\) write data to CGRAM (line-by-line, turning pixels on/off)

&#x20;   3\) set DDRAM address (i.e. cursor position)

&#x20;   \*) optional: turn cursor on&#x20;

&#x20;   4\) send command from (1) above&#x20;
