# 1000 e kadar asal
for i in range(1,1000):
    bol = 1

    if (i < 2):
        print('')

    elif (i == 2):
        print(i,' asaldir')

    else:
        for a in range(2,i):

            if(i%a==0):
                bol = 0
                break
            
        if(bol == 1):
            print(i,' sayisi asaldir')