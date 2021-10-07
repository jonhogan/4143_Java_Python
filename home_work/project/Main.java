import java.util.Random;


class Main {
  public static void main(String[] args) {
   for(int i = 0; i < 6; i++)
   {
    System.out.println(Random());
   }
  }

  static int Random()
  {
    int x = (int)(Math.random()*1000);
    
    x = (x%50)+1;
    return x;
  }
}