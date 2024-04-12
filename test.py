import pandas as pd

data  = pd.read_csv("Application_Projet_E1/performance.csv")

data["Model"] = data["Model"].astype(str)
filtered_data = data[(data['Model'] == '2016') & (data['Classe'] == 0)]


print(filtered_data)









# performance_year2016_2017      = data[(data["Model"] == '2017') & (data["Classe"] == 1)]
# performance_year2016_2017_2018 = data[(data["Model"] == '2018') & (data["Classe"] == 1)]
# print(performance_year2016_2017_2018)