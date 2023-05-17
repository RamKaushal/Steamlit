import pandas as pd
import streamlit as st

batsmen_path     = "https://raw.githubusercontent.com/RamKaushal/Steamlit/main/IPL2023_Batsman.csv"
bowler_path      = "https://raw.githubusercontent.com/RamKaushal/Steamlit/main/IPL2023_Bowler.csv"
scoreboard_path  = "https://raw.githubusercontent.com/RamKaushal/Steamlit/main/IPL2023_Match_Scoreboard.csv"
matches_path     = "https://raw.githubusercontent.com/RamKaushal/Steamlit/main/IPL2023_Matches.csv"

batsmen_df = pd.read_csv(batsmen_path,encoding = 'unicode_escape')
bowler_df = pd.read_csv(bowler_path)
scoreboard_df = pd.read_csv(scoreboard_path)
matches_df = pd.read_csv(matches_path,encoding = 'unicode_escape')

dfs = ['batsmen_df','bowler_df','scoreboard_df','matches_df']


st.header("JIO IPL 2023 ANALYSIS")
st.subheader("Please select the dataset you want to analyse")
df_select = st.selectbox('Dataset',['batsmen','bowler','scoreboard','matches'])
if df_select == 'batsmen':
    col1,col2,col3,col4,col5,col6 = st.columns(6)                                               
    with col1:
        st.metric('Unique Batters',batsmen_df['Batsman'].nunique())
    with col2:
        st.metric('Total Teams',batsmen_df['team'].nunique())
    with col3:
        st.metric('Total runs',batsmen_df['Run'].sum())
    with col4:
        st.metric('Total balls bowled',batsmen_df['Ball'].sum())
    with col5:
        st.metric("Total 4's",batsmen_df['4s'].sum())
    with col6:
        st.metric("Total 6's",batsmen_df['6s'].sum())
    st.write(batsmen_df)
    st.subheader("Please select the team")
    teams_df = st.selectbox('Team',batsmen_df['team'].unique())
    batsmen_df_f  = batsmen_df[batsmen_df['team'] ==  teams_df]
    col1,col2,col3,col4,col5,col6 = st.columns(6)                                               
    with col1:
        st.metric('Unique Batters',batsmen_df_f['Batsman'].nunique())
    with col2:
        st.metric('Total Teams',batsmen_df_f['team'].nunique())
    with col3:
        st.metric('Total runs',batsmen_df_f['Run'].sum())
    with col4:
        st.metric('Total balls bowled',batsmen_df_f['Ball'].sum())
    with col5:
        st.metric("Total 4's",batsmen_df_f['4s'].sum())
    with col6:
        st.metric("Total 6's",batsmen_df_f['6s'].sum())
    st.write(batsmen_df_f)
    


if df_select == 'bowler':
    st.write(bowler_df)
if df_select == 'scoreboard':
    st.write(scoreboard_df)
if df_select == 'matches':
    st.write(matches_df)
