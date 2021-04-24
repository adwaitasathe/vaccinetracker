import pandas as pd
from TwitterAPI import TwitterAPI

# Function to read input data
def read_data(input_file):
    input_pd = pd.read_csv(input_file)
    return  input_pd

# Function to clean data
def clean_data(input_df):
    input_df['people_vaccinated'] = input_df['people_vaccinated'].fillna(0)
    input_df['people_fully_vaccinated'] = input_df['people_fully_vaccinated'].fillna(0)
    input_df[['people_vaccinated', 'people_fully_vaccinated']] = input_df[['people_vaccinated', 'people_fully_vaccinated']].astype(int)
    return input_df

# Function to calculate total Vaccine distributed, First Dose, All dose, based on input string

def calculate_total(input_field,input_file):
    input_df = read_data(input_file)
    total = input_df[input_field].sum()
    return total


# Function to read input data

def getallData(input_file):
    input_df = read_data(input_file)
    clean_df = clean_data(input_df)
    clean_df = clean_df[['date','location','people_vaccinated','people_fully_vaccinated']]

    return clean_df

# Function to find monthly Vaccination count based on Month and state - bar graph
def byStateandMonth_bar(state,input_file):
    input_df = read_data(input_file)
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

# Function to find monthly Vaccination count based on Month and state - line graph

def byStateandMonth_line(state,input_file):
    input_df = read_data(input_file)
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

# Function to compare statewise comparison of Vaccine count

def compareState(state_list,input_file):
    input_df = read_data(input_file)
    clean_df = clean_data(input_df)

    clean_df = clean_df[['date', 'location', 'people_vaccinated', 'people_fully_vaccinated']]
    clean_df = clean_df.loc[clean_df['location'].isin(state_list)]
    final_df = clean_df.groupby(['location']).sum().reset_index()
    print(final_df)
    final_df = final_df.set_index('location')
    return final_df


# Function to Get Live Tweets From Twitter

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
