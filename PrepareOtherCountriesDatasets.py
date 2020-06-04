import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def prepare_dataset_for_country_wanted(country_name, df):
    df_country = df[df['Country/Region']==country_name]
    
    # assume as confirmed number raised above 100, epidemic starts
    df_country = df_country[df_country.Confirmed>100.0] 
    
    df_country['ObservationDate'] = df['ObservationDate'].astype('datetime64[ns]')

    #e.g. uk, France have more regions than mainland and their seperated record
    df_country = df_country.groupby(['ObservationDate']).sum().reset_index()
    # instead of label dates, counting numbers of days into epidemic and use it as shaerd x-axis
    start_date = df_country['ObservationDate'].iloc[0]   
    df_country['Days'] = (df_country.ObservationDate-start_date+timedelta(days=1)).dt.days

    df_country['Confirmed_Total'] = df_country['Confirmed'].astype(int)
    df_country['Death_Total'] = df_country['Deaths'].astype(int)
    # Mortality_Rate should be calculated based on Confirmed_Daily and Death_Daily
    # here only needs other countries rough data to compare in graph
    # therefore not needed yet
    # possibility to find other countries' Tested_Cases?
    df_country = df_country[['Days', 'Confirmed_Total', 'Death_Total']]
    print(df_country)
    df_country.to_csv(f'datasets/{country_name}_from_kaggle.csv', sep=',', index = False)

#
df = pd.read_csv('datasets/world_corona_from_kaggle.csv')
wanted_countries = ['UK','Germany', 'France', 'Italy', 'Spain']
for country in wanted_countries:
    prepare_dataset_for_country_wanted(country, df)

