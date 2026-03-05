import math
r = 2

def circle_stats(r):
    area = math.pi * (r**2)
    c = 2*math.pi *r

    return area,c

a,c=circle_stats(2)

print(a)
print(c)