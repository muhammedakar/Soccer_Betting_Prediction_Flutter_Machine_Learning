import streamlit as st
from streamlit import components
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Data Sapiens",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

model = joblib.load("deployment/bet_predict.pkl")

week = st.number_input('Week', value=0, step=1)

teams = ['Trabzonspor', 'Kasımpaşa', 'Konyaspor', 'Pendikspor',
         'Kayserispor', 'Sivasspor', 'Adana', 'Fenerbahce', 'Karagumruk',
         'Alanya', 'Istanbulspor', 'Antalyaspor', 'Rize', 'Galatasaray',
         'Hatayspor', 'Basaksehir', 'Beşiktaş', 'Gaziantep', 'Ankaragücü',
         'Samsunspor']

referees = ['Zorbay Kucuk', 'Bahattin Simsek', 'Burak Pakkan', 'Cagdas Altay',
            'Halil Umut Meler', 'Murat Erdogan', 'Ümit Ozturk',
            'Abdulkadir Bitigen', 'Rare', 'Tugay Numanoglu', 'Ali Sansalan',
            'Atilla Karaoğlan', 'Mert Guzenge', 'Burak Seker', 'Kadir Saglam',
            'Arda Kardesler', 'Cihan Aydin', 'Volkan Bayarslan',
            'Turgut Doman', 'Direnç Tosunoğlu', 'Emre Kargin']

teams_info = {
    'Trabzonspor': [98.88, 75, 75, 73, 74],
    'Kasımpaşa': [27.93, 67, 66, 67, 66],
    'Konyaspor': [26.5, 66, 69, 71, 69],
    'Pendikspor': [20.58, 67, 67, 67, 66],
    'Kayserispor': [29.35, 72, 66, 68, 66],
    'Sivasspor': [20.13, 67, 69, 66, 67],
    'Adana': [38.63, 70, 74, 73, 72],
    'Fenerbahce': [201.45, 78, 74, 76, 76],
    'Karagumruk': [24.83, 67, 67, 67, 67],
    'Alanya': [25.13, 69, 70, 68, 69],
    'Istanbulspor': [7.8, 65, 64, 65, 65],
    'Antalyaspor': [29.98, 72, 68, 69, 69],
    'Rize': [31.28, 65, 66, 65, 65],
    'Galatasaray': [193.38, 79, 78, 78, 78],
    'Hatayspor': [26.75, 68, 66, 65, 67],
    'Basaksehir': [44.2, 73, 72, 71, 72],
    'Beşiktaş': [138.93, 77, 75, 73, 74],
    'Gaziantep': [22.33, 69, 69, 66, 67],
    'Ankaragücü': [34.68, 70, 68, 68, 69],
    'Samsunspor': [33.23, 69, 69, 69, 69]
}

referee = st.selectbox('Refree', referees)

team_home, team_away = st.columns(2)

with team_home:
    home = st.selectbox('Home Team', teams)
with team_away:
    away = st.selectbox('Away Team', teams)
team_home_info = [33.23, 69, 69, 69, 69]
team_away_info = [33.23, 69, 69, 69, 69]
team_home_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
team_away_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if home == 'Alanya':
    team_home_info = teams_info[home]
    team_home_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Ankaragücü':
    team_home_info = teams_info[home]
    team_home_code = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Antalyaspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Basaksehir':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Beşiktaş':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Fenerbahce':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Galatasaray':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Gaziantep':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Hatayspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Istanbulspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Karagumruk':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Kasımpaşa':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
elif home == 'Kayserispor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
elif home == 'Konyaspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
elif home == 'Pendikspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
elif home == 'Rize':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
elif home == 'Samsunspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
elif home == 'Sivasspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
elif home == 'Trabzonspor':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
elif home == 'Adana':
    team_home_info = teams_info[home]
    team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
else:
    st.title('Hata Var!')

if away == 'Alanya':
    team_away_info = teams_info[away]
    team_away_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Ankaragücü':
    team_away_info = teams_info[away]
    team_away_code = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Antalyaspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Basaksehir':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Beşiktaş':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Fenerbahce':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Galatasaray':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Gaziantep':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Hatayspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Istanbulspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Karagumruk':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Kasımpaşa':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
elif away == 'Kayserispor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
elif away == 'Konyaspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
elif away == 'Pendikspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
elif away == 'Rize':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
elif away == 'Samsunspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
elif away == 'Sivasspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
elif away == 'Trabzonspor':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
elif away == 'Adana':
    team_away_info = teams_info[away]
    team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
else:
    st.title('Hata Var!')

select_referee = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if referee == 'Ali Sansalan':
    select_referee = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Arda Kardesler':
    select_referee = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Atilla Karaoğlan':
    select_referee = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Bahattin Simsek':
    select_referee = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Burak Pakkan':
    select_referee = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Burak Seker':
    select_referee = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Cagdas Altay':
    select_referee = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Cihan Aydin':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Direnç Tosunoğlu':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Emre Kargin':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Halil Umut Meler':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Kadir Saglam':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Mert Guzenge':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
