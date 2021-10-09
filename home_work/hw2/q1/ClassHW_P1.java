/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         10/11/21                                                   
*   
*    Program for Question 1: Write an OOP code (A case study:
*    Should be unique; If you are copying code from online you will
*    be caught) that has the following OOP features: inheritance(any),
*    polymorphism (runtime and compile time), abstraction and
*    encapsulation (20 points)
*/
import java.util.*;

public class ClassHW_P1
{
    public static void main(String[] args)
    {
        String name;
        String weapon;
        Scanner scan= new Scanner(System.in);
        PlayerChar p1;
        
        System.out.println("Name your character");
        System.out.println("Entering a blank line will give you a default name.\n");
        name = scan.nextLine();

        if (name.equals("")){
            p1 = new PlayerChar();
        }else{
            p1 = new PlayerChar(name);
        }

        Gnoll gnoll = new Gnoll();
     
        p1.printStats();

        System.out.println("Welcome, " + p1.getName() +".\n\nYou open your eyes, heavy with sleep. The sound of twigs snapping"
        + " awakend you. Prepare for battle!\nChoose your weapon: Mace, Dagger, Staff");
        
        weapon = scan.nextLine();

        System.out.println("\nYou ready your " + weapon.toLowerCase() + ". Suddenly a gnoll appears and rushed you!");

        while(p1.currHP < 0 & gnoll.currHP < 0){
            p1.attack(weapon);
            gnoll.attack();
        }






        scan.close();
    }
} 