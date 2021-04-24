import pandas as pd

def read_data():
    input1 = 'covid.csv'
    input_pd = pd.read_csv(input1)
    return  input_pd

def clean_data(input_df):
    input_df['people_vaccinated'] = input_df['people_vaccinated'].fillna(0)
    input_df['people_fully_vaccinated'] = input_df['people_fully_vaccinated'].fillna(0)
    input_df[['people_vaccinated', 'people_fully_vaccinated']] = input_df[['people_vaccinated', 'people_fully_vaccinated']].astype(int)
    return input_df

def getallData():

    input_df = read_data()
    clean_df = clean_data(input_df)
    clean_df = clean_df[['date','location','people_vaccinated','people_fully_vaccinated']]

    #print(pd2)
    #pd4 = pd2[['location']].groupby(['location']).aggregate[sum('people_vaccinated')]
    print(clean_df.head())
    return clean_df

#print(getallData())

def byStateandMonth(state):
    input_df = read_data()
    clean_df = clean_data(input_df)

    clean_df = clean_df[['date', 'location', 'people_vaccinated', 'people_fully_vaccinated']]
    clean_df=clean_df.loc[clean_df['location'] == state]
    clean_df['year'] = pd.DatetimeIndex(clean_df['date']).year
    clean_df['month'] = pd.DatetimeIndex(clean_df['date']).month
    final_df = clean_df.groupby(['location','year','month']).sum()
    return final_df

byStateandMonth()