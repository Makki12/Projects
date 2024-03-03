# This code calculates 2 numbers LCM (EKOK).

a = int(input('Ilk sayiyi girin'))
b = int(input('Iki sayiyi girin'))

maxi = a

if (b > maxi):
    maxi = b

for i in range(maxi,a*b+1):
    if  (i % a == 0 and i % b == 0):
        print('EKOK: ',i)
        break