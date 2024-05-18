import turtle
SHAPE = input('Shape : ')

if SHAPE == 'Square':

    a = int(input('point : '))
    turtle.penup()
    turtle.right(90)
    turtle.fd(a / 2)
    turtle.right(90)
    turtle.fd(a / 2)
    turtle.pendown()

    for x in range(4):
        turtle.right(90)
        turtle.fd(a)

if SHAPE == 'Rectangle':

    a = input('point : ').split(' ')
    turtle.penup()
    turtle.right(90)
    turtle.fd(int(a[0]) / 2)
    turtle.right(90)
    turtle.fd(int(a[1]) / 2)
    turtle.pendown()

    for x in range(2):
        turtle.right(90)
        turtle.fd(int(a[0]))
        turtle.right(90)
        turtle.fd(int(a[1]))

if SHAPE == 'Triangle':

    a = int(input('point : '))
    turtle.penup()
    turtle.right(90)
    turtle.fd(a / 2)
    turtle.right(90)
    turtle.fd(a / 2)
    turtle.pendown()

    for x in range(3):
        turtle.right(180 - 60)
        turtle.fd(a)

if SHAPE == 'Circle':
    
    a = int(input('Radius : '))
    turtle.penup()
    turtle.right(90)
    turtle.fd(a)
    turtle.left(90)
    turtle.pendown()

    turtle.circle(a)

if SHAPE == 'Pentagon':

    a = int(input('point : '))
    turtle.penup()
    turtle.right(90)
    turtle.fd(a)
    turtle.right(90)
    turtle.fd(a / 2)
    turtle.pendown()

    for x in range(5):

        turtle.left(108 - 180)
        turtle.fd(a)

if SHAPE == 'Oval':

    a = input('Radius : ').split(' ')
    turtle.penup()
    turtle.left(180)
    turtle.fd(int(a[0]))
    turtle.right(45 - 180)
    turtle.pendown()
    for x in range(2):
        turtle.circle(int(a[0]),90)
        turtle.circle(int(a[1]),90)