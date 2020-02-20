import turtle, math
turtle.speed(9)
turtle.shape('turtle')
turtle.width(3)

sides = 100
r = 30

len = 2*r*(math.sin(math.pi/sides))
len_small = (r*(math.sin(math.pi/sides)))/2
print(len, len_small)
count = 1

turtle.setheading(90)

while count < 10:

    for i in range(int(sides/2 + 1)):
        turtle.forward(len)
        turtle.right(360 / sides)    

    for i in range(int(sides/2 + 10)):
        turtle.forward(len_small)
        turtle.right(360 / sides)    
    count += 1

turtle.exitonclick()

