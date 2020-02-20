#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    pass
    count = 0
    while count < 2:
        count = 0
        while wall_is_on_the_left() == False:
            if wall_is_beneath() == False:
                break
            move_left()
            if wall_is_on_the_left() == True:
                count += 1

        while wall_is_on_the_right() == False:
            if wall_is_beneath() == False:
                break
            move_right()
            if wall_is_on_the_right() == True:
                count += 1

        while wall_is_beneath() == False:
            move_down()

    while wall_is_on_the_left() == False:
        move_left()

if __name__ == '__main__':
    run_tasks()
