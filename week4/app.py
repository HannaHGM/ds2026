from shiny import ui, render, App

#UI
app_ui = ui.page(
    ui.input_slider("slider", "Slider", 0, 100, 50), 
    ui.output_code("value")
    )

#SERVER
def server(input, output, session):
    @render.code
    def value():
        return f'{input.slider()}'

#APP
app = App(app_ui, server)