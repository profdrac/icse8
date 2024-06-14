#WAP to the grades of a student by asking for his/her marks in 4 subjects:
# percentage >=90 - Grade A
# percentage >=75 and <90 - Grade B
# percentage >=55 and <75 - Grade C
# percentage >=35 and <55 - Grade D
# percentage < - Failed

print('Enter marks in 4 subjects:')
p=int(input())
c=int(input())
b=int(input())
m=int(input())
sum=p+c+b+m
per=sum/400*100
if per>=90:
	print('Grade A')
elif per>=75 and per<90:
	print('Grade B')
elif per>=55 and per<75:
	print('Grade C')
elif per>=35 and per<55:
	print('Grade D')
else:
	print('Failed')
