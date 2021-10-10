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
*
*/

public class ClassHW_P1
{
    public static void main(String[] args)
    {
        Rectangle rectangle = new Rectangle(3, 9);      //Create rectangle object

        System.out.println("Height is: " + rectangle.getHeight() + "\tLength is: " + rectangle.getLength());   //Print out the height and length of the rectangle
        System.out.println("Area of the rectangle is: " + rectangle.area() + "\n");                            //Print out the area of the rectangle

        rectangle.setHeight(15);        //Change height
        rectangle.setLength(3);         //Change length

        System.out.println("New height is: " + rectangle.getHeight() + "\tNew length is: " + rectangle.getLength()); //Print out the  new height and length of the rectangle
        System.out.println("New area of the rectangle is: " + rectangle.area() + "\n\n");                            //Print out the new area of the rectangle

        RectPrism prism = new RectPrism(2, 4, 9);       //Create prism object

        System.out.println("Height is: " + prism.getHeight() + "\tLength is: " + prism.getLength() + "\tWidth is: " + prism.getWidth()); //Print out the height, width and length of the prism
        System.out.println("Area of the prism is: " + prism.area() + "\n");                                                              //Print out the area of the prism

        prism.setHeight(15);            //Change height
        prism.setLength(3);             //Change length
        prism.setWidth(13);             //Change width

        System.out.println("New height is: " + prism.getHeight() + "\tNew length is: " + prism.getLength() + "\tNew width is:" + prism.getWidth());//Print out the new height, width and length of the prism
        System.out.println("New area of the prism is: " + prism.area());                                                                           //Print out the new area of the prism
    }
} 