import turtle
turtle.shape('turtle')
turtle.speed(5)

len = 10
count = 0

while count < 10:
    for i in range(4):
        turtle.forward(len)
        turtle.left(90)
    turtle.right(135)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(135)
    len += 15
    count += 1
    
turtle.exitonclick()