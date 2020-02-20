#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    pass
    num = 0
    while wall_is_on_the_right() == False: #считаем размерность поля
        move_right()
        num += 1
    num -= 1 #количество закрашенных клеток
    while num > 0: #рисуем клетки по кругу, на каждом круге уменьшая на 2 кол-во закрашенных клеток
        move_down()
        for i in range(num):
            fill_cell()
            move_down()
        move_left()
        for i in range(num):
            fill_cell()
            move_left()
        move_up()
        for i in range(num):
            fill_cell()
            move_up()
        move_right()
        for i in range(num):
            fill_cell()
            move_right()
        move_left()
        move_down()
        num -= 2
    while wall_is_on_the_left() == False:
        move_left()
    while wall_is_beneath() == False:
        move_down()








    # while wall_is_beneath() == False:
    #     move_down()
    #     for i in range(3):
    #         fill_cell()
    #         move_down()
    # while wall_is_on_the_left() == False:
    #     move_left()
    #     for i in range(3):
    #         fill_cell()
    #         move_left()
    # while wall_is_above() == False:
    #     move_up()
    #     for i in range(3):
    #         fill_cell()
    #         move_up()
    # move_down()
    # for i in range(num):
    #     move_right(n=2)
    #     fill_cell()
    #     move_right(n=2)
    # move_up()
    # move_left()
    # for i in range(num):
    #     move_down(n=2)
    #     fill_cell()
    #     move_down(n=2)
    # move_right()
    # move_up()
    # for i in range(num):
    #     move_left(n=2)
    #     fill_cell()
    #     move_left(n=2)
    # move_down()
    # move_right()
    # for i in range(num):
    #     move_up(n=2)
    #     fill_cell()
    #     move_up(n=2)
    # move_left()
    # while wall_is_beneath() == False:
    #     move_down()
    # print(num)

if __name__ == '__main__':
    run_tasks()
