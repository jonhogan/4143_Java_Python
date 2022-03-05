/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         10/11/21                                                   
*   
*    Program for Question 3: Create a calculator class which can perform
*    certain operands: addition, subtraction,multiplication, division,
*    and modulo. Now, add Java exception handling to your code by defining
*    two exception classes SyntaxError and RuntimeError. A SyntaxError exception
*    should be thrown when an illegal character is found, a closing ) is not found,
*    or a = is not used twice in an expression or an unwanted alphanumeric character
*    inside the equation. A RuntimeError exception should be thrown when a divide by
*    zero occurs. The exceptions should propagate the error to the main program
*    which prints the diagnostics of the error. You must handle these errors using
*    Java exceptions and the message should be printed by a Java exception handler
*    in a catch clause. (30 points)
*
*/
import java.util.*;
import java.util.regex.*;

public class Calculator{
        
        public static void main(String[] args) throws SyntaxError, RuntimeError {

                // Get user input
                Scanner scan = new Scanner(System.in);
                String userString = getUserString(scan);
                boolean cont = true;
                String repeat;
        
                while (cont){
                    try {
        
                        checkUserString(userString); //Check for errors
        
                        Pattern p = Pattern.compile("\\d+");
                        Pattern o = Pattern.compile("\\D");
                        Matcher m = p.matcher(userString);
                        Matcher n = o.matcher(userString);
        
                        Vector<Double> numbers = new Vector<Double>(1, 1);
                        Vector<String> operands = new Vector<String>(1, 1);
                        double finalNum = 0;
        
                        while (m.find()){
                            double temp = Double.valueOf(m.group());
                            numbers.add(temp);
                        }
        
                        while (n.find()){
                            String temp2 = n.group();
                            if(temp2.charAt(0) == '+' || temp2.charAt(0) == '-' || temp2.charAt(0) == '*'
                                    || temp2.charAt(0) == '/' || temp2.charAt(0) == '%'){
                                operands.add(temp2);
                            }
                        }
        
                        while (operands.size() > 0){
                            String tempS = operands.elementAt(0);
                            char c = tempS.charAt(0);
                            if(c == '+'){
                                finalNum = addition(numbers.elementAt(0), numbers.elementAt(1));
                                numbers.set(0, finalNum);
                                numbers.remove(1);
                                operands.remove(0);
                            }else if(c == '-'){
                                finalNum = subtraction(numbers.elementAt(0), numbers.elementAt(1));
                                numbers.set(0, finalNum);
                                numbers.remove(1);
                                operands.remove(0);
                            }else if(c == '*'){
                                finalNum = multiply(numbers.elementAt(0), numbers.elementAt(1));
                                numbers.set(0, finalNum);
                                numbers.remove(1);
                                operands.remove(0);
                            }else if(c == '/'){
                                finalNum = divide(numbers.elementAt(0), numbers.elementAt(1));
                                numbers.set(0, finalNum);
                                numbers.remove(1);
                                operands.remove(0);
                            }else {
                                finalNum = modulo(numbers.elementAt(0), numbers.elementAt(1));
                                numbers.set(0, finalNum);
                                numbers.remove(1);
                                operands.remove(0);
                            }
                        }
                        System.out.println("The value is " + numbers.get(0));
                    } catch (SyntaxError e){
                        System.out.println(e.getErrorMessage());
                    } catch (RuntimeError e){
                        System.out.println(e.getErrorMessage());
                    } finally {
                        System.out.println("Enter another expression? (Yes/No)");
                        repeat = scan.nextLine();
                        repeat = repeat.toLowerCase();
                        if(repeat.contains("yes")){
                            userString = getUserString(scan);
                        }else{cont = false;}
                       
                    }
                    
                }
                   
                
               
        }
        
