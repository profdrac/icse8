# WAP to get month number and display season of the year
# 12,1,2    -->     Winter
# 3,4,5     -->     Spring
# 6,7,8     -->     Summer
# 9, 10, 11 -->     Autumn

seasons=['Winter','Spring','Summer','Autumn']
month=int(input('Enter month number: '))
if month==12 or month==1 or month==2:
    print('Its',seasons[0],'season')
elif month==3 or month==4 or month==5:
    print('Its',seasons[1],'season')
elif month==6 or month==7 or month==8:
    print('Its',seasons[2],'season')
elif month==9 or month==10 or month==11:
    print('Its',seasons[3],'season')
else:
    print('Not a valid month!')
