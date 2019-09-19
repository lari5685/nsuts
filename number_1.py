i = int(input())
m = abs(i)
if i%2 == 0:
	h = (m // 2) * (m + 1)
else:
	h = m * ((m + 1) // 2)
		
if i <= 0:
	h = -1 * h
print(h)
