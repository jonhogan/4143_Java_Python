public class npc implements character {

    int str;
    int intel;
    int cons;
    int dex;
    int wis;
    int agi;
    int level;

    void npc(int n){
        level = n;
        str = strength(level);
        intel = intelligence(level);
        cons = constitution(level);
        dex = dexterity(level);
        wis = wisdom(level);
        agi = agility(level);
    }

    int strength(int n){
        return (4+3*n);
    }

    int intelligence(int n){
        return (3+2*n);
    }

    int constitution(int n){
        return (4+3*n);
    }

    int dexterity(int n){
        return (4+3*n);
    }

    int wisdom(int n){
        return  (3+2*n);;
    }

    int agility(int n){
        return  (4+3*n);
    }

    void getStrength(){
        System.out.println(str);
    }

    void getIntelligence(){
        System.out.println(intel);
    }

    void getConstitution(){
        System.out.println(cons);
    }

    void getDexterity(){
        System.out.println(dex);
    }

    void getWisdom(){
        System.out.println(wis);
    }

    void getAgility(){
        System.out.println(agi);
    }
    
}
