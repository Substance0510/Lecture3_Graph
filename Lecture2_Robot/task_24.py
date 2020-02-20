#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    pass
    def cross():
        for i in range(3):
            move_right()
            fill_cell()
        move_down()
        move_left()
        for i in range(3):
            fill_cell()
            move_up()
    move_down(n=2)
    cross()
    move_left()
    move_down()


if __name__ == '__main__':
    run_tasks()
