# #"به نام خدا"# #
# # from graphics import *

# # def main():
# #     win = GraphWin("My سفره هفتسین.py",600, 600)

# #     O = Oval(Point(200, 500 ), Point(400, 550 ))
# #     O.setFill('blue')
# #     O.setOutline('blue')
# #     O.draw(win)

# #     aO = Oval(Point(5, 400),  Point(205, 450 ))
# #     aO.setFill('blue')
# #     aO.setOutline('blue')
# #     aO.draw(win)

# #     bO = Oval(Point(400, 405 ), Point(595, 450 ))
# #     bO.setFill('blue')
# #     bO.setOutline('blue')
# #     bO.draw(win)

# #     cO = Oval(Point(400, 200 ), Point(595, 250 ))
# #     cO.setFill('blue')
# #     cO.setOutline('blue')
# #     cO.draw(win)

# #     dO = Oval(Point(200, 300 ), Point(400, 350 ))
# #     dO.setFill('blue')
# #     dO.setOutline('blue')
# #     dO.draw(win)

# #     eO = Oval(Point(5, 200),  Point(205, 250 ))
# #     eO.setFill('blue')
# #     eO.setOutline('blue')
# #     eO.draw(win)

# #     OO = Oval(Point(50, 240) , Point(30, 210) )
# #     OO.setFill('orange')
# #     OO.setOutline('orange')
# #     OO.draw(win)
# #     for X in range(1, 5):
# #         OO2 = OO.clone()
# #         OO2.move(1 + 30 * X, 0)
# #         OO2.draw(win)
# #     o = Oval(Point(230, 290 ), Point(375, 340 ))
# #     o.setFill('brown')
# #     o.setOutline('brown')
# #     o.draw(win)

# #     R = Rectangle(Point(225, 320 ), Point(375, 340 ))
# #     R.setFill('blue')
# #     R.setOutline('blue')
# #     R.draw(win) 

# #     p = Polygon(Point(500, 190 ), Point(580, 230 ), Point(420, 230 ), Point(500, 190 ))
# #     p.setFill('brown')
# #     p.setOutline('brown')
# #     p.draw(win)

# #     bc = Circle(Point(500, 410 ), 30)
# #     bc.setFill('white')
# #     bc.setOutline('white')
# #     bc.draw(win)

# #     ll = Line(Point(510, 430 ), Point(490, 350 ))
# #     ll.setFill('white')
# #     ll.setWidth(9)
# #     ll.draw(win)

# #     ac = Circle(Point(105, 410 ), 30)
# #     ac.setFill('gray')
# #     ac.setWidth(9)
# #     ac.setOutline('gold')
# #     ac.draw(win)

# #     t = Text(Point(105, 410 ),'250')
# #     t.setSize(15)
# #     t.setTextColor('gold')
# #     t.draw(win)

# #     L = Line(Point(295, 410 ), Point(305, 490 ))
# #     L.setWidth(4)
# #     L.draw(win)

# #     c = Circle(Point(300, 490 ), 50)
# #     c.setFill('red')
# #     c.setOutline('red')
# #     c.draw(win)

# #     r = Rectangle(Point(250, 90) , Point(350, 150 ))
# #     r.setFill('yellow')
# #     r.draw(win)

# #     l = Line(Point(260, 5),  Point(260, 90) )
# #     l.setFill('green')
# #     l.setWidth(2)
# #     l.draw(win)
# #     for x in range(1, 10):
# #         l2 = l.clone()
# #         l2.move(1 + 9 * x, 0)
# #         l2.draw(win)

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #______________________________________________________________________________________________
# #"به نام خدا"#
# # from graphics import *

# # def main():
# #     win = GraphWin("My graphics.py",600, 600)

# #     r = Rectangle(Point(420, 60) , Point(480, 240 ))
# #     r.setWidth(3)
# #     r.draw(win)

# #     R = Rectangle(Point(0, 310),  Point(600, 490 ))
# #     R.setFill("grey")
# #     R.draw(win)

# #     Cr = Circle(Point(450, 100 ), 25)
# #     Cy = Circle(Point(450, 150 ), 25)
# #     Cg = Circle(Point(450, 200 ), 25)
# #     Cr.setFill("black")
# #     Cy.setFill("black")
# #     Cg.setFill("black")
# #     Cr.draw(win)
# #     Cy.draw(win)
# #     Cg.draw(win)

# #     l = Line(Point(450, 320 ), Point(450, 480 ))
# #     l.setWidth(5)
# #     l.draw(win)

# #     L = Line(Point(70, 320) , Point(70, 480) )
# #     L.setFill("white")
# #     L.setWidth(5)
# #     L.setOutline("white")
# #     L.draw(win)

# #     c = Circle(Point(35, 350) ,30)
# #     c.setFill("red")
# #     c.draw(win)

# #     C = Circle(Point(35, 450) , 30)
# #     C.setFill("blue")
# #     C.draw(win)

# #     time.sleep(0.5)
# #     cr = Circle(Point(450, 100 ), 20)
# #     cr.setFill("red")
# #     cr.draw(win)
# #     time.sleep(1)
# #     cr.undraw()
# #     time.sleep(1)
# #     cy = Circle(Point(450, 150 ), 20)
# #     cy.setFill("yellow")
# #     cy.draw(win)
# #     time.sleep(1)
# #     cy.undraw()
# #     time.sleep(1)
# #     cg = Circle(Point(450, 200 ), 20)
# #     cg.setFill("green")
# #     cg.draw(win)

# #     time.sleep(1)
# #     cg.undraw()

