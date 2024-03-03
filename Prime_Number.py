# This code inputs a number and check if its prime number or not

x = int(input("sayi giriniz: "))

bol = 1

if (x < 2):
    print("asal sayi değildir")

elif (x == 2):
    print("asaldir")

else:
    for i in range(2,x):

        if(x % i == 0):
            print("asal sayi değildir")
            bol = 0
            break
        
    if(bol == 1):
        print("sayi asaldir")