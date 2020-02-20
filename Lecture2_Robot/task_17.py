#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    pass
    while cell_is_filled() == False:
        move_up()
    move_right()
    if cell_is_filled() == True:
        print('Hello!')
    else:
        move_left(n=2)

if __name__ == '__main__':
    run_tasks()
