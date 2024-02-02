from dash.dependencies import Input, Output
from dash import dcc, html 
import dash_bootstrap_components as dbc
from dash import Dash, callback
# import pages
from pages.chatbot.chatbot_view import render_chatbot
from pages.chatbot.chatbot_controller import *
from pages.page_not_found import page_not_found
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext, PromptHelper, StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI

from app import app





search_bar = dbc.Row(
    [
        dbc.Col(html.Div(), width=9),

        dbc.Col(dbc.NavLink("Auto Regressive Model", style={"color": "white"}, href="/prediction_ar"), width="auto"),
         dbc.Col(dbc.NavLink("Global Change", style={"color": "white"}, href="/prediction_gh"), width="auto"),
        dbc.Col(dbc.NavLink("Help", style={"color": "white"}, href="/help"), width="auto"),

    ],
    #no_gutters=True,
    className="ml-auto flex-nowrap mt-12 mt-md-0",
    align="end",

)

#def render_navbar(brand_name:str = "Chatbot", brand_color:str = "#165AA7"):
    
#    return navbar
    
navbar = dbc.Navbar(
    [

        html.A(

            dbc.Row(
                [

                    dbc.Col(
                        html.Img(src=app.get_asset_url('ad.png'), height="80%", width="80%")
                        , style={'marginLeft': "40px", 'width': "300px"}),

                ],
                align="center",
                #no_gutters=True,
            ),
            href="/",
        ),

        #dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        #dbc.Collapse(
        #    search_bar, id="navbar-collapse", navbar=True, is_open=False, className="ml-auto"
        #),

    ],
    color="black",
    dark=True
)
#def serve_content():
#    """
#    :return: html div component
#    """
#    return 
    
#    [html.Div(
#        dcc.Location(id='url', refresh=False),
#        html.Div(id='page-content')
#    ])


search_bar = dbc.Row(
    [
        dbc.Col(html.Div(), width=9),

        dbc.Col(dbc.NavLink("Explainable AI", style={"color": "white"}, href="/xAI/"), width="auto"),
        dbc.Col(dbc.NavLink("Help", style={"color": "white"}, href="/help"), width="auto"),

    ],
    #no_gutters=True,
    className="ml-auto flex-nowrap mt-12 mt-md-0",
    align="end",

)

navbar_layout = dbc.Navbar(
    [

        html.A(

            dbc.Row(
                [

                    dbc.Col(
                        html.Img(src=app.get_asset_url('ad.png'), height="80%", width="80%")
                        , style={'marginLeft': "40px", 'width': "300px"}),

                ],
                align="center",
                #no_gutters=True,
            ),
            href="/",
        ),

        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            search_bar, id="navbar-collapse", navbar=True, is_open=False, className="ml-auto"
        ),

    ],
    color="dark",
    dark=True
)

