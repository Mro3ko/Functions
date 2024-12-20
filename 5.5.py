import turtle
import figures 

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def draw_square_at_location(length, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_square(length)


def draw_triangle_at_location(length, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_triangle(length)


def draw_rectangle_at_location(length_a, length_b, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_rectangle(length_a, length_b)

#draw_square_at_location(100, -100, 100)
#draw_square_at_location(100, 100, -100)
#draw_triangle_at_location(100, -200, 200)
#draw_triangle_at_location(100, 200, -200)
#draw_rectangle_at_location(150, 80, -300, 300)
#draw_rectangle_at_location(150, 80, 300, -300)

pen.hideturtle()
window.mainloop()
