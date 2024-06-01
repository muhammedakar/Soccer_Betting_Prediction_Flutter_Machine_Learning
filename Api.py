from flask import Flask, request, jsonify
import joblib
import json

app = Flask(__name__)

model = joblib.load("deployment/bet_total_goal.pkl")


@app.route('/', methods=['POST'])
def post_example():
    data = request.form.get('input')
    data = json.loads(data)

    team_home_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    team_away_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    select_referee = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

    if data['home'] == 'Alanya':
        team_home_info = teams_info[data['home']]
        team_home_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Ankaragücü':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Antalyaspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Basaksehir':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Beşiktaş':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Fenerbahce':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Galatasaray':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Gaziantep':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Hatayspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Istanbulspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Karagumruk':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Kasımpaşa':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Kayserispor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif data['home'] == 'Konyaspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif data['home'] == 'Pendikspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif data['home'] == 'Rize':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif data['home'] == 'Samsunspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif data['home'] == 'Sivasspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif data['home'] == 'Trabzonspor':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif data['home'] == 'Adana':
        team_home_info = teams_info[data['home']]
        team_home_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if data['away'] == 'Alanya':
        team_away_info = teams_info[data['away']]
        team_away_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Ankaragücü':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Antalyaspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Basaksehir':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Beşiktaş':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Fenerbahce':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Galatasaray':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Gaziantep':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Hatayspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Istanbulspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Karagumruk':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Kasımpaşa':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Kayserispor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif data['away'] == 'Konyaspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif data['away'] == 'Pendikspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif data['away'] == 'Rize':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif data['away'] == 'Samsunspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif data['away'] == 'Sivasspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif data['away'] == 'Trabzonspor':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif data['away'] == 'Adana':
        team_away_info = teams_info[data['away']]
        team_away_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if data['referee'] == 'Ali Sansalan':
        select_referee = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Arda Kardesler':
        select_referee = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Atilla Karaoğlan':
        select_referee = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Bahattin Simsek':
        select_referee = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Burak Pakkan':
        select_referee = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Burak Seker':
        select_referee = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Cagdas Altay':
        select_referee = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Cihan Aydin':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Direnç Tosunoğlu':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Emre Kargin':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Halil Umut Meler':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Kadir Saglam':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Mert Guzenge':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Murat Erdogan':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Rare':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif data['referee'] == 'Tugay Numanoglu':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif data['referee'] == 'Turgut Doman':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif data['referee'] == 'Volkan Bayarslan':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif data['referee'] == 'Zorbay Kucuk':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif data['referee'] == 'Ümit Ozturk':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif data['referee'] == 'Abdulkadir Bitigen':
        select_referee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def predict_review_score(Hafta, Home_Value, Away_Value, Home_Atk, Home_Ort, Home_Def, Home_Gen, Away_Atk, Away_Ort,
                             Away_Def, Away_Gen, home_bets, draw_bets, away_bets, Alt_Bet, Ust_Bet, Home_Point,
                             Away_Point,
                             Home_Alanya, Home_Ankaragücü,
                             Home_Antalyaspor, Home_Basaksehir, Home_Beşiktaş, Home_Fenerbahce, Home_Galatasaray,
                             Home_Gaziantep, Home_Hatayspor, Home_Istanbulspor, Home_Karagumruk, Home_Kasımpaşa,
                             Home_Kayserispor, Home_Konyaspor, Home_Pendikspor, Home_Rize, Home_Samsunspor,
                             Home_Sivasspor,
                             Home_Trabzonspor, Away_Alanya, Away_Ankaragücü, Away_Antalyaspor, Away_Basaksehir,
                             Away_Beşiktaş, Away_Fenerbahce, Away_Galatasaray, Away_Gaziantep, Away_Hatayspor,
                             Away_Istanbulspor, Away_Karagumruk, Away_Kasımpaşa, Away_Kayserispor, Away_Konyaspor,
                             Away_Pendikspor, Away_Rize, Away_Samsunspor, Away_Sivasspor, Away_Trabzonspor,
                             Referee_AliSansalan, Referee_ArdaKardesler, Referee_AtillaKaraoğlan,
                             Referee_BahattinSimsek,
                             Referee_BurakPakkan, Referee_BurakSeker, Referee_CagdasAltay, Referee_CihanAydin,
                             Referee_DirençTosunoğlu, Referee_EmreKargin, Referee_HalilUmutMeler, Referee_KadirSaglam,
                             Referee_MertGuzenge, Referee_MuratErdogan, Referee_Rare, Referee_TugayNumanoglu,
                             Referee_TurgutDoman, Referee_VolkanBayarslan, Referee_ZorbayKucuk, Referee_ÜmitOzturk):
        features = [Hafta, Home_Value, Away_Value, Home_Atk, Home_Ort, Home_Def, Home_Gen, Away_Atk, Away_Ort, Away_Def,
                    Away_Gen, home_bets, draw_bets, away_bets, Alt_Bet, Ust_Bet, Home_Point, Away_Point, Home_Alanya,
                    Home_Ankaragücü, Home_Antalyaspor,
                    Home_Basaksehir, Home_Beşiktaş, Home_Fenerbahce, Home_Galatasaray, Home_Gaziantep, Home_Hatayspor,
                    Home_Istanbulspor, Home_Karagumruk, Home_Kasımpaşa, Home_Kayserispor, Home_Konyaspor,
                    Home_Pendikspor,
                    Home_Rize, Home_Samsunspor, Home_Sivasspor,
                    Home_Trabzonspor, Away_Alanya, Away_Ankaragücü, Away_Antalyaspor, Away_Basaksehir, Away_Beşiktaş,
                    Away_Fenerbahce, Away_Galatasaray, Away_Gaziantep, Away_Hatayspor, Away_Istanbulspor,
                    Away_Karagumruk,
                    Away_Kasımpaşa, Away_Kayserispor, Away_Konyaspor, Away_Pendikspor, Away_Rize, Away_Samsunspor,
                    Away_Sivasspor, Away_Trabzonspor, Referee_AliSansalan, Referee_ArdaKardesler,
                    Referee_AtillaKaraoğlan,
                    Referee_BahattinSimsek,
                    Referee_BurakPakkan, Referee_BurakSeker, Referee_CagdasAltay, Referee_CihanAydin,
                    Referee_DirençTosunoğlu, Referee_EmreKargin, Referee_HalilUmutMeler, Referee_KadirSaglam,
                    Referee_MertGuzenge, Referee_MuratErdogan, Referee_Rare, Referee_TugayNumanoglu,
                    Referee_TurgutDoman,
                    Referee_VolkanBayarslan, Referee_ZorbayKucuk, Referee_ÜmitOzturk]

        prediction = model.predict([features])

        return prediction[0]

    predicted_score = predict_review_score(data['week'], team_home_info[0], team_away_info[0], team_home_info[1],
                                           team_home_info[2], team_home_info[3], team_home_info[4], team_away_info[1],
                                           team_away_info[2], team_away_info[3], team_away_info[4],
                                           data['home_bets'], data['draw_bets'], data['away_bets'], data['alt_bet'], data['ust_bet'],
                                           data['home_point'],
                                           data['away_point'], *team_home_code, *team_away_code,
                                           *select_referee)

    return jsonify(response=f'{predicted_score:.2f}')


if __name__ == '__main__':
    app.run(debug=True)
