# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/1 9:17
# @Author   : tangky
# @Site     : 
# @File     : heapq_try.py
# @Software : PyCharm

# from heapq import *
#
# print(heapify([1, 2, 3, 4]))

import datetime
import heapq
import types
import time


class Task:
    def __init__(self, wait_until, coro):
        self.coro = coro
        self.waiting_until = wait_until

    def __eq__(self, other):
        return self.waiting_until == other.waiting_until

    def __lt__(self, other):
        return self.waiting_until < other.waiting_until


class SleepingLoop:
    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        # Start all the corotinues:
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))
        while self._waiting:
            now = datetime.datetime.now()
            task = heapq.heappop(self._waiting)
            if now < task.waiting_until:
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds())
                time.sleep(delta.total_seconds())
                now = datetime.datetime.now()
            try:
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                pass


@types.coroutine
def sleep(seconds):
    now = datetime.datetime.now()
    wait_until = now + datetime.timedelta(seconds=seconds)
    actual = yield wait_until
    return actual - now


async def countdown(label, length, *, delay=0):
    print(label, 'waiting', delay, 'seconds before starting countdown')
    delta = await sleep(delay)
    print(label, 'starting after waiting', delta)
    while length:
        print(label, 'T-minus', length)
        waited = await sleep(1)
        length -= 1
    print(label, 'lift-off')


def main():
    loop = SleepingLoop(
        countdown('A', 5, delay=0)
    )
    start = datetime.datetime.now()
    loop.run_until_complete()
    print('Total elapsed time is', datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
