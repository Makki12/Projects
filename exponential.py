# This code inputs 2 numbers and takes x^y

x = int(input("sayi giriniz: "))
y = int(input("2.sayi giriniz: "))

sayac = 1
carpim = 1

if y == 0 :
   print("1")

elif y < 0 :
   print("hesaplanamaz")
   
else :
   while sayac != y+1 :
    carpim = carpim*x
    sayac = sayac + 1
    print(carpim)