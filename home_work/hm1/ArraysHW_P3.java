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

public class ArraysHW_P3 
{
     public static void main(String[] args)
    {
      String S = "Before trying to do any of the steps below, you should read the article through at least once for basic understanding. " +
      "Then go back and review, following these steps. He ran his machine up to the stone porch and ascending the steps rang the door bell. " +
      "They directed their steps toward the sea, which was lit up by the rising moon. She breathed a sigh of relief, and her light steps " +
      "fell gradually into the measure of his. This was fully four feet under water and the lower story of the place was two steps lower down.";

      System.out.println("Given String: " + S + "\n\n\n");

      String S2 = S.replaceAll("\\p{Punct}" ,"");


      //Split words for counting
      String[] words = S2.split("\s");

      for(int i = 0; i < words.length; i++)
      {
        words[i] = words[i].toLowerCase();
      }
      
      String[] noDups;
      String[] S_Words = new String[words.length]; //Store the words from the string
      
      int counter = 0;                             //Counter variable

      Arrays.sort(words);

      for (int i = 0; i < words.length; i++)
      {
        boolean dup = false;
        for(int j = 0; j < i; j++)
        {
          if (words[j].equals(words[i]) && i != j){dup = true;}
        }

        if (!dup){counter++;}
      }

      for (int i = 0; i < words.length; i++)
      {
        S_Words[i] = words[i]; //Store the original word list in a new array
      }

      noDups = new String[counter];
      int[] wordCounter = new int[counter];
     
      
      RemoveDups(words, words.length);

      for (int i = 0; i < counter; i++)
      {
        noDups[i] = words[i];  //Store the unique words in a new array
      }

      words = null;           //Free up the memory from the array that is no longer needed

      for (int i = 0; i < noDups.length; i++)
      {
        for (int j = 0; j < S_Words.length; j++)
        {
          if (S_Words[j].equals(noDups[i]))
          {
            wordCounter[i] = wordCounter[i] +1;
          }
        }
      }

      B_Sort(wordCounter,noDups);
      
      System.out.println("The five most common words in the string are: ");
      for (int i = 0; i < 5; i++)
      {
        System.out.println("word: '" + noDups[i] + "' appears " + wordCounter[i] + " times.");
      }
    }
  

    static void RemoveDups(String[] a, int n)
    {
      String[] temp = new String[n];

      int i = 0;
      int j = 0;
      
      for (i = 0; i < n - 1; i++)
      {
        if (a[i].equals(a[i + 1])){continue;}
        else{temp[j++] = a[i];}
      }

      temp[j++] = a[n - 1];

      for (i = 0; i < n; i++)
      {
        a[i] = temp[i];
      }
    }

    static void B_Sort(int[] int_array, String[] str_array)
    {
      int n = int_array.length;

      int temp_int;
      String temp_str;

      //Sort the two arrays using the count array to get the most common
      //words and their count to the lower elements of the array
      for (int i = 0; i < n - 1; i++)
      {
        for (int j = 0; j < n - i - 1; j++)
        {
          if(int_array[j] < int_array[j + 1])
          {
            temp_int = int_array[j];
            temp_str = str_array[j];

            int_array[j] = int_array[j + 1];
            str_array[j] = str_array[j + 1];

            int_array[j + 1] = temp_int;
            str_array[j + 1] = temp_str;
          }
        }
      }
    }
}