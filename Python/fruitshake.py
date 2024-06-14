#WAP to order a fruit-shake and display money to be paid

shake = ['Banana','Mango','Strawberry','Mixed']
rate = [80,100,120,70]
print('Shake-Options:\n1. Banana\n2. Mango\n3. Strawberry\n4. Mixed')
ch = int(input('What is your choice:'))
print('You ordered for', shake[ch-1], 'shake and you need to pay Rs.', rate[ch-1])