# #     c.undraw()
# #     C.undraw()
# #     c1 = c.clone()
# #     C1 = C.clone()
# #     c1.move(1, 0)
# #     C1.move(1, 0)
# #     c1.draw(win)
# #     C1.draw(win)
# #     time.sleep(0.1)
# #     c2 = c1.clone()
# #     C2 = C1.clone()
# #     c2.move(1, 0)
# #     C2.move(1, 0)
# #     c2.draw(win)
# #     C2.draw(win)
# #     c1.undraw()
# #     C1.undraw()
# #     time.sleep(0.1)
# #     c3 = c2.clone()
# #     C3 = C2.clone()
# #     c3.move(2, 0)
# #     C3.move(1, 0)
# #     c3.draw(win)
# #     C3.draw(win)
# #     c2.undraw()
# #     C2.undraw()
# #     time.sleep(0.1)
# #     c4 = c3.clone()
# #     C4 = C3.clone()
# #     c4.move(2, 0)
# #     C4.move(2, 0)
# #     c4.draw(win)
# #     C4.draw(win)
# #     c3.undraw()
# #     C3.undraw()
# #     time.sleep(0.1)
# #     c5 = c4.clone()
# #     C5 = C4.clone()
# #     c5.move(2, 0)
# #     C5.move(2, 0)
# #     c5.draw(win)
# #     C5.draw(win)
# #     c4.undraw()
# #     C4.undraw()
# #     time.sleep(0.1)
# #     c6 = c5.clone()
# #     C6 = C5.clone()
# #     c6.move(2, 0)
# #     C6.move(2, 0)
# #     c6.draw(win)
# #     C6.draw(win)
# #     c5.undraw()
# #     C5.undraw()
# #     time.sleep(0.1)
# #     c7 = c6.clone()
# #     C7 = C6.clone()
# #     c7.move(2, 0)
# #     C7.move(2, 0)
# #     c7.draw(win)
# #     C7.draw(win)
# #     c6.undraw()
# #     C6.undraw()
# #     time.sleep(0.1)
# #     c8 = c7.clone()
# #     C8 = C7.clone()
# #     c8.move(3, 0)
# #     C8.move(2, 0)
# #     c8.draw(win)
# #     C8.draw(win)
# #     c7.undraw()
# #     C7.undraw()
# #     time.sleep(0.1)
# #     c9 = c8.clone()
# #     C9 = C8.clone()
# #     c9.move(3, 0)
# #     C9.move(2, 0)
# #     c9.draw(win)
# #     C9.draw(win)
# #     c8.undraw()
# #     C8.undraw()
# #     time.sleep(0.1)
# #     c10 = c9.clone()
# #     C10 = C9.clone()
# #     c10.move(3, 0)
# #     C10.move(3, 0)
# #     c10.draw(win)
# #     C10.draw(win)
# #     c9.undraw()
# #     C9.undraw()
# #     time.sleep(0.1)
# #     c11 = c10.clone()
# #     C11 = C10.clone()
# #     c11.move(4, 0)
# #     C11.move(3, 0)
# #     c11.draw(win)
# #     C11.draw(win)
# #     c10.undraw()
# #     C10.undraw()
# #     time.sleep(0.1)
# #     c12 = c11.clone()
# #     C12 = C11.clone()
# #     c12.move(4, 0)
# #     C12.move(3, 0)
# #     c12.draw(win)
# #     C12.draw(win)
# #     c11.undraw()
# #     C11.undraw()
# #     time.sleep(0.1)
# #     c13 = c12.clone()
# #     C13 = C12.clone()
# #     c13.move(4, 0)
# #     C13.move(5, 0)
# #     c13.draw(win)
# #     C13.draw(win)
# #     c12.undraw()
# #     C12.undraw()
# #     time.sleep(0.1)
# #     c14 = c13.clone()
# #     C14 = C13.clone()
# #     c14.move(4, 0)
# #     C14.move(5, 0)
# #     c14.draw(win)
# #     C14.draw(win)
# #     c13.undraw()
# #     C13.undraw()
# #     time.sleep(0.1)
# #     c15 = c14.clone()
# #     C15 = C14.clone()
# #     c15.move(5, 0)
# #     C15.move(5, 0)
# #     c15.draw(win)
# #     C15.draw(win)
# #     c14.undraw()
# #     C14.undraw()
# #     time.sleep(0.1)
# #     c16 = c15.clone()
# #     C16 = C15.clone()
# #     c16.move(5, 0)
# #     C16.move(6, 0)
# #     c16.draw(win)
# #     C16.draw(win)
# #     c15.undraw()
# #     C15.undraw()
# #     time.sleep(0.1)
# #     c17 = c16.clone()
# #     C17 = C16.clone()
# #     c17.move(5, 0)
# #     C17.move(6, 0)
# #     c17.draw(win)
# #     C17.draw(win)
# #     c16.undraw()
# #     C16.undraw()
# #     time.sleep(0.1)
# #     c18 = c17.clone()
# #     C18 = C17.clone()
# #     c18.move(5, 0)
# #     C18.move(6, 0)
# #     c18.draw(win)
# #     C18.draw(win)
# #     c17.undraw()
# #     C17.undraw()
# #     time.sleep(0.1)
# #     c19 = c18.clone()
# #     C19 = C18.clone()
# #     c19.move(5, 0)
# #     C19.move(6, 0)
# #     c19.draw(win)
# #     C19.draw(win)
# #     c18.undraw()
# #     C18.undraw()
# #     time.sleep(0.1)
# #     c20 = c19.clone()
# #     C20 = C19.clone()
# #     c20.move(5, 0)
# #     C20.move(6, 0)
# #     c20.draw(win)
# #     C20.draw(win)
# #     c19.undraw()
# #     C19.undraw()
# #     time.sleep(0.1)
# #     c21 = c20.clone()
# #     C21 = C20.clone()
# #     c21.move(5, 0)
# #     C21.move(6, 0)
# #     c21.draw(win)
# #     C21.draw(win)
# #     c20.undraw()
# #     C20.undraw()
# #     time.sleep(0.1)
# #     c22 = c21.clone()
# #     C22 = C21.clone()
# #     c22.move(5, 0)
# #     C22.move(6, 0)
# #     c22.draw(win)
# #     C22.draw(win)
# #     c21.undraw()
# #     C21.undraw()
# #     time.sleep(0.1)
# #     c23 = c22.clone()
# #     C23 = C22.clone()
# #     c23.move(5, 0)
# #     C23.move(6, 0)
# #     c23.draw(win)
# #     C23.draw(win)
# #     c22.undraw()
# #     C22.undraw()
# #     time.sleep(0.1)
# #     c24 = c23.clone()
# #     C24 = C23.clone()
# #     c24.move(5, 0)
# #     C24.move(7, 0)
# #     c24.draw(win)
# #     C24.draw(win)
# #     c23.undraw()
# #     C23.undraw()
# #     time.sleep(0.1)
# #     c25 = c24.clone()
# #     C25 = C24.clone()
# #     c25.move(6, 0)
# #     C25.move(7, 0)
# #     c25.draw(win)
# #     C25.draw(win)
# #     c24.undraw()
# #     C24.undraw()
# #     time.sleep(0.1)
# #     c26 = c25.clone()
# #     C26 = C25.clone()
# #     c26.move(6, 0)
# #     C26.move(7, 0)
# #     c26.draw(win)
# #     C26.draw(win)
# #     c25.undraw()
# #     C25.undraw()
# #     time.sleep(0.1)
# #     c27 = c26.clone()
# #     C27 = C26.clone()
# #     c27.move(6, 0)
# #     C27.move(7, 0)
# #     c27.draw(win)
# #     C27.draw(win)
# #     c26.undraw()
# #     C26.undraw()
# #     time.sleep(0.1)
# #     c28 = c27.clone()
# #     C28 = C27.clone()
# #     c28.move(6, 0)
# #     C28.move(8, 0)
# #     c28.draw(win)
# #     C28.draw(win)
# #     c27.undraw()
# #     C27.undraw()
# #     time.sleep(0.1)
# #     c29 = c28.clone()
# #     C29 = C28.clone()
# #     c29.move(7, 0)
# #     C29.move(8, 0)
# #     c29.draw(win)
# #     C29.draw(win)
# #     c28.undraw()
# #     C28.undraw()
# #     time.sleep(0.1)
# #     c30 = c29.clone()
# #     C30 = C29.clone()
# #     c30.move(7, 0)
# #     C30.move(8, 0)
# #     c30.draw(win)
# #     C30.draw(win)
# #     c29.undraw()
# #     C29.undraw()
# #     time.sleep(0.1)
# #     c31 = c30.clone()
# #     C31 = C30.clone()
# #     c31.move(7, 0)
# #     C31.move(8, 0)
# #     c31.draw(win)
# #     C31.draw(win)
# #     c30.undraw()
# #     C30.undraw()
# #     time.sleep(0.1)
# #     c32 = c31.clone()
# #     C32 = C31.clone()
# #     c32.move(7, 0)
# #     C32.move(8, 0)
# #     c32.draw(win)
# #     C32.draw(win)
# #     c31.undraw()
# #     C31.undraw()
# #     time.sleep(0.1)
# #     c33 = c32.clone()
# #     C33 = C32.clone()
# #     c33.move(7, 0)
# #     C33.move(8, 0)
# #     c33.draw(win)
# #     C33.draw(win)
# #     c32.undraw()
# #     C32.undraw()
# #     time.sleep(0.1)
# #     c34 = c33.clone()
# #     C34 = C33.clone()
# #     c34.move(7, 0)
# #     C34.move(8, 0)
# #     c34.draw(win)
# #     C34.draw(win)
# #     c33.undraw()
# #     C33.undraw()
# #     time.sleep(0.1)
# #     c35 = c34.clone()
# #     C35 = C34.clone()
# #     c35.move(7, 0)
# #     C35.move(9, 0)
# #     c35.draw(win)
# #     C35.draw(win)
# #     c34.undraw()
# #     C34.undraw()
# #     time.sleep(0.1)
# #     c36 = c35.clone()
# #     C36 = C35.clone()
# #     c36.move(8, 0)
# #     C36.move(9, 0)
# #     c36.draw(win)
# #     C36.draw(win)
# #     c35.undraw()
# #     C35.undraw()
# #     time.sleep(0.1)
# #     c37 = c36.clone()
# #     C37 = C36.clone()
# #     c37.move(8, 0)
# #     C37.move(10, 0)
# #     c37.draw(win)
# #     C37.draw(win)
# #     c36.undraw()
# #     C36.undraw()
# #     time.sleep(0.1)
# #     c38 = c37.clone()
# #     C38 = C37.clone()
# #     c38.move(8, 0)
# #     C38.move(10, 0)
# #     c38.draw(win)
# #     C38.draw(win)
# #     c37.undraw()
# #     C37.undraw()
# #     time.sleep(0.1)
# #     c39 = c38.clone()
# #     C39 = C38.clone()
# #     c39.move(8, 0)
# #     C39.move(11, 0)
# #     c39.draw(win)
# #     C39.draw(win)
# #     c38.undraw()
# #     C38.undraw()
# #     time.sleep(0.1)
# #     c40 = c39.clone()
# #     C40 = C39.clone()
# #     c40.move(8, 0)
# #     C40.move(11, 0)
# #     c40.draw(win)
# #     C40.draw(win)
# #     c39.undraw()
# #     C39.undraw()
# #     time.sleep(0.1)
# #     c41 = c40.clone()
# #     C41 = C40.clone()
# #     c41.move(8, 0)
# #     C41.move(11, 0)
# #     c41.draw(win)
# #     C41.draw(win)
# #     c40.undraw()
# #     C40.undraw()
# #     time.sleep(0.1)
# #     c42 = c41.clone()
# #     C42 = C41.clone()
# #     c42.move(8, 0)
# #     C42.move(11, 0)
# #     c42.draw(win)
# #     C42.draw(win)
# #     c41.undraw()
# #     C41.undraw()
# #     time.sleep(0.1)
# #     c43 = c42.clone()
# #     C43 = C42.clone()
# #     c43.move(9, 0)
# #     C43.move(11, 0)
# #     c43.draw(win)
# #     C43.draw(win)
# #     c42.undraw()
# #     C42.undraw()
# #     time.sleep(0.1)
# #     c44 = c43.clone()
# #     C44 = C43.clone()
# #     c44.move(9, 0)
# #     C44.move(11, 0)
# #     c44.draw(win)
# #     C44.draw(win)
# #     c43.undraw()
# #     C43.undraw()
# #     time.sleep(0.1)
# #     c45 = c44.clone()
# #     C45 = C44.clone()
# #     c45.move(9, 0)
# #     C45.move(11, 0)
# #     c45.draw(win)
# #     C45.draw(win)
# #     c44.undraw()
# #     C44.undraw()
# #     time.sleep(0.1)
# #     c46 = c45.clone()
# #     C46 = C45.clone()
# #     c46.move(9, 0)
# #     C46.move(11, 0)
# #     c46.draw(win)
# #     C46.draw(win)
# #     c45.undraw()
# #     C45.undraw()
# #     time.sleep(0.1)
# #     c47 = c46.clone()
# #     C47 = C46.clone()
# #     c47.move(9, 0)
# #     C47.move(11, 0)
# #     c47.draw(win)
# #     C47.draw(win)
# #     c46.undraw()
# #     C46.undraw()
# #     time.sleep(0.1)
# #     c48 = c47.clone()
# #     C48 = C47.clone()
# #     c48.move(9, 0)
# #     C48.move(11, 0)
# #     c48.draw(win)
# #     C48.draw(win)
# #     c47.undraw()
# #     C47.undraw()
# #     time.sleep(0.1)
# #     c49 = c48.clone()
# #     C49 = C48.clone()
# #     c49.move(11, 0)
# #     C49.move(11, 0)
# #     c49.draw(win)
# #     C49.draw(win)
# #     c48.undraw()
# #     C48.undraw()
# #     time.sleep(0.1)
# #     c50 = c49.clone()
# #     C50 = C49.clone()
# #     c50.move(14, 0)
# #     C50.move(11, 0)
# #     c50.draw(win)
# #     C50.draw(win)
# #     c49.undraw()
# #     C49.undraw()
# #     time.sleep(0.1)
# #     c51 = c50.clone()
# #     C51 = C50.clone()
# #     c51.move(18, 0)
# #     C51.move(11, 0)
# #     c51.draw(win)
# #     C51.draw(win)
# #     c50.undraw()
# #     C50.undraw()
# #     time.sleep(0.1)
# #     c52 = c51.clone()
# #     C52 = C51.clone()
# #     c52.move(29, 0)
# #     C52.move(11, 0)
# #     c52.draw(win)
# #     C52.draw(win)
# #     c51.undraw()
# #     C51.undraw()
# #     time.sleep(0.1)
# #     c53 = c52.clone()
# #     C53 = C52.clone()
# #     c53.move(38, 0)
# #     C53.move(11, 0)
# #     c53.draw(win)
# #     C53.draw(win)
# #     c52.undraw()
# #     C52.undraw()
# #     time.sleep(0.1)
# #     c54 = c53.clone()
# #     C54 = C53.clone()
# #     c54.move(43, 0)
# #     C54.move(11, 0)
# #     c54.draw(win)
# #     C54.draw(win)
# #     c53.undraw()
# #     C53.undraw()
# #     time.sleep(0.1)
# #     c55 = c54.clone()
# #     C55 = C54.clone()
# #     c55.move(30, 0)
# #     C55.move(11, 0)
# #     c55.draw(win)
# #     C55.draw(win)
# #     c54.undraw()
# #     C54.undraw()
# #     time.sleep(0.1)
# #     c56 = c55.clone()
# #     C56 = C55.clone()
# #     c56.move(43, 0)
# #     C56.move(13, 0)
# #     c56.draw(win)
# #     C56.draw(win)
# #     c55.undraw()
# #     C55.undraw()
# #     time.sleep(0.1)
# #     c57 = c56.clone()
# #     C57 = C56.clone()
# #     c57.move(30, 0)
# #     C57.move(14, 0)
# #     c57.draw(win)
# #     C57.draw(win)
# #     c56.undraw()
# #     C56.undraw()
# #     time.sleep(0.1)
# #     c58 = c57.clone()
# #     C58 = C57.clone()
# #     c58.move(18, 0)
# #     C58.move(9, 0)
# #     c58.draw(win)
# #     C58.draw(win)
# #     c57.undraw()
# #     C57.undraw()
# #     time.sleep(0.1)
# #     c59 = c58.clone()
# #     C59 = C58.clone()
# #     c59.move(12, 0)
# #     C59.move(6, 0)
# #     c59.draw(win)
# #     C59.draw(win)
# #     c58.undraw()
# #     C58.undraw()
# #     time.sleep(0.1)
# #     c60 = c59.clone()
# #     C60 = C59.clone()
# #     c60.move(7, 0)
# #     C60.move(4, 0)
# #     c60.draw(win)
# #     C60.draw(win)
# #     c59.undraw()
# #     C59.undraw()
# #     time.sleep(0.1)
# #     c61 = c60.clone()
# #     C61 = C60.clone()
# #     c61.move(7, 0)
# #     C61.move(2, 0)
# #     c61.draw(win)
# #     C61.draw(win)
# #     c60.undraw()
# #     C60.undraw()
# #     time.sleep(0.1)
# #     c62 = c61.clone()
# #     C62 = C61.clone()
# #     c62.move(3, 0)
# #     C62.move(2, 0)
# #     c62.draw(win)
# #     C62.draw(win)
# #     c61.undraw()
# #     C61.undraw()
# #     time.sleep(0.1)
# #     c63 = c62.clone()
# #     C63 = C62.clone()
# #     c63.move(3, 0)
# #     C63.move(2, 0)
# #     c63.draw(win)
# #     C63.draw(win)
# #     c62.undraw()
# #     C62.undraw()
# #     time.sleep(0.1)
# #     c64 = c63.clone()
# #     C64 = C63.clone()
# #     c64.move(2, 0)
# #     C64.move(1, 0)
# #     c64.draw(win)
# #     C64.draw(win)
# #     c63.undraw()
# #     C63.undraw()
# #     time.sleep(0.1)
# #     c65 = c64.clone()
# #     C65 = C64.clone()
# #     c65.move(1, 0)
# #     C65.move(1, 0)
# #     c65.draw(win)
# #     C65.draw(win)
# #     c64.undraw()
# #     C64.undraw()

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #______________________________________________________________________________________________
# #"به نام خدا"# #
# # from graphics import *

