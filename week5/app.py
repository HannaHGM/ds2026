from shiny import ui, render, App
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

# UI -----------------------------------
app_ui = ui.page_sidebar(
    ui.sidebar("SIDEBAR YAY", 
               ui.input_slider(id='slider2', 
                               label="sidebar slider", 
                               min=100, max=200, value=100),
               ui.input_select(id="line_select", 
                               label="Pick a line", 
                               choices=["central", "district", "H&C"]
                               ),
               ),
    ui.h1("TfL Dashboard"),
    ui.h2("Check it out before leaving the house"),
    ui.input_slider(id = "slider1", 
                    label="SLIDER YAY", 
                    min=0, max=100, value=10),
    ui.output_code("value"),
    ui.output_table("status_table"),
    ui.output_text("health_badge"),
)

# SERVER -----------------------------
def server(input, output, session):
    @render.code
    def value():
        return f"The value is {input.slider1()}"
    
    def network_status():
        url = "https://api.tfl.gov.uk/line/mode/tube/status"
        r = requests.get(url, timeout=10)
        data = r.json()
        
        rows = []

        for line in data:
            name = line['name']
            statuses = line.get('lineStatuses', 'unknown')
            description = statuses[0].get('statusSeverityDescription', None)
            reason = statuses[0].get('reason', None)
            
            rows.append({
                "name": name, 
                "status": description, 
                "reason": reason,
            })
        
        return pd.DataFrame(rows)
    
    @render.table
    def status_table(): 
        df = network_status()
        return df
    
    @render.text
    def health_badge(): 
        df = network_status()
        good = (df['status'] == 'Good Service').sum()
        tot = len(df)
        return f"{good} / {tot} lines have good service"        

# APP -------------------------------
app = App(app_ui, server)