from datetime import date
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from princiaplProgram import*


app = dash.Dash(__name__)

colors = {
    "box" : "#1e2742",
    "background" : "#13192f",
    "Heartcolor":"#dc3545" ,
    "tempolor":"#0d6efd" ,

    "Heading2" :"#d1d5db",
    "comments":"#8ea3a5",
    "Heading":"#00d4ad",
    "light-green":"#00ff93",
    "light-blue":"#05a3e4",
    "pink":"#d184dc",
    "yellow":"#ffc23b",
    "white":"#ffffff"
}






app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

       dcc.Interval(
        id='my_interval_time',
        interval=1000, 
        n_intervals=0
       ),
       dcc.Interval(
        id='my_interval',
        interval=2000, 
        n_intervals=0
       ),
       dcc.Interval(
        id='my_interval2',
        interval=150, 
        n_intervals=0
       ),
   

    
    html.Div(
        id='header',
        style={
            'display':'flex',
            'justify-content': 'space-evenly',
            'textAlign': 'center',
            'color': colors['comments'],
            'font-size':'30px',
            'margin': '15px',
    }),

    html.Div(
        style = {
            'display':'flex',
            'justify-content': 'center',
            'background':colors["background"]
        },
        
        children=[
            html.Div(
                style={
                'display':'flex',
                'justify-content':'space-evenly',
                'backgroundColor': colors['box'],
                'color':colors['comments'],
                'textAlign' : 'center',
                'font-size': '30px',
                'width': '70%',
                'height':'380px',
                'border-radius': '3px',
                'padding': '20px',
                'margin': '10px',
                'box-shadow': '0 0 5px 5px #131825',
                    },

                children=[
                    html.Div(
                        children=[
                            html.Img(style={"width":"300px"},src=app.get_asset_url('face.png')),
                            html.Div(children=[html.H3("Mr/s "+pat1.namePatient)]),
                        ]
                    ),

                    html.Div(
                        style={
                            'width':'600px',
                            'color':'#E2E2E2'
                            },
                        children=[
                            html.Div(
                                style={
                                    'margin-top':'60px',
                                    'margin-bottom':'60px',
                                    },
                                children=[ 
                                    html.A(style={'margin-right':'50px'},children=["Sex :"+Sex]),
                                    html.A("Age :"+str(AgePatient)),]),
                            html.Div(
                                style={
                                    'margin-top':'60px',
                                    'margin-bottom':'60px',
                                    },                                
                                children=[                    
                                    html.A(style={'margin-right':'50px'},children=["Blood :"+blood]),
                                    html.A("Room :"+roomNumber),]),
                            html.Div(
                                style={
                                    'margin-top':'60px',
                                    'margin-bottom':'60px',
                                    },                                
                                children=[ html.A("Case :"+patientCase)])
                        ]
                    )
                

                   
                    



                    
                ]
            ),
            #Body Position 
            html.Div(
            id='body_pos',
            style={
            'display':'inline-block',
            'backgroundColor': colors['box'],
            'color':colors['comments'],
            'textAlign' : 'center',
            'font-size': '30px',
            'width': '250px',
            'height':'380px',
            'border-radius': '3px',
            'padding': '20px',
            'margin': '10px',
            'box-shadow': '0 0 5px 5px #131825',
                },
            )
            
            ]), 


    html.Div(
        style = {
            'display':'flex',
            'justify-content': 'space-around',
            'background':colors["background"]
        },
        
        children=[
            # body temperature Value 
            html.Div(
            id='body_temp',
            style={
                'display':'inline-block',
                'backgroundColor': colors['box'],
                'color':colors['comments'],
                'textAlign' : 'center',
                'font-size': '30px',
                'width': '250px',
                'border-radius': '3px',
                'padding': '20px',
                'margin': '10px',
                'box-shadow': '0 0 5px 5px #131825',
                },
            ),


            #Room Temperature Value
            html.Div(
            id='room_temp',
            style={
                'display':'inline-block',
                'backgroundColor': colors['box'],
                'color':colors['comments'],
                'textAlign' : 'center',
                'font-size': '30px',
                'width': '250px',
                'border-radius': '3px',
                'padding': '20px',
                'margin': '10px',
                'box-shadow': '0 0 5px 5px #131825',
                },
            ),

            #Room Humidity Value

            html.Div(
            id='room_hum',
            style={
                'display':'inline-block',
                'backgroundColor': colors['box'],
                'color':colors['comments'],
                'textAlign' : 'center',
                'font-size': '30px',
                'width': '250px',
                'border-radius': '3px',
                'padding': '20px',
                'margin': '10px',
                'box-shadow': '0 0 5px 5px #131825',
                },
            ),

            #Heart Beats Per Minute
            html.Div(
            id='heart-beats',
            style={
                'display':'inline-block',
                'backgroundColor': colors['box'],
                'color':colors['comments'],
                'textAlign' : 'center',
                'font-size': '30px',
                'width': '250px',
                'border-radius': '3px',
                'padding': '20px',
                'margin': '10px',
                'box-shadow': '0 0 5px 5px #131825',
                },
            ),
    ]),


            #Heart Bits Graph
            html.Div(
            style={
            'display':'inline-block',
            'backgroundColor': colors['box'],
            'color':colors['comments'],
            'textAlign' : 'center',
            'font-size': '30px',
            'height':'500px',
            'width':'95%',
            'border-radius': '3px',
            'padding': '20px',
            'margin': '10px',
            'box-shadow': '0 0 5px 5px #131825',
                },
            children=[

                html.Div(style={'display':'flex','justify-content': 'center'},
                    children=[
                        html.Img(style={"width":"60px"},src=app.get_asset_url('heart.png')),
                        html.Div(
                        style={
                        'color':colors["white"],
                        'padding':'10px',
                        'margin-right': '5px'},
                        children=["Heart Beats Monitor"]),
                
                    ]),
                    dcc.Graph(id='hb-graph')
            ]),    

         

])