# # def main():
# #     win = GraphWin("My graphic.py",600, 600)

# #     r = Rectangle(Point(70, 50),  Point(520, 550 ))
# #     r.setFill("green")
# #     r.setWidth(3)
# #     r.setOutline("white")
# #     r.draw(win)

# #     c = Circle(Point(300, 300 ), 50)
# #     c.setWidth(3)
# #     c.setOutline("white")
# #     c.draw(win)
   
# #     C = Circle(Point(300, 300 ), 5)
# #     C.setFill("white")
# #     C.setOutline("white")
# #     C.draw(win)

# #     l = Line(Point(70, 300) , Point(520, 300 ))
# #     l.setFill("white")
# #     l.setWidth(3)
# #     l.setOutline("white")
# #     l.draw(win)

# #     CB = Circle(Point(300, 105 ), 45)
# #     CB.setWidth(3)
# #     CB.setOutline("white")
# #     CB.draw(win)

# #     CR = Circle(Point(300, 495 ), 45)
# #     CR.setWidth(3)
# #     CR.setOutline("white")
# #     CR.draw(win)

# #     FCB = Rectangle(Point(185, 50) , Point(405, 120 ))
# #     FCB.setFill("green")
# #     FCB.setWidth(3)
# #     FCB.setOutline("white")
# #     FCB.draw(win)

