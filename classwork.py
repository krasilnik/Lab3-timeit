from os import path
from timeit import timeit

# f = open("text.txt", "w")
# while (path.getsize("text.txt") / (1024*1024)) < 50:
#     f.write("1231231231123")

s = """
res = 0
f1 = open("text.txt", "r")
for line in f1.readlines():
    if line.strip().isdigit():
        res+=1
f1.close()
"""
print(timeit(s, number=10))

s = """
res = 0
f2 = open("text.txt", "r")
for line in f2:
    if line.strip().isdigit():
        res+=1
f2.close()
"""
print(timeit(s, number=10))

s = """
f3 = open("text.txt", "r")
res = sum(int(line.strip().isdigit()) for line in f3)
f3.close()
"""

print(timeit(s, number=10))

# 1.8392863
# 1.6402581000000003
# 1.6764083000000003
