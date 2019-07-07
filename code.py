# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data = data.rename({'Total': 'Total_Medals'},axis = 1)
data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'], 'Both', 
(np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')))
better_event = data['Better_Event'].value_counts(ascending = False).index.tolist()[0]
print(better_event)


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop([146],inplace = True)

def top_ten(column_name):
    country_list = []
    top10 = top_countries.nlargest(10,column_name)
    country_list = list(top10['Country_Name'])
    return country_list
top_10_summer = top_ten('Total_Summer')
top_10_winter = top_ten('Total_Winter')
top_10 = top_ten('Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar(x='Country_Name',y='Total_Summer')
winter_df.plot.bar(x='Country_Name',y='Total_Winter')
top_df.plot.bar(x='Country_Name',y='Total_Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'])[0]
print(summer_max_ratio)
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'])[0]
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = list(top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'])[0]
print(top_max_ratio)
print(top_country_gold)




# --------------
#Code starts here
data_1 = data.drop([146])
data_1['Total_Points'] = (3*data_1['Gold_Total'])+(2*data_1['Silver_Total'])+(data_1['Bronze_Total'])
most_points = data_1['Total_Points'].max()
best_country = list(data_1[data_1['Total_Points']==most_points]['Country_Name'])[0]
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]#.size.unstack
# print(aaa)

best.plot.bar(stacked=True)

plt.xlabel('United States')


plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)




