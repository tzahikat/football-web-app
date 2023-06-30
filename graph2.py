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
    clean_data['xg_diff'] = clean_data['xg1']+clean_data['xg2']-clean_data['score1']-clean_data['score2']
    leagues_name_df = clean_data[['league_id', 'league']]
    leagues_name_df = leagues_name_df.drop_duplicates()
    league_names = leagues_name_df.set_index('league_id')
    selected_df = clean_data[clean_data['league_id'].isin(ids)]
    grouped_data = [group['xg_diff'].values for _, group in selected_df.groupby('league_id')]

    # Create a list of Box traces for each league
    traces = []
    for i, data in enumerate(grouped_data):
        trace = go.Box(
            y=data,
            name=league_list[i]
        )
        traces.append(trace)

    # Create the layout
    layout = go.Layout(
        title='Distribution of xg_diff by Different Leagues',
        xaxis=dict(title='League Name'),
        yaxis=dict(title='xg_diff')
    )

    # Create the figure
    fig = go.Figure(data=traces, layout=layout)
    return fig
