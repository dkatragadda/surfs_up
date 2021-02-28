# Surfs Up 

## Overview of the Surfs Up Analysis
The purpose of this analysis was to use our skills in connecting to a Sqlite database and calculating the temperature trends for the months of June and December in Oahu. This analysis will help determine the feasibility of running a surf and ice-cream shop all year-round. We used the sqlalchemy package to connect to the sqlite database available and store the results in a dataframe after retrieving the results from the database.

## Results

* The June temperature stats are as shown below. The mean temperature in June is 74.9 degrees Fahrenheit. 

![June_Stats](https://github.com/dkatragadda/surfs_up/blob/main/Resources/June_Temp_Stats.png)

* The December temperature stats are as shown below. The mean temperature in December is 71 degrees Fahrenheit.

![Dec_Stats](https://github.com/dkatragadda/surfs_up/blob/main/Resources/Dec_Temp_Stats.png)

* The IQR for June is 4 degrees F and the IQR for December is 5 degrees F. 


## Summary

Based on the analysis completed, the weather in Oahu is considerably favourable to opening a surf and ice-cream shop year-around. The standard deviation for the month of June is 3.25 degrees F and the standard deviation for the month of December is 3.74 degrees F. The results show that the temperature does not swing wildly based on the data.   


Two additional queries that would help in gathering more information regarding the temperature are:
1. Create the temp stats for the months of June and December after grouping by the year to see if the temperatures have remained consistent or increased in the recent years since we are looking at a dataset from 2010 to 2017. 
2. We can also retrieve information regarding the precipitation in Oahu to understand how much rainfall is received as that could be detrimental for a surf and ice-cream shop. 
