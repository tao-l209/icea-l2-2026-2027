from functools import partial

from shiny.express import ui
from shiny.ui import page_navbar

ui.page_opts(
    title="App with navbar",  
    page_fn=partial(page_navbar, id="page"),  
)

with ui.sidebar(bg="#f8f8f8"):  
    "Sidebar"  

"Main content"

with ui.sidebar(position="right", bg="#f8f8f8"):  
    "Sidebar"

ui.page_opts(
    title="App with navbar",  
    page_fn=partial(  
        page_navbar,  
        id="page",  
        navbar_options=navbar_options(position="fixed-bottom"),  
    ),  
)

