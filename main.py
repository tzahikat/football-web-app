
import numpy as np
import pandas as pd
import streamlit as st
import graph1
import graph2
import graph3
from PIL import Image

icon = Image.open('3297636.ico')
st.set_page_config(layout="wide", page_icon=icon)  # Set the layout to wide

# Set up the Streamlit app
st.title("The Evolution of Football in Recent Years")
st.write('This graph goal is to expose the viewer to the average score across all major leagues that were sampled by season.The viewer can observe and gain insight such as the decrease in the average score per season,But this information is generelized and in order to gain valuable insight we need to dive deeper')
fig3 = graph3.fig()
st.plotly_chart(fig3, use_container_width=True)
st.write('---')

league_options = {"French Ligue 1": 1843,
                  "Barclays Premier League": 2411,
                  "Spanish Primera Division": 1869,
                  "Italy Serie A": 1854,
                  "German Bundesliga": 1845,
                  "Major League Soccer": 1951,
                  "Brasileiro Série A": 2105,
                  "Argentina Primera Division": 5641,
                  "Portuguese Liga": 1864,
                  "Dutch Eredivisie": 1849
                  }


selected_leauges1 = st.multiselect(
    "Select Leagues", options=league_options.keys(), default=["Italy Serie A", "Spanish Primera Division", "German Bundesliga", "French Ligue 1", "Barclays Premier League"]
)
if len(selected_leauges1) == 0:
    selected_leauges1 = [1854, 1869, 1845, 1843, 2411]

st.write('This graph goal is examine the average goals number across major leagues by seasons.The viewers can gain valuable insights such as the differences between leagues and seasons.By understanding those diffrences individuals would be able to understand the leagues characteristics better and can compare players or clubs easily ')
fig1 = graph1.fig(selected_leauges1)
st.plotly_chart(fig1, use_container_width=True)
st.write('---')

selected_leauges2 = st.multiselect(
    "Select Leagues", options=league_options.keys(), default=["Italy Serie A", "Spanish Primera Division", "German Bundesliga", "French Ligue 1", "Barclays Premier League"], key=2
)
if len(selected_leauges2) == 0:
    selected_leauges2 = [1854, 1869, 1845, 1843, 2411]

st.write('This graph goal is compare leagues in terms of the model prediction against real world results.The metric xg1/xg2 represent the number of goals predicted for each team in a match.The derived metric the we used named expected goals diffrentiation and his formula is (xg1+xg2)-(score1+score2).The viewers can understand and evaluate the model strength and distribution proprties by different leagues.')
fig2 = graph2.fig(selected_leauges2)
st.plotly_chart(fig2, use_container_width=True)