# #     FCR = Rectangle(Point(185, 550 ), Point(405, 480 ))
# #     FCR.setFill("green")
# #     FCR.setWidth(3)
# #     FCR.setOutline("white")
# #     FCR.draw(win)

# #     cB = Circle(Point(300, 80) , 5)
# #     cB.setFill("white")
# #     cB.setOutline("white")
# #     cB.draw(win)

# #     cR = Circle(Point(300, 520 ), 5)
# #     cR.setFill("white")
# #     cR.setOutline("white")
# #     cR.draw(win)

# #     ckB = Circle(Point(70, 50),  20)
# #     ckB.setWidth(3)
# #     ckB.setOutline("white")
# #     ckB.draw(win)
# #     ckB = ckB.clone()
# #     ckB.move(450, 0)
# #     ckB.draw(win)

# #     ckR = Circle(Point(70, 550) , 20)
# #     ckR.setWidth(3)
# #     ckR.setOutline("white")
# #     ckR.draw(win)
# #     ckR = ckR.clone()
# #     ckR.move(450, 0)
# #     ckR.draw(win)

# #     lm = Circle(Point(300, 200 ), 22)
# #     lm.setFill("red")
# #     lm.setWidth(12)
# #     lm.setOutline("blue")
# #     lm.draw(win)
# #     tlm = Text(Point(300, 192 ), "messi")
# #     Tlm = Text(Point(300, 210 ), "10 C")
# #     tlm.setSize(12)
# #     Tlm.setSize(18)
# #     tlm.setTextColor("white")
# #     Tlm.setTextColor("gold")
# #     tlm.draw(win)
# #     Tlm.draw(win)

