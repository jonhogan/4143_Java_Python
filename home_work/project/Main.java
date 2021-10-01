import java.util.Random;


class Main {
  public static void main(String[] args) {
   for(int i = 0; i < 6; i++)
   {
    System.out.println(Random()%50);
   }
  }

  static int Random()
{
    return (int)(Math.random()*1000);
}
}