        // Check for Errors
        static void checkUserString(String userString) throws SyntaxError, RuntimeError {
                // Variables for the operands
                boolean equalSign = false; //Check for a single '='
                int openParen = 0;         //Count the Yer of '('
                int closeParen = 0;        //Count the Yer of ')'
                userString = userString.toUpperCase();
        
                //Check if the second char is '='
                if(userString.charAt(1) == '='){
                    equalSign = true;
                   
                    //Check for unexpected symbols
                    for (int i = 0; i < userString.length(); i++){
                        if(userString.charAt(i) == '+'){
                            symbolCheck(userString, i);
                        }else if(userString.charAt(i) == '-'){
                            symbolCheck(userString, i);
                        }else if(userString.charAt(i) == '*'){
                            symbolCheck(userString, i);
                        }else if(userString.charAt(i) == '/'){
                            symbolCheck(userString, i);
                            //Check for divide by Zero
                            if(userString.charAt(i + 1) == '0'){
                                throw new RuntimeError(userString + "\t\t\tRuntime Error: Divide by Zero");
                            }
                        }else if(userString.charAt(i) == '%'){
                            symbolCheck(userString, i);
                            //Check for mod by Zero
                            if(userString.charAt(i + 1) == '0'){
                                throw new RuntimeError(userString + "\t\t\tRuntime Error: Mod by Zero");
                            }
                        }else if(userString.charAt(i) == '('){
                            openParen++;
                        }else if(userString.charAt(i) == ')'){
                            closeParen++;
                        }else if(userString.charAt(i) == '=' && i != 1){
                            equalSign = false;
                            throw new SyntaxError(userString + "\t\t\tSyntax Error: Unexpected '='");
                        }
                    }
                    
                    for(int i = 1; i < userString.length(); i++){
                        if("ABCDEFGHIJKLMNOPQRSTUVWXYZ".contains("" + userString.charAt(i))){
                                throw new SyntaxError(userString + "\t\t\tSyntax Error: More than one Variable");
                        }
                }
                    
                    //Throw the correct error for unpaired parenthesis 
                    if(openParen < closeParen){ //Missing open paren
                        throw new SyntaxError(userString + "\t\t\tSyntax Error: Expected '('");
                    } //Missing close paren
                    else if(closeParen < openParen){
                        throw new SyntaxError(userString + "\t\t\tSyntax Error: Expected ')'");
                    }
                }else {
                    //Check for a missing '='
                    throw new SyntaxError(userString + "\t\t\tSyntax Error: Expected '='");
                }
            }
        
            //Check for duplicate operands
            static void symbolCheck(String userString, int index) throws SyntaxError, RuntimeError {
                if(userString.charAt(index + 1) == '+'){
                    throw new SyntaxError(userString + "\t\t\tSyntax Error: Unexpected '+'");
                }else if(userString.charAt(index + 1) == '*'){
                    throw new SyntaxError(userString + "\t\t\tSyntax Error: Unexpected '*'");
                }else if(userString.charAt(index + 1) == '/'){
                    throw new SyntaxError(userString + "\t\t\tSyntax Error: Unexpected '/'");
                }else if(userString.charAt(index + 1) == '%'){
                    throw new SyntaxError(userString + "\t\t\tSyntax Error: Unexpected '%'");
                }
            }
        
            // Method that adds the selected values and returns the result
            static double addition(double X, double Y){
                double result = X + Y;
                return result;
            }
        
            // Method that subtracts the selected values and returns the result
            static double subtraction(double X, double Y){
                double result = X - Y;
                return result;
            }
        
            // Method that multiples the selected values and returns the result
            static double multiply(double X, double Y){
                double result = X * Y;
                return result;
            }
        
            // Method that divides the selected values and returns the result
            static double divide(double X, double Y){
                double result = X / Y;
                return result;
            }
        
            // Method that mods the first value by the second value and returns the result
            static double modulo(double X, double Y){
                double result = X % Y;
                return result;
            }
        
            // Gets the user's expression and cleans it up
            static String getUserString(Scanner scan){
                System.out.print("Enter your expression: ");
                String userString = scan.nextLine();
                userString = userString.replaceAll("\\s", "");
                System.out.println("Expression Entered: " + userString);
                return userString;
            }
}
        
     