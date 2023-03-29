import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import the .csv file
os.chdir('C:/cygwin64/home/10755/IBI1_2022-23/Practical7')
covid_data = pd.read_csv("full_data.csv")
# show the 2nd column every 100th to the 1000th
data_collection_1 = covid_data.iloc[0:1001:100, 2]
# show the total cases of afghanistan
data_collection_2 = covid_data.loc[covid_data['location'] == 'Afghanistan', 'total_cases']
data_collection_check = covid_data.loc[0:81, 'total_cases']
# print(data_collection_2)
# retrieve the data on 31 March 2020, then pick out the data of the total world
data_31Mar_new_cases_all = covid_data.loc[covid_data['date'] == '2020-03-31', ['location','new_cases']]
data_31Mar_new_deaths_all = covid_data.loc[covid_data['date'] == '2020-03-31', ['location', 'new_deaths']]
data_31Mar_new_cases = data_31Mar_new_cases_all.loc[covid_data['location'] != 'World', :]
data_31Mar_new_deaths = data_31Mar_new_deaths_all.loc[covid_data['location'] != 'World', :]
# calculate the mean
cases_mean = np.mean(data_31Mar_new_cases['new_cases'])
deaths_mean = np.mean(data_31Mar_new_deaths['new_deaths'])
#print(cases_mean, deaths_mean)
# make a boxplot of the data
plt.boxplot(data_31Mar_new_cases['new_cases'])
plt.title('new_cases_on_March_31')
plt.show()
plt.boxplot(data_31Mar_new_deaths['new_deaths'])
plt.title('new_deaths_on_March_31')
plt.show()
# play with the world data
world_datas = covid_data.loc[covid_data['location'] == 'World', :]
plt.plot(world_datas['date'], world_datas['new_cases'], 'r+')
plt.plot(world_datas['date'], world_datas['new_deaths'], 'bo')
plt.xticks(rotation=-90)
plt.title('world_new_cases')
plt.show()
