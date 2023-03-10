
"""
Multiples of 3 or 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import logging

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')


def sum_of_multiples(x: int):
    sum_of = sum(i for i in range(1, x) if i % 3 == 0 or i % 5 == 0)
    logging.info(f'x < {x:,}, the sum of the multiples of 3 or 5 is: {sum_of:,}')


sum_of_multiples(10)
sum_of_multiples(1000)
