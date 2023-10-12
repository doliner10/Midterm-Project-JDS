

# _Parking Meters By City_
# _Comparing the number of meters and average rates across U.S. cities_

October 12th, 2023

Jacob McGill, Shuting Yao, Daniel Oliner 

# Introduction:
This project analyzes the number of parking meters and average rates across a sample of several U.S. cities. In this analysis, we’ve selected a sample of eight cities, representing varying populations and geographic regions. The goal is to compare the amount of parking kiosks and meters between cities, as well as the average cost of parking between cities. 

# Sources of Data: 
Data used in this analysis was sourced from each respective official city government website, where parking and transportation data was publicly available (we uploaded the relevant data for each city into the /file directory).  The final list of cities considered were: 

New York City
Los Angeles
San Francisco
Charlotte
Phoenix
Indianapolis
San Diego
San Jose

These cities were selected because they had the highest population in 2022 as estimated by the U.S. Census Bureau and provided public data on parking kiosks. Only eight cities have been considered here but a more comprehensive analysis could be conducted by including a larger sample of U.S. cities with a greater range in populations, or by considering other factors that may affect parking meter availability and rates. But given limitations in the availability of data and the time constraint, we elected to focus our efforts on these eight cities and their populations for simplicity. 


# Code: 
Our code is ran in python with the packages specified in requirements.text. Each city had an individual .py that was run with “code/”insert city”.py” to clean and collect the data on parking kiosks and meters. Afterwards, combine_data.py was ran to combine the data into a single CSV and also analyzed the count of kiosks in each city, the average rate, and produced graphs representing both values. The results of the analysis (count of meters and kiosks for each city and the average rate) written as a CSV to the analysis file along with graphs representing this data.
Methodology: 

For each city, we read-in the respective .csv parking meter data into a python file (for example “code/nyc.py”). Each dataset included many variables that were not necessary in our analysis (such as “Meter ID”, “Meter Type, “latitude/longitude”, etc) so we began by narrowing down the data to include only variables pertaining to street address and meter rates. We also focused on rates for noncommercial parking, since that information was not reported equally across cities.  Next, we created a function that determined the average rate for each meter. This step was fairly simple for meters with flat/constant rates, but for meters with dynamic pricing we computed the average rate across all hours of operation. Once we had city-level data defined within the parameters of our analysis, with an entry for “City”, “Street Address” and “Rate” corresponding to each meter, we wrote into a single file for cross-city analysis. 

# Limitations:

We had several limitations in our data. Several of the cities we analyzed had a mix of both parking meters ( which served a single car) and parking meters, which can serve several cars, so this may underestimate the amount of parking that city governments charge for. Also, our analysis did not include private parking lots or parking garages, so future work could look into collecting data. This analysis would be improved by looking at other factors that may affect parking meter availability and average rates. We discussed several other factors that may be relevant in further analysis, such as population density, cost of living, land use regulations and public transportation availability. However, official publicly-available data pertaining to these factors proved more difficult to obtain, so we elected to focus solely on population as an interesting initial analysis that we could conduct in the time allotted. Further analysis that includes additional relevant factors and features a larger sample of cities would be an interesting extension of our research.

# Results: 
Our analysis provided the following results:






The following graph compares the count of meters/kiosks between cities:




As can be seen, San Francisco and Los Angeles had the highest number of parking meters/kiosks of the 8 cities analyzed, with New York and San Diego coming in 3rd and 4th. We also compared average parking rates:


There is less spread in the average of parking meter rates. New York has the highest average rate, followed by San Francisco. Given the high cost of living in New York coupled with the relatively scarce parking availability in the previous graph, it is unsurprising that New York has the highest average rate. 
