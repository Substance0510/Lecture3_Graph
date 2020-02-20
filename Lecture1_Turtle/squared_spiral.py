import turtle
turtle.shape('turtle')
turtle.speed(5)

len = 5

while len < 150:
    turtle.left(90)
    turtle.forward(len)
    len += 5

turtle.exitonclick()