# #     ag = Circle(Point(150, 110 ), 22)
# #     ag.setFill("red")
# #     ag.setWidth(12)
# #     ag.setOutline("blue")
# #     ag.draw(win)
# #     tag = Text(Point(150, 105 ), "griezmann")
# #     Tag = Text(Point(150, 125 ), "7")
# #     tag.setSize(10)
# #     Tag.setSize(18)
# #     tag.setTextColor("white")
# #     Tag.setTextColor("white")
# #     tag.draw(win)
# #     Tag.draw(win)

# #     n = Circle(Point(445, 110 ), 22)
# #     n.setFill("red")
# #     n.setWidth(12)
# #     n.setOutline("blue")
# #     n.draw(win)
# #     tn = Text(Point(445, 100 ), "N.JR")
# #     Tn = Text(Point(445, 120 ), "11")
# #     tn.setSize(15)
# #     Tn.setSize(15)
# #     tn.setTextColor("white")
# #     Tn.setTextColor("white")
# #     tn.draw(win)
# #     Tn.draw(win)

# #     cr = Circle(Point(300, 400 ), 28)
# #     cr.setFill("white")
# #     cr.setOutline("white")
# #     cr.draw(win)
# #     tcr = Text(Point(300, 392 ), "ronaldo")
# #     Tcr = Text(Point(300, 410 ), "7 C")
# #     tcr.setSize(12)
# #     Tcr.setSize(18)
# #     Tcr.setTextColor("gold")
# #     tcr.draw(win)
# #     Tcr.draw(win)

# #     gb = Circle(Point(445, 510 ), 28)
# #     gb.setFill("white")
# #     gb.setOutline("white")
# #     gb.draw(win)
# #     tgb = Text(Point(445, 500 ), "bale")
# #     Tgb = Text(Point(445, 525 ), "9")
# #     tgb.setSize(18)
# #     Tgb.setSize(18)
# #     tgb.draw(win)
# #     Tgb.draw(win)

# #     v = Circle(Point(150, 510 ), 28)
# #     v.setFill("white")
# #     v.setOutline("white")
# #     v.draw(win)
# #     tv = Text(Point(150, 504 ), "V.JR")
# #     Tv = Text(Point(150, 525 ), "11")
# #     tv.setSize(16)
# #     Tv.setSize(18)
# #     tv.draw(win)
# #     Tv.draw(win)

# #     d = Polygon(Point(50, 30),  Point(50, 570) , Point(540, 570 ), Point(540, 30) , Point(50, 30)) 
# #     d.setWidth(35)
# #     d.setOutline("brown")
# #     d.draw(win)

# #     d1 = Polygon(Point(45, 25),  Point(45, 575) , Point(545, 575 ), Point(545, 25) , Point(45, 25)) 
# #     d2 = Polygon(Point(60, 40),  Point(60, 560) , Point(530, 560 ), Point(530, 40) , Point(60, 40)) 
# #     d1.setWidth(3)
# #     d2.setWidth(3)
# #     d1.setOutline("white")
# #     d2.setOutline("white")
# #     d1.draw(win)
# #     d2.draw(win)

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #_______________________________________________________________________________________________________________
# #"به نام خدا"# #
# # from graphics import *

# # def main():
# #     win = GraphWin("My graphic.py",600, 600)

# #     c = Circle(Point(150, 80) , 60)
# #     c.draw(win)

# #     p = Polygon(Point(70, 150) , Point(90, 170) , Point(70, 360) , Point(50, 340) , Point(70, 150) )
# #     P = Polygon(Point(230, 150 ), Point(210, 170 ), Point(230, 360 ), Point(250, 340 ), Point(230, 150 ))
# #     p.draw(win)
# #     P.draw(win)

# #     rp = Rectangle(Point(95, 360) , Point(145, 500 ))
# #     RP = Rectangle(Point(205, 360 ), Point(155, 500 ))
# #     rp.draw(win)
# #     RP.draw(win)

# #     r = Rectangle(Point(90, 140) , Point(210, 360 ))
# #     r.draw(win)



# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# # __------------------------------------------------------------------------------------------------------__
# # from graphics import *
# # def main():
# #     win = GraphWin("My Rectangle 3D.py",600, 600)

# #     pl = Polygon(Point(200, 200 ), Point(300, 250 ), Point(300, 400 ), Point(200, 350 ), Point(200, 200 ))
# #     P = Polygon(Point(200, 200 ), Point(300, 150 ), Point(400, 200 ), Point(300, 250 ), Point(200, 200 ))
# #     pr = Polygon(Point(400, 200 ), Point(300, 250 ), Point(300, 400 ), Point(400, 350 ), Point(400, 200 ))
# #     pl.setFill('red')
# #     pl.draw(win)
# #     P.setFill('grey')
# #     P.draw(win)
# #     pr.setFill('blue')
# #     pr.draw(win)

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# # __------------------------------------------------------------------------------------------------------__
# # from graphics import *
# # def main():
# #     win = GraphWin("My Triangle 3D.py", 600, 600)

