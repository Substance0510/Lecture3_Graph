#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    pass
    def cross():
        for i in range(3):
            move_down()
            fill_cell()
        move_left()
        move_up()
        for i in range(3):
            fill_cell()
            if wall_is_on_the_right() == False:
                move_right()
#Start of the program:
    move_right()
    for j in range(5):
        cross()
        if wall_is_on_the_right() == False:
            move_up(n=2)
            move_right(n=2)

    move_up()
    move_left(n=2)

if __name__ == '__main__':
    run_tasks()