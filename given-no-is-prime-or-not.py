x=int(input('enter a number'))
y=2
while(y<=x//2):
    if(x%y==0):
        break
    y+=1
if y>x//2:
    print('its a prime no')
else:
    print('not a prime number')


