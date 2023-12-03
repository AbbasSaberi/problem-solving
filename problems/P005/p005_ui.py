from nicegui import ui
from p005_solution import P005

class Options:
    def __init__(self):
        self.visible = False 
        self.first = True

options = Options()

def show_ui(visible):
    options.visible = visible
    if options.first:
        options.first = False
        create_ui()
    
def create_ui():
    with ui.column().bind_visibility_from(options, 'visible') as root:
        numberInput1 = ui.input('Number 1')
        numberInput2 = ui.input('operator')
        numberInput3 = ui.input('Number 2')
        with ui.row():
            ui.button('Check Number', on_click=lambda: calculate())

        output = ui.label()

    def calculate():
        number1 = int(numberInput1.value)
        number2 = (numberInput2.value)
        number3 = int(numberInput3.value)
        result = P005(number1 , number2 , number3)

        output.text = result

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()