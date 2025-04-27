# weight-distribution-sundae

## SSCP - Weight Distribution Sundae

## Weight Distribution Sundae

I wanted to make a thorough method of estimating weight distribution for designing Sundae. It consists of weighing individual components and finding their locations in CAD relative to the overall CG. On September 4, I successfully verified my method by matching Arctan's weight distribution. It's not perfect, as the overall vehicle weight in my model is 13 kg less than its measured weight in August of 2016. The absence of the DDL data logger, electrical boards & wire, glue fillets, and filler used to fit chassis in my model could explain the 13 kilogram difference. I will attach the matlab script after I refine the weights further.&#x20;

&#x20;   As of Sept 4, 2016, Arctan's estimated weight distribution is as follows:

&#x20;       49% Front, 51% Rear, 42.5% Left, 57.5% Right

&#x20;   This output from my model is surprisingly close to the most recent weighing using the DDL's professional-grade vehicle scales. We now can use these scales instead of bathroom scales, yay!

Now that I have validated the weight distribution estimation method, I'll use this as a tool for placing components in Sundae. Ideally we would have 50/50 left right & 60/40 front rear (55/45 front rear minimum).

Hypothetical Configurations (see spreadsheet for more)

* Arctan with motors in rear: 42.6/57.4 F/R
* Arctan with with 1 motor on non-driver side: 47.3/52.7 F/R & 43.6/56.4 L/R
* Sundae-hrh-010 layout #1: 54.8/45.2 F/R & 45.2/54.8 L/R
* Sundae-hrh-010 layout #1 with titanium roll cage: 55/45 F/R & 45.3/54.7 L/R
* Sundae-hrh-010 with "vertical" battery pack:

Arctan with motors in rear: 42.6/57.4 F/R

Arctan with with 1 motor on non-driver side: 47.3/52.7 F/R & 43.6/56.4 L/R

Sundae-hrh-010 layout #1: 54.8/45.2 F/R & 45.2/54.8 L/R

Sundae-hrh-010 layout #1 with titanium roll cage: 55/45 F/R & 45.3/54.7 L/R

Sundae-hrh-010 with "vertical" battery pack:

#### Embedded Content

Embedded content: [Embedded Content](weight-distribution-sundae.md)

![](../../../../assets/docs_32dp.png)

#### Embedded Content

Embedded content: [Embedded Content](weight-distribution-sundae.md)

![](../../../../assets/sheets_32dp.png)
