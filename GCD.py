# This code calculates 2 numbers GCD (EBOB).

a = int(input('Ilk sayiyi girin: '))
b = int(input('Iki sayiyi girin: '))

mini = a

if (b < mini):
    mini = b #5 a = 10
    
for i in range(mini, 0, - 1):
    if (a % i == 0 and b % i == 0):
        print('EBOB: ', i)
        break