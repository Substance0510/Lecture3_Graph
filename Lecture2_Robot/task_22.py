#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    pass
    even_num = 0
    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        even_num += 1

        while wall_is_on_the_left() == False:
            fill_cell()
            move_left()

        if wall_is_beneath() == False:
            fill_cell()
            move_down()
            even_num += 1
    if wall_is_beneath() == True:
        fill_cell()
        if even_num % 2 == 0:
            while wall_is_on_the_right() == False:
                move_right()
                fill_cell()
            while wall_is_on_the_left() == False:
                move_left()
        else:
            print('Bingo!')


if __name__ == '__main__':
    run_tasks()
