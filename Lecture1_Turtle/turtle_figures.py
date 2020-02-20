import turtle, math
turtle.shape('turtle')
turtle.speed(5)

def side_step(r,f):
    turtle.right(r)
    turtle.penup()
    turtle.forward(f)
    turtle.pendown()

#squared squared
len = 10
count = 0

while count < 5:
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

#side step
side_step(90,100)

#spider
count = 0
while count < 12:

    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(30)
    count += 1

#side step
side_step(90,200)

#square spiral
len = 5

while len < 150:
    turtle.left(90)
    turtle.forward(len)
    len += 5

#side step
side_step(190,300)

#polygons
sides = 3 #изначальное количество сторон многоугольника
len = 20 #изначальная длина стороны фигуры
r = len/(3**0.5) #радиус описанной окружности треугольника, т.к. изначально рисуем именно его

while sides < 10: #до тех пор, пока количество сторон не превысит указанной величины
    angle = ((sides - 2)*180/sides)/2 #половина внутреннего угла многоугольника
    turtle.left(180 - angle) #устанавливаем нужное направление черепахи относительно оси X
    for i in range(sides): #рисуем многоугольник по количеству сторон
        turtle.forward(len)
        turtle.left(360 / sides)
    turtle.right(360 / sides + angle) #возвращаем курсор на ось X
    turtle.penup() #поднимаем ручку
    turtle.forward(10) #проходим 10 пикселей вперёд
    turtle.pendown() #опускаем ручку
    sides += 1 #добавляем количество сторон
    r += 10 #добавляем к радиусу величину шага, на который шагнули вперёд выше
    len = 2*r*(math.sin(math.pi/sides)) #высчитываем длину стороны через радиус для следующей фигуры
    
#side step
side_step(90,300)

#star
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

#side step
side_step(20,100)

#spring
sides = 100
r = 30

len = round(2*r*(math.sin(math.pi / sides)),2)
len_small = round((r*(math.sin(math.pi/sides))) / 2,2)
print(len, len_small)
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