#!/usr/bin/env python
# coding: utf-8

# In[471]:


import pandas as pd
import plotly.express as px


# In[472]:


masks=pd.read_csv("masks.csv")


# In[473]:


maskss=pd.read_csv("maskss.csv")
maskss


# In[474]:


df5= maskss.melt(id_vars = 'Factors', value_vars=list(maskss.columns[1:]))
df5


# In[475]:


#total environmental factors gowns
Totals=pd.read_csv("Total.csv")


# In[476]:


dff = Totals.melt(id_vars = 'Factors', value_vars=list(Totals.columns[1:]))
dff.head(2)

drapes=pd.read_csv("Drapes.csv")
drapes

d= drapes.melt(id_vars = ' Factors', value_vars=list(drapes.columns[1:]))
d
d.rename({'variable':'Drapes','value':'Value'},axis=1,inplace=True)
d
# In[477]:


dff.rename({'variable':'Gowns','value':'Values'},axis=1,inplace=True)
dff.head(2)


# In[478]:


df2= masks.melt(id_vars = 'Factors', value_vars=list(masks.columns[1:]))
df2.head(2)


# In[479]:


df2.rename({'variable':'Masks','value':'Values'},axis=1,inplace=True)
df2.head(2)


# In[480]:


df5.rename({'variable':'Masks','value':'Values'},axis=1,inplace=True)
df5


# In[481]:


#pip install jupyter-dash


# In[510]:


#from jupyter_dash import JupyterDash
import plotly.express as px
import dash
from dash import dcc
from dash import  html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px

# Iris bar figure
def drawFigure1():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        dff, x="Gowns", y="Values", color="Factors",title="Disposable,Reusable,Revolution-Zero Gowns",
                        color_discrete_map={'CO2(KGs)': '#d62728', 'Energy(MJ)': '#ED9121', 'Water(KGs)': '#00FFF5',
                                            'Waste(KGs)': '#834333'})
                    #color_discrete_sequence = ['#e6701d', '#3566c1', '#ffc61c', '#a7a6a7'])
                        #color_discrete_map={'Detergents':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})

                        
                    .update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(0,0,0,0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# Text field
def drawFigure2():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(df2,x="Masks",y="Values",color="Factors",title="Reusable and Single Use Masks")
                                  #color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(9, 74, 123, 1)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])


def drawFigure3():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df5,x="Masks",y="Values",color="Factors",title="Single Use and Reusable Masks  ",

                        color_discrete_map={'CO2(KGs)': '#d62728', 'Energy(MJ)': '#ED9121', 'Water(KGs)': '#00FFF5',
                                            'Land Use(PT)': '#834333'})

                        
                        #color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(6, 72, 120, 4)',
                        #paper_bgcolor= 'rgba(9, 74, 122, 1)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])


def drawFigure4():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(d, x=" Factors", y="Value", color=" Factors", title="Drapes and Tapes",
                                  color_discrete_map={'CO2(KGs)': '#d62728', 'Energy(MJ)': '#ED9121',
                                                      'Water(KGs)': '#00FFF5', ' Waste(KGs)': '#834333', })
                        .update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(8, 73, 123, 2)',
                        # paper_bgcolor= 'rgba(9, 74, 123, 1)',

                    ),
                    config={
                        'displayModeBar': False

                    }

                )

            ])
        ),
    ])



#draw text1
def drawText1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Key Environmental Impact from Gowns"),
                ], style={'textAlign': 'left'})
            ])
        ),
    ])


# Drawtext2
def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Other Environmental Impact from Masks"),
                ], style={'textAlign': 'left','font':12})
            ])
        ),
    ])


def drawText3():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Key Environmental Impact from Masks"),
                    
                ], style={'textAlign': 'left','font':12,})
            ])
        ),
    ])


def drawText4():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Environmental Impact of Drapes and Tapes"),

                ], style={'textAlign': 'Left', 'font': 12, })
            ])
        ),
    ])


#app = JupyterDash(__name__)
# Build App
app = dash.Dash(__name__,
                  
    external_stylesheets=[dbc.themes.BOOTSTRAP],
                  meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                 )
server=app.server
                 
colors={'background':'#000000','text':'#000000'}

app.layout = html.Div(style={'backgroundColor':colors['background']},children=[
    
    html.Div([ 
        html.H1("Environmental Impact of Medical Textiles")
        
    ],style={'textAlign':'center','color':'#FFFFFF'}),
    
    
    dbc.Card(         
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText1()
                ],xs=12,md=12, lg=6),
                dbc.Col([
                    drawText3()
                ],xs=12,md=8, lg=6),
                
                ],align='center'),            
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure1() 
                ], xs=12,md=8, lg=6),
                
                dbc.Col([
                    drawFigure3() 
                ], xs=12,md=8, lg=6),
                
              ], align='center'),      
            html.Br(),
             dbc.Row([
                dbc.Col([
                    drawText2() 
                ], xs=12,md=8, lg=6),
                dbc.Col([
                    drawText4()
                ], xs=12,md=6, lg=6),
                
              ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure2()
                ], xs=12, md=6, lg=6),
                dbc.Col([
                    drawFigure4
                    ()
                ], xs=12, md=6, lg=6),

            ], align='center'),
            html.Br(),

            dbc.Row([

                 dbc.Col([
                        ''
                    ], xs=12, md=6, lg=6),


                dbc.Col([

                    html.Img(src=app.get_asset_url('logo.jpg'), style={'height': '100%', 'width': '100%','textAlign': 'right'}),

                ], style={'textAlign': 'right'}, xs=12, md=12, lg=6),
            ], align='right'),

        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook

#app.run_server( debug = True,port=8053)
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:





# In[ ]:




