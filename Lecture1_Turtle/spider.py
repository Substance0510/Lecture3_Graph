import turtle
turtle.shape('turtle')
turtle.speed(5)

count = 0

while count < 12:
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(30)
    count += 1
    
turtle.exitonclick()