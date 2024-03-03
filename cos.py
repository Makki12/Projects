# This code calculates the cos function.

carp1 = 1
carp2 = 1 
topla = 1
sign = -1

x = float(input('cosinüs icin x degeri girin'))

if(x<3 and x>0):
    for i in range(1, 25):
        carp1 = carp1 * x
        carp2 = carp2 * i
        if (i %2 == 0):# i nin tek oldugu durum (toplama veya cikarma)
            topla = topla +sign * carp1/carp2
            sign = sign * -1
        print("COS(",x,")= ", topla)