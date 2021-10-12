import jdk.internal.org.jline.reader.SyntaxError;

public class CheckInput {

    static void checkInput(String userInput) throws SyntaxError, RuntimeError{
        boolean equalSign = false;          // More than one equal sign.
        int pareLeft = 0;                   // Count of '(' symbols.
        int pareRight = 0;                  // Count of ')' symbols.
        int addCount = 0;                   // Count of '+' symbols.
        int subCount = 0;                   // Count of '-' symbols.
        int mulCount = 0;                   // Count of '*' symbols.
        int divCount = 0;                   // Count of '/' symbols.
        int modCount = 0;                   // Count of '%' symbols.
        
        // Throw a Syntax error if an equal sign is not in the correct position
        if (userInput.charAt(1) == '=') 
        {
            equalSign = true;
                
                
            /**
             * Loop through the string and check for the amount of operations needed
             */
            for (int i = 0; i < userInput.length(); i++) 
            {
                System.out.println(userInput.charAt(i));
        
                if (userInput.charAt(i) == '+') 
                {
                    addCount++;
                    symbolCheck(userInput, i);
                } 
                else if (userInput.charAt(i) == '-') 
                {
                    subCount++;
                    symbolCheck(userInput, i);
                } 
                else if (userInput.charAt(i) == '*') 
                {
                    mulCount++;
                    symbolCheck(userInput, i);
                } 
                else if (userInput.charAt(i) == '/') 
                {
                    divCount++;
                    symbolCheck(userInput, i);
                       
                    if (userInput.charAt(i + 1) == '0')                              // if Divide by 0 throw a Runtime error.
                    {
                        throw new RuntimeError(userInput);
                    }
                } 
                else if (userInput.charAt(i) == '%') 
                {
                    modCount++;
                    symbolCheck(userInput, i);
                            
                    if (userInput.charAt(i + 1) == '0')                              // if Mod by 0 throw a Runtime Error.
                    {
                        throw new RuntimeError(userInput);
                    }
                } 
                else if (userInput.charAt(i) == '(') 
                {
                    pareLeft++;
                } 
                else if (userInput.charAt(i) == ')') 
                {
                    pareRight++;
                } 
                else if (userInput.charAt(i) == '=' && i != 1) 
                {
                    equalSign = false;
                    throw new SyntaxError(userInput);
                }
            }
                
            /**
             * If the amount of parentheses doesn't match  
             * Throw an error for more ')' than '('.
             * else Throw an error for more '(' than ')'
             */
            if (pareLeft < pareRight) 
            {
                throw new SyntaxError(userInput);
            } 
            else if (pareRight < pareLeft) 
            {
                throw new SyntaxError(userInput);
            }
        } 
        else 
        {
            throw new SyntaxError(userInput);
        }
        
        
        static void symbolCheck(String userInput, int i) 
        {
            
        }
        

    }
}
    

