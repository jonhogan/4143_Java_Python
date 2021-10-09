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
        Scanner scan= new Scanner(System.in);
        playerChar p1;
        
        System.out.println("Name your character");
        System.out.println("Entering a blank line will give you a default name.");
        name = scan.nextLine();
        if (name.equals("")){
            p1 = new playerChar();
        }else{
            p1 = new playerChar(name);
        }
     
        //System.out.println(p1.getStr());

        System.out.println("Welcome, " + p1.getName() +". On a table before you there is equipment. Prepare for battle!");





        scan.close();
    }
} 