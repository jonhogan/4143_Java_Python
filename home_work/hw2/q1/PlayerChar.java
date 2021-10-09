public class PlayerChar extends Character{

    
    PlayerChar(){

        level=0;
        maxHP = health();
        str = statRoll();
        intel = statRoll();
        dex = statRoll();
        cons = statRoll();
        wis = statRoll();
        charisma = statRoll();
        currHP = maxHP;
        name = "Bob the Nameless";
    }

    PlayerChar(String cName){

        level=0;
        maxHP = health();
        str = statRoll();
        intel = statRoll();
        dex = statRoll();
        cons = statRoll();
        wis = statRoll();
        charisma = statRoll();
        currHP = maxHP;
        name = cName;
    }

    void printStats(){
        System.out.println("\n\nName: " + name + "\nHealth: " + getMaxHP() + "\nStrength: " + getStr()
        + "\nDexterity: " + getDex() + "\nIntelligence: " + getIntel() + "\nWisdom: " + getWis()
        + "\nConstitution: " + getCons() + "\nCharisma: " + getCharisma());
    }
}
