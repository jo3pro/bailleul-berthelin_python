import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

from main import CHEMIN_ABSOLU, pourcentage_de_communes_défa_par_dép_selon_range_0_25_50_75_100 as dictRangePourcent

app = dash.Dash(__name__)
# command to launch: cloeberthelin$ /usr/local/bin/python3 /Users/cloeberthelin/labo_school/bailleul-berthelin_python/bailleul-berthelin_python/app.py
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

breakpoint

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
"""
df = pd.DataFrame({
	"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
	"Amount": [4, 1, 2, 2, 4, 5],
	"City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
"""


dep_list = []
pourcentage_list = []
with open(CHEMIN_ABSOLU, mode='r', encoding='utf8') as f:
    for elem in f:
        dep_list.append([elem.split(',')[0]])
        pourcentage_list.append([elem.split(",")[1].split('\n')[0]])

depTitle = str(dep_list[0])
depTitle = depTitle.split("['")[1].split("']")[0]

pourcenTitle = str(pourcentage_list[0])
pourcenTitle = pourcenTitle.split("['")[1].split("']")[0]
pourcentage_list.pop(0)
dep_list.pop(0)

data = {depTitle: dep_list, pourcenTitle: pourcentage_list}
#df = pd.DataFrame(data=data)
tableDf = pd.DataFrame(data=data)


def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ], className="tableColor")


vtest = dictRangePourcent()

df = pd.DataFrame({
    "LesRanges": ['0', '0-25', '25-50', '50-75', '75-100'],
    # "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [vtest['0'], vtest['0-25'], vtest['25-50'], vtest['50-75'], vtest['75-100']]
})
fig = px.bar(df, x="LesRanges", y="Amount", barmode="group")


fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Tableau de bord',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Villes en zone agricole défavorisée', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    html.Div(children='test table', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    generate_table(tableDf)
])
"""
df = pd.read_csv('/Users/cloeberthelin/labo_school/bailleul-berthelin_python/bailleul-berthelin_python/pourcent_defavorise.csv')

def generate_table(dataframe, max_rows=100):
	return html.Table([
		html.Thead(
			html.Tr([html.Th(col) for col in dataframe.columns])
		),
		html.Tbody([
			html.Tr([
				html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
			]) for i in range(min(len(dataframe), max_rows))
		])
	])


app = dash.Dash(__name__)

app.layout = html.Div([
	html.H4(children='Pourcentage zones agricoles défavorisées par département en France (2017)'),
	generate_table(df)
])"""

if __name__ == '__main__':
    app.run_server(debug=True)
