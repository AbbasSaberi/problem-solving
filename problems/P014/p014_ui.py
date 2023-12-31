from nicegui import ui
from p014_solution import P014

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
        for x1 in range(0, numberInput1.value):
            numberInput2 = ui.input('Number 1(list)')
        numberInput3 = ui.input('Number 2')
        for x2 in range(0, numberInput3.value):
            numberInput4 = ui.input('Number 2(list)')
        with ui.row:
            ui.button('Check Number', on_click=lambda: check_number())
        output = ui.label()

    def check_number():
        number1 = int(numberInput2.value)
        number2 = int(numberInput4.value)
        result = P014(number1, number2)

        output.text = result

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()