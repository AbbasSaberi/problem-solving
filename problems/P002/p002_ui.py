from nicegui import ui
import P002

Number_Input1 = ui.input('Text input 1')
Number_Input2 = ui.input('Text input 2')

ui.button('OK' , on_click=lambda: Clik())

ui.run()

def Clik():
    number_1 = int(Number_Input1.value)
    number_2 = int(Number_Input2.value)

    result = P002.function(number_1 , number_2)

    p = ui.notify(str(result))
    ui.label(str(result))