# SSCP - DigikeyBOM_tips

# DigikeyBOM_tips

For Admin use only when ordering for solar car digikey account.

1. Load BOM into Excel

2. Use Excel command such as =IF(ISNA(MATCH(U7,E$2:E$249,0)),"No Duplicate","Duplicate") by copying part numbers to another column to find duplicate part numbers

3. Possibly add board if doing multiple orders to the designator field by paste special->add to the designator field

3. consolidate

4. go to BOM manager in digikey

5. import BOM including customer reference as designator field

6. Export file and use the =IF(ISNA(MATCH(U7,E$2:E$249,0)),"Not Imported","Imported") to compare part numbers or customer references digikey included. (it does not always import all in an excel sheet)

7. Hit Place Order.

8. Go back to main menu, then go to web history

9. Finish order.

