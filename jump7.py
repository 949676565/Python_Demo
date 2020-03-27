
k = 0
s = ''

for i in range(1,101):
	if (i % 7 == 0 or i % 10 == 7 or i // 10 == 7):
		continue
	else : 
		s += '{}\t'.format(i)
		k += 1;
		if (k == 7) :
			print(s)
			s = ''
			print('\n')
			k = 0