l=[0.5,-0.2,-0.3,-0.2,0,4,-2,0,0.2,0.3,0.2,0,0]*5

#----------------------Header------------------------------------
@app.callback(Output('header','children') ,
    Input('my_interval_time', 'n_intervals')
)
def update_layout(n):
    time=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)
    return [  
                html.Div(children="Date : "+str(date.today())),
                html.Div(children="Time : "+time)

            ]

#-----------------------Body Temperature-----------------------------------
@app.callback(Output('body_temp','children') ,
    Input('my_interval', 'n_intervals')
)
def update_layout(n):
    bodyTempV=randint(37,42)
    bodyTempMsg=pat1.BodyTemperature(bodyTempV)
    return [    html.Div(
                    style={
                    
                    'background':colors["light-green"],
                    'color':colors["white"],
                    'border-radius':'5px',
                    'padding':'10px',
                    'margin': '0 auto'},
                    children=["Body Temperature"]),
                html.H2(style={'color':colors["white"]},children=[str(bodyTempV)+"°"]),
                html.Div(children=[bodyTempMsg])
            ]


#-----------------------Room Temperature-----------------------------------
@app.callback(Output('room_temp','children') ,
    Input('my_interval', 'n_intervals')
)
def update_layout(n):
    roomTempV=randint(17,35)
    roomTempMsg=pat1.roomTemperature(roomTempV)
    return [    html.Div(
                    style={
                    
                    'background':colors["pink"],
                    'color':colors["white"],
                    'border-radius':'5px',
                    'padding':'10px 5px 10px 5px',
                    'margin': '0 auto'},
                    children=["Room Temperature"]),
                html.H2(style={'color':colors["white"]},children=[str(roomTempV)+"°"]),
                html.Div(children=[roomTempMsg])   
            ]



#-----------------------Room humidity -----------------------------------
@app.callback(Output('room_hum','children') ,
    Input('my_interval', 'n_intervals')
)
def update_layout(n):
    roomHumV=randint(30,70)
    roomHumMsg=pat1.roomHumidity(roomHumV)
    return [    html.Div(
                    style={
                    
                    'background':colors["light-blue"],
                    'color':colors["white"],
                    'border-radius':'5px',
                    'padding':'10px',
                    'margin': '0 auto'},
                    children=["Room Humidity"]),
                html.H2(style={'color':colors["white"]},children=[str(roomHumV)+"%"]),
                html.Div(children=[roomHumMsg])
            ]


