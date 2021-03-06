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
# print(region_list)

app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Covid Dashboard', style={'textAlign': 'center', \
                                                                      'marginTop': 40, 'marginBottom': -50}),
    html.Div([
        html.P('The first two graphs visualize the number of cases per week (the graph on the left)'
               ' and the total number of cases till now (the graph on the right). '),
        html.P("The two grahps below visualize the occupation of the medical beds and the occupation of the ICU beds. "
               "Since august 2021 the Italian goverment will look at the occupation of the medical and ICU beds for changing colors."),
        html.P("The color will change based on analytical measures and the border values provided by the government."),

        dcc.Dropdown(id='dropdown', style={'width': '200px'},
                     options=region_list,
                     value='22'),
        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),

        html.P(id='zone_type', style={'textAlign': 'center'}),

        dcc.Graph(id='bar_plot')
    ], style={'margin': '100px', }),


])

@app.callback(Output(component_id='bar_plot', component_property='figure'),
              Output(component_id='zone_type', component_property='children'),
              Output("loading-output-1", "children"),
              [Input(component_id='dropdown', component_property='value')])


def graph_update(dropdown_value):
    df = lastupdate_data(dropdown_value)
    df_total = total_data(dropdown_value)
    df_medical = get_medicaldata(dropdown_value)
    df_ICU = get_ICUdata(dropdown_value)

    title_1 = f'Cases per week.<br>' \
              f' In the last 24 hours there were {df["value"].iloc[-1]} positive tests.<br> '

    title_2 = f'Total cases.'

    fig = make_subplots(rows=2, cols=2, subplot_titles=(title_1, title_2,
                                                        'Medical bed occupation',
                                                        'ICU bed occupation'),
                        )

    # fig.add_trace(go.Scatter(x=df['date'], y=df['value'], name='test per day',\
    #                             line=dict(color='Black', width=0.5, dash='dot')
    #                             # label={'Positive test per day'}
    #                             ),  row=1, col=1)

    df_rolweek = df.resample('W', on='date').mean()
    fig.add_trace(go.Scatter(x=df_rolweek.index, y=df_rolweek['value'],
                    name='Week average',
                    line=dict(color='Blue', width=1),
                    ),  row=1, col=1)


    fig['layout']['xaxis2'].update(title_text='Dates')
    fig['layout']['yaxis2'].update(title_text='Positive tests')

    fig.update_layout(height=700,
                      # title=f'Last update {df["date"].iloc[-1]}',
                      # xaxis_title='Dates',
                      # yaxis_title='Positive tests',
                      margin=dict(l=20, r=200, t=100, b=20),
                      )

    fig.add_trace(go.Scatter(x=df_total['date'], y=df_total['value'], name='Total case per day', \
                             line=dict(color='Black', width=0.5)
                             # label={'Positive test per day'}
                             ), row=1, col=2
                  )
    fig['layout']['xaxis2'].update(title_text='Dates')
    fig['layout']['yaxis2'].update(title_text='Total Positive tests')
    # fig.update_layout(height=700,
    #                   xaxis_title='Dates',
    #                   yaxis_title='Total Positive tests',
    #                   margin=dict(l=20, r=200, t=100, b=20),
    #                   )

    # df_medical_sum = df_medical.resample('W', on='date')
    fig.add_trace(go.Scatter(x=df_medical['date'], y=df_medical['value'], name='Medical bed occupation', \
                             line=dict(color='black', width=2)
                             # label={'Positive test per day'}
                             ), row=2, col=1
                  )
    fig['layout']['xaxis3'].update(title_text='Dates')
    fig['layout']['yaxis3'].update(title_text='Medical beds occupied (%)')

    fig.add_trace(go.Scatter(x=df_ICU['date'], y=df_ICU['value'], name='ICU occupation', \
                             line=dict(color='black', width=2)
                             # label={'Positive test per day'}
                             ), row=2, col=2
                  )
    fig['layout']['xaxis4'].update(title_text='Dates')
    fig['layout']['yaxis4'].update(title_text='ICU occupied (%)')

    # Colors Medical beds
    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=-10,
                  x1=df_ICU['date'].iloc[-1], y1=15,
                  fillcolor="white",
                  row=2, col=1,
                  opacity=0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=15,
                  x1=df_ICU['date'].iloc[-1], y1=30,
                  fillcolor="yellow",
                  row=2, col=1,
                  opacity=0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=30,
                  x1=df_ICU['date'].iloc[-1], y1=40,

                  fillcolor="orange",
                  row=2, col=1,
                  opacity=0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=40,
                  x1=df_ICU['date'].iloc[-1], y1=100,
                  fillcolor="red",
                  row=2, col=1,
                  opacity=0.5,
                  line_width=0
                  )

    #Colors ICU
    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=-10,
                  x1=df_ICU['date'].iloc[-1], y1=10,
                  fillcolor="white",
                  row=2, col=2,
                  opacity = 0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=10,
                  x1=df_ICU['date'].iloc[-1], y1=20,
                  fillcolor="yellow",
                  row=2, col=2,
                  opacity = 0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=20,
                  x1=df_ICU['date'].iloc[-1], y1=30,

                  fillcolor="orange",
                  row=2, col=2,
                  opacity=0.5,
                  line_width=0
                  )

    fig.add_shape(type="rect",
                  x0=df_ICU['date'].iloc[0], y0=30,
                  x1=df_ICU['date'].iloc[-1], y1=100,
                  fillcolor="red",
                  row=2, col=2,
                  opacity=0.5,
                  line_width=0
                  )

    color_zone = change_color(dropdown_value)

    value_output = f'The color code for this region is {color_zone}. \n' \
                    f'Last update {df["date"].iloc[-1]}'

    value = ""
    return fig, value_output, value


if __name__ == '__main__':
    app.run_server()



