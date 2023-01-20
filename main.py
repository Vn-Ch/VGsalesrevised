import dash
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

#data exploration with pandas

df = pd.read_csv("vgsales.csv")

#print(df[:5])
#print(df.loc[:5,["World Sales"]])
print(df.Genre.nunique())
print(df.Genre.unique())
print(sorted(df.Year.unique()))

#data visualization with Plotly

fig_pie = px.pie(data_frame=df, names="Genre", values='Japan Sales' )
fig_pie.show()

fig_bar = px.bar(data_frame=df, x='Genre', y='North American Sales')
fig_bar.show()

fig_hist = px.histogram(data_frame=df, x='Year', y='North American Sales', color='Year', animation_frame='Genre', title='Sales by year feat Genre')
fig_hist.show()

#Interactive graphing with Dash

app = dash.Dash(__name__)
server = app.server

app.layout=html.Div([
    html.H1('Graph Analysis with Charming Data'),
    dcc.Dropdown(id='genre-choice', options=[{'label':x, 'value':x} for x in sorted(df.Genre.unique())],
                 value='Sports'
                 ),
    dcc.Graph(id='my-graph', figure={})
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphing(value_genre):
    print(value_genre)
    dff = df[df.Genre==value_genre]
    fig = px.bar(data_frame=dff, x='Year', y='World Sales')

    return fig

if __name__=='__main__':
    app.run_server()