# #     pr = Polygon(Point(300, 150 ), Point(360, 400 ), Point(120, 380 ), Point(300, 150 ))
# #     pl = Polygon(Point(300, 150 ), Point(400, 360 ), Point(360, 400 ), Point(300, 150 ))
# #     pr.setFill("yellow")
# #     pl.setFill("blue")
# #     pr.draw(win)
# #     pl.draw(win)

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# #__-----------------------------------------------------------------------------------------------------__
# # from graphics import *
# # def main():
# #     win = GraphWin("My Pentagon 3D.py", 600, 600)

# #     pr = Polygon(Point(260, 200 ), Point(370, 290 ), Point(330, 430 ), Point(200, 430 ), Point(150, 290 ), Point(260, 200 ))
# #     pr.setFill("orange")
# #     pr.draw(win)
# #     pl = pr.clone()
# #     pl.move(25, 10)
# #     pl.draw(win)

# #     pu = Polygon(Point(260, 200 ), Point(285, 210 ), Point(269, 220 ), Point(260, 200 ))
# #     pdl= Polygon(Point(200, 430 ), Point(225, 440 ), Point(220, 430 ), Point(200, 430 ))
# #     pu.setFill("orange")
# #     pdl.setFill("orange")
# #     pu.setOutline("orange")
# #     pdl.setOutline("orange")
# #     pu.draw(win)
# #     pdl.draw(win)

# #     l1 = Line(Point(260, 200 ), Point(285, 210 ))
# #     l1.draw(win)
# #     l2 = Line(Point(150, 290 ), Point(175, 300 ))
# #     l2.draw(win)
# #     l3 = Line(Point(200, 430 ), Point(225, 440 ))
# #     l3.draw(win)

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# #__------------------------------------------------------------------------------------------------------------------__
# # from graphics import *
# # def main():
# #     win = GraphWin("My graphics.py", 600, 600)

# #     rr = Rectangle(Point(50, 200) , Point(150, 400 ))
# #     rb = Rectangle(Point(550, 200 ), Point(450, 400 ))
# #     rr.setFill("red")
# #     rb.setFill("blue")
# #     rr.draw(win)
# #     rb.draw(win)

# #     while True:

# #         win.getMouse()

# #         c = Circle(Point(200, 370 ), 30)
# #         c.setFill("black")
# #         c.draw(win)

# #         for x in range(1, 21):
# #             time.sleep(0.02)
# #             RR = rr.clone()
# #             RR.move(1 * x, 0)
# #             RR.draw(win)
# #         for circle in range(1, 21):
# #             C = c.clone()
# #             C.move(1 + circle * 10, 0)
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(0.02)
# #             C.undraw()
# #         c1 = C.clone()
# #         c1.draw(win)
# #         for X in range(1, 21):
# #             time.sleep(0.005)
# #             RR = RR.clone()
# #             RR.move(-1, 0)
# #             RR.draw(win)
# #         for x in range(1, 21):
# #             time.sleep(0.02)
# #             RB = rb.clone()
# #             RB.move(-1 * x, 0)
# #             RB.draw(win)
# #         for circle in range(1, 21):
# #             C1 = c1.clone()
# #             C1.move(-1 - circle * 10, 0)
# #             C1.draw(win)
# #             c1.undraw()
# #             time.sleep(0.02)
# #             C1.undraw()
# #         c2 = C1.clone()
# #         c2.draw(win)
# #         for X in range(1, 21):
# #             time.sleep(0.02)
# #             RB = RB.clone()
# #             RB.move(1, 0)
# #             RB.draw(win)
# #         for x in range(1, 21):
# #             time.sleep(0.02)
# #             RR = RR.clone()
# #             RR.move(1, 0)
# #             RR.draw(win)
# #         for circle in range(1, 21):
# #             C2 = c2.clone()
# #             C2.move(1 + circle * 10, 0)
# #             C2.draw(win)
# #             c2.undraw()
# #             time.sleep(0.02)
# #             C2.undraw()
# #         c3 = C2.clone()
# #         c3.draw(win)
# #         for X in range(1, 21):
# #             time.sleep(0.02)
# #             RR = RR.clone()
# #             RR.move(-1, 0)
# #             RR.draw(win)
# #         for x in range(1, 21):
# #             time.sleep(0.02)
# #             RB = RB.clone()
# #             RB.move(-1, 0)
# #             RB.draw(win)
# #         for circle in range(1, 11):
# #             C3 = c3.clone()
# #             C3.move(1 - circle * 10, 0)
# #             C3.draw(win)
# #             c3.undraw()
# #             time.sleep(0.02)
# #             C3.undraw()
# #         c4 = C3.clone()
# #         c4.draw(win)
# #         for X in range(1, 21):
# #             time.sleep(0.02)
# #             RB = RB.clone()
# #             RB.move(1, 0)
# #             RB.draw(win)
# #         c4.undraw()

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# #__------------------------------------------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My graphics.py", 600, 600)

# #     while True:

# #         c = Circle(Point(300, 300 ) , 5)
# #         c.setFill('black')
# #         c.draw(win)
# #         INPUT = input('Wor Sor Dor A : ')
# #         if INPUT == 'W':
# #             c.move(0, -50)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
# #         if INPUT == 'S':
# #             c.move(0, 50)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
# #         if INPUT == 'D':
# #             c.move(50, 0)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
# #         if INPUT == 'A':
# #             c.move(-50, 0)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
# #         if INPUT == 'WD':
# #             c.move(50, -50)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
# #         if INPUT == 'DW':
# #             c.move(50, -50)
# #             C = c.clone()
# #             C.draw(win)
# #             c.undraw()
# #             time.sleep(1)
# #             C.undraw()
        
# #         C.undraw()

# #     win.getMouse()
# #     win.close()

# # main()
# #
# # __--------------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My graphics.py", 600, 600)

# #     l = Line(Point(280, 200 ), Point(260, 300 ))
# #     l.setFill("brown")
# #     l.setWidth(6)
# #     l.draw(win)

