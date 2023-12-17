from nicegui import ui
from p003_solution import Year

class Options:
    def __init__(self):
        self.visible = False 
        self.first = True

options = Options()

def show_ui(visible):
    options.visible = visible
    if options.first:
        options.first = False
        root = create_ui()
    
def create_ui():
    with ui.column().bind_visibility_from(options, 'visible') as root:
        numberInput1 = ui.input('year 1')
        numberInput2 = ui.input('year 2')
        ui.button('Check Year', on_click=lambda: check_number())
        output = ui.label()

    def check_number():
        number1 = int(numberInput1.value)
        number2 = int(numberInput2.value)
        result = Year(number1 , number2)
        output.text = (result , ' dey')

    return root

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()
