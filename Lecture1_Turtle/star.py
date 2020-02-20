import turtle
turtle.shape('turtle')
turtle.speed(5)

n = 9
turtle.left(135)

def star():
    for i in range (n):
        turtle.forward(100)
        turtle.stamp()
        turtle.left(180 - 180/n)

if n % 2 == 0:
    n += 1
    star()
else:
    star()
    
turtle.exitonclick()