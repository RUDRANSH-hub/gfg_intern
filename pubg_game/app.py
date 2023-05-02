# %%writefile app.py
import streamlit as st
import pandas as pd
import pickle
# import pubg_model
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model
# Create a sidebar
st.sidebar.title('PUBG Win Prediction')

def predict_win_place_perc(DBNOs, headshotKills, killPlace, killPoints, killStreaks,
                           longestKill, matchType, numGroups, rankPoints, roadKills,
                           teamKills, vehicleDestroys, weaponsAcquired, winPoints,
                           playersJoined, totalDistance, killswithoutMoving,
                           headshot_rate, killsNorm, damageDealtNorm, maxPlaceNorm,
                           matchDurationNorm, traveldistance, healsnboosts, assist):
    
    # Load the pre-trained CatBoost model
    
#     model = pickle.load(open('pubg_model','rb'))
    model=load_model('pubg_model')


    # Encode matchType as a one-hot vector
    matchType_encoded = pd.get_dummies([matchType], prefix='matchType').reindex(
        columns=model.feature_names_).fillna(0)

    # Create a DataFrame with the input features
    input_df = pd.DataFrame({
        'DBNOs': [DBNOs],
        'headshotKills': [headshotKills],
        'killPlace': [killPlace],
        'killPoints': [killPoints],
        'killStreaks': [killStreaks],
        'longestKill': [longestKill],
        'numGroups': [numGroups],
        'rankPoints': [rankPoints],
        'roadKills': [roadKills],
        'teamKills': [teamKills],
        'vehicleDestroys': [vehicleDestroys],
        'weaponsAcquired': [weaponsAcquired],
        'winPoints': [winPoints],
        'playersJoined': [playersJoined],
        'totalDistance': [totalDistance],
        'killswithoutMoving': [killswithoutMoving],
        'headshot_rate': [headshot_rate],
        'killsNorm': [killsNorm],
        'damageDealtNorm': [damageDealtNorm],
        'maxPlaceNorm': [maxPlaceNorm],
        'matchDurationNorm': [matchDurationNorm],
        'traveldistance': [traveldistance],
        'healsnboosts': [healsnboosts],
        'assist': [assist]
    })

    # Concatenate the one-hot encoded matchType with the input DataFrame
    input_df = pd.concat([input_df, matchType_encoded], axis=1)

    # Make the prediction using the pre-trained model
    pred = model.predict(input_df)[0]

    return pred



def app():
    st.title('PUBG Win Place Prediction')
    
    DBNOs = st.number_input('DBNOs', min_value=0)
    headshotKills = st.number_input('Headshot Kills', min_value=0)
    killPlace = st.number_input('Kill Place', min_value=1)
    killPoints = st.number_input('Kill Points', min_value=0)
    killStreaks = st.number_input('Kill Streaks', min_value=0)
    longestKill = st.number_input('Longest Kill', min_value=0)
    matchType = st.selectbox('Match Type', ['solo', 'duo', 'squad', 'solo-fpp', 'duo-fpp', 'squad-fpp'])
    numGroups = st.number_input('Num Groups', min_value=1)
    rankPoints = st.number_input('Rank Points', min_value=0)
    roadKills = st.number_input('Road Kills', min_value=0)
    teamKills = st.number_input('Team Kills', min_value=0)
    vehicleDestroys = st.number_input('Vehicle Destroys', min_value=0)
    weaponsAcquired= st.number_input('Weapons Acquired', min_value=0)
    winPoints = st.number_input('Win Points', min_value=0)
    playersJoined = st.number_input('Players Joined', min_value=1)
    totalDistance = st.number_input('Total Distance', min_value=0)
    killswithoutMoving = st.number_input('Kills Without Moving', min_value=0)
    headshot_rate = st.number_input('Headshot Rate', min_value=0)
    killsNorm = st.number_input('Kills Norm', min_value=0)
    damageDealtNorm = st.number_input('Damage Dealt Norm', min_value=0)
    maxPlaceNorm = st.number_input('Max Place Norm', min_value=0)
    matchDurationNorm = st.number_input('Match Duration Norm', min_value=0)
    traveldistance = st.number_input('Travel Distance', min_value=0)
    healsnboosts = st.number_input('Heals and Boosts', min_value=0)
    assist = st.number_input('Assist', min_value=0)

    if st.button('Predict Win Place Percentage'):
        result = predict_win_place_perc(DBNOs, headshotKills, killPlace, killPoints, killStreaks,
                                        longestKill, matchType, numGroups, rankPoints, roadKills,
                                        teamKills, vehicleDestroys, weaponsAcquired, winPoints,
                                        playersJoined, totalDistance, killswithoutMoving,
                                        headshot_rate, killsNorm, damageDealtNorm, maxPlaceNorm,
                                        matchDurationNorm, traveldistance, healsnboosts, assist)
        st.success('The predicted Win Place Percentage is {:.2f}'.format(result))




if __name__ == '__main__':
    app()
