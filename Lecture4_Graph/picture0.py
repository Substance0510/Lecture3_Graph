import graph as gr

gr.penSize(5)
gr.brushColor('yellow')
gr.circle(200, 200, 100)
gr.penSize(2)
gr.brushColor('green')
gr.circle(160, 170, 20)
gr.circle(240, 170, 20)
gr.brushColor('black')
gr.circle(160, 170, 5)
gr.circle(240, 170, 5)
gr.line(180, 170, 220, 170)
gr.line(140, 170, 110, 150)
gr.line(260, 170, 290, 150)
gr.moveTo(160, 230)
gr.penSize(5)
x_for_smile = 165
y_for_smile = 237
count_for_y = 7
while x_for_smile < 250:
    gr.lineTo(x_for_smile, y_for_smile)
    x_for_smile += 5
    if x_for_smile <= 200:
        y_for_smile += count_for_y
        count_for_y -= 1
    else:
        y_for_smile -= count_for_y
        count_for_y += 1

gr.run()
