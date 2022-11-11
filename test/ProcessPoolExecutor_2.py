# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import random
from concurrent.futures import ProcessPoolExecutor, as_completed

mp_fn_args=[(2,3,"a"),(4,5,"b")]
mp_fn_args.append((7,8,"c"))

print(*zip(*mp_fn_args))


def print_self(num1,num2,name):
    print("num1:{}\nnum2{}name{}".format(num1,num2,name))




# with ProcessPoolExecutor() as ex:
#     ex.map(print_self,*mp_fn_args)


def fib(n):
  if n > 30:
    raise Exception('can not > 30, now %s' % n)
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)


nums = [random.randint(0, 33) for _ in range(0, 10)]

def use_submit():
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(fib, n): n for n in nums}
        for f in as_completed(futures):
            try:
                print('fib(%s) result is %s.' % (futures[f], f.result()))
            except Exception as e:
                print(e)

def use_map():
     with ProcessPoolExecutor(max_workers=3) as executor:
        try:
          results = executor.map(fib, nums)
          for num, result in zip(nums, results):
            print('fib(%s) result is %s.' % (num, result))
        except Exception as e:
          print(e)

use_map()