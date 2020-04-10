#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:41:14 2020
This scrip resume all the functions that I used in the Coronavirus Project.
These functions are:
    1. 

@author: yasel (88yasel@gmail.com)
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

  if value < 0.05:
    color = 'green'
  else:
    color = 'red'

  return 'color: %s' % color