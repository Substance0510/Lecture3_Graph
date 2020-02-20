#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    pass
    for i in range(4):
        move_right()
        move_down()
        if i == 1:
            fill_cell()
            move_up()


if __name__ == '__main__':
    run_tasks()
