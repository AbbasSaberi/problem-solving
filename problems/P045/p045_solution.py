from graphics import *

def main():
    win = GraphWin("My graphics.py",600, 600)

    INPUT = input('The name of the figure : ')

    if INPUT == 'Square':

        point = int(input('Point : '))

        p1 = 300 - point
        p2 = 300 + point


        Shape = Rectangle(Point(p1,p1), Point(p2,p2))
        Shape.draw(win)
    
    if INPUT == 'Rectangle':

        point = input('Point : ').split(' ')

        p1 = int(point[0])
        p2 = int(point[1])

        Shape = Rectangle(Point(300 -p1,300 -p2), Point(300 + p1,300 + p2))
        Shape.draw(win)

    if INPUT == 'Circle':

        point = int(input('Radius : '))

        p = point * 2

        Shape = Circle(Point(300,300), p)
        Shape.draw(win)
    
    if INPUT == 'Triangle':

        point = int(input('point : '))

        p1 = 300 - point
        p2 = 300 + point
        p3 = 300 - point

        Shape = Polygon(Point(300,p1),Point(p2,p2),Point(p3,p2))
        Shape.draw(win)
    
    if INPUT == 'Oval':

        point = input('Point : ').split(' ')

        p1 = int(point[0])
        p2 = int(point[1])

        Shape = Oval(Point(300 -p1,300 -p2), Point(300 + p1,300 + p2))
        Shape.draw(win)

    win.getMouse()
    win.close()

main()