# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser. (Press CTRL+C to quit)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from dash.dependencies import Input, Output

# Checking dash installation
print(dcc.__version__)

# Get a pre-set CSS stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Changing the background color and text font
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
fig0 = go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))

fig0.update_layout(
    margin=dict(t=0, l=0, r=0, b=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# read the data from prepared file
df = pd.read_csv('SurveyDashInput.csv')


def figure_creator(tabIdentifier):
    if tabIdentifier == "Data Management":
        fig = go.Figure(go.Sunburst(
            labels=df['Storage Solutions'],
            parents=df['Storage Solutions Parents_1'],
            values=df['Storage Values'])
        )
    elif tabIdentifier == "Data Processing":
        fig = go.Figure(go.Sunburst(
            labels=df['Data Processing'],
            parents=df['Data Processing Parents'],
            values=df['Processing Values'])
        )
    elif tabIdentifier == "Data Analysis":
        fig = go.Figure(go.Sunburst(
            labels=df['Data Analysis'],
            parents=df['Data Analysis Parents'],
            values=df['Data Analysis Values'])
        )
    elif tabIdentifier == "Machine Learning":
        fig = go.Figure(go.Sunburst(
            labels=df['Machine Learning'],
            parents=df['Machine Learning Parents'],
            values=df['Machine Learning Values'])
        )


    fig.update_layout(
        margin=dict(t=1, l=0, r=0, b=0),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig

# Styling the tabs
tabs_styles = {
    'height': '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


# Generate the layout for the multi-tab dashboard
#    style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']},

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline",
             value='tab-2',
             parent_className='custom-tabs',
             className='custom-tabs-container',
             children=[
                 dcc.Tab(label=df['Tabs'][0],
                         value=df['Tabs'][0],
                         children=[dcc.Graph(figure=figure_creator(df['Tabs'][0]))],
                         style=tab_style,
                         selected_style=tab_selected_style
                         ),
                 dcc.Tab(label=df['Tabs'][1],
                         value=df['Tabs'][1],
                         children=[dcc.Graph(figure=figure_creator(df['Tabs'][1]))],
                         style=tab_style, selected_style=tab_selected_style
                         ),
                 dcc.Tab(label=df['Tabs'][2],
                         value=df['Tabs'][2],
                         children=[dcc.Graph(figure=figure_creator(df['Tabs'][2]))],
                         style=tab_style, selected_style=tab_selected_style
                         ),
                 dcc.Tab(label=df['Tabs'][3],
                         value=df['Tabs'][3],
                         children=[dcc.Graph(figure=figure_creator(df['Tabs'][3]))],
                         style=tab_style, selected_style=tab_selected_style
                         )
             ]),
    html.Div(id='tabs-content-inline')
])


@app.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):
    if tab == df['Tabs'][0]:
        return html.Div([
            html.H1(df['SubTitles'][0], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])
    elif tab == df['Tabs'][1]:
        return html.Div([
            html.H1(df['SubTitles'][1], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])
    elif tab == df['Tabs'][2]:
        return html.Div([
            html.H1(df['SubTitles'][2], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])
    elif tab == df['Tabs'][3]:
        return html.Div([
            html.H1(df['SubTitles'][3], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])
    elif tab == df['Tabs'][4]:
        return html.Div([
            html.H1(df['SubTitles'][4], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])
    elif tab == df['Tabs'][5]:
        return html.Div([
            html.H1(df['SubTitles'][5], style={'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text']})
        ])


if __name__ == '__main__':
    # active "hot-reloading" by default
    app.run_server(debug=True)
