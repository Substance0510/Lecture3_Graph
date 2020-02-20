#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    pass
    small_c = 0
    big_c = 0
    n = 13
    move_right()
    move_down()
    while small_c <= n:
        fill_cell()
        move_down()
        small_c += 1

        if small_c == n:
            move_right()
            for i in range (n-1):
                move_up()
                fill_cell()
                small_c -= 1
            big_c += 1
            n -= 2
            small_c -= 1
            move_right()
            move_down()

            if big_c == 6:
                fill_cell()
                move_down()
                move_left(n=12)
                break


if __name__ == '__main__':
    run_tasks()
