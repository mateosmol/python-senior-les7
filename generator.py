# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
#
# res = gen()
# print(res)
# for _ in res:
#     print(_)

import os

def raise_to_the_degrees(num, max_degree):
    i = 0
    for _ in range(max_degree):
        yield num**i
        i += 1

j = 1
for j in range(500):
    res = raise_to_the_degrees(j, 500)
    for _ in res:
        print(_)
    print("\033[H\033[J", end="")
