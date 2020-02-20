#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    pass
    num = 0
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            num += 1
        if num == 5:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
