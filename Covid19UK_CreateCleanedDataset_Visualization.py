import csv
import json
import urllib.request
import pandas as pd
import numpy as np
import plotly.express as px

# Import UK data from Jeff's endpoint
with urllib.request.urlopen("https://api.covid19uk.live/historyfigures") as url:
    x = json.loads(url.read().decode())
    #print(x)

data = []
for row in x['data']:
    data.append({'Confirmed':row['confirmed'], 'Death': row['death'], 'Tested': row['tested'], 'Tests_Done': row['test_done']})

df = pd.DataFrame.from_dict(data, orient='columns')
#print(df)

# Prepare UK data
df_uk = df[df.Confirmed>100.0]
df_uk['Date'] = pd.date_range(start='03/05/2020', periods=len(df_uk), freq='D')
#print(df_uk)

df_uk['Confirmed_Total'] = df_uk['Confirmed']
df_uk['Death_Total'] = df_uk['Death']
df_uk['Tested_Case'] = df_uk.Tests_Done.diff()
df_uk['Tested_Person'] = df_uk.Tested.diff()
df_uk['Confirmed'] = df_uk.Confirmed.diff()
df_uk['Death'] = df_uk.Death.diff()
df_uk['Mortality_Rate'] = np.round((df_uk.Death.values/df_uk.Confirmed.values)*100,2)
df_uk['Positive_Rate'] = np.round((df_uk.Confirmed.values/df_uk.Tested_Person.values)*100,2)

df_uk = df_uk[['Date', 'Tested_Case', 'Tested_Person', 'Confirmed', 'Positive_Rate','Death', 'Mortality_Rate', 'Confirmed_Total', 'Death_Total']]
#print(df_uk)
df_uk.to_csv(r'datasets/cov_uk.csv', index = False)

# Dawing charts for UK
fig_daily_confirmed = px.line(df_uk, x= 'Date', y='Confirmed',
             title='UK COVID-19 Daily Confirmed Since Epidemic Began ')
fig_daily_confirmed.show()

fig_confirmed_total = px.line(df_uk, x= 'Date', y='Confirmed_Total',
             title='UK COVID-19 Confirmed in Total Since Epidemic Began ')
fig_confirmed_total.show()