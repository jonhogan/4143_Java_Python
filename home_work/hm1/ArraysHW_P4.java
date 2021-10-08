/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         09/15/21                                                   
*   
*    Program for Question 3: You are given a string S. 
*       Find 5 high frequency words using several array operations.
*       
*
*/

import java.util.*;

public class ArraysHW_P4 
{
     public static void main(String[] args)
    {
      String S = "this is my first programming assignment";
      StringBuilder S2 = new StringBuilder(S.length());

      System.out.println("Given String: " + S + "\n\n\n");

      //Split the long string into individual words
      String[] words = S.split("\s");
      
      for (int i = words.length; i > 0 ; i--)
      {
        S2.append(words[i-1]); //add words to S2
        S2.append(" ");        //add spacing for readability
      }

      System.out.println(S2); //Print out the string in reverse order
    }
}