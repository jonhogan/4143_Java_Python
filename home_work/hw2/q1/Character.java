import java.util.*;
import java.security.*;

public class Character {
    
    int str;
    int intel;
    int dex;
    int cons;
    int wis;
    int charisma;
    int maxHP = 0;
    int currHP = maxHP;
    String name;
    SecureRandom rand = new SecureRandom();
    int level;

    int d6(){
        return (rand.nextInt(1000)%6)+1;
    }
    int d20(){
        return (rand.nextInt(1000)%20)+1;
    }
    int d4(){
        return (rand.nextInt(1000)%4)+1;
    }

    

    public int statRoll(){
        int x = d6();
        int y = d6();
        int z = d6();

        return x+y+z;
    }


    public int health(){
        int x = rand.nextInt(1000);
        
        if (level < 4){
            x = (x%6)+2;
        }else if(level < 7){
            x = (x%6)+3;
        }else{
            x = (x%6)+4;
        }

        return maxHP + x;

    }

    public String getName(){
        return name;
    }

    public int getStr(){
        return str;
    }

    public int getIntel(){
        return intel;
    }

    public int getDex(){
        return dex;
    }

    public int getCons(){
        return cons;
    }

    public int getWis(){
        return wis;
    }

    public int getCharisma(){
        return charisma;
    }

    public int getMaxHP(){
        return maxHP;
    }

    public void updateHealth(int h){
        if ((currHP + h) > maxHP)
        {
            currHP = maxHP;
        }else{
            currHP += h;
        }
    }
}
