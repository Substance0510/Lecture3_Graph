#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    pass
    num = 1
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            num += 1
            if num == 4:
                break
            move_right()
        else:
            move_right()
            num = 1

if __name__ == '__main__':
    run_tasks()
