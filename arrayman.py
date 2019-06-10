import math
import os
import random
import re
import sys


n, m = map(int, raw_input().split())
v = [0] * (n + 1)

for _ in range(m):
    a, b, k = map(int, raw_input().split())
    v[a] += k
    if b + 1 <= n:
        v[b + 1] -= k

max_sum = 0
s = 0
for i in v:
    s += i
    max_sum = max(max_sum, s)

print(max_sum)