# #     c = Circle(Point(200, 300 ), 7)
# #     c.setFill("purple")
# #     c.draw(win)
# #     for y in range(1, 8):
# #         c1 = c.clone()
# #         c1.move(15 * y, 0)
# #         c1.setFill("purple")
# #         c1.draw(win)
# #     for y in range(1, 8):
# #         c2 = c.clone()
# #         c2.move(15 * y - 5, 15)
# #         c2.setFill("purple")
# #         c2.draw(win)
# #     for y in range(1, 7):
# #         c3 = c.clone()
# #         c3.move(15 * y + 1, 30)
# #         c3.setFill("purple")
# #         c3.draw(win)
# #     for y in range(1, 6):
# #         c4 = c.clone()
# #         c4.move(15 * y + 8, 45)
# #         c4.setFill("purple")
# #         c4.draw(win)
# #     for y in range(1, 5):
# #         c5 = c.clone()
# #         c5.move(15 * y + 15, 60)
# #         c5.setFill("purple")
# #         c5.draw(win)
# #     for y in range(1, 4):
# #         c6 = c.clone()
# #         c6.move(15 * y + 23, 75)
# #         c6.setFill("purple")
# #         c6.draw(win)
# #     for y in range(1, 3):
# #         c7 = c.clone()
# #         c7.move(15 * y + 31, 90)
# #         c7.setFill("purple")
# #         c7.draw(win)
# #     for y in range(1, 2):
# #         c8 = c.clone()
# #         c8.move(15 * y + 39, 105)
# #         c8.setFill("purple")
# #         c8.draw(win)
# #     l = Line(Point(350, 120 ), Point(320, 400 ))

# #     win.getMouse()
# #     win.close()

# # main()
# #
# #
# #__-------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My pistol.py" , 1260, 600)

# #     t1 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t1.setFill("gold")
# #     t1.draw(win)
# #     t2 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t2.setFill("gold")
# #     t2.draw(win)
# #     t3 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t3.setFill("gold")
# #     t3.draw(win)
# #     t4 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t4.setFill("gold")
# #     t4.draw(win)
# #     t5 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t5.setFill("gold")
# #     t5.draw(win)
# #     t6 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t6.setFill("gold")
# #     t6.draw(win)
# #     t7 = Rectangle(Point(995, 255 ), Point(1005, 26 0))
# #     t7.setFill("gold")
# #     t7.draw(win)

# #     R = Polygon(Point(1084, 27 0), Point(1098, 27 0), Point(1108, 31 8), Point(1092, 31 8))
# #     R.setFill("black")
# #     R.draw(win)

# #     p = Polygon(Point(990, 250 ), Point(1000, 25 0), Point(1000, 24 2), Point(1002, 24 2),Point(1002, 25 0), Point(1100, 25 0), Point(1100, 24 2),Point(1105, 24 2), Point(1105, 25 0), Point(1110, 26 0), Point(1100, 26 5), Point(1110, 32 0), Point(1090, 32 0), Point(1080, 26 5), Point(990, 265 ))
# #     p.setFill("black")
# #     p.draw(win)

# #     r = Polygon(Point(1084, 27 0), Point(1098, 27 0), Point(1108, 31 8), Point(1092, 31 8))
# #     r.setFill("brown")
# #     r.setOutline("brown")
# #     r.draw(win)

# #     P = Polygon(Point(990, 250 ), Point(1080, 25 0), Point(1080, 26 0), Point(990, 260 ), Point(990, 250 ))
# #     P.setFill("gray")
# #     P.setOutline("gray")
# #     P.draw(win)

# #     while True:

# #         time.sleep(0.02)

# #         T1 = t1.clone()
# #         T2 = t2.clone()
# #         T3 = t3.clone()
# #         T4 = t4.clone()
# #         T5 = t5.clone()
# #         T6 = t6.clone()
# #         T7 = t7.clone()

# #         for x1 in range(1, 124):

# #             time.sleep(0.005)
# #             T1.move(-4, 0)
# #             T1.draw(win)
# #             t1.undraw()
# #             time.sleep(0.005)
# #             T1.undraw()

# #         for x2 in range(1, 124):

# #             time.sleep(0.005)
# #             T2.move(-4, 0)
# #             T2.draw(win)
# #             t2.undraw()
# #             time.sleep(0.005)
# #             T2.undraw()

# #         for x3 in range(1, 124):

# #             time.sleep(0.005)
# #             T3.move(-4, 0)
# #             T3.draw(win)
# #             t3.undraw()
# #             time.sleep(0.005)
# #             T3.undraw()

# #         for x4 in range(1, 124):

# #             time.sleep(0.005)
# #             T4.move(-4, 0)
# #             T4.draw(win)
# #             t4.undraw()
# #             time.sleep(0.005)
# #             T4.undraw()


# #         for x5 in range(1, 124):

# #             time.sleep(0.005)
# #             T5.move(-4, 0)
# #             T5.draw(win)
# #             t5.undraw()
# #             time.sleep(0.005)
# #             T5.undraw()

# #         for x6 in range(1, 124):

# #             time.sleep(0.005)
# #             T6.move(-4, 0)
# #             T6.draw(win)
# #             t6.undraw()
# #             time.sleep(0.005)
# #             T6.undraw()

# #         for x7 in range(1, 124):
        
# #             time.sleep(0.005)
# #             T7.move(-4, 0)
# #             T7.draw(win)
# #             t7.undraw()
# #             time.sleep(0.005)
# #             T7.undraw()



# #         r = R.clone()
# #         time.sleep(0.005)

# #         for r_down in range(1, 91):

# #             r.move(1, 4)
# #             r.draw(win)
# #             R.undraw()
# #             time.sleep(0.02)
# #             r.undraw()
        
# #         for r_up in range(1, 84):

# #             r.move(-1, -4)
# #             r.draw(win)
# #             time.sleep(0.02)
# #             r.undraw()

# #         win.getMouse()
# #     win.close()

# # main()
# #
# #__---------------------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My clock.py" , 600, 600)

# #     C = Circle(Point(300, 300 ), 150)
# #     C.setWidth(50)
# #     C.setOutline("blue")
# #     C.draw(win)

# #     l = Line(Point(200, 60) , Point(230, 150 ))
# #     L = Line(Point(400, 60) , Point(370, 150 ))
# #     l.setFill("black")
# #     L.setFill("black")
# #     l.setWidth(4)
# #     L.setWidth(4)
# #     l.setOutline("black")
# #     L.setOutline("black")
# #     l.draw(win)
# #     L.draw(win)

# #     cl = Circle(Point(200, 60) , 10)
# #     cl.setFill("black")
# #     cl.draw(win)

# #     CL = Circle(Point(400, 60) , 10)
# #     CL.setFill("black")
# #     CL.draw(win)

# #     c = Circle(Point(300, 300 ), 100)
# #     c.setWidth(10)
# #     c.setOutline("red")

# #     A = 0
# #     B = 0
# #     while True:

# #         t = Text(Point(300, 300 ),f"{A}:{B}")
# #         t.setSize(36)
# #         t.draw(win)
# #         time.sleep(1)
# #         t.undraw()
# #         B += 1

