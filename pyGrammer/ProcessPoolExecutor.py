# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
# -*- coding: utf-8 -*-
import random
from concurrent.futures import ProcessPoolExecutor


def fib(n, test_arg):

    if n > 30:

        raise Exception('can not > 30, now %s' % n)

    if n <= 2:

        return 1

    return fib(n-1, test_arg) + fib(n-2, test_arg)

def use_map():

    nums = [random.randint(0, 33) for _ in range(0, 10)]

    with ProcessPoolExecutor() as executor:

        try:
            results = executor.map(fib, nums, nums)

            for num, result in zip(nums, results):

                print('fib(%s) result is %s.' % (num, result))

        except Exception as e:

            print(e)

