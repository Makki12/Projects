# This code gets 2 input and output prime numbers beetween those numbers.

a = int(input("Baslangic girin"))
b = int(input("Bitis girin"))

mini = a 
maxi = a 

if(b < mini):
    mini = b
if(b > maxi):
    maxi = b 

for i in range(mini,maxi+1):
    bol = 1

    if (i < 2):
        print("")

    elif (i == 2):
        print(i," asaldir")

    else:
        for a in range(2, i):
            if(i % a == 0):
                bol = 0
                break
            
        if(bol == 1):
            print(i," sayisi asaldir")