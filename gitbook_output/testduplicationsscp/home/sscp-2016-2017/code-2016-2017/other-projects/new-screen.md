# SSCP - New Screen

# New Screen

Datasheet

http://www.newhavendisplay.com/specs/NHD-0216KZW-AG5.pdf

Investigate spi on board. Try to get board to board communication. Find a good library.

NOTES:

To use screen:

    1) follow initialization sequence for 8-bit mode (on data sheet; see "Screen_Init()" in button_board)

    2) send commands (check if busy before sending each command; see "Send_Command(uint16_t data)")

To send commands:

    1) follow instruction description for format (each instruction described using 10 bits on data sheet)

    2) pad the 10 bits from (1) above with six 0's (create 16 bits total)

    3) convert to hexadecimal and send command (see "Send_Command(uint16_t data)")

To create/display custom characters:

    0) optional: turn cursor off

    1) set CGRAM address (0x00 to 0x07 or 0x08?)

    2) write data to CGRAM (line-by-line, turning pixels on/off)

    3) set DDRAM address (i.e. cursor position)

    *) optional: turn cursor on 

    4) send command from (1) above 