elif referee == 'Murat Erdogan':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
elif referee == 'Rare':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
elif referee == 'Tugay Numanoglu':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
elif referee == 'Turgut Doman':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
elif referee == 'Volkan Bayarslan':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
elif referee == 'Zorbay Kucuk':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
elif referee == 'Ümit Ozturk':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
elif referee == 'Abdulkadir Bitigen':
    select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
else:
    st.title('Hata Var!')
col1, col2, col3 = st.columns(3)

with col1:
    home_bet = st.number_input('Home Bet', min_value=0.0)
with col2:
    draw_bet = st.number_input('Draw Bet', min_value=0.0)
with col3:
    away_bet = st.number_input('Away Bet', min_value=0.0)


def predict_review_score(Hafta, Home_Value, Away_Value, Home_Atk, Home_Ort, Home_Def, Home_Gen, Away_Atk, Away_Ort,
                         Away_Def, Away_Gen, home_bets, draw_bets, away_bets, Home_Alanya, Home_Ankaragücü,
                         Home_Antalyaspor, Home_Basaksehir, Home_Beşiktaş, Home_Fenerbahce, Home_Galatasaray,
                         Home_Gaziantep, Home_Hatayspor, Home_Istanbulspor, Home_Karagumruk, Home_Kasımpaşa,
                         Home_Kayserispor, Home_Konyaspor, Home_Pendikspor, Home_Rize, Home_Samsunspor, Home_Sivasspor,
                         Home_Trabzonspor, Away_Alanya, Away_Ankaragücü, Away_Antalyaspor, Away_Basaksehir,
                         Away_Beşiktaş, Away_Fenerbahce, Away_Galatasaray, Away_Gaziantep, Away_Hatayspor,
                         Away_Istanbulspor, Away_Karagumruk, Away_Kasımpaşa, Away_Kayserispor, Away_Konyaspor,
                         Away_Pendikspor, Away_Rize, Away_Samsunspor, Away_Sivasspor, Away_Trabzonspor,
                         Referee_AliSansalan, Referee_ArdaKardesler, Referee_AtillaKaraoğlan, Referee_BahattinSimsek,
                         Referee_BurakPakkan, Referee_BurakSeker, Referee_CagdasAltay, Referee_CihanAydin,
                         Referee_DirençTosunoğlu, Referee_EmreKargin, Referee_HalilUmutMeler, Referee_KadirSaglam,
                         Referee_MertGuzenge, Referee_MuratErdogan, Referee_Rare, Referee_TugayNumanoglu,
                         Referee_TurgutDoman, Referee_VolkanBayarslan, Referee_ZorbayKucuk, Referee_ÜmitOzturk):
    features = [Hafta, Home_Value, Away_Value, Home_Atk, Home_Ort, Home_Def, Home_Gen, Away_Atk, Away_Ort, Away_Def,
                Away_Gen, home_bets, draw_bets, away_bets, Home_Alanya, Home_Ankaragücü, Home_Antalyaspor,
                Home_Basaksehir, Home_Beşiktaş, Home_Fenerbahce, Home_Galatasaray, Home_Gaziantep, Home_Hatayspor,
                Home_Istanbulspor, Home_Karagumruk, Home_Kasımpaşa, Home_Kayserispor, Home_Konyaspor, Home_Pendikspor,
                Home_Rize, Home_Samsunspor, Home_Sivasspor,
                Home_Trabzonspor, Away_Alanya, Away_Ankaragücü, Away_Antalyaspor, Away_Basaksehir, Away_Beşiktaş,
                Away_Fenerbahce, Away_Galatasaray, Away_Gaziantep, Away_Hatayspor, Away_Istanbulspor, Away_Karagumruk,
                Away_Kasımpaşa, Away_Kayserispor, Away_Konyaspor, Away_Pendikspor, Away_Rize, Away_Samsunspor,
                Away_Sivasspor, Away_Trabzonspor, Referee_AliSansalan, Referee_ArdaKardesler, Referee_AtillaKaraoğlan,
                Referee_BahattinSimsek,
                Referee_BurakPakkan, Referee_BurakSeker, Referee_CagdasAltay, Referee_CihanAydin,
                Referee_DirençTosunoğlu, Referee_EmreKargin, Referee_HalilUmutMeler, Referee_KadirSaglam,
                Referee_MertGuzenge, Referee_MuratErdogan, Referee_Rare, Referee_TugayNumanoglu, Referee_TurgutDoman,
                Referee_VolkanBayarslan, Referee_ZorbayKucuk, Referee_ÜmitOzturk]

    prediction = model.predict([features])

    return prediction[0]


if st.button('Predict'):
    predicted_score = predict_review_score(week, team_home_info[0], team_away_info[0], team_home_info[1],
                                           team_home_info[2], team_home_info[3], team_home_info[4], team_away_info[1],
                                           team_away_info[2], team_away_info[3], team_away_info[4],
                                           home_bet, draw_bet, away_bet, *team_home_code, *team_away_code,
                                           *select_referee)
    st.success(f"🤩 {predicted_score[0]}")
