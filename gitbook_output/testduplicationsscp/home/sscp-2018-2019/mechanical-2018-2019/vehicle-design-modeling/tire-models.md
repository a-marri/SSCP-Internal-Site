# SSCP - Tire Models

# Tire Models

Goals for the Cycle: Develop a tire model accurate enough for dynamic vehicle modeling under a variety of slip conditions up to and including non-linear tire behavior; validate the tire model on a more sensor-equipped vehicle than Sundae; document model of Michelin tires and process for future use.

Timeline of Progress (working)

Late spring/early summer 2018

* Initial research into adapting existing brush/Fiala tire models for solar car purposesReached out to experts in the field to get a better feel for the differences between the solar tire and a standard tire, or standard bicycle & motorcycle tiresresearch cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.Reached out to Michelin asking for data and/or help
* Initial research into adapting existing brush/Fiala tire models for solar car purposes
* Reached out to experts in the field to get a better feel for the differences between the solar tire and a standard tire, or standard bicycle & motorcycle tiresresearch cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.
* research cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.
* Reached out to Michelin asking for data and/or help

* Initial research into adapting existing brush/Fiala tire models for solar car purposes
* Reached out to experts in the field to get a better feel for the differences between the solar tire and a standard tire, or standard bicycle & motorcycle tiresresearch cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.
* research cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.
* Reached out to Michelin asking for data and/or help

Initial research into adapting existing brush/Fiala tire models for solar car purposes

Reached out to experts in the field to get a better feel for the differences between the solar tire and a standard tire, or standard bicycle & motorcycle tires

* research cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.

research cited by one that it's nearly impossible to get a good bike/motorcycle tire model with the brush/Fiala equations. We assume this carries over to solar tires as well.

Reached out to Michelin asking for data and/or help

July/August 2018

* Michelin sent TIR files for tires at 2 pressures (4 bar/5 bar). Began researching Pacejka models & trying to find a program that could read our data without paying money, eventually gave up and began trying to write custom Pacejka model + file reader.Michelin not responsive to further inquiries.Continued talking to tire experts; looked into ways to pull brush model parameters out of the Magic Formula data. This is still something that is maybe doable, and could be compared to the MF model down the road
* Michelin sent TIR files for tires at 2 pressures (4 bar/5 bar). Began researching Pacejka models & trying to find a program that could read our data without paying money, eventually gave up and began trying to write custom Pacejka model + file reader.Michelin not responsive to further inquiries.
* Michelin not responsive to further inquiries.
* Continued talking to tire experts; looked into ways to pull brush model parameters out of the Magic Formula data. This is still something that is maybe doable, and could be compared to the MF model down the road

* Michelin sent TIR files for tires at 2 pressures (4 bar/5 bar). Began researching Pacejka models & trying to find a program that could read our data without paying money, eventually gave up and began trying to write custom Pacejka model + file reader.Michelin not responsive to further inquiries.
* Michelin not responsive to further inquiries.
* Continued talking to tire experts; looked into ways to pull brush model parameters out of the Magic Formula data. This is still something that is maybe doable, and could be compared to the MF model down the road

Michelin sent TIR files for tires at 2 pressures (4 bar/5 bar). Began researching Pacejka models & trying to find a program that could read our data without paying money, eventually gave up and began trying to write custom Pacejka model + file reader.

* Michelin not responsive to further inquiries.

Michelin not responsive to further inquiries.

Continued talking to tire experts; looked into ways to pull brush model parameters out of the Magic Formula data. This is still something that is maybe doable, and could be compared to the MF model down the road

September 2018

* Got a Pacejka model running but slightly buggy (negative slip angles lead to weird behavior)source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdfTalked with John Subosits from DDL about the model. some takeaways: most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 
* Got a Pacejka model running but slightly buggy (negative slip angles lead to weird behavior)source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf
* source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.
* http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf
* Talked with John Subosits from DDL about the model. some takeaways: most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 
* most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.
* As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.
* Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 

* Got a Pacejka model running but slightly buggy (negative slip angles lead to weird behavior)source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf
* source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.
* http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf
* Talked with John Subosits from DDL about the model. some takeaways: most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 
* most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.
* As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.
* Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 

Got a Pacejka model running but slightly buggy (negative slip angles lead to weird behavior)

* source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.
* http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf

source was mainly the appendix in a master's thesis, attached below. Should find and check with an actual Pacejka book in the case of typos.

http://publications.lib.chalmers.se/records/fulltext/239258/239258.pdf

Talked with John Subosits from DDL about the model. some takeaways: 

* most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.
* As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.
* Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 

most tires: can calculate rolling resistance in N of "drag" by multiplying normal load*0.01.

As expected, lateral behavior is most important and effects of camber can be mostly ignored. Aligning moment is for steering feedback.

Reminder to pay attention to nominal loading and the load vs. mu curves - Will get highest lateral force return at nominal load, which is above what the actual load on the car will probably be. 

