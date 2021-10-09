import java.util.*;

public class playerChar implements Character{

    int str;
    int intel;
    int dex;
    int cons;
    int wis;
    int charisma;
    int maxPlayerHP = 0;
    int currPlayerHP = maxPlayerHP;
    String name;
    Random rand = new Random();
    int level;

    int d6 = (rand.nextInt(1000)%6)+1;
    int d20 = (rand.nextInt(1000)%20)+1;
    int d3 = (rand.nextInt(1000)%3)+1;


    playerChar(){

        level=0;
        maxPlayerHP = health();
        str = statRoll();
        intel = statRoll();
        dex = statRoll();
        cons = statRoll();
        wis = statRoll();
        charisma = statRoll();
        maxPlayerHP = health();
        name = "Bob the Nameless";
    }

    playerChar(String cName){

        level=0;
        maxPlayerHP = health();
        str = statRoll();
        intel = statRoll();
        dex = statRoll();
        cons = statRoll();
        wis = statRoll();
        charisma = statRoll();
        maxPlayerHP = health();
        name = cName;
    }

    public int statRoll(){
        int x = d6;
        int y = d6;
        int z = d6;

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

        return maxPlayerHP + x;

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

    public void updateHealth(int h){
        if ((currPlayerHP + h) > maxPlayerHP)
        {
            currPlayerHP = maxPlayerHP;
        }else{
            currPlayerHP += h;
        }
    }

    
}
