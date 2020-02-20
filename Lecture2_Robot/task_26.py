#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    pass
    def cross():
        for i in range(3):
            fill_cell()
            if wall_is_beneath() == False: #чтобы на последней строке не упереться в нижнюю стену
                move_down()
        move_left()
        if wall_is_beneath() == True: #на последней строке, из-за условия выше, мы не делаем один шаг вниз
            move_up()
        else:
            move_up(n=2)
        for i in range(3):
            fill_cell()
            if wall_is_on_the_right() == False:
                move_right()

    # Start of the program:
    move_right()    #Выходим на исходную
    for k in range(5):  #5 раз
        if k >= 1:  #Со второй итерации, но исключая шестую, нам нужно возвращаться на исходную и двигаться вниз
            move_left(n=37)
            move_down(n=3)
        for j in range(10): #по 10 крестов
            cross()
            if wall_is_on_the_right() == False: #чтобы не упереться в конце в правую стену
                move_up()
                move_right(n=2)

#Возвращаемся на точку:
    move_up()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
