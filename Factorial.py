# This code calcultes inputted numbers factorial.

x = int(input("sayi giriniz:"))

carp = 1

for sayac in range(1, x+1):
   carp *=sayac
   
print(x,"faktoriyel:",carp)
