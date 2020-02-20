import turtle, math
turtle.shape('turtle')
turtle.speed(5)

sides = 100
r = 30

len = round(2*r*(math.sin(math.pi / sides)),2)
len_small = round((r*(math.sin(math.pi/sides))) / 2,2)
count = 1

turtle.setheading(90)

while count < 7:

    for i in range(int(sides / 2 + 1)):
        turtle.forward(len)
        turtle.right(360 / sides)

    for i in range(int(sides / 2 - 1)):
        turtle.forward(len_small)
        turtle.right(360 / sides)

    count += 1

turtle.exitonclick()