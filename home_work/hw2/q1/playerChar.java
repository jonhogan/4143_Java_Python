import java.util.*;

public class playerChar implements Character{

    int str;
    int intel;
    int dex;
    int cons;
    int wis;
    int charisma;
    int playerHP = 0;
    String name;
    Random rand = new Random();
    int level;


    playerChar(String cName){

        level=0;
        str = statRoll();
        intel = statRoll();
        dex = statRoll();
        cons = statRoll();
        wis = statRoll();
        charisma = statRoll();
        playerHP = health();
        name = cName;
    }

    public int statRoll(){
        int x = rand.nextInt(1000);
        int y = rand.nextInt(1000);
        int z = rand.nextInt(1000);

        x = (x%6)+1;
        y = (y%6)+1;
        z = (z%6)+1;

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

        return playerHP + x;

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

    
}
