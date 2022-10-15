package HiLo;
import java.util.Scanner;

public class HiLo {

    public static void main(String args[]){
        //Create a random number for the player to guess
        int guessMe;
        int round;
        int playerGuess;
        int score = 0;
        Scanner scan = new Scanner(System.in);
        boolean replay = true;

        System.out.println("Welcome to HiLo Guess, a random number guessing game.");
        System.out.println("The rules are simple, you will have five chances to guess the number.");
        System.out.println("The number will always be between 1-100 (inclusive), The faster you guess, the higher your score.");

        //main game loop
        while (replay){
            guessMe = (int)(Math.random() * 100 +1);
            round = 1;

            //secondary game loop
            while(true){
                System.out.print("Round " + round + "\nWhat is your guess?: ");

            }
        }

        //System.out.println(guessMe);



    }
    
}
