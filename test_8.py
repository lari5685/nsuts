max = 11**6
min = 0
n_m	= 0

def number(n, num):
	if n > num:
		return '<'
	if n < num:
		return '>'
	if n == num:
		return '='

for i in range(max):
	n = 1
	max = 10**6
	min = 0
	while True:
		n += 1

		num = min + (max - min )//2

		#print('? '+ str(num))

		inp = number(num, i)

		if inp == '=':
			#print('! ', str(num))
			break

		if inp == '>':
			min = num + 1

		elif inp == '<':
			max = num - 1

	if n > n_m:
		n_m = n
	#print(str(i)+' '+str(n))
print(n_m)
