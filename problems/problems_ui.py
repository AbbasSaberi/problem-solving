import os
import sys
for dir in [f for f in os.listdir('.') if os.path.isdir(os.path.join('.', f))]:
    sys.path.append(dir)

from nicegui import ui
from P001 import p001_ui
from P002 import p002_ui
from P003 import p003_ui
from P004 import p004_ui
from P005 import p005_ui
from P006 import p006_ui
from P007 import p007_ui
from P008 import p008_ui
from P009 import p009_ui
from P010 import p010_ui
from P011 import p011_ui
from P012 import p012_ui
from P013 import p013_ui

class Problem:
    def __init__(self):
        self.number = 1

def gen_dict(a, b):
    return dict(map(lambda x: (x, str(x)),range(a, b + 1)))

def show_problem(problem_number):
    problem.visible = problem_number > 0
    
    p001_ui.show_ui(problem_number == 1)
    p002_ui.show_ui(problem_number == 2)
    p003_ui.show_ui(problem_number == 3)
    p004_ui.show_ui(problem_number == 4)
    p005_ui.show_ui(problem_number == 5)
    p006_ui.show_ui(problem_number == 6)
    p007_ui.show_ui(problem_number == 7)
    p008_ui.show_ui(problem_number == 8)
    p009_ui.show_ui(problem_number == 9)
    p010_ui.show_ui(problem_number == 10)
    p011_ui.show_ui(problem_number == 11)
    p012_ui.show_ui(problem_number == 12)
    p013_ui.show_ui(problem_number == 13)

    
problem = Problem()

with ui.row():
    with ui.column():
        ui.label('Select a problem:')
        problems = gen_dict(1, 50)
        ui.select(problems, on_change=lambda e: show_problem(e.value)).bind_value(problem, 'number')
        ui.separator()


ui.run(port=80)