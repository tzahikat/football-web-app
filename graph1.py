
import pandas as pd
import plotly.graph_objects as go

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

def fig(league_list):
    ids = []
    if len(league_list) == 0:
        ids = [1854, 1869, 1845, 1843, 2411]
    else:
        for item in league_list:
            if item in league_options:
                ids.append(league_options[item])

    data = pd.read_csv('spi_matches (2).csv')
    clean_data = data.dropna()
    avg_goals_per_game = clean_data.groupby(['season', 'league_id']).apply(
        lambda x: (x['score1'] + x['score2']).sum() / len(x))
    filtered_df = clean_data[clean_data['league_id'].isin(ids)]
    avg_scores_df = avg_goals_per_game.reset_index()
    leagues_name_df = clean_data[['league_id', 'league']]
    leagues_name_df = leagues_name_df.drop_duplicates()
    league_names = leagues_name_df.set_index('league_id')
    # Merge the original DataFrame with the new DataFrame containing the average scores
    new_df = pd.merge(filtered_df, avg_scores_df, on=['season', 'league_id'], how='left')

    # Displaying the new DataFrame
    fin_df = new_df[['season', 'league_id', 0]]

    traces = []
    i=0
    for league_id, data in fin_df.groupby('league_id'):
        trace = go.Scatter(
            x=data['season'],
            y=data[0],
            name=league_list[i]

        )
        traces.append(trace)
        i += 1
    layout = go.Layout(
        title='Average Match Score by Season for Different Leagues',
        xaxis=dict(title='Season'),
        yaxis=dict(title='Avg Score per Game'),
        showlegend=True
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig
