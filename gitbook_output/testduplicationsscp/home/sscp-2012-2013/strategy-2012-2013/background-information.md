# SSCP - Background Information

# Background Information

0) What sort of strategy are you talking? I see a general partition between (A) RACE strategy and (B) DESIGN strategy. Of course your design will influence your race strategy, so keep this in mind as you discover other dependencies between car/race variables.

1) Take a look at the spiral notebook on Strategy from 1994. Though the pages may be a little yellowed, the intro at least gives a nice overview of factors to consider and attitudes surrounding solar racing strategy. Note that this Strategy notebook revolves mostly around RACE strategy, as opposed to design strategy and other optimizations.

2) Consider your constraints. These include race rules and component specs. For example...

            •  Solar panel area

            •  Battery capacity

            •  Available charging stations (Challenger class)

            •  Mass of car; total load incl. driver/passenger and ballast

3) Consider benchmarks. Numbers you have from the past. Numbers you can derive from equations and spec sheets. For example...

            •  Typical array output 1-1.3kW at solar noon; output may drop to below 80W when overcast

            •  Power consumption 1.1-1.5kW at target speed 90kph (56mph)

4) Now consider your most basic model. There may be several pre-existing versions of this first step. They should include the most fundamental measurements (aka insolation) and/or the easiest measurements to record/analyze (aka speed). A simplified model is sufficient to compare different race scenarios: factors you neglect will affect each set of input car parameters relatively evenly. For example… this is how we came up with the models to help decide between Cruiser and Challenger classes for 2013.

5) Now go crazy. Consider all variables. These are wild and free and possibly unbounded. The more features, the better your model can theoretically train to predict the future. Consider, for example...

            •  Weather: cloud cover, wind speed, wind direction, humidity, air density...

            •  Road gradient

            •  Slowing for control stops

            •  Stickiness of Australian bitumen, which may affect your rolling resistance

            •  ...and many, many more.

6) Tailor the model, train the model with data and math, and go go go be fancier and more accurate than ever before. There's a lot to be done in this space, so just be sure to prioritize which factors most affect your strategy.

(7) …this is where the TODO comes in. Check out more resources on this site and elsewhere, get a feel for the relative contributions of each part of the car, and have fun putting it all together in equations and heuristics and pretty optimizations. Good luck! Victory depends on you.

