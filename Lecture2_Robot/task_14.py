#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    pass
    def wall_above():
        if wall_is_above() == False:
            move_up()
            fill_cell()
            move_down()

    def wall_beneath():
        if wall_is_beneath() == False:
            move_down()
            fill_cell()
            move_up()

    while wall_is_on_the_right() == False:
        wall_above()
        wall_beneath()
        if wall_is_beneath() and wall_is_above() == True:
            fill_cell()
        move_right()
    wall_above()
    wall_beneath()
    if wall_is_beneath() and wall_is_above() == True:
        fill_cell()


if __name__ == '__main__':
    run_tasks()
