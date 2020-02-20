#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    pass
    num = 1
    move_right()
    fill_cell()
    while wall_is_on_the_right() == False:
        if num > 1:
            fill_cell()
        for i in range(num):
            if wall_is_on_the_right() == False:
                move_right()
        num += 1


if __name__ == '__main__':
    run_tasks()
