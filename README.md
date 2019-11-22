# Brooklyn Weather and Arrests

We looked at correlations between weather and arrests in Brooklyn between 01/01/2019 and 09/30/2019 to see if there were any interesting relationships. We specifically examined the relationship between the particular weather condition on a given day and the arrests taken place that day.

## Contributors 
 -Findlay Bowditch ([github](https://github.com/fbowditch))
 -Chris Shaw ([github](https://github.com/JackBurton11/))

## Background
This was our 2nd 48-hour project at the Flatiron School (NYC Data Science)

## Project Purpose and Description
 - The goal of this project was to test our ability to gather information from a real-world database and use our knowledge of statistical analysis and hypothesis testing to generate analytical insights that can be meaningful. 
 
## Data:
 
- **Dark Sky**
	- Weather Data for Brooklyn  
	- https://darksky.net/dev
- **NYC Open Daya**
	- Arrest Data for Brooklyn
	- https://dev.socrata.com/
	
## Tools (all in Python):
   - pandas
   - SQLAlchemy
   - MySQL Server on AWS RDS
   - Seaborn/Matplotlib
   - SciPy/NumPy

# Hypotheses 
 
 -H01: There is no significant difference between the forecast for a particular day in Brooklyn and the number of arrests for that day.
 -Ha1: There is a significant difference between the forecast for a particular day in Brooklyn and the number of arrests.
 
 -H02: There is no significant difference between the forecast for a particular day in Brooklyn and the number of arrests by gender.
 -Ha2: There is a significant difference between the forecast for a particular day in Brooklyn and the number of arrests by gender.
 
 ### Hypothesis Testing
 - T-Test
 - ANOVA

