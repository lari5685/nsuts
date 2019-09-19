max = 10**6
min = 0
while True:

	num = min + (max - min )//2

	print('? '+ str(num))

	inp = input()

	if inp == '=':
		print('! ' + str(num))
		break

	if inp == '>':
		min = num + 1

	elif inp == '<':
		max = num - 1
