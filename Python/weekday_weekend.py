#WAP to get day number and check if its a weekday or weekend

day=int(input('Enter day number:'))
if day>=1 and day<=5:
	print('Weekday')
elif day==6 or day==7:
	print('Weekend')
else:
	print('Invalid day')
