from nicegui import ui
from p016_solution import slohsen

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
        numberInput = ui.input('Number')
        ui.button('Check Number', on_click=lambda: check_number())
        output = ui.label()

    def check_number():
        number = int(numberInput.value)
        result = slohsen(number)
        for X in range(number , 1):
            for x in list(result):
                output.text = str(x) * X

    return root

if __name__ in {"__main__", "__mp_main__"}:
    show_ui(True)
    ui.run()