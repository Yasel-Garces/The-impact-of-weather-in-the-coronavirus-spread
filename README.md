<img src="img/covid-19.jpeg">

# Project Title
The impact of weather in the coronavirus spread

# Motivation
With more than 775 748 peoples infected and 37109 deaths (03/30/2020) and with a significative decrease of usual human activity, the COVID-19 will be remembered as a sad part of mankind's history. I, like many others, am trying to keep doing what I love to do and avoid get crazy thinking about the impact of this crisis in my family and people around the World. I am not a politician, I don't have any kind of power, but, at the same time, I feel that I need to do something else, and for that reason I began this project as a modest contribution of what I think could be some interesting open questions about the COVID-19:

1. Is there some relationship between the temperature and the spread of the virus? In such a case, what is the minimum temperature that help to slow down it spread?
2. Has the humidity some kind of impact on the spread of the virus?
3. What happens with the virus at different atmospheric pressures?

# File Description
* This project was developed in Python 3, and all the results and codes are included in the Jupyter notebook named "_Has the weather an impact on the spread of the coronavirus?_".
	* Mostly classical libraries for data analysis and visualization were used (like `numpy`, `pandas`, `matplotlib`, `seaborn` and `scipy` for the statistical analysis).
	* Also, the library `scikit-posthocs` was used for the posthoc analysis. See details about installation and use [here](https://scikit-posthocs.readthedocs.io/en/latest/installation/).
* "_functions.py_": It includes some utility functions that were used in the notebook.
* Directory "_Weather_": This directory is composed of 10 csv files. Each file contains the weather information for one city from December 2019 to March 30, 2020 (121 observations), condensed into 18 variables. See the section "Weather data" in the notebook for details.
* Directory "_novel-corona-virus-2019-dataset_": It contains daily level information about the new cases, deaths, and recovery by country. This dataset was obtained from [Kaggle](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset). Please, go through this link for more information about this dataset.
* Directory "_img_": It contains two images used to embellishment the notebook and this README.

# Author 
Yasel Garces    
 email: 88yasel@gmail.com     
[LinkedIn](https://www.linkedin.com/in/yasel-garces-suarez/)


# License
[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.
