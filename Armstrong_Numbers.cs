// This code gets 2 input and outputs the Armstrong Numbers.
// The armstrong number for a given number base is a number that is the sum of its own digits each raised to the power of the number of digits.


Console.WriteLine("1.sayiyi giriniz: ");
int sayi1 = Convert.ToInt16(Console.ReadLine());
                                                                                            //mod al 10 a bol
Console.WriteLine("2.sayiyi giriniz: ");
int sayi2 = Convert.ToInt32(Console.ReadLine());

var sayac1 = 0;

int basamak = 0;

double toplam1 = 0;
double sonuc = 0;


int aralik1 = sayi1 + 1;

int gercek_Aralik1 = aralik1;


while (aralik1 < sayi2)
{
    while (aralik1 != 0)
{
    aralik1 = aralik1 / 10;
    sayac1 = sayac1 +1;
}

    aralik1 = gercek_Aralik1;

while (aralik1 != 0)
{
    basamak = aralik1 %10;
    sonuc = Math.Pow(basamak, sayac1);
    toplam1 = toplam1 + sonuc;
    aralik1 = aralik1 / 10;
}
    if (toplam1 == gercek_Aralik1)
    {
        Console.WriteLine(toplam1);
        }
            
    toplam1 = 0;
    sayac1 = 0;
    gercek_Aralik1 = gercek_Aralik1 +1;
    aralik1 = gercek_Aralik1;

} 