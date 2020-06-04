import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_country_confirmed_case(country_name, index):
    df = pd.read_csv(f'datasets/{country_name}_from_kaggle.csv')

    cmap=plt.cm.get_cmap(plt.cm.viridis,200)# 200 colors sampling
    n=50 # get nth color in sample
    color = cmap(50+n*index)

    p, = plt.plot(df['Days'], df['Confirmed_Total'], color=color,label=country_name)
    return p

def plot_country_death_case(country_name, index):
    df = pd.read_csv(f'datasets/{country_name}_from_kaggle.csv')

    cmap=plt.cm.get_cmap(plt.cm.viridis,200)#  colors sampling
    n=50 # get nth color in sample
    color = cmap(50+n*index)
    
    p, = plt.plot(df['Days'], df['Death_Total'], color=color,label=country_name)
    return p
#
wanted_countries = ['UK', 'Germany', 'France', 'Italy','Spain']

fig_confirmed = plt.figure()
plt.title('Epidemic Development in selected European Countries')
plt.xlabel('Days in Epidemic')
plt.ylabel('Confirmed Cases in Total')

lns_confirmed = []
for index,country in enumerate(wanted_countries):
    p = plot_country_confirmed_case(country, index)
    lns_confirmed.append(p)
fig_confirmed.legend(handles=lns_confirmed, loc='best')

plt.show()

fig_death = plt.figure()
plt.title('Epidemic Development in selected European Countries')
plt.xlabel('Days in Epidemic')
plt.ylabel('Death Cases in Total')

lns_death = []
for index,country in enumerate(wanted_countries):
    p = plot_country_death_case(country, index)
    lns_death.append(p)
fig_death.legend(handles=lns_death, loc='best')

plt.show()
