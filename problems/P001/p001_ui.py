from nicegui import *
import P001

Number_Input = ui.input('Text input')

ui.button('OK', on_click=lambda: Clik())

ui.run()

def Clik():
    number = int(Number_Input.value)

    result = P001.even_odd(number)

    ui.notify(result)
    ui.label(result)