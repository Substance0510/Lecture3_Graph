import graph as gr

gr.canvasSize(1000, 700)
gr.windowSize(1000, 700)

points = []


def rectangle(x1, y1, x2, y2, pencolor, brush):
    """Прорисовка цветных прямоугольников для раскраски полотна"""
    gr.brushColor(brush)
    gr.penColor(pencolor)
    gr.rectangle(x1, y1, x2, y2)

def duga(xstart, xmax, xstep, ystart, ystep, yincrease):
	""" Функция рисует округлые холмы и пологие склоны (дуги), в зависимости
		от переданных значений шагов для координат X и Y. Координаты увеличиваются не
		в равной степени, за что отвечает параметр yincrease. Максимальное значение Y
		не учитывается. """
    while xstart < xmax:
        points.append((xstart, ystart))
        xstart += xstep
        ystart -= ystep
        ystep += yincrease

def ptushka(xpt, ypt, size=1):
	""" Функция рисует птушек, используя функцию рисования дуг (холмов) и
		используя глобальную переменную для создания списка точек point, которая
		создаёт пустой список в начале функции. Параметр size отвечает за размер
		птушек по оси X и, как следствие, за угол между крыльями (размах)."""
    global points
    points = []
    gr.moveTo(xpt, ypt)
    duga(xpt, xpt + 36*size, 3*size, ypt, 1, -0.5)
    gr.polygon(points)
    points = []
    duga(xpt + 33*size, xpt + 74*size, 3*size, ypt + 16, 4, -0.4)
    gr.polygon(points)


# def polygon()

# раскраска полотна
rectangle(0, 0, 1000, 150, '#FFE4C4', '#FFE4C4')
rectangle(0, 150, 1000, 300, '#FFE4B5', '#FFE4B5')
rectangle(0, 300, 1000, 450, '#FAEBD7', '#FAEBD7')
rectangle(0, 450, 1000, 700, '#4169E1', '#4169E1')
# солнце
gr.brushColor('yellow')
gr.penColor('yellow')
gr.circle(500, 150, 50)
# первые горы
gr.moveTo(0, 350)
gr.brushColor('orange')
gr.penColor('orange')
gr.penSize(5)
points.append((0, 350))
points.append((10, 320))
duga(10, 190, 10, 320, 2, 1)
points.append((200, 145))
points.append((210, 165))
points.append((400, 280))
points.append((490, 270))
points.append((540, 290))
points.append((600, 220))
points.append((650, 250))
points.append((700, 210))
duga(700, 800, 5, 210, 1, 0.4)
duga(800, 850, 5, 110, 10, -2)
points.append((890, 160))
points.append((950, 120))
points.append((970, 180))
points.append((1000,250))
gr.polygon(points)

# Вторые горы
gr.moveTo(0, 375)
gr.brushColor('#BC0000')
gr.penColor('#BC0000')
points = []
points.append((0, 490))
points.append((0, 375))
points.append((5, 375))
points.append((15, 390))
duga(20, 150, 9, 373, 20, -4)
points.append((180, 390))
points.append((230, 420))
points.append((280, 350))
points.append((350, 365))
points.append((400, 400))
points.append((500, 380))
duga(505, 620, 9, 375, 12, -1.7)
duga(620, 700, 10, 350, -10, 1)
points.append((750, 350))
points.append((800, 380))
points.append((830, 340))
points.append((900, 350))
points.append((950, 300))
points.append((980, 310))
points.append((1000, 290))
points.append((1000, 470))
gr.polygon(points)

# Третьи горы
gr.moveTo(0, 700)
gr.brushColor('#4F1946')
gr.penColor('#4F1946')
points = []
points.append((0, 700))
points.append((0, 375))
points.append((110, 400))
points.append((190, 520))
duga(190, 400, 5.7, 520, -10, 0.3)
points.append((470, 690))
points.append((560, 600))
points.append((610, 620))
duga(615, 900, 8, 622, -5, 0.5)
duga(895, 1010, 9, 500, 12, -1.7)
points.append((1000, 700))
gr.polygon(points)

# Птушки
gr.brushColor('black')
gr.penColor('black')
ptushka(490, 250)
ptushka(400, 230, 0.5)
ptushka(510, 310, 0.7)
ptushka(390, 340, 1.5)
ptushka(700, 490, 1.2)
ptushka(750, 570, 0.7)
ptushka(800, 520)
ptushka(600, 500)
ptushka(650, 550, 1.7)

gr.run()
