/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         09/15/21                                                   
*   
*    Program for Question 1: Given an array with 20 elements, find the largest and smallest number
*
*/

import java.util.*;

public class ArraysHW_P1 
{
     public static void main(String args[])
  {
      int[] Z = new int[20];
      int min;
      int max;

      Random random = new Random();

      for (int i = 0; i < Z.length; i++)
      {
        Z[i] = random.nextInt(400) + 1;
      }

      min = Z[0];
      max = Z[0];

      for (int i = 1; i < Z.length; i++)
      {
        if (Z[i] < min){min = Z[i];}
        if (Z[i] > max){max = Z[i];}
      }

      System.out.println("The minimum number in Array Z: " + min);
      System.out.println("The maximum number in Array Z: " + max);

    }

  
}
