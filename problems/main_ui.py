# # from nicegui import ui

# # with ui.scene().classes('w-full h-64') as scene:
# #     scene.box1(1.8 , 1.8 , 5).material('black').move(x=-1.1, y=0, z= 2.5)
# #     scene.box1(1.8 , 1.8 , 5).material('black').move(x=1.1, y=0, z= 2.5)
# #     scene.box1(4 , 2 , 0.5).material('black').move(x=0, y=0, z=5.2)
# #     scene.box1(4 , 2 , 0.4).material('black').move(x=0, y=0, z=5.6)
# #     scene.box1(4 , 2 , 4).material('black').move(x=0, y=0, z=7.8)
# #     scene.box1(0.2 , 2 , 0.2).material('black').move(x=0, y=-0.2, z=5.2)
# #     scene.box1(1 , 1.4 , 3.5).material('black').move(x=-2.5,y=0,z=8.1)
# #     scene.box1(1 , 1.4 , 3.5).material('black').move(x=2.5,y=0,z=8.1)
# #     scene.box1(0.5 , 1.5 , 0.5).material('orange').move(x=-2.7,y=-0.1,z=6.4)
# #     scene.box1(0.5 , 1.5 , 0.5).material('orange').move(x=2.7,y=-0.1,z=6.4)
# #     scene.box1(4 , 2 , 3.5).material('black').move(x=0,y=0,z=11.5)
# #     scene.box1(3 , 2 , 2.5).material('orange').move(x=0,y=-0.5,z=11.5)
# #     scene.box1(0.8 , 2.5 , 1).material('white').move(x=0.8,y=-0.3,z=12)
# #     scene.box1(0.8 , 2.5 , 1).material('white').move(x=-0.8,y=-0.3,z=12)
# #     scene.box1(0.4 , 2.5 , 0.5).material('blue').move(x=-0.8,y=-0.4,z=12)
# #     scene.box1(0.4 , 2.5 , 0.5).material('red').move(x=0.8,y=-0.4,z=12)
# #     scene.box1(0.2 , 2.5 , 0.1).move(x=0.9,y=-0.4,z=12.2)
# #     scene.box1(0.2 , 2.5 , 0.1).move(x=-0.7,y=-0.4,z=12.2)
# #     scene.box1(3.5 , 2 , 1.5).material('black').move(x=0,y=-0.9,z=10.8)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=-0.6,z=7.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=0.6,z=8.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=-0.6,z=9.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=-0.6,z=7.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=0.6,z=8.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=-0.6,z=9.4)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=-0.9,z=3.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=0.9,z=4.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=-0.9,z=5.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=-0.9,z=3.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=0.9,z=4.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=-0.9,z=5.5)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=-0.8,y=-1,z=9)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-0.8,y=-1,z=8)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=0.8,y=-1,z=9)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=0.8,y=-1,z=8)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=-0.8,y=1,z=9)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-0.8,y=1,z=8)
# #     scene.box1(0.3 , 0.3 , 0.3).material('blue').move(x=0.8,y=1,z=9)
# #     scene.box1(0.3 , 0.3 , 0.3).material('red').move(x=0.8,y=1,z=8)
# #     scene.sphere(150).material('yellow').move(x=600,y=-600,z=600)
# #     scene.spot_light('yellow', intensity=1999, distance=10000, angle=10000000).move(600, -600, 600)

# # ui.run()
# # __--------------------------------------------------------------------------------------------------__
from nicegui import ui
from nicegui.events import KeyEventArguments

def handle_key(e: KeyEventArguments):
    if e.modifiers and e.action.keydown:
        if e.key.arrow_left:
            box1.move(x=box1.x + -1, y=box1.y, z=box1.z)
        elif e.key.arrow_right:
            box1.move(x=box1.x + 1, y=box1.y, z=box1.z)
        elif e.key.arrow_up:
            box1.move(x=box1.x, y=box1.y + 1, z=box1.z)
        elif e.key.arrow_down:
            box1.move(x=box1.x, y=box1.y + -1, z=box1.z)
        elif e.key == '0':
            box1.move(x=box1.x, y=box1.y, z=box1.z + 1)
            ui.timer(0.2, lambda: (box1.move(x=box1.x, y=box1.y, z=box1.z - 1)), once=True)
        if e.key == 'a':
            box2.move(x=box2.x + -1, y=box2.y, z=box2.z)
        elif e.key == 'd':
            box2.move(x=box2.x + 1, y=box2.y, z=box2.z)
        elif e.key == 'w':
            box2.move(x=box2.x, y=box2.y + 1, z=box2.z)
        elif e.key == 's':
            box2.move(x=box2.x, y=box2.y + -1, z=box2.z)
        elif e.key.shift:
            box2.move(x=box2.x, y=box2.y, z=box2.z + 1)
            ui.timer(0.2, lambda: (box2.move(x=box2.x, y=box2.y, z=box2.z - 1)), once=True)


keyboard = ui.keyboard(on_key=handle_key)

with ui.scene().classes('w-full h-64') as scene:

    scene.spot_light('green', intensity=10000, distance=100000000000, angle=1999999999999999).move(-40, 0, 2)
    scene.spot_light('green', intensity=10000, distance=100000000000, angle=1999999999999999).move(40, 0, 2)
    scene.spot_light('green', intensity=10000, distance=100000000000, angle=1999999999999999).move(0, 40, 2)
    scene.spot_light('green', intensity=10000, distance=100000000000, angle=1999999999999999).move(0, -40, 2)
    scene.spot_light('green', intensity=100000000, distance=100000000000, angle=1999999999999999).move(0, 0, 2)

    box1 = scene.box().material('blue').move(x=1.5, y=0.5, z=0.5)
    box2 = scene.box().material('red').move(x=-1.5, y=-0.5, z=0.5)

    scene.box(3 , 3 , 0.2).material('black').move(x=14.5, y=2, z= 0.8)

ui.run()
# # __-----------------------------------------------------------------------------------------------------------__