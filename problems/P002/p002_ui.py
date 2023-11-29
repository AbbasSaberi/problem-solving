from nicegui import ui
from P002.p002 import c , d , e , f

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
        numberInput2 = ui.input('Number 2')
        with ui.row():
            ui.button('+', on_click=lambda y: calculate(y))
            ui.button('-', on_click=lambda y: calculate(y))
            ui.button('/', on_click=lambda y: calculate(y))
            ui.button('*', on_click=lambda y: calculate(y))
        output = ui.label()

    def calculate(x):
        operation = x.sender.text
        number1 = int(numberInput1.value)
        number2 = int(numberInput2.value)

        if operation == '+':
            result = c(number1, number2)
        elif operation == '-':
            result = d(number1, number2)
        elif operation == '/':
            result = int(f(number1, number2))
        elif operation == '*':
            result = e(number1, number2)

        output.text = result

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()