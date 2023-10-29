# Crime Reports Analysis (January - August 2023)
This project is a comprehensive analysis of crime reports from January to August 2023.

## Project Overview
In this project, I’ve conducted data cleaning, enrichment, and exploratory data analysis (EDA) on the crime reports dataset. The cleaned and enriched data was then used to create an interactive dashboard on Tableau.

## Interactive Dashboard
Here is the link to the Tableau dashboard
https://public.tableau.com/views/CrimenesenColombia/Dashboard22?:language=es-ES&:display_count=n&:origin=viz_share_link

The Tableau dashboard provides a detailed view of each crime. You can click on a specific crime and explore various aspects such as:

The frequency of the crime in different locations
The most commonly used weapons
The day of the week when the crime is most reported
The dashboard also provides demographic insights into the victims, breaking down the data by age group and gender.

## Conclusions and Insights
After a thorough analysis of the crime reports from January to August 2023, several key insights were drawn:

1. Crime Distribution: The distribution of crimes across different locations was not uniform. Certain areas reported higher crime rates, and the places with more reports are also the most densely populated places, but checking the ratio of crimes reported vs the population density we can see that the main cities of the country aren't the more dangerous as usually thought because, the main cities report more crimes but the probability to be a victim of any crime is higher in another place like towns, secondary cities, and less populated places, for example, the top 3 places where is higher the probability of be a victim of a crime are Granada, Ricaurte and San Pedro.

2. Weapons Used: The data revealed patterns in the types of weapons used in different crimes. Most of the crimes reported are without the use of any weapon, especially for non-violent crimes, but the second most common weapons in general are firearms and used to be the most common in crimes like murders, Kidnapping, and terrorism; This represents a big problem since it is a country where the carrying of weapons is not legalized.

3. Crime Timing: The frequency of crimes varied across different days of the week. The weekends are the days when more crimes are reported, especially violent crimes tend to be reported on weekends.

4. Victim Demographics: There are more masculine victims in violent crimes except for domestic violence and sexual crimes where most of the victims are women. Also, the victims of all crimes are usually adults except for sex crimes where there is a large proportion of victims who are adolescents and minors.

## Repository Structure
This repository is organized into two main folders: data and notebooks.

### Data Folder
The data folder contains two subfolders:

raw_data: This folder contains the raw data files.
processed_data: This folder contains the processed data files after cleaning and enrichment.

### Notebooks Folder
The notebooks folder contains all the Jupyter notebooks and scripts used for data cleaning, enrichment, and EDA:

01_Importing_and_cleaning_data.ipynb: This Jupyter notebook contains all the scripts used for data cleaning.
02_EDA.ipynb: This Jupyter notebook contains all the scripts used for EDA.
03_Enrichment.ipynb: This Jupyter notebook contains all the scripts used for data enrichment.
toolbox.py: This Python script contains several useful functions used in the notebooks.
Feel free to explore this repository and provide any feedback or insights. Happy exploring!
