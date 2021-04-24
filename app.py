'''
Course : INFO 6101 Data Science Eningeering with Python
Project Name: Covid Vaccination Tracker
Author :
1 - Adwait Sathe
2 - Snehal Zagade
'''

# Importing all the necessary Libraries
import streamlit as st
from functions import *

# Global variables
input_file = 'covid.csv'

# HomePage styling
html_temp = """
<div style="background-color:#800000;padding:1px; border-radius: 30px;">
<h1><center style= "color:white;">Vaccine Tracker</style></center></h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.markdown(
    """
<style>
.css-1l02zno {
    background-color:#800000;
    background-attachment: fixed;
    flex-shrink: 0;
    height: 100vh;
    color:black;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 100;
    margin-left: 0px;
}
.css-145kmo2 {
    font-size: 1rem;
    color: white;
    margin-bottom: 0.4rem;
}
.css-1vbb94r {
    width: 100%;
    margin-bottom: 1rem;
    border-collapse: collapse;
    border-radius: 30px;
    background-color: white;
    font-weight: bold;
}

.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 3rem 1rem 10rem;
    max-width: 730px;
}

canvas{
    width:800px !important;
    height:420px !important;
}

.css-1wrcr25 {
    display: flex;
    flex-direction: row;
    -webkit-box-pack: start;
    place-content: flex-start;
    -webkit-box-align: stretch;
    align-items: stretch;
    position: absolute;
    inset: 0px;
    overflow: hidden;
    background: url("http://stories.uh.edu/covid-19/assets/ag2dSlL11z/covidbackground05-2560x1440.jpeg") repeat 0 0;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}body{background-color: lightgreen;
    font-family: "Times New Roman", Times, serif}
</style>
""",
    unsafe_allow_html=True,
)

# Button on the sidebar to get Daily Vaccine Data
get_all_data = st.sidebar.button("Get Daily Vaccine Data")

# Option on sidebar to get statewise monthly data
state = st.sidebar.selectbox("State wise Vaccination",
                             ['Select a State',
                              'Arizona',
                              'Arkansas',
                              'California',
                              'Colorado',
                              'Connecticut',
                              'Florida',
                              'Georgia',
                              'New Jersey',
                              'New York State',
                              'Massachusetts'
                              ],
                             index=0
                             )

# Option on sidebar to compare multi state vaccination
multiselect = st.sidebar.multiselect("State wise Vaccination",
                                     ['Select a State',
                                      'Arizona',
                                      'Arkansas',
                                      'California',
                                      'Colorado',
                                      'Connecticut',
                                      'Florida',
                                      'Georgia',
                                      'New Jersey',
                                      'New York State',
                                      'Massachusetts'
                                      ]
                                     )
# Option on sidebar to get live twitter Data

get_tweets_vaccine = st.sidebar.button("Get Real time Tweets for Hashtag #IGotVaccinated")

# Call Respective Function Based on Input Selected
if get_all_data:
    r = getallData(input_file)
    st.table(r)
elif get_tweets_vaccine:
    output_str = getTweets()
    st.write(output_str)
elif state != 'Select a State':
    result_bar = byStateandMonth_bar(state,input_file)
    result_line = byStateandMonth_line(state,input_file)
    st.bar_chart(result_bar)
    st.line_chart(result_line)
elif multiselect:
    state_result = compareState(multiselect,input_file)
    st.bar_chart(state_result)
else:
    total_distributed = calculate_total('total_distributed',input_file)
    total_first_dose = calculate_total('people_vaccinated',input_file)
    total_second_dose = calculate_total('people_fully_vaccinated',input_file)
    total_vaccination = calculate_total('total_vaccinations',input_file)


    st.subheader("Current Vaccination Count of Overall USA")
    st.title("Total Distributed:   " + str(int(total_distributed)))
    st.title("Total Vaccination :" + str(int(total_vaccination)))
    st.title("Total 1st Dose :" + str(int(total_first_dose)))
    st.title("Total 2nd Dose : " + str(int(total_second_dose)))
