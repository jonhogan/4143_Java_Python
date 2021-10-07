import java.util.*;

public class playerCharacter extends character {

    int pStr;
    int pIntel;
    int pCons;
    int pDex;
    int pWis;
    int pAgi;
    int pLevel;
   
    void playerCharacter(){
        pLevel = 1;
        stats();

        pStr = str;
        pIntel = intel;
        pCons = cons;
        pDex = dex;
        pWis = wis;
        pAgi = agi;

    }

    void getStrength(){
        System.out.println(pStr);
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
