#WAP to check if a user can vote or not by asking age of a person

age=int(input('Enter age:'))
if age>=18 and age<=100:
	print('You can vote')
else:
	print('You cannot vote yet for',(18-age),'years')
