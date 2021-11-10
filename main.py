#This application will show the currect positive covid tests in Italy
#The application will be used to give an indication if certain regions in Italy will change there color.

#The data that will be used comes from pcm-dpc/COVID-19

from GetData import *
import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc

from plotly.subplots import make_subplots
from dash.dependencies import Input, Output


app = dash.Dash()
region_list = get_regions()

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Covid Dashboard', style={'textAlign': 'center', \
                                                                      'marginTop': 40, 'marginBottom': 40}),

    dcc.Dropdown(id='dropdown', style={'marginleft': '200px', 'width': '200px'},
                 options=region_list,
                 value='22'),
    dcc.Graph(id='bar_plot')
])

@app.callback(Output(component_id='bar_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])


def graph_update(dropdown_value):
    df = lastupdate_data(dropdown_value)
    df_total = total_data(dropdown_value)

    title_1 = f'Cases per day. In the last 24 hours there were {df["value"].iloc[-1]} positive tests. ' \
              f'Last update {df["date"].iloc[-1]}'

    title_2 = f'Total cases.'

    fig = make_subplots(rows=2, cols=1, subplot_titles=(title_1, title_2),
                        shared_xaxes=True,
                        )

    fig.add_trace(go.Scatter(x=df['date'], y=df['value'], name='test per day',\
                                line=dict(color='Black', width=0.5, dash='dot')
                                # label={'Positive test per day'}
                                ),  row=1, col=1)

    df_rolweek = df.resample('W', on='date').mean()
    fig.add_trace(go.Scatter(x=df_rolweek.index, y=df_rolweek['value'],
                    name='Week average',
                    line=dict(color='Blue', width=1),
                    ),  row=1, col=1)

    fig.add_hline(y=50, line_dash="dash", line_color="yellow", name='start Yellow zone')
    fig.add_hline(y=150, line_dash="dash", line_color="orange", name='start Orange zone')
    fig.add_hline(y=250, line_dash="dash", line_color="red", name='start Red zone')

    fig.update_layout(height=700,
                      yaxis_title='Positive tests',
                      margin=dict(l=20, r=200, t=100, b=20),
                      )

    fig.add_trace(go.Scatter(x=df_total['date'], y=df_total['value'], name='sum total case per day', \
                             line=dict(color='Black', width=0.5)
                             # label={'Positive test per day'}
                             ), row=2, col=1
                  )
    fig.update_layout(height=700,
                      xaxis_title='Dates',
                      yaxis_title='Total Positive tests',
                      margin=dict(l=20, r=200, t=100, b=20),
                      )
    return fig


if __name__ == '__main__':
    app.run_server()


