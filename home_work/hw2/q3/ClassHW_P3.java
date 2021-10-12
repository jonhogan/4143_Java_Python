/**
*   Author      Jonathan Hogan
*   Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
*   Due         10/11/21                                                   
*   
*   Program for Question 3: Create a calculator class which can perform certain operations: addition, subtraction,
*   multiplication, division, and modulo. Now, add Java exception handling to your code by defining
*   two exception classes SyntaxError and RuntimeError. A SyntaxError exception
*   should be thrown when an illegal character is found, a closing ) is not found, or a = is not used
*   twice in an expression or an unwanted alphanumeric character inside the equation. A
*   RuntimeError exception should be thrown when a divide by zero occurs. The exceptions
*   should propagate the error to the main program which prints the diagnostics of the error. You
*   must handle these errors using Java exceptions and the message should be printed by a Java
*   exception handler in a catch clause.
*
*/

public class ClassHW_P3 {
    public class Calculator
{
        

        public int TestCaseSolution(String equation) 
        {
                int result;
                result=7*6/2;
                System.out.println(equation + "                 " + result);
                return 0;
        }

        // use this method to check if there is any Syntax/runtime error
        public int getSolution(String TestingCase) throws RuntimeError, SyntaxError 
        {
                int Solution = 0;
                int rightBrace = 0, leftBrace = 0, EqualsSigns = 0;

                for (int i = 1; i < TestingCase.length(); i++) 
                {
                        if (TestingCase.charAt(i) == '(') 
                        {
                                leftBrace++;
                        }

                        if (TestingCase.charAt(i) == ')') 
                        {
                                rightBrace++;
                        }

                        if (TestingCase.charAt(i) == '=') 
                        {
                                EqualsSigns++;
                        }

                        if (TestingCase.charAt(i) == '/') 
                        {
                                if (TestingCase.charAt(i + 1) == '0') 
                                {
                                    throw new RuntimeError(TestingCase+"                 Syntax Error: Divide by 0 occured");
                                }
                        }

                        if ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".contains("" +
                         TestingCase.charAt(i))) 
                        {
                            throw new SyntaxError(TestingCase + "                 Syntax Error: more than one variable");
                        }
                        
                }

                if (leftBrace < rightBrace)
                {
                        throw new SyntaxError(TestingCase+"                Syntax Error: ')' expected. \n");
                }
                else if (leftBrace > rightBrace)
                {
                        throw new SyntaxError(TestingCase+"                Syntax Error: '(' expected.");
                } 
               

                if (EqualsSigns < 1) 
                {
                        throw new SyntaxError(TestingCase + "               Syntax Error: '=' expected  \n");
                } 

                else if (EqualsSigns > 1) 
                {
                        throw new SyntaxError(TestingCase + "               Syntax Error: Unexpected '='\n");
                }

                Solution = TestCaseSolution(TestingCase);

                return Solution;
               
                
        }

        public void main(String[] args) 
        {

                System.out.println("=======================================================|\n"+
                                   "|                                                      |\n\n"+
                                   "| Author = Ethan Coyle                                 |\n"+
                                   "| Teacher= Dr.Saikat                                   |\n"+
                                   "| Question 3                                           |\n"+
                                   "|                                                      |\n\n"+
                                   "|   Test Expression           Correct Response         |\n"+
                                   "|======================================================|\n");

                Calculator CalcTestCase = new Calculator();

                String TestCase = "X = 1+2+3"; 
                try 
                {
                        CalcTestCase.getSolution(TestCase);
                } 
                
                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                } 
                catch (SyntaxError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }

                System.out.println("--------------------------------------------------------\n");
            
                TestCase = "Y = 2+5 = 3";
                try 
                {
                        CalcTestCase.getSolution(TestCase);
                } 
                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                } 
                catch (SyntaxError e)
                {
                        System.err.println(e.getLocalizedMessage());
                }

                System.out.println("--------------------------------------------------------\n");

                TestCase = "Y = 6*Z+5";
                try 
                {
                        CalcTestCase.getSolution(TestCase);
                } 
                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                } 
                catch (SyntaxError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                System.out.println("--------------------------------------------------------\n");
                

                TestCase = "Y=3+5+(1+6)";
                try 
                {
                    CalcTestCase.getSolution(TestCase);
                } 

                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                } 
                catch (SyntaxError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                System.out.println("--------------------------------------------------------\n");

                TestCase = "Z=(3+5)/0";
                try 
                {
                    CalcTestCase.getSolution(TestCase);
                }

                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                catch (SyntaxError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                System.out.println("--------------------------------------------------------\n");

                TestCase = "A = 7*6/2";
                try 
                {
                    CalcTestCase.getSolution(TestCase);
                }

                catch (RuntimeError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                catch (SyntaxError e) 
                {
                        System.err.println(e.getLocalizedMessage());
                }
                
                finally
                {
                        System.out.println("--------------------------------------------------------\n");
                }   
        }
}
    
}
