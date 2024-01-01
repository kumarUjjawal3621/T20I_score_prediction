import streamlit as st 
import pickle

st.title('Cricxpert')
st.caption('Predict Team Total')

pipe = pickle.load(open('pipe.pkl','rb'))

teams=['Pakistan',
 'India',
 'Australia',
 'New Zealand',
 'England',
 'West Indies',
 'Sri Lanka',
 'South Africa',
 'Bangladesh',
 'Ireland',
 'Afghanistan',
 'Zimbabwe',
 'Netherlands',
 'Scotland',
 'United Arab Emirates',
 'Hong Kong',
 'Oman',
 'Nepal',
 'Kenya',
 'Canada',
 'Malaysia',
 'Papua New Guinea',
 'Namibia',
 'Singapore',
 'Bermuda',
 'Jersey',
 'Vanuatu',
 'United States of America',
 'Germany',
 'Spain',
 'Kuwait',
 'Botswana',
 'Qatar',
 'Maldives',
 'Denmark',
 'Thailand',
 'Nigeria',
 'Guernsey',
 'ICC World XI',
 'Italy',
 'Uganda',
 'Philippines',
 'Belgium',
 'Cayman Islands',
 'Norway',
 'Ghana',
 'Portugal',
 'Romania',
 'Bahrain',
 'Luxembourg',
 'Gibraltar',
 'Bhutan',
 'Bulgaria',
 'Czech Republic',
 'Saudi Arabia',
 'Iran',
 'Isle of Man']

## Taking 7 inputs
batting= st.selectbox('Batting team',sorted(teams))

bowling= st.selectbox('Bowling team', sorted(teams))

inn=[1,2]
inning= st.selectbox('Inning',inn)

score=st.number_input('Current score')

over=st.number_input('Overs completed')

lfor=st.number_input('Runs in Last 5 overs')

wickets=st.number_input('Wickets lost')

import pandas as pd
ipt=pd.DataFrame({'over': [over],'score': [score],'wickets': [wickets],'batting': [batting],'bowling': [bowling],'inning' :[inning],'Last5oversRuns' :[lfor]})


if st.button('Predict Score'):
    result = pipe.predict(ipt)
    st.header("Predicted Score - " + str(int(result[0])))