# #         A_str = str(A)
# #         B_str = str(B)
# #         A_B_str = str(f'{A}:{B}')
# #         if f'{}' == f'{}:{}':
# #             t = Text(Point(300, 300 ),f"{A}:{B}")
# #             t.setSize(36)
# #             t.draw(win)
# #             for X in range(3):
# #                 for x in range(3):
# #                     time.sleep(0.1)
# #                     c.draw(win)
# #                     time.sleep(0.1)
# #                     c.undraw()
# #                 time.sleep(0.5)
# #             if win.getMouse():
# #                 t.undraw()
# #         if B == 60:
# #             A += 1
# #             B = 0

# # main()
# #
# #__----------------------------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My Hello_سلام.py", 200, 200)

# #     r = Rectangle(Point(10, 10),  Point(190, 190 ))
# #     r.setFill('blue')
# #     r.setOutline('blue')
# #     r.draw(win)

# #     t = Text(Point(100, 100 ),"""Hello
# # سلام""")
# #     t.setFill('gold')
# #     t.setSize(36)
# #     t.setTextColor('gold')
# #     t.draw(win)

# #     while win.getMouse():
# #         print(f'Hello')
    
# # main()

# #__----------------------------------------------------------------------------------------------------__
# # from graphics import *

# # def main():
# #     win = GraphWin("My baze(graphics).py", 1280, 720)
# #     win.setBackground('orange')

# #     P1 = Circle(Point(50, 180) , 10)
# #     P1.setFill('blue')

# #     p = Polygon(Point(50, 180), Point(290, 180), Point(290, 260), Point(900, 260), Point(900, 200), Point(1020, 200) ,Point(1020, 360), Point(160, 360),Point(160, 430), Point(1200, 430), Point(1200, 600), Point(210, 600), Point(210, 690),Point(210,600),Point(1200,600),Point(1200,430),Point(160,430),Point(160,360),Point(1020,360),Point(1020,200),Point(900,200),Point(900,260),Point(290,260),Point(290,180),Point(50,180))
# #     p.setWidth(30)
# #     p.setOutline('grey')

# #     P = Line(Point(180, 690), Point(240, 690))
# #     P.setWidth(4)

# #     l = Line(Point(200, 520), Point(1160, 520))
# #     l.setFill('red')
# #     l.setWidth(38)

# #     victori = Rectangle(Point(640, 360 ), Point(640, 360 ))
# #     victori.setFill('green')
# #     victori.setWidth(600)
# #     victori.setOutline('green')

# #     VICTORI1 = Text(Point(640, 330 ), "P1")
# #     VICTORI1.setFill('blue')
# #     VICTORI1.setSize(36)
# #     VICTORI2 = Text(Point(640, 380 ), 'victori')
# #     VICTORI2.setSize(30)

# #     R = Rectangle(Point(600, 580 ), Point(680, 580 ))
# #     R.setFill('black')
# #     R.setWidth(100)

# #     v = Text(Point(640, 580 ), 'NEXT')
# #     v.setFill('purple')
# #     v.setSize(36)



# #     T_IF = Text(Point(640, 360 ), ''':gear:
# # Automatic(a) or Manual(m)''')
# #     T_IF.setSize(36)
# #     T_IF.draw(win)

# #     IF = win.getKey()

# #     T_IF.undraw()

# #     p.draw(win)
# #     P.draw(win)
# #     l.draw(win)
# #     P1.draw(win)

# #     if IF == 'a':

# #         while True:

# #             A = 2 
# #             T = 0
# #             t = 0
# #             while win.getKey() == 'w':
# #                 P1.move(0, -A)
# #                 A += 2
# #                 if A == 20 + t:
# #                     if T != 8:
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1
# #             A = 2
# #             T = 0
# #             t = 0
# #             while win.getKey() == 'd':
# #                 P1.move(A, 0)
# #                 A += 2
# #                 if A == 20 + t:
# #                     if T != 8:
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1

# #             A = 2
# #             T = 0
# #             t = 0
# #             while win.getKey() == 'a':
# #                 P1.move(-A, 0)
# #                 A += 2
# #                 if A == 20 + t:
# #                     if T != 8:
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1

# #             A = 2
# #             T = 0
# #             t = 0
# #             while win.getKey() == 's':
# #                 P1.move(0, A)
# #                 A += 2
# #                 if A == 20 + t:
# #                     if T != 8:
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1

# #             V = win.getKey()
# #             if V == 'p':
# #                 p.undraw()
# #                 P1.undraw()
# #                 victori.draw(win)
# #                 VICTORI1.draw(win)
# #                 VICTORI2.draw(win)
# #                 R.draw(win)
# #                 v.draw(win)
# #                 P.undraw()
# #                 l.undraw()
# #                 if win.getMouse():
# #                     win.close()
    
# #     if IF == 'm':

# #         T = 1
# #         t = 0
        
# #         while True:

# #             A = 1
# #             while win.getKey() == 'w':
# #                 P1.move(0, -A)
# #                 A += 1
# #                 g = win.getKey()
# #                 if T != 8:
# #                     if g == '+':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1
# #                 if T != 1:
# #                     if g == '-':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= T
# #                         T -= 1

# #             A = 1
# #             while win.getKey() == 'd':
# #                 P1.move(A, 0)
# #                 A += 1
# #                 g = win.getKey()
# #                 if T != 8:
# #                     if g == '+':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1
# #                 if T != 8:
# #                     if g == '-':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= T
# #                         T -= 1

# #             A = 1
# #             while win.getKey() == 's':
# #                 P1.move(0, A)
# #                 A += 1
# #                 g = win.getKey()
# #                 if T != 8:
# #                     if g == '+':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1
# #                 if T != 1:
# #                     if g == '-':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= T
# #                         T -= 1

# #             A = 1
# #             while win.getKey() == 'a':
# #                 P1.move(-A, 0)
# #                 A += 1
# #                 g = win.getKey()
# #                 if T != 8:
# #                     if g == '+':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= t
# #                         T += 1
# #                 if T != 1:
# #                     if g == '-':
# #                         t += 8
# #                         time.sleep(0.3)
# #                         A -= T
# #                         T -= 1
# #             V = win.getKey()
# #             if V == 'p':
# #                 p.undraw()
# #                 P1.undraw()
# #                 victori.draw(win)
# #                 VICTORI1.draw(win)
# #                 VICTORI2.draw(win)
# #                 R.draw(win)
# #                 v.draw(win)
# #                 P.undraw()
# #                 l.undraw()
# #                 if win.getMouse():
# #                     win.close()

# # main()

# #__---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------__
# from graphics import *
# def main():
#     win = GraphWin()