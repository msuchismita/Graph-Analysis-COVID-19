import pandas as pd 
rows = pd.read_csv("../data/COVID-19_Case_Surveillance_Public_Use_Data.csv", chunksize=600000) 
for i, chuck in enumerate(rows): 
    chuck.to_csv('../data/out{}.csv'.format(i)) # i is for chunk number of each iteration
