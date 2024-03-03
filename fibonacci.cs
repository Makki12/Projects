// Ask for a number and writes the fibonacci numbers until that number.

Console.WriteLine("Sayi giriniz: ");
var Sayi1 = Convert.ToInt32(Console.ReadLine());

int x = 1;

int y = 1;

int z = 0;

int sayac = 0;


   if(Sayi1 == 1){

        Console.WriteLine(x);

   }else if(Sayi1 == 0){
        Console.WriteLine("0");
   }
     else{
        Console.WriteLine(x);
        Console.WriteLine(y);
        while(sayac < Sayi1 -2) {
        z = x+y;
        x = y;
        y = z;
        sayac++;
        Console.WriteLine(z);
   }
} 
