from math import copysign

n = int(input())

am  = abs(1-n)+1
d   = int(copysign(1.0, n)) if n != 0 else -1
ans = (2+d*(am-1))*am

print(int(ans)//2)
