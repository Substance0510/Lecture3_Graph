#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass
    small_c = 1
    big_c = 1
    while small_c < 29:
        move_right()
        fill_cell()
        small_c += 1
        if small_c == 28:
            move_down()
            while small_c > 1:
                fill_cell()
                move_left()
                small_c -= 1
            move_down()
            big_c += 1
            if big_c == 7:
                break
    move_right()


if __name__ == '__main__':
    run_tasks()
