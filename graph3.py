import pandas as pd
import plotly.graph_objects as go

def fig():
    data = pd.read_csv('spi_matches (2).csv')
    clean_data = data.dropna()

    # Grouping by "season" and calculating the average goals per game
    avg_goals_per_game = clean_data.groupby('season').apply(lambda x: (x['score1'] + x['score2']).sum() / len(x))

    # Creating a new DataFrame with the average goals per game
    new_df = pd.DataFrame(avg_goals_per_game, columns=['average_goals_per_game'])

    # Creating a bar plot
    fig = go.Figure()
    fig.add_trace(go.Bar(x=new_df.index, y=new_df['average_goals_per_game'], name='Average Goals per Game'))

    # Adding a line plot on top of the bar plot
    fig.add_trace(go.Scatter(x=new_df.index, y=new_df['average_goals_per_game'], mode='lines+markers',
                             marker=dict(color='red'), name='Average Goals per Game'))

    # Setting labels and title
    fig.update_layout(xaxis_title='Season', yaxis_title='Average Goals per Game', title='Average Goals per Game by Season')
    fig.update_layout(yaxis=dict(range=[1.8, 3]))
    # Rotating x-axis labels for better readability (optional)
    fig.update_xaxes(tickangle=45)
    return fig
