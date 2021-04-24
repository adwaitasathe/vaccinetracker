import pandas as pd
from TwitterAPI import TwitterAPI
def read_data():
    input1 = 'covid.csv'
    input_pd = pd.read_csv(input1)
    return  input_pd

def clean_data(input_df):
    input_df['people_vaccinated'] = input_df['people_vaccinated'].fillna(0)
    input_df['people_fully_vaccinated'] = input_df['people_fully_vaccinated'].fillna(0)
    input_df[['people_vaccinated', 'people_fully_vaccinated']] = input_df[['people_vaccinated', 'people_fully_vaccinated']].astype(int)
    return input_df

def calculate_total(input_field):
    input_df = read_data()
    total = input_df[input_field].sum()
    print(total)
    return total

calculate_total('total_vaccinations')

def getallData():
    input_df = read_data()
    clean_df = clean_data(input_df)
    clean_df = clean_df[['date','location','people_vaccinated','people_fully_vaccinated']]

    print(clean_df.head())
    return clean_df


def byStateandMonth_bar(state):
    input_df = read_data()
    clean_df = clean_data(input_df)

    clean_df = clean_df[['date', 'location', 'people_vaccinated', 'people_fully_vaccinated']]
    clean_df=clean_df.loc[clean_df['location'] == state]
    clean_df['year'] = pd.DatetimeIndex(clean_df['date']).year
    clean_df['month'] = pd.DatetimeIndex(clean_df['date']).month
    final_df = clean_df.groupby(['location','year','month']).sum().reset_index()
    final_df['month'] = final_df['month'].replace([1], 'Jan')
    final_df['month'] = final_df['month'].replace([2], 'Feb')
    final_df['month'] = final_df['month'].replace([3], 'Mar')
    final_df['month'] = final_df['month'].replace([4], 'Apr')
    print(final_df)
    final_df = final_df.set_index('month')
    return final_df

def byStateandMonth_line(state):
    input_df = read_data()
    clean_df = clean_data(input_df)

    clean_df = clean_df[['date', 'location', 'people_vaccinated', 'people_fully_vaccinated']]
    clean_df = clean_df.loc[clean_df['location'] == state]
    clean_df['year'] = pd.DatetimeIndex(clean_df['date']).year
    clean_df['month'] = pd.DatetimeIndex(clean_df['date']).month
    final_df = clean_df.groupby(['location', 'year', 'month']).sum().reset_index()
    final_df['month'] = final_df['month'].replace([1], 'Jan')
    final_df['month'] = final_df['month'].replace([2], 'Feb')
    final_df['month'] = final_df['month'].replace([3], 'Mar')
    final_df['month'] = final_df['month'].replace([4], 'Apr')
    print(final_df)
    final_df = final_df.set_index('month')
    return final_df

#print(byStateandMonth_line('Arizona'))


def compareState(state_list):
    input_df = read_data()
    clean_df = clean_data(input_df)

    clean_df = clean_df[['date', 'location', 'people_vaccinated', 'people_fully_vaccinated']]
    clean_df = clean_df.loc[clean_df['location'].isin(state_list)]
    final_df = clean_df.groupby(['location']).sum().reset_index()
    print(final_df)
    final_df = final_df.set_index('location')
    return final_df


#print(compareState(['California', 'Georgia', 'New Jersey']))

def getTweets():
    consumer_key = 'f6sxSv3IkOnEyNIwF9Ycayf6i'
    consumer_secret = 'mvVQNtYGDDe5Tv3T3Wwa5SL1GYaqY9PFow91m4jSs0t7bbtltV'
    access_token_key = '3166578447-hoMCQrwmdoeJRj14aoPIwj2G7hWINgdvAmkOv9F'
    access_token_secret = 'FndXsZ7REb8PekqUZMwaxRtHU2ubj3W8Xk9RmoaPGyWsV'
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = api.request('search/tweets', {'q': '#IGotVaccinated'})
    output = ""
    for item in r:
        output = output + item['text']
    print(output)
    return output
#getTweets()