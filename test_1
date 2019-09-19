s=0
print('0 to 10^9')
for i in range(0,10**9, 1):
	s+=i
	m=abs(i)
	if i%2 == 0:
		h = (m // 2)*(m + 1)
	else:
		h = m*((m + 1)//2)
		
	if i <= 0:
		h=-1*h
	
	if h==s:
		pass
	else:
		print('err::'+str(h)+' '+str(s))
		print(i)
		break
		
print('ok')
input()
