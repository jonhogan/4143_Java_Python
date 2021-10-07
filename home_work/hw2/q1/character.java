import java.util.Random;

public class character {
    int str;
    int intel;
    int cons;
    int dex;
    int wis;
    int agi;
    int level;
    Random random = new Random(); 

    void stats(){
        str = statRoll();
        intel = statRoll();
        cons = statRoll();
        dex = statRoll();
        wis = statRoll();
        agi = statRoll();
    }

    
    int statRoll(){
        int x = (random.nextInt()*1000);
        int y = (random.nextInt()*1000);
        int z = (random.nextInt()*1000);

        x = (x%6)+1;
        y = (y%6)+1;
        z = (z%6)+1;
        

        return x+y+z;
    }

    
}
