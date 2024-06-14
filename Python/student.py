#WAP to calculate percentage and average marks of a student in 4 subjects

print('Enter marks in 4 subjects:')
p=int(input())
c=int(input())
b=int(input())
m=int(input())
sum=p+c+b+m
avg=sum/4
per=sum/400*100
print('You have',avg,'average marks and your percentage marks are',per,'%')
