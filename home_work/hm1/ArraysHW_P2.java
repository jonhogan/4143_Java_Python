/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         09/15/21                                                   
*   
*    Program for Question 2: Given an array X = {10, 100, 40, 28, 98, 37, 12, 63}.
*       a. Copy the array in a different variable Y.
*       b. Sort the array in descending order and print the array.
*       c. Calculate the AVG value of the elements and insert it to array Y on it’s correct position,
*          print it.
*       d. Perform comparison between Y and X. If not same, perform delete operation to make it
*          same
*
*/

import java.util.*;

public class ArraysHW_P2 
{
     public static void main(String[] args)
  {
      int sum = 0;
      int avg = 0;
      int count = 0;
      int location = 0;

      boolean isSame = true;
    
      int[] X = {10, 100,40,28,98,37,12,63};
      int[] Y = Arrays.copyOf(X, X.length + 1); //Copy of array X, larger by one element for the average

      /** Test Code
      * 
      * System.out.println(Arrays.toString(X));
      *
      */

      Arrays.sort(X); //Sort the array
      descend(X);     //Reverse the order

      System.out.println("Array X: " + Arrays.toString(X) + "\n");
    
     
     //Find avg
     for (int i = 0; i < X.length; i++){sum += X[i];}
     avg = sum/X.length;

     Y[X.length] = avg;

     System.out.println("The average value of Array X: " + avg + "\n");

     /** Test Code
       System.out.println(Arrays.toString(Y));
     */

      Arrays.sort(Y); //Sort the array
      descend(Y);     //Reverse the order
      
      System.out.println("Array Y: " + Arrays.toString(Y) + "\n");

      while (isSame)
      {
          if (X[count] != Y[count] && isSame)
          {
              location = count;
          }
          isSame = (X[count] == Y[count]);
          count++;
          if (count == Y.length){break;}
      }

      System.out.println("Array X equals Array Y: " + isSame + "\n");
      
      //System.out.println(location);  //Test line

      Y = deleteElement(Y, location);
      isSame = true;

      while (isSame)
      {
          if (X[count] != Y[count] && isSame)
          {
              location = count;
          }
          isSame = (X[count] == Y[count]);
          count++;
          if (count == Y.length){break;}
      }

      System.out.println("Array X equals Array Y: " + isSame + "\n");

  }

  private static void descend(int[] x)
  {

   int n = x.length;

   for (int i = 0; i < n/2; i++)
   {
     int temp = x[i];     //Temp storage of the first half of the array
     x[i] = x[n - i -1];  //Move the first half to the second half of the array
     x[n - i -1] = temp;  //Move the second half to the first half
   }
  }

  public static int[] deleteElement(int[] array, int index)
  {
    //Check if the array is empty or if the location is outside
    //of the range of the array
    if (array == null || index < 0 || index >= array.length)
    {  
        return array; // If true return source array
    }
  
    //Create temp array of size - 1
    int[] temp = new int[array.length - 1];
  
    //Copy the elements to the temp array, skipping the index
    for (int i = 0, j = 0; i < array.length; i++)
    {
        //If the current index is the one being deleted
        if (i == index) {continue;}
  
        //Copy all elements except for the index array
        temp[j++] = array[i];
    }
  
        // Return the array with the element deleted
        return temp;
  }
}
