#WAP to get a day no from user and check whether its a weekday or weekend (using list)
msg=['Weekday','Weekend','Invalid day']
day=int(input('Enter day number: '))
if day>0 and day<6:
    print('Its a',msg[0])
elif day==6 or day==7:
    print('Its a',msg[1])
else:
    print('Its an',msg[2])