footer_layout = html.Footer(
    html.Div(
        [

            # html.H5(
            #
            #     '',
            #     className='one columns',
            #     style={'textAlign': 'right'}
            # ),
            # html.Div(
            #             [
            # # html.Img(src=app.get_asset_url('favicon.ico'),  width="80px", style={
            # #                 'height': '50%',
            # #                 'width': '50%'
            # #             }),
            #                 ], className='one columns', style={'textAlign': 'center', 'verticalAlign': 'center'}),
            # html.Img(
            #
            #     src="/static/img/cancerProteomics.png",
            #     id='well_text',
            #     className='three columns'
            #     ,
            #     style={'width': '150px', 'height': '50px', 'backgroundPosition': 'center', 'paddingTop': '10px'}
            #
            # ),
            # html.H5(
            #
            #     '',
            #     className='three columns',
            #     style={'textAlign': 'right'}
            # ),

            # ul list components

            html.Div(

                # ['Supported By NIH ', html.A('LINCS', href='http://www.lincsproject.org/', target="_blank"),
                #  ' Program'],
                [
                    html.H5(
                        'University of Cincinnati',
                        style={'textAlign': 'left', 'color': 'White'}
                    ),
                    html.H5(
                        'College of Medicine',
                        style={'textAlign': 'left', 'color': 'White'}
                    ),
                  #  html.H5(
                  #      'Department of Cancer Biology',
                  #      style={'textAlign': 'left', 'color': 'White'}
                  #  ),
                ],
                className='four columns',
                style={'textAlign': 'right', 'color': 'White', 'height': '85px', 'backgroundPosition': 'center',
                       'paddingTop': '25px', 'paddingLeft': '50px'}
            ),
           

            html.Div(

                # ['Supported By NIH ', html.A('LINCS', href='http://www.lincsproject.org/', target="_blank"),
                #  ' Program'],
                [
                    html.H5(
                        'Supported By:',

                        style={'textAlign': 'left', 'color': 'White'}
                    ),
                    html.H5(
                        'UC Advanced Research Computing / UC CoM',

                        style={'textAlign': 'left', 'color': 'White'}
                    )

                ],
                className='four columns',
                style={'textAlign': 'right', 'color': 'White', 'height': '85px', 'backgroundPosition': 'center',
                       'paddingTop': '25px'}
            ),
            html.Div(

                # ['Supported By NIH ', html.A('LINCS', href='http://www.lincsproject.org/', target="_blank"),
                #  ' Program'],
                [
                   
                   
                    html.H5(
                        html.A('Contact Us', href="mailto:behrouzshamsaei@gmail.com"), style={'textAlign': 'left'})

                ],
                className='four columns',
                style={'textAlign': 'right', 'color': 'White', 'height': '85px', 'backgroundPosition': 'center',
                       'paddingTop': '25px'}
            )

            # dcc.Dropdown(id='gene_dropdown',
            #              multi=True,
            #              value=[STARTING_DRUG],
            #              className='three columns',
            #              options=[{'label': i, 'value': i} for i in df['NAME'].tolist()]
            #              ),
            # html.H5(
            #
            #     '',
            #     className='two columns',
            #     style={'textAlign': 'right'}
            # ),
        ],
        className='row'
    ),
    style={'width': '100%', 'backgroundColor': 'black', 'bottom': '0px', 'marginTop': '30px'}
)





app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    
    dcc.Location(id='url', refresh=False),

    html.Div(navbar_layout),

    # content will be rendered in this element
    html.Div(id='page-content',
             style={'minHeight': ': 100vh'}),
    #html.Div(footer_layout)

],
    style={'marginBottom': '0px', 'marginTop': '0px'})


def init_index(directory_path):
    # model params
    # max_input_size: maximum size of input text for the model.
    # num_outputs: number of output tokens to generate.
    # max_chunk_overlap: maximum overlap allowed between text chunks.
    # chunk_size_limit: limit on the size of each text chunk.
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    # llm predictor with langchain ChatOpenAI
    # ChatOpenAI model is a part of the LangChain library and is used to interact with the GPT-3.5-turbo model provided by OpenAI
    num_output = 4096    

    prompt_helper = PromptHelper(max_input_size, num_output, chunk_overlap_ratio= 0.1, chunk_size_limit=1024)
    #prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    # read documents from docs folder
    documents = SimpleDirectoryReader(directory_path).load_data()
    # docs = SimpleDirectoryReader(directory_path).load_data()
    # init index with documents data
    # This index is created using the LlamaIndex library. It processes the document content and constructs the index to facilitate efficient querying
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

    # save the created index
    #index.save_to_disk('index.json')
    index.storage_context.persist(persist_dir='OneDrive_1_1-27-2024.json')

# create index
#init_index("OneDrive_1_1-27-2024")
#app.layout = serve_content()

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    """
    :param pathname: path of the actual page
    :return: page
    """

    if pathname in '/' or pathname in '/chatbot':
        return render_chatbot()
    return page_not_found()
    
    

#index = construct_index("complete_docs")
if __name__ == '__main__':
    app.run_server(debug=False, port=8050, host='0.0.0.0')
