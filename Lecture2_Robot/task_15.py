#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    pass
    if wall_is_above() and wall_is_on_the_left() == True:
        while wall_is_on_the_right() == False:
            move_right()
            move_down()
    elif wall_is_above() and wall_is_on_the_right() == True:
        while wall_is_on_the_left() == False:
            move_left()
            move_down()
    elif wall_is_beneath() and wall_is_on_the_left() == True:
        while wall_is_on_the_right() == False:
            move_right()
            move_up()
    else:
        while wall_is_on_the_left() == False:
            move_left()
            move_up()



if __name__ == '__main__':
    run_tasks()
