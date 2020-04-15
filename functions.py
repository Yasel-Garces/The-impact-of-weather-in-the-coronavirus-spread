#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:41:14 2020
This scrip resume all the functions that I used in the Coronavirus Project.
These functions are:
    1. transform_dtypes: Transform the data type to the correct format
    2. 

@author: Yasel (88yasel@gmail.com)
"""
#--------------------------------------------------------
import pandas as pd

def transform_dtypes(df):
    ## Transform the data type to the correct format
    # input: df (data frame)
    # output: data types transformed data frame
    #-----------------
    # 'ObservationDate' to datetime
    df['ObservationDate']=pd.to_datetime(df['ObservationDate'],exact=False).dt.date
    # 'Confirmed','Deaths','Recovered' to int
    df[['Confirmed','Deaths','Recovered']]=df[['Confirmed',
                                               'Deaths',
                                               'Recovered']].astype('int')
    # 
    df[['Province/State','Country/Region']]=df[['Province/State',
                                                'Country/Region']].astype('category')
    return df

#-------------------------------------------------------- 
def cases_country_city(df):
    # Extract the data of the last day
    df_lastDay=df.loc[df['ObservationDate']==max(df['ObservationDate']),:]
    countries=['US', 'Italy','Spain']
    function = lambda country: df_lastDay.loc[df_lastDay['Country/Region']==country,:].sort_values(by='Confirmed',
                                                                             ascending=False).iloc[0,[2,5]]
    result={country: list(function(country)) for country in countries}
    return df_lastDay, result
#--------------------------------------------------------
def trim_axs(axs, N):
    """
    Reduce *axs* to *N* Axes. All further Axes are removed from the figure.
    """
    axs = axs.flat
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]    
#--------------------------------------------------------
def color_p_value(value):
  """
  Colors elements in a dateframe
  green if p-value<0.05, else red.
  """

  if (value < 0.05) | (value<0):
    color = 'green'
  else:
    color = 'red'

  return 'color: %s' % color
#--------------------------------------------------------
# Function to factorize the average temperature
def factor_hum(val):
    if (val>=30) & (val<=50):
        return '30-50'
    elif val<30:
        return '<30'
    else:
        return '>50'
#--------------------------------------------------------
def t_test_byCities(cities2test,df):
    from scipy import stats
    # Empty dictionary to store the results
    results_pvalue=dict()
    results_stat=dict()
    # For each key in the dictionary, run the test with each of 
    # the values of this key
    for main_city in cities2test.keys():
        # List with the cities to test with "hot_city"
        paired_cities=cities2test[main_city]
        # Extract the information of the "main_city"
        main_city_values=df.loc[df['Province/State']==main_city,['Confirmed','Days Since First Case']]
        # Define an empty dictiona ry to store the partial results 
        p_value=dict()
        stas_value=dict()
        # Run the test for each pair of cities
        for city in paired_cities:
            # Extract the number of new cases of city
            city_values=df.loc[df['Province/State']==city,['Confirmed','Days Since First Case']]
            # Get the max number of observations available in both cities
            max_mutual_obs=min(main_city_values.shape[0],city_values.shape[0])
            # Store the information in X (key country) and Y (test country)
            X=main_city_values.loc[main_city_values['Days Since First Case']<max_mutual_obs,'Confirmed']
            Y=city_values.loc[city_values['Days Since First Case']<max_mutual_obs,'Confirmed']
            # Run the t-student hypothesis test
            stat, p = stats.ttest_ind(X, Y,equal_var=False)
            # Save the p-value result in "partial". Because this is a one tail test, the p-value is divided by 2
            p_value[city]=p/2
            stas_value[city]=stat
        # Include the dictionary with partial results in the general dictionary
        results_pvalue[main_city]=p_value
        results_stat[main_city]=stas_value
    # Tranform the dictionary to a dataframe        
    results_pvalue=pd.DataFrame.from_dict(results_pvalue, orient='columns')
    results_stat=pd.DataFrame.from_dict(results_stat, orient='columns')
    return (results_pvalue, results_stat)
#--------------------------------------------------------        
        