#-----------------------Heart Beats BPM-----------------------------------
@app.callback(Output('heart-beats','children') ,
    Input('my_interval', 'n_intervals')
)
def update_layout(n):
    hbpm=randint(50,130)
    bpm=" "+"BPM"
    if hbpm>50 and hbpm<100:
        children = [    html.Div(
                            style={
                            
                            'background':colors["yellow"],
                            'color':colors["white"],
                            'border-radius':'5px',
                            'padding':'10px',
                            'margin': '0 auto'},
                            children=["Heart Beats"]),
                        html.H2(style={'color':colors["white"]},children=[str(hbpm)+bpm]),
                        html.Div(children=["Normal Heart Beats"])
                     ]
    else :
        children = [    html.Div(
                            style={
                            
                            'background':colors["yellow"],
                            'color':colors["white"],
                            'border-radius':'5px',
                            'padding':'10px',
                            'margin': '0 auto'},
                            children=["Heart Beats"]),
                        html.H2(style={'color':colors["white"]},children=[str(hbpm)+bpm]),
                        html.Div(style={'color':'red'},children=["WARNING!"])
                    ]
    return children


#-----------------------Body Postions-----------------------------------
@app.callback(Output('body_pos','children' ) ,
    Input('my_interval', 'n_intervals')
)
def update_layout(n):

    positions=['S','U','D','R','L'] # S:Standing, U:Laying Up, D:Laying Down, R:Laying Right, L:Laying Left
    pos=positions[randint(0,5)]
    if pos=='S':
        source=app.get_asset_url('Standing.png')
    elif pos=='U':
        source=app.get_asset_url('Up.png')
    elif pos=='D':
        source=app.get_asset_url('Down.png')
    elif pos=='R':
        source=app.get_asset_url('Right.png')
    elif pos=='L':
        source=app.get_asset_url('Left.png')

    
    if answer=='yes':
        bodyPosMsg=pat1.BodyPosition(pos,specificPos)
        if bodyPosMsg=="Warning! Patient in the wrong position":
        
            children= [ html.Div(
                            style={
                            
                            'background':colors["Heartcolor"],
                            'color':colors["white"],
                            'border-radius':'5px',
                            'padding':'10px 5px 10px 5px',
                            'margin': '0 auto'},
                            children=["Patient Position"]),

                         html.Img(
                            src=source,
                            style={'width':'auto','hight':'30%','margin':'30px 30px 5px 30px'}
                        ),
                        html.Div(children=[bodyPosMsg],style={'color':'#dc3545'})

                    ]
        else :
           children= [   html.Div(
                            style={
                            
                            'background':colors["Heartcolor"],
                            'color':colors["white"],
                            'border-radius':'5px',
                            'padding':'10px 5px 10px 5px',
                            'margin': '0 auto'},
                            children=["Patient Position"]),
                        html.Img(
                            src=source,
                            style={'width':'auto','hight':'30%','margin':'30px 30px 5px 30px'}
                        ),
                    ]

    else :
            children= [   html.Div(
                            style={
                            
                            'background':colors["Heartcolor"],
                            'color':colors["white"],
                            'border-radius':'5px',
                            'padding':'10px 5px 10px 5px',
                            'margin': '0 auto'},
                            children=["Patient Position"]),
                        html.Img(
                            src=source,
                            style={'width':'auto','hight':'30%','margin':'30px 30px 5px 30px'}
                        ),
                    ]


    return children
#----------Graphs------------------------------------------------

#-----------------------Heart Beats-----------------------------------
@app.callback(Output('hb-graph','figure') ,
    Input('my_interval2', 'n_intervals')
)

def update_layout(n):
    l.append(l[0])
    l.pop(0)
    heartbeats = pd.DataFrame({
    "HB": l
    })


    fig1 = px.line(heartbeats,y="HB",)

    fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['box'],
    font_color=colors['comments']
    )

    return fig1


if __name__ == '__main__':
    app.run_server(debug=True)